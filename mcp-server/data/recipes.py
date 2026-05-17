"""
鲜之绝大师配方库 — Master Recipes
基于陆金华大师视频教程及达人创作整理
"""

RECIPES = [
    {
        "id": "drunken-crab",
        "name": "花雕熟醉蟹",
        "name_en": "Huadiao Drunken Crab",
        "category": "醉卤菜谱",
        "difficulty": "中等",
        "time": "准备10分钟 + 浸泡24小时",
        "product": "金标醉卤",
        "product_id": "gold-pickle-sauce",
        "description": "陆金华大师传授。选用六月黄大闸蟹，以金标醉卤为主料，花雕酒为辅，一汁成菜，零翻车。",
        "ingredients": [
            "大闸蟹/六月黄 4-6只",
            "金标醉卤 500ml（一瓶）",
            "花雕酒 100ml（可选，增加层次）",
            "姜片 5片",
            "葱段 适量"
        ],
        "steps": [
            "螃蟹刷洗干净，上笼蒸15分钟至熟透",
            "蒸好的螃蟹晾凉备用",
            "将金标醉卤倒入容器，加入姜片葱段",
            "（可选）加入100ml花雕酒增香",
            "将螃蟹完全浸入醉卤中",
            "密封冷藏浸泡24小时以上",
            "取出切块装盘，淋少许醉卤即可"
        ],
        "tips": [
            "浸泡时间越长越入味，48小时最佳",
            "醉卤可重复使用2-3次（每次补一点新醉卤）",
            "剩下的醉卤汁别倒——拿来拌面、蘸饺子绝了"
        ],
        "video_reference": "大师视频002-分享：醉虾蟹秘笈、014-醉卤：神器万物醉"
    },
    {
        "id": "drunken-shrimp",
        "name": "醉虾",
        "name_en": "Drunken Shrimp",
        "category": "醉卤菜谱",
        "difficulty": "简单",
        "time": "准备5分钟 + 浸泡4-6小时",
        "product": "金标醉卤",
        "product_id": "gold-pickle-sauce",
        "description": "最经典的醉卤用法。罗氏虾/基围虾焯熟后浸入金标醉卤，鲜甜虾肉吸收醉卤复合风味，简单高级。",
        "ingredients": [
            "活虾（罗氏虾/基围虾）500g",
            "金标醉卤 300ml",
            "姜片 3片",
            "料酒 少许"
        ],
        "steps": [
            "虾洗净，挑去虾线",
            "水开下虾，加姜片料酒，焯2-3分钟至变红",
            "捞出过冰水（肉更弹）",
            "沥干后倒入金标醉卤浸泡",
            "密封冷藏4-6小时",
            "取出摆盘即可"
        ],
        "tips": [
            "夏天做醉虾，冰镇后口感最佳",
            "加几片柠檬增加清新层次",
            "醉卤汁可以循环用——泡鸡爪、泡毛豆都行"
        ],
        "video_reference": "大师视频002-分享：醉虾蟹秘笈"
    },
    {
        "id": "drunken-chicken-feet",
        "name": "醉卤鸡爪",
        "name_en": "Drunken Chicken Feet",
        "category": "醉卤菜谱",
        "difficulty": "简单",
        "time": "准备10分钟 + 浸泡6小时",
        "product": "金标醉卤",
        "product_id": "gold-pickle-sauce",
        "description": "鸡爪焯熟去骨（或不去），金标醉卤一泡即成。追剧下酒神器，比外面卖的卤鸡爪好吃十倍。",
        "ingredients": [
            "鸡爪 500g",
            "金标醉卤 300ml",
            "姜片、料酒 适量",
            "小米辣（可选）"
        ],
        "steps": [
            "鸡爪洗净剪指甲",
            "冷水下锅，加姜片料酒，煮15分钟",
            "捞出过冷水，沥干",
            "倒入金标醉卤，加入小米辣",
            "密封冷藏6小时以上"
        ],
        "tips": ["去骨版更入味但麻烦，不去骨也好吃", "泡过夜风味最佳"],
        "video_reference": "达人视频-醉卤鸡爪大头虾-退休阿姨张姐"
    },
    {
        "id": "red-braised-pork",
        "name": "大师红烧肉",
        "name_en": "Master's Red-Braised Pork",
        "category": "经典菜谱",
        "difficulty": "中等",
        "time": "准备15分钟 + 炖煮60分钟",
        "product": "老酱油",
        "product_id": "aged-soy-sauce",
        "description": "陆金华大师亲自传授。红烧肉的精髓在酱油——好酱油自带回甘，不用加糖都有层次。等老酱油上市后用这道菜开光。",
        "ingredients": [
            "五花肉 500g",
            "老酱油 3勺（即将上市）",
            "冰糖 适量",
            "姜片、八角、桂皮",
            "料酒"
        ],
        "steps": [
            "五花肉切3cm方块，冷水下锅焯水",
            "热锅少许油，下冰糖炒糖色",
            "下五花肉翻炒上色",
            "加老酱油、料酒、姜片、八角、桂皮",
            "加开水没过肉，大火烧开转小火",
            "炖60分钟至肉酥烂，收汁即可"
        ],
        "tips": [
            "老酱油自带浓郁酱香，糖可以少放",
            "肉要选三层五花，肥瘦相间最好",
            "老酱油上市前可用金标醉卤代替——别有一番风味"
        ],
        "video_reference": "大师视频011-传授：红烧肉秘籍"
    },
    {
        "id": "buddha-jumps-wall",
        "name": "佛跳墙",
        "name_en": "Buddha Jumps Over the Wall",
        "category": "国宴级菜谱",
        "difficulty": "高级",
        "time": "准备2小时 + 炖煮4-6小时",
        "product": "金标醉卤 + 老酱油",
        "product_id": "gold-pickle-sauce",
        "description": "陆金华大师的封神之作。1999年财富全球论坛上以此菜惊艳世界。传统做法极繁复，大师用一生功力化繁为简——金标醉卤替代传统料汁调配，家庭版也能做出国宴味道。",
        "ingredients": [
            "鲍鱼、海参、鱼翅（可用平替：猪蹄筋、花菇、鹌鹑蛋）",
            "金标醉卤 200ml",
            "老抽/老酱油 适量",
            "高汤 1000ml",
            "姜片、葱段、花雕酒"
        ],
        "steps": [
            "所有干货提前泡发（海参3天，鲍鱼2天）",
            "泡发好的食材分别焯水去腥",
            "砂锅底铺姜片葱段",
            "码入所有食材，加高汤、金标醉卤",
            "大火烧开，撇浮沫",
            "转小火慢炖4-6小时",
            "出锅前加少许花雕酒提香"
        ],
        "tips": [
            "金标醉卤替代了传统佛跳墙需要的十几种调料配比",
            "家庭版用猪蹄筋、花菇、鹌鹑蛋组合，成本低一样好吃",
            "炖的时候不要频繁揭盖——'佛跳墙'的香就是靠密封炖出来的"
        ],
        "video_reference": "大师视频020-022：佛跳墙讲解系列 + 023-缘启：入厨学佛跳"
    },
    {
        "id": "cold-salad-dressing",
        "name": "万能凉拌汁",
        "name_en": "Universal Cold Dressing",
        "category": "快手菜谱",
        "difficulty": "零难度",
        "time": "2分钟",
        "product": "金标醉卤",
        "product_id": "gold-pickle-sauce",
        "description": "金标醉卤最日常的用法——直接做凉拌汁。不用调酱油醋糖比例，一瓶醉卤倒下去，凉拌菜零翻车。",
        "ingredients": [
            "金标醉卤 3-4勺",
            "蒜末、葱花 适量",
            "香油 少许",
            "你喜欢的任何蔬菜/豆制品"
        ],
        "steps": [
            "蔬菜/豆制品切好焯水或直接生食",
            "金标醉卤加蒜末葱花调匀",
            "淋在菜上，加几滴香油",
            "拌匀即可"
        ],
        "tips": [
            "醉卤自带复合调味，不需要额外加盐糖醋",
            "拌黄瓜、皮蛋豆腐、木耳、海带丝——通杀"
        ]
    },
    {
        "id": "eight-treasure-chili",
        "name": "八宝辣酱",
        "name_en": "Eight-Treasure Chili Sauce",
        "category": "幹酱菜谱",
        "difficulty": "中等",
        "time": "准备20分钟",
        "product": "幹酱",
        "product_id": "chili-sauce",
        "description": "上海经典本帮菜。豆腐干、肉丁、笋丁、花生等八样食材，以幹酱炒制。有了幹酱，这道功夫菜的调味一步到位。",
        "ingredients": [
            "猪肉丁 100g",
            "豆腐干 2块",
            "笋丁、花生、虾仁",
            "幹酱 2大勺",
            "甜面酱 1勺（可选）",
            "糖、料酒"
        ],
        "steps": [
            "所有食材切小丁",
            "热油先炒肉丁至变色",
            "加入豆腐干丁、笋丁翻炒",
            "加幹酱、少许糖、料酒",
            "翻炒均匀，加少许水焖2分钟",
            "出锅前加花生和虾仁"
        ],
        "tips": [
            "幹酱自带鲜辣底味，不需要再加酱油和辣椒",
            "配米饭、拌面都是一绝"
        ],
        "video_reference": "达人视频-八宝辣酱-大头的餐桌、八宝酱丁-味道•家等"
    },
    {
        "id": "shanghai-noodle-topping",
        "name": "上海辣肉浇头",
        "name_en": "Shanghai Spicy Pork Noodle Topping",
        "category": "幹酱菜谱",
        "difficulty": "简单",
        "time": "15分钟",
        "product": "幹酱",
        "product_id": "chili-sauce",
        "description": "本帮面馆的灵魂浇头。肉丁用幹酱炒制，鲜辣入味，浇在面上——一碗本帮辣肉面就齐了。",
        "ingredients": [
            "猪肉丁 200g",
            "幹酱 2大勺",
            "姜末、料酒",
            "面条（细面最佳）"
        ],
        "steps": [
            "肉丁加料酒姜末腌制10分钟",
            "热油炒肉丁至焦香",
            "加幹酱翻炒均匀",
            "加少许水焖煮3分钟收汁",
            "煮好的面条浇上辣肉",
            "撒葱花"
        ],
        "video_reference": "达人视频-本帮辣肉面-钱厂长饿了、上海辣肉浇头-二姐厨房日记"
    }
]

# Scene-based recipe recommendations
SCENE_MAP = {
    "想喝酒配什么": ["drunken-crab", "drunken-shrimp", "drunken-chicken-feet"],
    "夏天没胃口": ["cold-salad-dressing", "drunken-shrimp"],
    "请客露一手": ["buddha-jumps-wall", "drunken-crab", "red-braised-pork"],
    "追剧零食": ["drunken-chicken-feet"],
    "拌面吃什么": ["shanghai-noodle-topping", "eight-treasure-chili"],
    "下饭神器": ["eight-treasure-chili"],
    "新手零翻车": ["cold-salad-dressing", "drunken-shrimp"]
}
