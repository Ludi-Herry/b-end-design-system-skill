# 贡献指南

欢迎贡献 B 端设计规范、组件选型判据、页面模板、审计规则与安装文档。请围绕一个明确的问题提交改动，并提供可核查的验证结果。

本项目是 AI Skill 与设计系统参考资产，不是独立前端应用或可安装的组件库。贡献前先阅读 [README.md](README.md) 和 [SKILL.md](SKILL.md)，了解规则如何被客户端读取、如何影响生成结果。

## 从哪里开始

| 路径 | 内容与用途 |
| --- | --- |
| `SKILL.md` | Skill 元信息、执行流程与规范导航 |
| `references/` | 设计基础、组件、浮层、页面骨架、反模式与人工走查清单 |
| `components.manifest.json` | 机器可读的组件用途、否定判据与页面类型 |
| `templates/` | 列表、表单、详情、看板的 TSX 参考组件 |
| `templates/README.md` | 模板消费端的依赖与构建前提 |
| `scripts/audit-design-rules.py` | 基于正则的设计规则检查脚本 |
| `scripts/test_audit_design_rules.py` | 审计命令的回归测试 |
| `docs/` | 各客户端的中文安装指南 |
| `.cursorrules`、`.windsurfrules` | 对应客户端的精简规则入口 |

