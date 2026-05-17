# 飞书云文档权限调试记录

## 场景

鲜之绝 Skill 需要读取飞书共享文件夹中的大师视频和达人视频，用于配方库。

## 错误路径

### 错误 1：未授权应用访问云文档

```
HTTP 200 - code: 99991672
Access denied. One of the following scopes is required: 
[drive:drive, drive:drive:readonly, space:document:retrieve]
```

**原因**：飞书应用（Bot）未开通云文档相关权限 scope。

### 错误 2：开通权限后仍不生效

在开放平台开通权限 scope 后，API 仍然返回 99991672。

**原因**：飞书开放平台的权限变更有两步：
1. 在「权限管理」中搜索并添加 scope
2. 在「版本管理与发布」中**创建新版本并发布**

只做第一步不发布 = 不生效。

## 需要的权限 Scope（读取云文档）

| Scope | 用途 |
|-------|------|
| `drive:drive` 或 `drive:drive:readonly` | 访问云空间、列出文件夹 |
| `space:document:retrieve` | 访问共享文档 |
| `docx:document:readonly` | 读取新版飞书文档正文 |
| `doc:document:readonly` | 读取旧版文档 |
| `drive:file:download` | 下载文件 |

## 正确操作流程

1. 打开应用权限页：`https://open.feishu.cn/app/{APP_ID}/permission`
2. 搜索并开通上述所有 scope
3. 左侧菜单 →「版本管理与发布」→ 创建新版本 → **发布**
4. 如需要管理员审批：`https://admin.feishu.cn` → 应用管理 → 审批权限申请
5. 验证：重新调用 API，检查 `code` 是否为 0

## API 调用示例

```bash
# 获取 tenant_access_token
TOKEN=$(curl -s -X POST "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal" \
  -H "Content-Type: application/json" \
  -d '{"app_id":"$APP_ID","app_secret":"$APP_SECRET"}' \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['tenant_access_token'])")

# 列出文件夹内容
curl -s "https://open.feishu.cn/open-apis/drive/v1/files?folder_token=$FOLDER_TOKEN&page_size=50" \
  -H "Authorization: Bearer $TOKEN"
```

## 环境变量

```bash
FEISHU_APP_ID=cli_a9353783c9381bd9
FEISHU_APP_SECRET=EVIznWltReQfdHLSkSuvaeUzKtdFaaLS
```
