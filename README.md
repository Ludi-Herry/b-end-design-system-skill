# B端设计系统与组件规范 AI Skill (Ludi Design System Skill)

> **让 AI 生成的代码，第一次拥有资深高级 UI/UX 设计师的灵魂与品味。**  
> 一套彻底终结“AI 拼装页面毫无设计感、组件乱堆、弹窗抽屉滥用、色彩失控”的可执行 AI 设计系统资产。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![AI-Ready](https://img.shields.io/badge/AI--Ready-Cursor%20%7C%20Claude%20%7C%20Windsurf%20%7C%20AGY-emerald.svg)]()
[![Design System](https://img.shields.io/badge/Design%20System-B--End%20Enterprise-purple.svg)]()
[![Tokens: 0.5px & Concentric](https://img.shields.io/badge/Tokens-0.5px%20%7C%20Concentric%20Radius-orange.svg)]()

---

## 为什么需要这个 Skill？

你是否也经历过这样的问题？
- 让 AI 生成一个后台页面，它只会粗暴地把 `Button + Input + Table` 随机堆砌，缺乏合理的业务组织；
- 列表里明明应该用**右侧侧边抽屉 (Drawer)** 快速查看详情，AI 偏偏弹出一个巨大的模态弹窗把整个屏幕遮死；
- 稍微填完一段表单，鼠标不小心在遮罩空白处点了一下，弹窗直接静默关闭，辛苦录入的数据瞬间蒸发；
- 状态标签（Badge）红、绿、黄、紫全靠 AI 随缘上色，刺眼的深底色破坏表格扫读体验；
- 粗黑的 `1px solid #000`、机械死板的数学居中、带阴影的卡片被父级直接裁切成半截……

**根本原因：AI 从来不缺写代码的能力，它缺少的是成体系的「设计决策约束」与「组件选型否定判据」！**

本 Skill 将十余年 B 端企业级设计系统与交互法则，转化为 Agent、Claude Code、Cursor、Windsurf、Codex 可以直接理解并 100% 严格执行的 **“AI 可执行设计规则层”**。

---

## 核心能力与特色亮点

### 1. B端六大经典页面模板骨架 (Page Archetypes)
补齐了“组件库说有什么零件、页面模板说怎么组装”之间缺的那一层。内置：
- **查询列表页**（单列/双列、筛选栏三态、批量浮动条、独立表格横滚容器）
- **分步/分组表单页**（Top-aligned 标签置顶、失焦即时校验、离开防丢脏检查）
- **单据/高级详情页**（DetailHeader、DescriptionGrid 四层亲密度区隔、Tabs 协同页签）
- **指标工作台与看板**（3-4 个核心 KPI 控制、统一时间口径、轻量原生趋势图）
- **设置页**（自服务即时生效 vs 规则配置显式提交判据）
- **异常与结果页**（五态覆盖、403/404/500 四要素配齐）

### 2. 组件选型七大否定判据 (The Seven AvoidWhen Rules)
> **“缺的从来不是能用什么，而是不该用什么。”**
- **量级不匹配**：选项 < 5 个强制单选框平铺；选项过多强制下拉带搜索；
- **模态 ≠ 阻断**：查看详情首选侧边抽屉 (Drawer) 保留背景上下文；高危删除才上 ConfirmDialog；
- **时长阈值**：< 1 秒禁止展示骨架屏（防止强闪烁）；1-3 秒按钮 Spin；> 10 秒强制百分比与取消出口；
- **重要性错配**：严禁把关键报错藏在气泡 (Tooltip) 内部；
- **语义错位**：原地改状态用 Button，跨路由跳文档用 Link；改动即生效用 Switch，随整表提交用 Checkbox。

### 3. 视觉微调与美学硬门禁 (Aesthetic Rules)
- **0.5px 精细微边框**：告别粗笨大黑线，赋予界面通透轻盈的高级质感；
- **光学同心圆角法则**：$R_{outer} = R_{inner} + Padding$，彻底消灭内角挤压畸变；
- **光学视觉重心**：拒绝机械居中；弹窗垂直固定于视口 38.2% 黄金分割位；
- **Badge 80% 浅底深字法则**：柔和微色调背景搭配高对比深色文字，告别刺眼配色；
- **主操作唯一性**：一个独立操作区严禁并列两个 Primary 按钮；审批页中立无诱导。

---

## 仓库结构 (Repository Structure)

```text
b-end-design-system-skill/
├── SKILL.md                          # 核心执行引擎与大模型调度规范
├── README.md                         # 项目介绍、规范概览与使用指南
├── LICENSE                           # MIT 开源协议
├── components.manifest.json          # 机器可读组件清单与否定判据契约
├── .cursorrules                      # Cursor 一键开箱即用规则
├── .windsurfrules                    # Windsurf 一键开箱即用规则
│
├── references/                       # 模块化深度规范库 (随时检索)
│   ├── 01-design-tokens-and-foundations.md     # 色彩、排版、0.5px微边框、同心圆角、阴影防裁切
│   ├── 02-primitive-components.md              # Button层级、Badge业务映射、输入控件否定判据
│   ├── 03-overlays-dialog-drawer.md            # 模态与阻断解耦、弹窗vs抽屉决策树、三档推荐尺寸
│   ├── 04-composite-components.md              # 表格对齐与冻结列、FilterPanel三态、DescriptionGrid
│   ├── 05-page-templates-and-archetypes.md     # 六大页面模板骨架与业务配方
│   ├── 06-component-priority-and-anti-patterns.md # 七大否定判据、40+ 条高频避坑红线
│   └── 07-design-system-audit-checklist.md     # 15 项视觉与交互交付硬门禁
│
├── templates/                        # 工业级开箱即用代码实战模板
│   ├── list-page-template.tsx        # 标准查询表格 + 批量浮条 + 抽屉编辑 + 确认删除
│   ├── form-page-template.tsx        # Top-aligned 标签 + 卡片分组 + 脏检查防丢失
│   ├── detail-page-template.tsx      # DetailHeader + DescriptionGrid + Tabs + 时间线
│   └── dashboard-page-template.tsx   # 工作台问候 + 4个核心指标卡 + 原生柱状图
│
└── scripts/                          # 自动化合规检查工具
    └── audit-design-rules.py         # Python 自动化设计系统规则检查脚本
```

---

## 如何在你的 AI 工具中使用？

### 方式 1：Cursor 用户 (推荐)
直接将本仓库的 [`.cursorrules`](.cursorrules) 复制到你的项目根目录下，或者在 `.cursor/rules/` 目录下添加指向 `SKILL.md` 的引用即可。

### 方式 2：Claude Code / Antigravity (AGY) / Codex 用户

请在[中文安装指南目录](docs/)中选择对应客户端的指南，先部署完整资源包，再将以下提示词输入客户端对话框；它不是 Shell 安装命令：

```text
请严格遵循 b-end-design-system 规范，为我生成一个客户合同管理列表页。
```

### 方式 3：直接复制提示词给任意大模型 (通用 Prompt)
在任意 AI 工具（ChatGPT、Claude、DeepSeek、Kimi 等）中直接粘贴以下引导词：

```markdown
请你扮演一名资深高级 UI/UX 设计专家与前端工程架构师。
在接下来的页面设计与前端代码生成中，你必须 100% 遵守以下设计系统硬门禁：
1. 页面骨架：从查询列表、分组表单、高级详情、指标看板六大骨架中精准选型，杜绝组件乱堆；
2. 浮层选型：查看详情与轻编辑首选侧边抽屉(Drawer)以保留背景上下文；高危删除才使用确认弹窗，且严禁开启点击遮罩静默关闭；
3. 原子规范：一个操作区最多 1 个 Primary 按钮；Badge 严格坚守 80% 浅底深字黄金法则；数值金额列绝对右对齐；
4. 视觉质感：使用 0.5px 精细微边框，内外容器遵循同心圆角公式 R_outer = R_inner + Padding，去除所有占位说明废话。
```

---

## 贡献与交流 (Contributing)

欢迎提交 Issue 和 Pull Request！如果你在实际业务项目中发现了新的 B 端反模式或更好的组件配方，非常欢迎为本项目贡献你的智慧！

## 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源协议。无论是个人学习、团队规范制定还是商业化项目落地，均可自由使用与二开。
