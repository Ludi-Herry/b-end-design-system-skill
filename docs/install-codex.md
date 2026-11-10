# 在 Codex 中安装

本指南将完整 Skill 文件复制到本机 Codex 的发现目录。
仅输入提示词不会复制或安装文件。

## 环境与源码

需要 Git 和 POSIX shell，例如 Linux/macOS 的 Bash 或 Windows 的 Git Bash。
使用系统文件管理器时，先创建全新的目标文件夹，再复制下方列出的全部六项，
保留目录结构；目标已存在时应停止，避免覆盖。只有可选审计脚本需要 Python 3。
TSX 模板要求项目已配置 React/TypeScript、`lucide-react` 和 Tailwind CSS；
安装 Skill 不会安装这些应用依赖。

在存放源码的目录中克隆上游仓库：

```sh
git clone https://github.com/Ludi-Herry/b-end-design-system-skill.git
cd b-end-design-system-skill
```

已有克隆时，直接进入该仓库根目录。下方复制命令必须在这里执行，
确保当前目录包含 `SKILL.md`、`LICENSE` 和三个资源目录。

## 选择范围并复制完整文件

| 范围 | 目标目录 |
| --- | --- |
| 项目级 | `<consumer-project>/.agents/skills/b-end-design-system/` |
| 用户级 | `~/.agents/skills/b-end-design-system/` |

选择一个范围。将 `/absolute/path/to/your-project` 替换为使用该 Skill 的项目绝对路径；
若需用户级安装，将 `skill_dir` 赋值替换为注释中的写法。不要重复安装同名 Skill。

```sh
(
  set -eu
  skill_dir="/absolute/path/to/your-project/.agents/skills/b-end-design-system"
  # 用户级安装请改用： skill_dir="$HOME/.agents/skills/b-end-design-system"
  mkdir -p "$(dirname "$skill_dir")"
  mkdir "$skill_dir"
  cp -R SKILL.md components.manifest.json LICENSE references templates scripts "$skill_dir/"
)
```

普通 `mkdir` 在目标已存在时会失败，`set -e` 随即停止，避免覆盖已有安装。
若创建目录后复制失败，请先检查部分复制的目标目录再处理。
`SKILL.md`、`components.manifest.json`、`LICENSE` 应直接位于 Skill 目录下，
与 `references/`、`templates/`、`scripts/` 三个目录同级。

## 确认发现并调用

在使用该 Skill 的项目中打开 Codex。CLI 或 IDE 扩展中运行 `/skills`，
或输入 `$` 并选择 `b-end-design-system`；桌面应用中查看 Skills。
明确调用示例：

```text
$b-end-design-system 请根据随附参考规范和检查清单审查客户列表页。
```

Codex 会自动检测 Skill 变化；未出现时重启 Codex。
检查所选 Skill 指向本次安装目录，并确认回复实际使用随附参考规范。
若未出现，请检查目标目录是否含 `SKILL.md`；项目级安装的会话是否位于使用项目中；
客户端设置或组织策略是否允许本地 Skill。

文件复制成功与客户端实际发现、调用是不同的验证步骤。
本指南尚未验证客户端 UI 中的发现和调用。

## 从使用项目运行可选审计

进入使用该 Skill 的项目或任意工作目录，将 `skill_dir` 设为上方选定的绝对安装路径。
用户级安装请改用 `skill_dir="$HOME/.agents/skills/b-end-design-system"`。
将审计目标替换为真实存在的源码文件或目录：

```sh
skill_dir="/absolute/path/to/your-project/.agents/skills/b-end-design-system"
python3 "$skill_dir/scripts/audit-design-rules.py" "/absolute/path/to/your-project/src"
```

脚本使用绝对路径，因此不依赖当前工作目录。检查输出，确认扫描了预期文件；
脚本的模式检查仅作为 `references/` 中人工检查清单的补充。

发现目录与调用方式依据 [Codex 官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。
