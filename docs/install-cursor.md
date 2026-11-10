# 在 Cursor 中安装

将完整 Skill 安装到使用它的项目的 `.cursor/skills/` 目录。仅复制旧版 `.cursorrules` 只能获得精简规则，不包含其中引用的规范、模板、组件清单和审计脚本。

## 安装项目级 Skill

需要 Git 和 POSIX Shell，例如 `sh`、Bash 或 Zsh；Windows 可使用 WSL 或 Git Bash。在目标项目之外选择一个尚不存在的源码目录：

```sh
git clone https://github.com/Ludi-Herry/b-end-design-system-skill.git "/absolute/path/to/b-end-design-system-source"
```

**源码目录**是上一步克隆的仓库；**目标项目**是在 Cursor 中打开的已有应用项目。替换下方两个绝对路径。子 Shell 遇到错误立即退出；`mkdir` 会拒绝已有 Skill 目录，避免合并或覆盖安装。

```sh
(
  set -eu
  source_dir=$(cd "/absolute/path/to/b-end-design-system-source" && pwd)
  project_dir=$(cd "/absolute/path/to/your-project" && pwd)
  skill_dir="$project_dir/.cursor/skills/b-end-design-system"
  mkdir -p "$(dirname "$skill_dir")"
  mkdir "$skill_dir"
  cp -R "$source_dir/SKILL.md" "$source_dir/LICENSE" \
    "$source_dir/components.manifest.json" "$source_dir/references" \
    "$source_dir/templates" "$source_dir/scripts" "$skill_dir/"
)
```

复制失败时，先检查新建目录再重试；命令同样拒绝覆盖不完整的安装。项目原有 `.cursorrules` 不会被修改。

也可用文件管理器在目标项目中新建 `.cursor/skills/b-end-design-system` 目录，将 `SKILL.md`、`LICENSE`、`components.manifest.json` 和完整的 `references`、`templates`、`scripts` 目录复制进去。不要只复制 `SKILL.md`。

如需用户级安装，将复制命令中的路径赋值替换为 `skill_dir="$HOME/.cursor/skills/b-end-design-system"`。选择一个安装范围即可，避免重复加载。下面的可选规则面向项目级安装，不能原样用于用户级路径。

项目级和用户级 Skill 的发现机制见 Cursor 官方 [Agent Skills 文档](https://cursor.com/docs/skills)。

## 可选：添加项目规则

Cursor 可按任务相关性选用 Skill，也支持手动调用。如需持续提醒 Agent 在 B 端界面任务中使用该 Skill，可在完成项目级安装后添加随附的 `.mdc` 规则。规则模板存放在源码仓库的 `integrations/cursor/`，避免在尚未安装 Skill 的源码仓库中自动生效。

```sh
(
  set -eu
  source_dir=$(cd "/absolute/path/to/b-end-design-system-source" && pwd)
  project_dir=$(cd "/absolute/path/to/your-project" && pwd)
  test -f "$project_dir/.cursor/skills/b-end-design-system/SKILL.md"
  mkdir -p "$project_dir/.cursor/rules"
  set -C
  cat "$source_dir/integrations/cursor/b-end-design-system.mdc" \
    > "$project_dir/.cursor/rules/b-end-design-system.mdc"
)
```

`set -C` 会拒绝已有规则文件；如有同名规则，请先检查其内容。规则使用 `alwaysApply: true`，正文将设计工作流限定于 B 端界面任务。Cursor 官方 [Rules 文档](https://prod.cursor.com/docs/rules) 说明了 `.mdc` 的 frontmatter 和文件引用：引用告知 Agent 应读取哪个文件，并不会自动内嵌文件内容。

## 在目标项目中验证

新建 Cursor 会话并打开目标项目，让启动发现机制运行。在 **Customize → Skills** 中确认出现 `b-end-design-system`。在 Agent 对话中输入 `/`，搜索并选择该 Skill；要求它读取已安装的 `SKILL.md`，从 Skill 目录打开 `references/05-page-templates-and-archetypes.md`，再选择适合的模板生成页面。这能检查完整资源是否可访问。若安装了可选规则，也请在 **Customize → Rules** 中确认该规则。

可选审计脚本需要 Python 3。在目标项目目录中，通过安装后的绝对路径调用脚本，并指定已有源码文件或目录：

```sh
(
  set -eu
  cd "/absolute/path/to/your-project"
  python3 "$PWD/.cursor/skills/b-end-design-system/scripts/audit-design-rules.py" src
)
```

源码目录名称不同时，请替换 `src`，并确认输出中的待测文件数量符合预期。该脚本基于启发式检查，不能替代人工检查清单，也不能证明 Cursor 已加载 Skill。用户级安装对应的脚本路径为 `"$HOME/.cursor/skills/b-end-design-system/scripts/audit-design-rules.py"`。

阅读 Skill 不需要安装前端依赖。只有将 TSX 模板用于应用时，才需要应用已配置 React、`lucide-react` 和 Tailwind CSS，并按现有项目调整模板。

本指南的文件复制与脚本命令已在临时目录验证；尚未实测 Cursor 客户端界面的加载与调用，请按上方步骤人工验收。
