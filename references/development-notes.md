# 鲜之绝 Skill 开发笔记

## 参考模板
金谷园饺子馆 Skill (github.com/JinGuYuan/jinguyuan-dumpling-skill) 是品牌 AI Skill 的参考实现。

## GitHub 推送
- 用户账号: kai157isme-lgtm
- 仓库: github.com/kai157isme-lgtm/xianzhijue-skill
- Fine-grained PAT 必须勾选 Contents: Read and Write，只有读权限 GET=200 / PUT=403
- git push 超时可用 GitHub Contents API 逐文件上传

## 飞书云文档
- Bot 凭证: ~/.hermes/.env
- 列文件夹: GET /drive/v1/files?folder_token=xxx
- 需要 drive:drive / drive:drive:readonly scope，缺权限 code 99991672
- 权限开通后需发布版本
- 大师视频: GeOUfp26JlxLfmdjqdqc8JAbnDh
- 达人视频: ALKJfCt25lMS6Xdr3ZRc5rgOnec

## 品牌 Skill 设计模式
1. 内容驱动 — 用户搜烹饪问题比搜品牌名多100倍
2. 7个标准MCP工具 — 品牌/产品/配方/指南/购买/荣誉/动态
3. brand_prompt 控制语气 — 鲜之绝"大师的日常"
4. 盲区诚实 — 价格库存不编造，引导天猫旗舰店
