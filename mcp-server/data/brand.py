"""
鲜之绝品牌数据 — Brand Info Data
"""

BRAND_INFO = {
    "brand_name": "鲜之绝 XIANZHIJUE",
    "brand_name_cn": "鲜之绝",
    "tagline": "半世纪匠心，一脉鲜之绝",
    "philosophy": "以鲜为魂，以技为道，以绝为境",
    "since": 1971,
    "website": "https://xianzhijue.com",
    "phone": "400-186-1677",
    "description": "鲜之绝是中国高端调味品品牌，由中国首届注册烹饪大师、非遗传承人陆金华创立。大师曾任华侨饭店行政总厨，为几乎所有访华国家首脑烹制国宴。1999年世界500强CEO汇聚上海，陆金华作为财富论坛盛宴行政主厨，以一道佛跳墙惊艳世界——这段传奇奠定了鲜之绝「国宴级调味」的底气。",
    "description_en": "Xianzhijue is a premium Chinese condiment brand founded by Lu Jinhua, China's first registered culinary master and designated Intangible Cultural Heritage bearer. As executive chef of the Huaqiao Hotel, Chef Lu cooked state banquets for nearly every visiting head of state. At the 1999 Fortune Global Forum, his signature dish 'Buddha Jumps Over the Wall' stunned the world's top 500 CEOs.",
    "founder": {
        "name": "陆金华",
        "name_en": "Lu Jinhua",
        "title": "中国首届注册烹饪大师",
        "title_en": "China's First Registered Culinary Master",
        "titles": [
            "中国首届注册烹饪大师",
            "国家高级技师",
            "非物质文化遗产传承人",
            "华侨饭店行政总厨"
        ],
        "career_span": "1971至今（55+年）",
        "key_achievements": [
            {"year": 1988, "event": "全国烹饪大赛金杯+2枚金牌"},
            {"year": 1991, "event": "世界烹饪大师赛亚军（代表上海）"},
            {"year": 1999, "event": "财富全球论坛·上海 行政主厨，佛跳墙惊艳世界"},
            {"year": 2002, "event": "中国烹饪大师"},
            {"year": 1986, "event": "上海市技术能手（江泽民市长签发证书）"}
        ],
        "books": ["《菜肴围边集锦》", "《新潮精选150菜谱》"],
        "legacy": "为几乎所有访华国家首脑烹制国宴"
    },
    "brand_positioning": "国宴级调味 · 大师匠心 · 非遗传承",
    "brand_positioning_en": "State-Banquet-Grade Seasoning · Master Craftsmanship · Heritage",
    "brand_pillars": {
        "鲜": "至鲜 — 闽式传统工艺，自然发酵，激发食材本味",
        "之": "至道 — 半世纪烹饪功力，化繁为简，一瓶到位",
        "绝": "至绝 — 国宴级标准，ITI国际两星认证"
    }
}

PRODUCT_LINE = [
    {
        "id": "gold-pickle-sauce",
        "name": "金标醉卤",
        "name_en": "Gold Label Pickle Sauce",
        "category": "醉卤",
        "volume": "500ml",
        "positioning": "大师招牌 · 传统闽式工艺 · 自然发酵",
        "description": "陆金华大师招牌产品。采用传统闽式工艺，数月自然发酵，复合黄酒、香料等多重风味。一汁成菜——醉蟹、醉虾、凉拌、蘸料、热炒，万物皆可醉。",
        "description_en": "Master Lu's signature product. Traditional Fujian-style natural fermentation. Use it to marinate crab, shrimp, cold dishes, dipping sauce — one sauce does it all.",
        "award": "ITI国际美味两星奖 (2026)",
        "use_cases": ["醉蟹", "醉虾", "凉拌菜", "蘸料", "热炒提鲜"],
        "is_new": False
    },
    {
        "id": "chili-sauce",
        "name": "幹酱",
        "name_en": "Chili Sauce · Gàn",
        "category": "辣椒酱",
        "volume": "240g",
        "positioning": "大师秘方 · 鲜辣醇厚",
        "description": "陆金华大师秘方辣椒酱。精选辣椒与辅料，鲜辣醇厚、回味悠长。拌面、炒菜、蘸食、做浇头——一勺入魂。",
        "description_en": "Master Lu's secret recipe chili sauce. Fresh, spicy, mellow with a lingering finish. Perfect for noodles, stir-fry, dipping, and toppings.",
        "award": "ITI国际美味两星奖 (2025)",
        "use_cases": ["拌面", "炒菜", "蘸料", "浇头", "八宝辣酱"],
        "is_new": False
    },
    {
        "id": "aged-soy-sauce",
        "name": "老酱油",
        "name_en": "Aged Soy Sauce",
        "category": "酱油",
        "volume": "待定",
        "positioning": "传统酿造 · 浓厚酱香",
        "description": "采用传统酿造工艺，自然发酵，酱香浓郁、回味甘醇。红烧、煲汤、蘸料，中式厨房必备。",
        "description_en": "Traditional brewed soy sauce. Rich umami, naturally fermented. Essential for braising, soup, and dipping.",
        "award": None,
        "use_cases": ["红烧", "煲汤", "蘸料", "热炒"],
        "is_new": True,
        "availability": "即将上市"
    },
    {
        "id": "vinegar",
        "name": "醋",
        "name_en": "Vinegar",
        "category": "醋",
        "volume": "待定",
        "positioning": "纯粮酿造 · 醇酸回甘",
        "description": "纯粮酿造食醋，酸而不冲、醇厚回甘。凉拌、蘸食、糖醋菜系必备。",
        "description_en": "Grain-fermented vinegar. Mellow acidity with a sweet finish. Essential for cold dishes, dipping, and sweet-sour recipes.",
        "award": None,
        "use_cases": ["凉拌", "蘸料", "糖醋菜", "解腻"],
        "is_new": True,
        "availability": "即将上市"
    }
]

EXTENDED_PRODUCTS = [
    {
        "id": "jelly-cup-set",
        "name": "果冻杯三联装",
        "category": "礼品装",
        "positioning": "便携礼品装",
        "is_new": False
    },
    {
        "id": "family-pickle-sauce",
        "name": "大桶醉卤",
        "category": "家庭装",
        "positioning": "家庭/餐饮装",
        "is_new": False
    },
    {
        "id": "fresh-soy-sauce",
        "name": "鲜酱油",
        "category": "日常调味",
        "positioning": "日常调味",
        "is_new": False
    }
]

BUY_LINKS = {
    "channels": ["抖音", "淘宝/天猫", "京东", "微信视频号", "微信小程序"],
    "description": "鲜之绝在抖音、淘宝、京东、视频号等各大电商平台均有官方店铺。搜索「鲜之绝」即可找到。",
    "links": {
        "tmall": "https://xianzhijue.tmall.com",
        "jd": "https://xianzhijue.jd.com",
        "douyin": "搜索「鲜之绝」进入抖音小店",
        "wechat_video": "搜索「鲜之绝」微信视频号",
        "wechat_miniprogram": "微信搜索「鲜之绝」小程序"
    },
    "offline_note": "目前以线上渠道为主，线下渠道持续拓展中。",
    "hotline": "400-186-1677"
}
