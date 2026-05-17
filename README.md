# 鲜之绝 · The Kitchen Maestro AI Skill

[![Version](https://img.shields.io/badge/version-0.1.2-blue)](https://github.com/kai157isme-lgtm/xianzhijue-skill)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-Streamable%20HTTP-orange)](https://modelcontextprotocol.io)
[![Language](https://img.shields.io/badge/lang-zh%20%7C%20en-brightgreen)]()

> **Your AI assistant now understands seasoning.** / **你的 AI 助手，现在也懂调味。**

Xianzhijue is China's first premium condiment brand to launch an AI Skill. Install it, and your AI assistant can teach you master-level recipes, recommend the right seasoning, and guide you to buy — all from a 55-year culinary legend who once cooked for heads of state.

鲜之绝是中国首个推出 AI Skill 的高端调味品品牌。安装后，你的 AI 助手就能获取大师配方、推荐调味方案、引导购买渠道——这一切来自一位曾为各国首脑掌勺的 55 年烹饪大师。

> *Half a century of mastery, now in your AI. Now in your kitchen.*  
> *半世纪大师匠心，装进 AI，装进你的厨房。*

---

## 🧑‍🍳 About Xianzhijue / 关于鲜之绝

Xianzhijue is a premium Chinese condiment brand founded by **Lu Jinhua**, China's first registered culinary master and a designated Intangible Cultural Heritage bearer. As executive chef of the Huaqiao Hotel, Chef Lu cooked state banquets for nearly every visiting head of state. At the 1999 Fortune Global Forum in Shanghai, his signature dish *Buddha Jumps Over the Wall* stunned the world's top 500 CEOs.

鲜之绝是中国高端调味品品牌，由中国首届注册烹饪大师、**非遗传承人陆金华**创立。大师曾任华侨饭店行政总厨，为几乎所有访华国家首脑烹制国宴。1999 年财富全球论坛，一道佛跳墙惊艳世界。

- 🌐 Website：[xianzhijue.com](https://xianzhijue.com)
- 📞 Phone：400-186-1677

| Product / 产品 | Positioning / 定位 | Awards / 奖项 |
|------|------|------|
| **Gold Label Pickle Sauce** 金标醉卤 | Master's signature · Fujian craft fermentation | ITI 2-Star |
| **Chili Sauce** 幹酱 | Master's secret recipe · fresh & mellow heat | ITI 2-Star |
| **Aged Soy Sauce** 老酱油 | Traditional brewing · deep umami | Coming soon |
| **Vinegar** 醋 | Grain-fermented · mellow acidity | Coming soon |

---

## 🤖 What This Skill Can Do / 能力清单

Once installed, your AI assistant can:

| Capability | Example Questions |
|------|------|
| **Brand Story** | "Who is Lu Jinhua?" "What is Xianzhijue?" |
| **Product Info** | "What's the difference between pickle sauce and soy sauce?" |
| **Master Recipes** ⭐ | "How to make drunken crab?" "What's the best marinade for braised beef?" |
| **Usage Guide** | "How do I use the pickle sauce?" "What goes well with chili sauce?" |
| **Buying Guide** | "Where to buy?" "Available on Douyin/TikTok shop?" |
| **Awards & Credentials** | "What awards has it won?" "What is ITI?" |
| **Latest News** | "When will the aged soy sauce launch?" |

---

## 📦 Installation / 安装

### Via GitHub

```bash
git clone https://github.com/kai157isme-lgtm/xianzhijue-skill.git ~/.hermes/skills/xianzhijue-skill/
```

### Via Hermes Agent

In your Hermes Agent conversation, simply say:

```
Install xianzhijue-skill
```

---

## 🏗️ Architecture / 架构

```
xianzhijue-skill/
├── SKILL.md          # AI agent behavior definition
├── skill.json        # Machine-readable metadata & MCP tool schemas
└── README.md         # This file (bilingual)
```

- **Protocol**：MCP Streamable HTTP (JSON-RPC 2.0)
- **MCP Endpoint**：`https://mcp.xianzhijue.com`

---

## 🎯 Design Philosophy / 设计理念

### Teach First, Sell Later / 先教后卖

Xianzhijue Skill's core strategy is **content-led discovery**:

1. User asks *"How to make drunken crab?"* → AI delivers a master recipe *(builds trust)*
2. Naturally introduces Gold Label Pickle Sauce as the solution *(solves the problem)*
3. Provides a purchase link *(reduces friction)*

Not an ad. A cooking mentor who happens to have great seasoning.

### Brand Voice / 品牌调性

**"The Master's Everyday"** — 55 years of depth without pretension. Like a trusted bottle of seasoning on your kitchen counter: authentic, professional, confident.

---

## 📄 License / 许可

MIT License © 鲜之绝 XIANZHIJUE

---

*Half a century of mastery, one lineage of Xianzhijue.*  
*半世纪匠心，一脉鲜之绝。*
