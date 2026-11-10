# 页面模板使用前提

这些 TSX 文件是参考组件，不是独立应用或可安装的组件库。安装 AI Skill 只会让助手能够读取这些文件。

复制模板前，业务应用需要具备：

- React 与 TypeScript，并由现有框架配置 JSX/TSX 编译。
- 使用业务项目已有的包管理器安装 `lucide-react`。
- 已配置 Tailwind CSS，且源码扫描范围包含复制后的组件位置。

例如，使用 npm 的已有应用可在业务项目目录安装图标依赖：

```bash
npm install lucide-react
```

沿用业务项目已有的 React、Tailwind 与框架配置。本仓库不提供 `package.json`、开发服务器、CSS 入口或 Tailwind 配置。

将选定的 `.tsx` 文件复制到应用源码目录，导入对应的命名导出，例如 `import { ListPageTemplate } from './list-page-template'`。接入真实业务数据前，请检查示例数据、操作处理与校验逻辑。运行业务项目已有的构建检查，并确认图标和样式正确呈现。

仅 `scripts/audit-design-rules.py` 需要 Python 3；脚本只使用标准库，无需安装 pip 包。请按 [SKILL.md](../SKILL.md#自动化校验脚本-lint-script) 使用脚本的绝对安装路径执行。
