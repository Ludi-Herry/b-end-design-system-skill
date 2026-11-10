# 在 Windsurf（Cascade）中安装

将完整 Skill 资源包安装到你在 Windsurf 中打开的项目。
仅输入设计提示词，不会安装 Skill 或其配套资源。

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

## 2. 复制到消费项目

替换下面两个绝对路径，消费项目必须已存在。请整块执行：
子 shell 遇错即停，`mkdir` 会在复制前拒绝已存在的 Skill 目录，
不会合并或更新旧安装。

```sh
(
  set -eu
  source_dir='/absolute/path/to/b-end-design-system-skill'
  project_dir='/absolute/path/to/your-project'
  cd "$project_dir"
  mkdir -p .windsurf/skills
  target_dir="$PWD/.windsurf/skills/b-end-design-system"
  mkdir "$target_dir"
  cp -R "$source_dir/SKILL.md" "$source_dir/LICENSE" \
    "$source_dir/components.manifest.json" "$source_dir/references" \
    "$source_dir/templates" "$source_dir/scripts" "$target_dir/"
)
```

安装后的目录结构：

```text
.windsurf/skills/b-end-design-system/
├── SKILL.md
├── LICENSE
├── components.manifest.json
├── references/
├── templates/
└── scripts/
```

请保留完整结构，`SKILL.md` 会引用配套目录。
无需替换规则文件，可保留现有 `.windsurfrules`。
若复制失败，请先检查新建的目标目录再重试；即使只是部分安装，
下次执行时 `mkdir` 也会拒绝该目录。

## 3. 检查发现与调用

在 Windsurf 中打开**消费项目**。进入 Cascade 的三点菜单，
打开自定义设置中的 **Skills**，检查是否出现 `b-end-design-system`，
然后在 Cascade 中显式调用：

```text
@b-end-design-system 使用已安装的 Skill 设计客户合同列表页。选择布局前，先读取页面模板参考规范。
```

Cascade 也会自动选择相关 Skill。请确认它读取了安装目录中的
`SKILL.md` 和配套资源；仅凭回答看起来合理，不能证明已发现 Skill。
若未出现，请核对打开的项目和安装路径。

## 当前官方文档与路径选择

[Windsurf 的 Skill 文档地址](https://docs.windsurf.com/windsurf/cascade/skills)
目前重定向到 [Devin Desktop 的 Cascade 文档](https://docs.devin.ai/desktop/cascade/skills)。
该文档仍支持旧工作区路径 `.windsurf/skills/`；
后继客户端 Devin Desktop 的首选路径则是 `.devin/skills/`。
本指南使用 Windsurf 路径；若为 Devin Desktop 安装，请同时替换安装和审计命令中的
`.windsurf/skills/` 为 `.devin/skills/`。当前后继客户端文档还列出
跨工具发现路径 `.agents/skills/`，以及全局目录
`~/.codeium/windsurf/skills/` 和 `~/.config/devin/skills/`。
同一次安装请选择一个位置，避免重复副本。

## 可选：从项目中运行审计

从消费项目根目录，通过已安装脚本的绝对路径运行：

```sh
(
  set -eu
  cd '/absolute/path/to/your-project'
  python3 "$PWD/.windsurf/skills/b-end-design-system/scripts/audit-design-rules.py" ./src
)
```

将 `./src` 替换为待检查的代码目录或文件。审计只使用 Python 标准库，
属于启发式检查，不能代替完整设计评审。TSX 模板假定应用已配置 React、
`lucide-react` 和 Tailwind 样式；复制 Skill 不会安装应用依赖。

本指南的文件复制与脚本命令已在临时目录验证；尚未实测 Windsurf/Devin 客户端界面的加载与调用，请按上方步骤人工验收。