Issues 与 PR 的目标都是上游 [Ludi-Herry/b-end-design-system-skill](https://github.com/Ludi-Herry/b-end-design-system-skill)。个人 fork 用于保存分支；本地 `origin` 不一定指向上游，不能据此选择提交目标。

## 准备本地环境

需要 Git；运行审计脚本和测试还需要 Python 3，脚本仅使用标准库，无需安装 pip 包。仓库没有 `package.json`、前端开发服务器或统一的前端构建命令。

先在 GitHub 创建自己的 fork，再将下面的 `YOUR_GITHUB_USER` 替换为你的用户名：

```bash
git clone https://github.com/YOUR_GITHUB_USER/b-end-design-system-skill.git
cd b-end-design-system-skill
git remote -v
git status --short
```

已有本地仓库时，直接进入仓库检查远端与工作区，不要重复克隆或覆盖个人配置。检查已有 `upstream`：

```bash
git remote get-url upstream
```

仅当它不存在时添加；若已存在但指向其他仓库，先核实用途，不要直接改写：

```bash
git remote add upstream https://github.com/Ludi-Herry/b-end-design-system-skill.git
```

确认 `upstream` 指向上游、工作区没有需要保留的未提交改动后，从上游 `main` 创建任务分支。分支名按贡献内容调整：

```bash
git fetch upstream
git switch -c docs/contributing-guide upstream/main
```

不要通过重置、清理、自动 stash 或覆盖文件来处理他人的本地修改。测试安装时也应保留已有 Skill、个人规则与配置，按对应客户端的安装指南合并或引用。

## 控制贡献范围与同步影响

修正文案、补充反例、修复模板或增加测试都欢迎直接提交。涉及全局规则、组件契约、安装路径或破坏兼容性的较大调整，建议先在上游 Issue 中说明问题、备选方案和迁移影响，避免重复投入。

每个 PR 聚焦一个目标，避免混入无关格式化、重构或依赖变更。修改一处规则时，检查下表中的关联资产；只同步实际受影响的内容。

| 贡献类型 | 同时检查与同步 | 应提供的证据 |
| --- | --- | --- |
| 设计规范与反模式 | `references/`、`SKILL.md` 的流程或导航、受影响的清单与模板 | 适用场景、边界、Do/Don't 示例与人工走查结果 |
| 组件或页面契约 | `components.manifest.json`、对应规范与模板 | 组件名称、字段及用途一致，解释调用方兼容性 |
| TSX 模板 | 对应规范、组件清单、`templates/README.md` 中受影响的前提 | 消费端构建结果、交互步骤与必要截图 |
| 审计脚本 | 规则说明、现有测试、`SKILL.md` 中的命令与退出码 | 最小违规及正常样例、回归测试、误报与漏报边界 |
| 安装与客户端规则 | `docs/`、README 使用入口、`.cursorrules`、`.windsurfrules` 中相关引用 | 实际安装位置、资源完整性、客户端发现与加载结果 |

新增规则应明确“何时使用、何时不使用、为什么”，避免只加绝对口号。保留既有规则的业务语义；改变默认行为时说明受影响的场景及替代方式。机器清单、正文与代码示例不能给出互相矛盾的指令。

## 本地检查

以下命令均在仓库根目录执行。按改动选择相关检查，并在 PR 中记录真实结果；未运行或无法验证的项目应明确说明原因。

### 审计脚本回归与 JSON 语法

```bash
python3 -B -m unittest discover -s scripts -p 'test_*.py' -v
python3 -m json.tool components.manifest.json >/dev/null
```

单元测试覆盖审计命令的输入、退出码、违规与读文件等边界。JSON 命令只检查语法，不验证组件契约、字段语义或清单与正文的一致性。纯文档改动通常只需核对事实、链接、示例命令与 diff；不必为文案新增测试。

### 设计规则审计

```bash
python3 scripts/audit-design-rules.py templates
```

也可传入实际业务源码文件或目录。脚本支持 `.tsx`、`.jsx`、`.vue`、`.html`；递归扫描不会进入符号链接目录，需要时单独指定其实际目录。安装到其他项目后，使用 [SKILL.md 的绝对路径调用方式](SKILL.md#自动化校验脚本-lint-script)。

| 退出码 | 含义 |
| --- | --- |
| `0` | 找到并检查了受支持的源码，未匹配到已实现规则中的违规项 |
| `1` | 匹配到违规项（包括 `WARNING`），或发生文件读取、目录扫描失败 |
| `2` | 目标不存在、文件类型不支持，或目录中没有受支持的源码 |

模板也可能命中规则，不能把上面的命令视为必然通过。脚本逐行匹配正则，不解析组件树、业务语义或跨行结构，可能误报或漏报；退出码 `0` 不能证明全部设计规范、交互或无障碍要求合格。不要通过忽略退出码或删减规则来掩盖问题，应解释具体发现并检查真实界面。

### 模板与客户端验收

TSX 模板需要已有 React + TypeScript 应用、`lucide-react` 与 Tailwind CSS，详见[模板使用前提](templates/README.md)。在消费端沿用现有包管理器和构建命令，确认样式扫描包含模板位置，并验证图标、类型、示例数据替换和操作处理。

按改动检查键盘焦点、加载防重、表单校验与离开防丢、危险操作确认，以及加载、空、错误等页面状态。结合 [人工走查清单](references/07-design-system-audit-checklist.md) 验证视觉与交互；涉及界面变化时附必要截图或操作记录。

安装文档或客户端规则变更应在对应客户端实际验收：资源是否完整、路径是否正确、Skill 是否被发现、引用是否被读取。仅把文件复制成功或让审计脚本通过，不能证明客户端已加载规则。记录客户端与版本；未实测的平台不要写成已支持或已通过。

## 提交 Issue

先搜索上游已有的开放与关闭 Issue，避免重复。问题报告请提供最小复现，规范建议请给出具体业务场景。不要把 PR 当作需求收集入口。

- [查看上游 Issues](https://github.com/Ludi-Herry/b-end-design-system-skill/issues)
- [新建上游 Issue](https://github.com/Ludi-Herry/b-end-design-system-skill/issues/new)

使用 GitHub CLI 时显式指定仓库；正文放入本地文件以保留换行：

```bash
gh issue list --repo Ludi-Herry/b-end-design-system-skill --state all
gh issue create --repo Ludi-Herry/b-end-design-system-skill --title "简述问题或建议" --body-file issue.md
```

可复制以下清单作为 Issue 正文：

```markdown
## 问题与目标
- 业务场景、受影响的规则或文件：
- 预期行为与实际行为：

## 复现或建议
- 最小复现步骤／Do 与 Don't 示例：
- 环境、客户端及版本（如适用）：
- 建议方案、兼容性影响与备选方案：

## 证据
- 命令与实际输出、脱敏截图或最小样例：
- 尚未验证的假设：
```

## 提交 Pull Request

提交前检查 diff，只暂存本次贡献的文件。使用自己的真实 Git 作者身份；可用 `git commit -s` 添加本人 `Signed-off-by`，确认你有权按本项目许可提交内容。仓库目前没有 DCO 文件或自动签署检查，不要将其描述为已有的强制门禁，也不要把工具或代理写成作者、共同作者或签署人。

提交信息和 PR 标题建议采用 `type(scope): 描述`，例如 `docs(install): 修正客户端资源安装路径`、`fix(audit): 报告源码读取失败`。常用类型：`feat`、`fix`、`docs`、`test`、`refactor`、`chore`。

确认 `origin` 是自己的 fork 后，将任务分支推送到 fork，再向上游 `main` 创建 PR。下面的分支名应与实际分支一致，`YOUR_GITHUB_USER` 应替换为本人用户名：

```bash
git diff --check
git push -u origin docs/contributing-guide
gh pr create --repo Ludi-Herry/b-end-design-system-skill --base main --head YOUR_GITHUB_USER:docs/contributing-guide --title "docs(contributing): 补充贡献流程" --body-file pr.md
```

也可以使用[上游 PR 页面](https://github.com/Ludi-Herry/b-end-design-system-skill/pulls)。无写入权限或提交失败时，报告具体问题，不要把 Issue 或 PR 改投到个人 fork。

可复制以下 PR 正文，按适用范围填写；有相关 Issue 时引用，只有确实完成并希望关闭它时才使用 `Fixes #编号`：

```markdown
## 问题与改动
- 解决的问题与最终行为：
- 修改范围及关联 Issue（如有）：
- 兼容性或迁移影响：

## 验证
- 实际执行的命令、目标与结果：
- 消费端／客户端环境及操作记录（如适用）：
- 未运行的检查、原因与剩余限制：

## 提交前清单
- [ ] 改动聚焦一个目标，已检查完整 diff
- [ ] 规范、清单、模板和安装入口已按影响同步
- [ ] 示例与链接可用，验证结果可复核
- [ ] 未包含凭据、个人数据、私有日志或无关文件
- [ ] 有权按 MIT 许可提交新增内容
```

欢迎使用 AI 辅助工作，提交者仍须理解改动、核实引用与依赖、运行相关检查，并负责后续评审回复。提供公开可读的复现、命令与结果；模型判断、不可访问的私有对话链接不能代替证据。不要批量提交未经验证的近似改动，也不要把个人意见表述为维护者决定。

## 安全与许可

提交前移除密钥、令牌、真实业务数据和未脱敏日志；示例使用虚构数据。安装步骤与脚本变更应说明文件写入、网络访问及对已有配置的影响。不要在公开 Issue 或 PR 中披露可被利用的漏洞细节；先检查上游是否提供私密漏洞报告入口，若没有，先请求维护者提供私密联系办法，不公开敏感材料。本仓库没有专门的安全政策或自动安全审计承诺。

本项目采用 [MIT License](LICENSE)。贡献时应确保你有权提交代码、文案、截图与其他素材，并保留适用的许可与版权声明；不要引入来源不明或许可不兼容的内容。
