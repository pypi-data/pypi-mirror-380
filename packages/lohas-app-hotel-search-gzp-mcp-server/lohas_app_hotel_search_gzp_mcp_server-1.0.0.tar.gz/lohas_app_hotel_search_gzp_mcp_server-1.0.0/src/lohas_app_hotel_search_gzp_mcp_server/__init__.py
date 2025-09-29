from mcp.server.fastmcp import FastMCP
import mysql.connector
import re
from typing import List, Dict, Any, Optional
import math
# from hotel_tag_classifier import classifier  # 引入我们刚写的模块
# 酒店类型分类器
from .hotel_intent import classifier
# 配置日志
import logging
from .config import DB_CONFIG  # ✅ 从 config.py 导入



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 酒店链接模板
# HOTEL_LINK_TEMPLATE = "https://yourbooking.com/hotel?id={hotel_id}"
# HOTEL_APP_LINK = "appInternalJump://hotel/{hotel_id}"  # 只是一个标记，不是真实网页
# HOTEL_LINK_TEMPLATE = '<a href="javascript:void(0)" data-hotel-id="{hotel_id}" style="color:#007AFF;text-decoration:underline">查看详情</a>'
HOTEL_LINK_TEMPLATE = '<a href="app-hotel-detail/{hotel_id}" class="hotel-link" style="color:#007AFF;text-decoration:underline">查看详情</a>'


# 创建 MCP 服务器
mcp = FastMCP("HotelMCP")

# =======================
# 数据库查询函数
# =======================
def query_hotels_by_name(name: str, offset: int, limit: int) -> List[Dict[str, Any]]:
    """根据酒店名称模糊查询未过期的酒店，支持分页"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT HotelID, Name, Name_CN, CityName, CityName_CN, StarRating, Address, Address_CN
            FROM dao_lv_data 
            WHERE (Name LIKE %s OR Name_CN LIKE %s) 
              AND expired = 0
            ORDER BY StarRating DESC 
            LIMIT %s OFFSET %s
        """
        pattern = f"%{name}%"
        cursor.execute(query, (pattern, pattern, limit, offset))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        logger.error(f"数据库查询失败: {e}")
        return []

def query_hotels_by_city(city_name: str, offset: int, limit: int) -> List[Dict[str, Any]]:
    """根据城市名称查询未过期的酒店，支持分页"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT HotelID, Name, Name_CN, CityName, CityName_CN, StarRating, Address, Address_CN
            FROM dao_lv_data 
            WHERE (CityName LIKE %s OR CityName_CN LIKE %s) 
              AND expired = 0
            ORDER BY StarRating DESC 
            LIMIT %s OFFSET %s
        """
        pattern = f"%{city_name}%"
        cursor.execute(query, (pattern, pattern, limit, offset))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    except Exception as e:
        logger.error(f"数据库按城市查询失败: {e}")
        return []





# =======================
# MCP Tool: 搜索酒店（返回 dict 或 str）
# =======================
@mcp.tool()
def search_hotels_by_name(hotel_name: str, offset: int = 0, limit: int = 10) -> Dict[str, Any]:
    """
    Search for hotels by name (English or Chinese), with pagination support.
    
    Parameters:
    - hotel_name (str): The name of the hotel to search for (required).
    - offset (int): Number of results to skip, used for pagination (default: 0).
    - limit (int): Maximum number of results to return (default: 10).
    
    Returns a dictionary with:
    - "content": Formatted Markdown string of hotel results.
    - "is_error": Boolean indicating if an error occurred.
    - "data": List of hotel objects if found, else null.
    - "should_fallback": True if no results or error, suggesting AI should use its own knowledge.
    
    Important:
    - If the first call returns few or no results, try increasing 'offset' to explore more.
    - Only fallback to your own knowledge if multiple attempts with different offsets still return no results.
    - Do not say "not found" immediately; use pagination to ensure thorough search.
    """
    if not hotel_name or len(hotel_name.strip()) == 0:
        return {
            "content": "Error: hotel_name is required.",
            "is_error": True,
            "should_fallback": True
        }

    hotels = query_hotels_by_name(hotel_name.strip(), offset, limit)

    if not hotels:
        return {
            "content": f"No hotels found matching '{hotel_name}'.",
            "is_error": False,
            "data": None,
            "should_fallback": True
        }

    result_lines = [f"Found {len(hotels)} hotel(s) matching '{hotel_name}':\n"]
    for h in hotels:
        name = h["Name_CN"] or h["Name"]
        city = h["CityName_CN"] or h["CityName"]
        star = h["StarRating"] or "N/A"
        address = h["Address_CN"] or h.get("Address", "Unknown")
        link = HOTEL_LINK_TEMPLATE.format(hotel_id=h["HotelID"])

        line = (
            f"- **{name}** ({city}) ⭐{star}, 链接： {link}\n"
            f"  地址: {address}"
        )
        result_lines.append(line)
    return {
        "content": "\n\n".join(result_lines),
        "is_error": False,
        "data": hotels,
        "should_fallback": False
    }

