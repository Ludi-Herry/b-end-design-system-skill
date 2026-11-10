# 在 Google Antigravity 中安装

将完整 Skill 资源包安装到消费项目。仅在提示词中要求使用此设计系统，
不会安装其指令或配套资源。以下工作区安装方式适用于 Antigravity App、CLI 和 IDE。

以下命令适用于 POSIX shell（macOS、Linux 或兼容的 Windows shell）。
使用原生 PowerShell 时，请改用等效的建目录和复制操作，并保留“目标已存在则拒绝”的保护，
不要直接粘贴 shell 语法。克隆需要 Git；只有可选审计需要 Python 3。

## 1. 获取源资源包

在存放源码的目录中执行，不要在消费项目内克隆。
如果 `b-end-design-system-skill` 已存在，请另选一个新的克隆目录：

```sh
git clone https://github.com/Ludi-Herry/b-end-design-system-skill.git b-end-design-system-skill
cd b-end-design-system-skill
pwd
```

记下 `pwd` 输出的绝对路径。此仓库是**源目录**；
你的应用仓库是**消费项目**。

## 2. 安装到消费项目工作区

替换下面两个绝对路径，消费项目必须已存在。请整块执行：
子 shell 遇错即停，`mkdir` 会在复制前拒绝已存在的 Skill 目录，
不会合并或更新旧安装。

```sh
(
  set -eu
  source_dir='/absolute/path/to/b-end-design-system-skill'
  project_dir='/absolute/path/to/your-project'
  cd "$project_dir"
  mkdir -p .agents/skills
  target_dir="$PWD/.agents/skills/b-end-design-system"
  mkdir "$target_dir"
  cp -R "$source_dir/SKILL.md" "$source_dir/LICENSE" \
    "$source_dir/components.manifest.json" "$source_dir/references" \
    "$source_dir/templates" "$source_dir/scripts" "$target_dir/"
)
```

安装后的目录结构：

```text
.agents/skills/b-end-design-system/
├── SKILL.md
├── LICENSE
├── components.manifest.json
├── references/
├── templates/
└── scripts/
```

请将配套资源保留在 `SKILL.md` 旁，以便相对引用正常解析。
无需替换项目规则文件。若复制失败，请先检查新建的目标目录再重试；
即使只是部分安装，下次执行时 `mkdir` 也会拒绝该目录。

## 3. 检查发现与调用

打开**消费项目**并开始新对话。Antigravity 在对话开始时发现 Skill 名称和描述，
并读取相关 Skill。App 可在提示面板中输入 `/b-end-design-system` 显式调用；
CLI 也会将已发现的 Skill 暴露为斜杠命令。IDE 可在智能体侧栏的
**Customizations** 菜单中检查已启用的 Skill，然后在对话中提及名称：

```text
使用已安装的 b-end-design-system Skill 设计客户合同列表页。选择布局前，先读取页面模板参考规范。
```

请确认智能体读取了安装目录中的 `SKILL.md` 和配套参考文件。
仅凭回答合理，不能证明已发现 Skill。若未出现，请检查工作区根目录和
资源包路径，再开始新对话。

## 工作区与全局目录

[Antigravity 官方 Skill 文档](https://antigravity.google/docs/skills)
默认使用 `.agents/skills/`，同时向后兼容 `.agent/skills/`。
工作区安装请选择一个位置。全局安装时，请根据实际使用的客户端选择目录，
将同一完整资源包复制到新建的 `b-end-design-system` 子目录中，
并保留“目标已存在则拒绝”的保护：

| 客户端 | 全局 Skill 目录 |
| --- | --- |
| Antigravity App | `~/.gemini/config/skills/` |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills/` |
| Antigravity IDE | `~/.gemini/config/skills/`（也支持旧路径 `~/.gemini/antigravity/skills/`） |

## 可选：从项目中运行审计

从消费项目根目录，通过已安装脚本的绝对路径运行：

```sh
(
  set -eu
  cd '/absolute/path/to/your-project'
  python3 "$PWD/.agents/skills/b-end-design-system/scripts/audit-design-rules.py" ./src
)
```

将 `./src` 替换为待检查的代码目录或文件。若采用全局安装，
请将脚本路径替换为该安装位置的绝对路径。审计只使用 Python 标准库，
属于启发式检查，不能代替完整设计评审。TSX 模板假定应用已配置 React、
`lucide-react` 和 Tailwind 样式；安装 Skill 不会安装这些依赖。

本指南的文件复制与脚本命令已在临时目录验证；尚未实测 Antigravity App、CLI、IDE 客户端界面的加载与调用，请按上方步骤人工验收。
