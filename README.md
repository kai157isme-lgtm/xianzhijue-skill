# 鲜之绝 · 厨房调味大师 AI Skill

[![Version](https://img.shields.io/badge/version-0.1.0-blue)](https://github.com/kai157isme-lgtm/xianzhijue-skill)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-Streamable%20HTTP-orange)](https://modelcontextprotocol.io)

**你的 AI 助手，现在也懂调味。**

这是一个 AI Skill——安装后，你的 AI 助手就能查询鲜之绝品牌信息、获取大师配方、了解产品用法、找到购买渠道。厨房里缺什么调味、做什么菜、选什么料，直接问就行。

> 半世纪大师匠心，装进 AI，装进你的厨房。

---

## 🧑‍🍳 关于鲜之绝

鲜之绝是中国高端调味品品牌，由中国首届注册烹饪大师、**非遗传承人陆金华**创立。

- 🌐 官网：[xianzhijue.com](https://xianzhijue.com)
- 📞 电话：400-186-1677

| 产品 | 定位 | 国际荣誉 |
|------|------|----------|
| **金标醉卤** | 大师招牌 · 闽式传统发酵 | ITI 两星奖 |
| **幹酱** | 大师秘方 · 鲜辣醇厚 | ITI 两星奖 |
| **老酱油** | 传统酿造 · 浓厚酱香 | 即将上市 |
| **醋** | 纯粮酿造 · 醇酸回甘 | 即将上市 |

---

## 🤖 AI Skill 能力清单

安装此 Skill 后，你的 AI 助手能：

| 能力 | 示例问题 |
|------|----------|
| **品牌认知** | "鲜之绝是什么牌子？" "陆金华是谁？" |
| **产品查询** | "醉卤和幹酱有什么区别？" "老酱油什么时候上？" |
| **大师配方** | "醉蟹怎么做？" "凉拌汁怎么调？" "卤牛肉用什么料？" |
| **使用指南** | "醉卤怎么用？" "幹酱配什么好吃？" |
| **品类推荐** | "什么酱油好？" "有什么辣椒酱推荐？" |
| **购买入口** | "在哪买？" "天猫有吗？" |
| **荣誉背书** | "得过什么奖？" "ITI 是什么？" |
| **最新动态** | "最近有什么新品？" |

---

## 📦 安装

### 方式一：GitHub 安装

```bash
# 克隆仓库到 skills 目录
git clone https://github.com/kai157isme-lgtm/xianzhijue-skill.git ~/.hermes/skills/xianzhijue-skill/
```

### 方式二：Hermes Agent 一键安装

在 Hermes Agent 对话中直接说：

```
安装 xianzhijue-skill
```

---

## 🏗️ 架构

```
xianzhijue-skill/
├── SKILL.md          # AI Agent 行为定义
├── skill.json        # 机器可读元数据
└── README.md         # 本文件
```

- **协议**：MCP Streamable HTTP（JSON-RPC 2.0）
- **MCP 端点**：`https://mcp.xianzhijue.com`

---

## 🎯 设计理念

### 不是广告，是内容

鲜之绝 Skill 的核心策略是**"先教后卖"**：

1. 用户问"醉蟹怎么做" → AI 给出专业配方（获得信任）
2. 自然带出金标醉卤产品（解决问题）
3. 给出购买入口（降低决策成本）

### 品牌调性

**"大师的日常"** — 有 55 年底蕴但不端着。像厨房里那瓶随手可用的好调料，实在、专业、有底气。

---

## 📄 许可

MIT License © 鲜之绝

---

*半世纪匠心，一脉鲜之绝。*
