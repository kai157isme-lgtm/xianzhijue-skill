# 鲜之绝 · 内容资产清单

> 最后更新: 2026-05-17
> 状态: 飞书云文档权限待开通 (需要 `drive:drive` / `drive:drive:readonly` / `space:document:retrieve`)

## 飞书共享文件夹

### 大师视频文件夹
- **链接**: `https://qcn4zmmk6zvl.feishu.cn/drive/folder/GeOUfp26JlxLfmdjqdqc8JAbnDh`
- **内容**: 陆金华大师做菜视频
- **用途**: 配方内容提取 → `get_recipes` 工具数据源

### 达人视频文件夹
- **链接**: `https://qcn4zmmk6zvl.feishu.cn/drive/folder/ALKJfCt25lMS6Xdr3ZRc5rgOnec`
- **内容**: KOL/达人种草视频
- **用途**: 品类教育场景素材 → `get_usage_guide` 灵感来源

## 权限问题

飞书应用 `cli_a9353783c9381bd9` 缺少以下权限:
- `drive:drive`
- `drive:drive:readonly`
- `space:document:retrieve`

**开通链接**: https://open.feishu.cn/app/cli_a9353783c9381bd9/auth?q=drive:drive,drive:drive:readonly,space:document:retrieve&op_from=openapi&token_type=tenant

## 内容集成计划

权限开通后:
1. 遍历两个文件夹，提取视频标题、描述、关键帧
2. 从大师视频中提取配方步骤 → 写入 `get_recipes` 数据
3. 从达人视频中提取使用场景 → 丰富 `get_usage_guide` 场景库
4. 视频链接作为 SKILL.md 示例素材
