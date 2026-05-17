"""
鲜之绝 MCP Server — Vercel Serverless Entry Point
MCP Streamable HTTP (JSON-RPC 2.0)
"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.brand import BRAND_INFO, PRODUCT_LINE, EXTENDED_PRODUCTS, BUY_LINKS
from data.recipes import RECIPES, SCENE_MAP

# ─── Tool Definitions ───────────────────────────────────────────────

TOOLS = [
    {
        "name": "get_brand_info",
        "description": "查询鲜之绝品牌故事、创始人陆金华大师介绍、品牌理念与发展历程。",
        "inputSchema": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "get_products",
        "description": "获取鲜之绝全产品线及产品详情。不传参数返回全部产品列表，传入product_id返回单品详情。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "product_id": {"type": "string", "description": "产品ID，不传则返回全部产品"}
            },
            "required": []
        }
    },
    {
        "name": "get_recipes",
        "description": "获取陆金华大师配方和烹饪教程。不传参数返回配方列表，传入recipe_id返回具体做法。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "recipe_id": {"type": "string", "description": "配方ID，不传则返回全部配方列表"}
            },
            "required": []
        }
    },
    {
        "name": "get_usage_guide",
        "description": "获取产品使用指南和场景化搭配建议。传入product_id返回该产品的使用场景和搭配。",
        "inputSchema": {
            "type": "object",
            "properties": {
                "product_id": {"type": "string", "description": "产品ID，不传返回通用指南"}
            },
            "required": []
        }
    },
    {
        "name": "get_buy_links",
        "description": "获取鲜之绝产品购买渠道。返回天猫、京东、抖音、视频号、微信小程序等入口。",
        "inputSchema": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "get_awards",
        "description": "获取鲜之绝国际荣誉与认证信息。返回ITI获奖记录、大师个人荣誉等。",
        "inputSchema": {"type": "object", "properties": {}, "required": []}
    },
    {
        "name": "get_latest_news",
        "description": "获取鲜之绝品牌最新动态和新品上市信息。",
        "inputSchema": {"type": "object", "properties": {}, "required": []}
    }
]

# ─── Tool Handlers ──────────────────────────────────────────────────

def handle_get_brand_info(args=None):
    return BRAND_INFO

def handle_get_products(args=None):
    product_id = (args or {}).get("product_id")
    if product_id:
        for p in PRODUCT_LINE:
            if p["id"] == product_id:
                return p
        for p in EXTENDED_PRODUCTS:
            if p["id"] == product_id:
                return p
        return {"error": f"产品 {product_id} 不存在"}
    return {
        "core_products": PRODUCT_LINE,
        "extended_products": EXTENDED_PRODUCTS
    }

def handle_get_recipes(args=None):
    recipe_id = (args or {}).get("recipe_id")
    if recipe_id:
        for r in RECIPES:
            if r["id"] == recipe_id:
                return r
        return {"error": f"配方 {recipe_id} 不存在"}
    return {
        "recipes": [{"id": r["id"], "name": r["name"], "category": r["category"],
                      "difficulty": r["difficulty"], "product": r["product"]}
                     for r in RECIPES],
        "scene_map": SCENE_MAP
    }

def handle_get_usage_guide(args=None):
    product_id = (args or {}).get("product_id")

    guides = {
        "gold-pickle-sauce": {
            "product": "金标醉卤",
            "tagline": "一汁成菜，万物皆可醉",
            "scenes": [
                {"scene": "醉卤浸泡", "usage": "焯熟的食材浸入醉卤，冷藏浸泡后直接吃。适用：螃蟹、虾、鸡爪、蛏子、毛豆、花生。", "ratio": "食材:醉卤 ≈ 2:1"},
                {"scene": "凉拌汁", "usage": "直接当凉拌汁用，不需要额外加调料。适用：黄瓜、皮蛋豆腐、木耳、海带丝。", "ratio": "3-4勺/盘"},
                {"scene": "蘸料", "usage": "蘸饺子、白切肉、白斩鸡。加蒜末更香。", "ratio": "原汁或加少许醋"},
                {"scene": "热炒提鲜", "usage": "炒菜时淋一勺醉卤替代酱油料酒，自带复合底味。", "ratio": "1-2勺/道菜"},
                {"scene": "炖煮调味", "usage": "红烧、煲汤时加醉卤，增加醇厚层次。", "ratio": "50-100ml/锅"}
            ],
            "dont": ["不要加水稀释（除非炖煮）", "开封后冷藏保存，3个月内用完"]
        },
        "chili-sauce": {
            "product": "幹酱",
            "tagline": "一勺入魂，鲜辣百搭",
            "scenes": [
                {"scene": "拌面/拌饭", "usage": "一勺幹酱直接拌热面/热饭，就是一碗本帮辣肉面。", "ratio": "1-2勺/碗"},
                {"scene": "热炒调味", "usage": "炒菜时代替辣椒和酱油，自带鲜辣底味。适用：红烧鸡块、炒肉丁、豆腐煲。", "ratio": "1-2勺/道菜"},
                {"scene": "蘸食", "usage": "蘸饺子、蘸白切肉、蘸火锅——比普通辣椒酱有层次得多。", "ratio": "原汁或加少许醋"},
                {"scene": "浇头/酱料", "usage": "炒肉丁加幹酱做成浇头，盖在面上就是本帮辣肉面。", "ratio": "2大勺/200g肉丁"},
                {"scene": "创意菜", "usage": "幹酱炒豆腐粉丝煲、肉糜豆腐煲、辣椒肉糜烧土豆。", "ratio": "随心"}
            ],
            "dont": ["不要高温久炸（辣椒会苦）", "开封后冷藏保存"]
        }
    }

    if product_id:
        return guides.get(product_id, {"error": f"产品 {product_id} 暂无使用指南"})

    return {
        "general": "鲜之绝产品遵循「一汁成菜」理念——大师已经把调料配好了，你只需要决定用在什么菜上。",
        "guides": list(guides.keys()),
        "message": "请指定 product_id 获取详细指南：gold-pickle-sauce（金标醉卤）或 chili-sauce（幹酱）"
    }

def handle_get_buy_links(args=None):
    return BUY_LINKS

def handle_get_awards(args=None):
    return {
        "product_awards": [
            {"product": "金标醉卤", "award": "ITI国际美味两星奖", "year": 2026},
            {"product": "幹酱", "award": "ITI国际美味两星奖", "year": 2025},
            {"product": "大桶醉卤", "award": "ITI国际美味奖", "year": 2025}
        ],
        "master_honors": [
            "1988 全国烹饪大赛金杯+2枚金牌",
            "1991 世界烹饪大师赛亚军",
            "1986 上海市技术能手",
            "1999 财富全球论坛行政主厨",
            "2002 中国烹饪大师",
            "中国首届注册烹饪大师",
            "非物质文化遗产传承人"
        ],
        "iti_note": "ITI（International Taste Institute）国际风味评鉴所，总部布鲁塞尔，被誉为食品界的「米其林」。两星奖代表综合评分80%-90%，为卓越美味认证。"
    }

def handle_get_latest_news(args=None):
    return {
        "news": [
            {
                "date": "2026-05",
                "content": "老酱油和醋两款新品即将上市，传统酿造工艺，敬请期待。",
                "type": "新品预告"
            },
            {
                "date": "2026-04",
                "content": "鲜之绝AI Skill正式上线GitHub，成为调味品行业首个AI原生品牌服务。",
                "type": "品牌动态"
            },
            {
                "date": "2026",
                "content": "金标醉卤荣获ITI国际美味两星奖，连续三年斩获国际认可。",
                "type": "荣誉"
            }
        ],
        "upcoming": "老酱油和醋正在最后筹备阶段，具体上市时间请关注鲜之绝官方渠道（天猫/抖音/公众号）。"
    }

# ─── MCP Dispatcher ─────────────────────────────────────────────────

TOOL_HANDLERS = {
    "get_brand_info": handle_get_brand_info,
    "get_products": handle_get_products,
    "get_recipes": handle_get_recipes,
    "get_usage_guide": handle_get_usage_guide,
    "get_buy_links": handle_get_buy_links,
    "get_awards": handle_get_awards,
    "get_latest_news": handle_get_latest_news,
}

def make_response(id, result):
    return {
        "jsonrpc": "2.0",
        "id": id,
        "result": {
            "content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=2)}]
        }
    }

def make_error(id, code, message):
    return {
        "jsonrpc": "2.0",
        "id": id,
        "error": {"code": code, "message": message}
    }

def handle_request(body):
    method = body.get("method", "")
    req_id = body.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {
                    "name": "xianzhijue-skill",
                    "version": "0.1.3"
                },
                "capabilities": {"tools": {}}
            }
        }

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"tools": TOOLS}
        }

    if method == "tools/call":
        params = body.get("params", {})
        tool_name = params.get("name", "")
        tool_args = params.get("arguments", {})

        handler = TOOL_HANDLERS.get(tool_name)
        if not handler:
            return make_error(req_id, -32601, f"Tool not found: {tool_name}")

        try:
            result = handler(tool_args)
            return make_response(req_id, result)
        except Exception as e:
            return make_error(req_id, -32603, str(e))

    if method == "notifications/initialized":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    return make_error(req_id, -32601, f"Method not found: {method}")

# ─── HTTP Handler ───────────────────────────────────────────────────

def handler(event, context=None):
    """Vercel serverless function handler."""
    try:
        if event.get("httpMethod", event.get("method", "GET")) != "POST":
            return {
                "statusCode": 405,
                "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"error": "Method not allowed. Use POST."})
            }

        body_str = event.get("body", "{}")
        if isinstance(body_str, dict):
            body = body_str
        else:
            body = json.loads(body_str)

        result = handle_request(body)

        headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        }

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps(result, ensure_ascii=False)
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": "Invalid JSON"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }

# For local testing
if __name__ == "__main__":
    import http.server
    import socketserver

    class MCPHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(content_length))
            result = handle_request(body)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(result, ensure_ascii=False).encode())

        def do_OPTIONS(self):
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()

    port = int(os.environ.get("PORT", 8000))
    print(f"🍶 鲜之绝 MCP Server running on port {port}")
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), MCPHandler) as httpd:
        httpd.serve_forever()