# 工具 2：按城市搜索酒店
@mcp.tool()
def search_hotels_by_city(city_name: str, offset: int = 0, limit: int = 10) -> Dict[str, Any]:
    """
    Search for hotels by city (English or Chinese), with pagination support.
    
    Parameters:
    - hotel_name (str): The name of the hotel to search for (required).
    - offset (int): Number of results to skip, used for pagination (default: 0).
    - limit (int): Maximum number of results to return (default: 10).
    
    Returns a dictionary with:
    - "content": Formatted Markdown string of hotel results.
    - "is_error": Boolean indicating if an error occurred.
    - "data": List of hotel objects if found, else null.
    - "should_fallback": True if no results or error, suggesting AI should use its own knowledge.
    
    Important:
    - If the first call returns few or no results, try increasing 'offset' to explore more.
    - Only fallback to your own knowledge if multiple attempts with different offsets still return no results.
    - Do not say "not found" immediately; use pagination to ensure thorough search.
    """
    if not city_name or len(city_name.strip()) == 0:
        return {
            "content": "Error: city_name is required.",
            "is_error": True,
            "should_fallback": True
        }

    results = query_hotels_by_city(city_name.strip(), offset, limit)

    if not results:
         return {
            "content": f"在城市 '{city_name}' 中未找到匹配的酒店。",
            "is_error": False,
            "data": None,
            "should_fallback": True
        }

    result_lines = [f"🏨 在 **{city_name}** 推荐以下 {len(results)} 家酒店：\n"]
    for h in results:
        name = h["Name_CN"] or h["Name"]
        city = h["CityName_CN"] or h["CityName"]
        star = h["StarRating"] or "N/A"
        address = h["Address_CN"] or h.get("Address", "Unknown")
        link = HOTEL_LINK_TEMPLATE.format(hotel_id=h["HotelID"])

        line = (
            f"- **{name}** ⭐{star}\n"
            f"  地址: {address}\n"
            f"  链接: {link}"
        )
        result_lines.append(line)

    return {
        "content": "\n\n".join(result_lines),
        "is_error": False,
        "data": results,
        "should_fallback": False
    }

