# hotel_intent.py
import mysql.connector
import threading
import logging
from typing import Dict, List, Optional
from config import DB_CONFIG  # ✅ 从 config.py 导入

# 日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



REFRESH_INTERVAL = 60  # 每60秒刷新一次


class HotelIntentClassifier:
    """
    全数据库驱动的酒店意图分类器
    所有规则均可通过数据库配置，无需修改代码
    """

    def __init__(self):
        self._intent_mapping: Dict[str, str] = {}              # keyword -> type_code
        self._desc_keywords: Dict[str, List[str]] = {}         # type_code -> [keywords]
        self._lock = threading.RLock()
        self._stop_event = threading.Event()
        self._refresh_thread = None

        # 初始化加载
        self._load_intent_mapping()
        self._load_description_keywords()

        # 启动后台刷新
        self._refresh_thread = threading.Thread(target=self._run_refresh_loop, daemon=True)
        self._refresh_thread.start()
        logger.info("✅ HotelIntentClassifier 初始化完成")

    def _run_refresh_loop(self):
        """后台自动刷新"""
        while not self._stop_event.wait(timeout=REFRESH_INTERVAL):
            try:
                self._load_intent_mapping()
                self._load_description_keywords()
            except Exception as e:
                logger.error(f"❌ 自动刷新失败: {e}")

    def _load_intent_mapping(self):
        """加载用户输入关键词 → 标准类型"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT k.keyword, t.type_code
                FROM ai_user_intent_keywords k
                JOIN ai_hotel_standard_types t ON k.standard_type_id = t.id
                WHERE k.enabled = 1 AND t.enabled = 1
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            new_mapping = {row["keyword"]: row["type_code"] for row in rows}
            cursor.close()
            conn.close()

            with self._lock:
                self._intent_mapping = new_mapping
            logger.info(f"🔄 刷新用户意图关键词: {len(new_mapping)} 个")

        except Exception as e:
            logger.error(f"❌ 加载用户意图关键词失败: {e}")

    def _load_description_keywords(self):
        """加载酒店描述关键词"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor(dictionary=True)
            query = """
                SELECT t.type_code, k.keyword
                FROM ai_hotel_type_description_keywords k
                JOIN ai_hotel_standard_types t ON k.standard_type_id = t.id
                WHERE k.enabled = 1 AND t.enabled = 1
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            new_keywords = {}
            for row in rows:
                code = row["type_code"]
                if code not in new_keywords:
                    new_keywords[code] = []
                new_keywords[code].append(row["keyword"])
            cursor.close()
            conn.close()

            with self._lock:
                self._desc_keywords = new_keywords
            logger.info(f"🔄 刷新描述关键词: {len(new_keywords)} 个类型")

        except Exception as e:
            logger.error(f"❌ 加载描述关键词失败: {e}")

    def classify_user_intent(self, user_input: str) -> Optional[str]:
        """将用户输入映射到标准类型"""
        if not user_input:
            return None

        with self._lock:
            mapping = self._intent_mapping.copy()

        # 按长度降序匹配，避免短词优先
        sorted_keywords = sorted(mapping.keys(), key=len, reverse=True)
        for keyword in sorted_keywords:
            if keyword in user_input:
                logger.info(f"🎯 匹配用户意图: '{keyword}' → '{mapping[keyword]}'")
                return mapping[keyword]
        return None

    def match_hotel_description(self, description: str, hotel_type: str) -> bool:
        """判断酒店描述是否匹配某类型"""
        if not description:
            return False

        with self._lock:
            keywords = self._desc_keywords.get(hotel_type, [])

        return any(keyword in description for keyword in keywords)

    def stop(self):
        """停止后台线程"""
        self._stop_event.set()


# 全局单例
classifier = HotelIntentClassifier()