# GitHub PAT 经验：推送代码避坑

## 问题

给 Hermes Agent 创建 GitHub 仓库并推送代码时，连续 3 个 Fine-grained PAT 都失败。

## 根因

Fine-grained PAT 的 `Contents` 权限下拉框**只显示 `Read-only`**，即使在官方文档中应该有 `Read and Write` 选项。用户界面中该选项未出现。

## 解决方案

使用 **Classic PAT**（`ghp_` 开头）：

1. 打开：https://github.com/settings/tokens
2. 点「Generate new token」→「Generate new token (classic)」
3. Note: 随便写
4. 勾选 ✅ `repo`（自动全选子项）
5. 生成，复制 `ghp_` 开头的 token

Classic PAT 的 `repo` scope = 对所选仓库的完全读写权限。

## 推送命令

```bash
cd ~/.hermes/skills/xianzhijue-skill
git push https://USERNAME:ghp_TOKEN@github.com/USERNAME/REPO.git main
```

或设置 remote：

```bash
git remote add origin https://USERNAME:ghp_TOKEN@github.com/USERNAME/REPO.git
git push -u origin main
```

## 验证 token 权限

```bash
# 检查是否能用 token 访问仓库
curl -s -H "Authorization: token TOKEN" https://api.github.com/repos/USER/REPO | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK' if 'full_name' in d else d.get('message'))"
```