@mcp.tool()
def search_hotels(
    city: Optional[str] = None,
    star_rating: Optional[float] = None,
    hotel_type: Optional[str] = None,
    limit: int = 10
) -> Dict[str, Any]:
    """
    Search hotels by city, star rating, or intent type (e.g., family, business).
    Supports pagination via offset and limit.
    
    Parameters:
    - city (str): City name in Chinese or English.
    - star_rating (float): Minimum star rating (e.g., 4.0).
    - hotel_type (str): Intent keyword like "亲子", "商务", "度假", "浪漫".
    - offset (int): Number of results to skip (for pagination), default 0.
    - limit (int): Max number of results per page, default 10.
    
    Returns:
    - content: Formatted Markdown string for display.
    - is_error: Boolean, True if system error occurred.
    - data: List of raw hotel objects, or null if none.
    - should_fallback: True only if no results found (suggest AI use its knowledge).
    
    Behavior:
    - Always sort by StarRating DESC.
    - If hotel_type is given, filter by description keywords.
    - If no results, suggest increasing offset or relaxing criteria.
    """
    # 1. 解析用户意图
    target_type = None
    if hotel_type:
        target_type = classifier.classify_user_intent(hotel_type)
        if not target_type:
            return {
                "error": "无法识别酒店类型，请使用：亲子、度假、商务、浪漫等关键词",
                "suggestions": ["亲子酒店", "带娃住哪", "商务出差", "蜜月旅行"]
            }

    # 2. 查询酒店数据
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                d.HotelID, 
                d.Name_CN, 
                d.CityName_CN, 
                d.StarRating, 
                d.Address_CN, 
                d.Latitude, 
                d.Longitude,
                dd.HotelDescription_CN
            FROM dao_lv_data d
            LEFT JOIN dao_lv_desc dd ON d.HotelID = dd.HotelID
            WHERE d.expired = 0
        """
        params = []



        if city:
            query += " AND (d.CityName = %s OR d.CityName_CN = %s)"
            params.extend([city, city])
        if star_rating:
            query += " AND d.StarRating >= %s"
            params.append(star_rating)

        # ✅ 最后才加 ORDER BY
        query += " ORDER BY d.StarRating DESC, d.HotelID DESC"

        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()

    except Exception as e:
        print(f"❌ 数据库查询失败: {e}")
        return {
            "content": f"系统错误：无法连接数据库或查询失败 ({str(e)})",
            "is_error": True,
            "data": None,
            "should_fallback": True
        }

    # # 3. 如果有 hotel_type，用描述关键词过滤
    # if target_type:
    #     filtered = []
    #     for row in results:
    #         desc = (row.get("HotelDescription_CN") or "").replace("<br />", " ")
    #         if classifier.match_hotel_description(desc, target_type):
    #             filtered.append(row)
    #     results = filtered

    # return {"hotels": results[:limit]}
     # 如果有 hotel_type，则用意图分类器过滤描述
    target_type = None
    if hotel_type:
        target_type = classifier.classify_user_intent(hotel_type)
        if not target_type:
            return {
                "content": f"无法理解酒店类型 '{hotel_type}'。可尝试：亲子、商务、度假、浪漫等。",
                "is_error": False,
                "data": None,
                "should_fallback": True
            }

        filtered = []
        for row in results:
            desc = (row.get("HotelDescription_CN") or "").replace("<br />", " ")
            if classifier.match_hotel_description(desc, target_type):
                filtered.append(row)
        results = filtered

    # 构建返回内容
    if not results:
        suggestion = (
            f"\n\n💡 提示：尝试调整搜索条件，或增加 offset={offset + limit} 继续翻页查看更多结果。"
            if offset == 0 else ""
        )
        return {
            "content": f"未找到符合条件的酒店。{suggestion}",
            "is_error": False,
            "data": None,
            "should_fallback": True  # 可让 AI 尝试用自己的知识补充
        }

    # ✅ 生成 Markdown 内容，包含链接
    result_lines = [f"为您找到 {len(results)} 家符合条件的酒店：\n"]
    for h in results:
        name = h["Name_CN"] or h["Name"] or "未知名称"
        city = h["CityName_CN"] or "未知城市"
        star = h["StarRating"] or "N/A"
        address = h["Address_CN"] or h.get("Address", "未知地址")
        link = HOTEL_LINK_TEMPLATE.format(hotel_id=h["HotelID"])

        line = (
            f"- **{name}** ({city}) ⭐{star}\n"
            f"  📍 地址: {address}\n"
            f"  🔗 [查看详情]{link}"
        )
        result_lines.append(line)

    return {
        "content": "\n\n".join(result_lines),
        "is_error": False,
        "data": results,
        "should_fallback": False  # 有结果，不需 fallback
    }



# =======================
# 运行服务
# =======================
if __name__ == "__main__":
    mcp.run(transport="stdio")
def main() -> None:
    mcp.run(transport="stdio")
