# 01 设计系统基石：Tokens 与基础规范 (Tokens & Foundations)

本规范定义 B 端界面中最底层的视觉物理法则与语义 Token。所有上层组件（原子、复合、页面）必须严格继承本规范，严禁硬编码任意色彩、圆角、阴影或边框。

---

## 一、色彩变量体系 (Color System)

B 端产品追求**长时间工作的低视觉疲劳、极高的信息扫描效率、精准的业务状态识别**。

### 1. 颜色分层架构

| 层次 | 变量前缀 | 说明与用法 |
| --- | --- | --- |
| **基础色盘 (Palette)** | `--color-blue-500` 等 | 物理色值阶梯（100-900），包含冷暖灰度与彩阶。业务代码**禁止直接使用**。 |
| **语义 Token (Semantic)** | `--color-brand-primary` 等 | 将色彩赋予功能职责。业务代码**必须使用**此层。 |
| **组件级 Token (Component)** | `--btn-primary-bg` 等 | 组件内部定制重写时使用，默认引用语义 Token。 |

### 2. 中性色微倾向法则 (Tinted Neutrals)

纯黑灰（`#000000` / `#808080`）在现代界面中显得沉闷死板。**中性色灰阶必须带微弱的主题色倾向**：
- 偏科技蓝品牌：中性色混合 2%–4% 的冷蓝（如 `slate` 或 `zinc` 偏蓝倾向），使文字、背景与主色浑然一体。
- 偏温暖/活力品牌：中性色混合极微弱的暖灰（如 `stone`）。

### 3. 核心语义 Token 清单

```css
:root {
  /* 页面与表面底色 */
  --color-bg-canvas: #f8fafc;       /* 整个 App 页面底色 */
  --color-bg-surface: #ffffff;      /* 卡片、表格、面板等内容承载面 */
  --color-bg-subtle: #f1f5f9;       /* 浅灰底，用于斑马纹、标签背景、输入框悬浮 */
  --color-bg-muted: #e2e8f0;        /* 禁用态背景、次级分割区底色 */

  /* 文字层级（保证对比度 WCAG AA 级以上） */
  --color-text-primary: #0f172a;    /* 主要标题、正文、强强调（Slate 900） */
  --color-text-secondary: #475569;  /* 次要信息、表头、属性标签、说明文案（Slate 600） */
  --color-text-tertiary: #94a3b8;   /* 占位符、图标辅助、不可用提示（Slate 400） */
  --color-text-disabled: #cbd5e1;   /* 禁用文字（Slate 300） */

  /* 边框体系 */
  --color-border-subtle: rgba(226, 232, 240, 0.8); /* 0.5px 精细微边框 */
  --color-border-default: #e2e8f0;                 /* 标准容器外框、输入框默认框 */
  --color-border-hover: #94a3b8;                   /* 悬浮交互态边框 */
  --color-border-focus: #3b82f6;                   /* 聚焦外光圈/主边框 */

  /* 品牌主色 */
  --color-brand-primary: #2563eb;   /* 主行动点、选中高亮、主按键 */
  --color-brand-hover: #1d4ed8;     /* 悬浮加深态 */
  --color-brand-active: #1e40af;    /* 按下激活态 */
  --color-brand-subtle: #eff6ff;    /* 品牌浅底（浅底深字 Badge、选中行背景） */

  /* 状态与语义色（四态） */
  --color-status-success: #16a34a;  /* 成功、正常、已完成、健康 */
  --color-status-success-bg: #f0fdf4;
  --color-status-warning: #ea580c;  /* 预警、待办、审核中、部分异常 */
  --color-status-warning-bg: #fff7ed;
  --color-status-danger: #dc2626;   /* 危险、阻断、错误、严重故障、扣款 */
  --color-status-danger-bg: #fef2f2;
  --color-status-info: #0284c7;     /* 运行中、常规提示、中性系统通知 */
  --color-status-info-bg: #f0f9ff;
}
```

---

## 二、0.5px 精细微边框规范 (0.5px Micro-Borders)

### 1. 核心设计原则
- **拒绝粗黑边框**：B 端系统最容易被浓重的 `1px solid #ccc` 搞得像上世纪表格。现代高级感的核心是**轻盈、通透、边界分明却不抢视觉重心**。
- **高 DPI 适配**：Retina 屏与 2K/4K 屏幕下，支持真正渲染 0.5px 的分割线与微边框。

### 2. 标准工程实现配方

```css
/* 配方 A：Tailwind / CSS 标准半透明微边框（首选） */
.border-subtle {
  border: 1px solid rgba(226, 232, 240, 0.7); /* 视觉效果等价于高清屏下的细腻边线 */
}

/* 配方 B：Retina 级物理 0.5px 分割线（用于卡片组、列表横线） */
.hairline-b {
  position: relative;
}
.hairline-b::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  right: 0;
  height: 1px;
  background-color: var(--color-border-subtle);
  transform: scaleY(0.5);
  transform-origin: 0 100%;
}
```

---

## 三、光学对齐与同心圆角 (Optical Alignment & Concentric Radius)

### 1. 同心圆角几何法则 (Concentric Radius Formula)

外层圆角与内层元素圆角如果相同，会出现内角显得“太尖”或留白不匀的视觉挤压缺陷。**必须严格执行同心圆角法则**：

$$R_{outer} = R_{inner} + Padding$$

例如：
- 外层容器内边距 `p-4`（16px），内部按钮圆角为 `r-md`（6px）时：
  $$R_{outer} = 6\text{px} + 16\text{px} = 22\text{px} \approx 20\text{px} \text{ 或 } 24\text{px}$$
- 卡片（`rounded-xl` 即 12px），卡片内边距 `12px`，内部嵌卡圆角应为 $12 - 12 = 0$（平直）或保留微圆角（4px）。

### 2. 标准圆角档位表

| Token | 数值 | 适用场景 |
| --- | --- | --- |
| `radius-none` | 0px | 紧贴屏幕的边栏、大屏全屏模块、折叠连体按钮中段 |
| `radius-xs` | 2px | 微型徽标、极小数值指示器 |
| `radius-sm` | 4px | 默认输入框（Input）、下拉框（Select）、表格内部紧凑按钮、代码块 |
| `radius-md` | 6px | 标准按钮（Button）、Toast 通知、气泡卡片（Popover） |
| `radius-lg` | 8px | 模态弹窗（Dialog/Modal）、抽屉（Drawer）内部模块、下拉浮层菜单 |
| `radius-xl` | 12px | 业务内容卡片（Card）、工作台 KPI 指标卡 |
| `radius-2xl` | 16px | 顶层悬浮面板、独立弹窗主容器 |
| `radius-full` | 9999px | 头像（Avatar）、胶囊状态标签（Badge）、开关滑块（Switch） |

### 3. 光学视觉重心法则 (Optical Center vs Mathematical Center)
- **拒绝机械居中**：包含文字+图标的按钮、带箭头的下拉菜单，不能仅用绝对数学居中。图标通常比字母有更高的视觉体量，需要根据视觉重心进行 1-2px 的光学微调。
- **弹窗垂直对齐**：模态弹窗（Modal）严禁放在屏幕正中垂直 50% 处（会产生“下坠”错觉），必须上浮，垂直位置固定在视口高度的 **38.2% 黄金分割位** 或 `margin-top: max(80px, 15vh)`。

---

## 四、阴影、层级与防裁切余量规范 (Shadows & Overflow Clearance)

### 1. 现代柔和弥散投影配方 (Layered Soft Shadows)

坚决杜绝生硬、浓黑的旧式投影。采用低不透明度、多层弥散、融入微蓝/冷灰调的现代光影配方：

```css
:root {
  /* 0 级：无阴影（平面卡片、内嵌模块） */
  --shadow-none: 0 0 #0000;

  /* 1 级：低位微浮（Card 常态、表格行悬浮高亮） */
  --shadow-card: 0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.04);

  /* 2 级：中位交互浮起（Card Hover 悬浮、下拉菜单 Dropdown、气泡 Popover） */
  --shadow-popover: 0 4px 6px -1px rgba(15, 23, 42, 0.06), 0 2px 4px -2px rgba(15, 23, 42, 0.05);

  /* 3 级：高位悬浮层（抽屉 Drawer、模态弹窗 Modal、浮动批量操作条 BulkActionBar） */
  --shadow-dialog: 0 20px 25px -5px rgba(15, 23, 42, 0.08), 0 8px 10px -6px rgba(15, 23, 42, 0.04);
}
```

### 2. 阴影被裁切的硬门禁 (Shadow Overflow Rule)

> **致命高频 Bug**：带阴影的卡片或浮层被父级 `overflow: hidden`、`overflow: auto` 或 `clip-path` 裁切成半截。

**铁律**：
- 阴影所在元素距离任意具有裁切属性（`overflow != visible`）的祖先容器边缘，其间距必须满足：
  $$\text{Margin/Padding} \ge \text{OffsetY} + \text{Blur} + \text{Spread}$$
- 当容器无法提供足够余量时，**严禁在内层挂深投影**；应将投影移至外层无裁切容器，或将内层降级为纯 `0.5px` 微边框描边区分层级。

---

## 五、间距与空间网格系统 (Spacing & Grid)

以 4px / 8px 为最小几何步进单位：

| 间距 Token | 数值 | 语义用法 |
| --- | --- | --- |
| `space-1` | 4px | 图标与文字间隙、内联标签小间距 |
| `space-2` | 8px | 紧凑表单行距、按钮内图标与文本间距、列表项内部元素空隙 |
| `space-3` | 12px | 表单项之间间距、卡片紧凑内边距（Compact Card Padding） |
| `space-4` | 16px | 标准容器内边距（Default Padding）、按钮两端留白、列表列间距 |
| `space-6` | 24px | 卡片与卡片之间间隙、区块（Section）纵向隔离、模态弹窗内边距 |
| `space-8` | 32px | 页面大模块（Section）分隔、空状态（Empty）留白 |
| `space-12` | 48px | 页面级主内容区与导航的大留白 |

---

## 六、排版与字阶 (Typography Hierarchy)

### 1. 字阶标准

| 级别 | 字号 / 行高 | 字重 (Font Weight) | 用途 |
| --- | --- | --- | --- |
| **Page Title** | 20px / 28px | 600 (Semibold) | 页面级一级主标题（PageHeader） |
| **Section Title** | 16px / 24px | 600 (Semibold) | 卡片大标题、模块分类标题、弹窗/抽屉主标题 |
| **Content Body** | 14px / 20px | 400 (Regular) | B 端核心正文、表格单元格数据、表单输入值、常规描述 |
| **Content Bold** | 14px / 20px | 500 (Medium) | 表格列头、关键字段名、高亮数值、主按钮文字 |
| **Caption / Help** | 12px / 16px | 400 (Regular) | 表单下方校验提示、次要辅助说明、时间戳、状态标签文案 |

### 2. 去除冗余解释性废话 (Zero Fluff Principle)
- **卡片与表单严禁加占位式副标题**：例如卡片标题是“用户列表”，不要再在下面挂一句浅灰色“这里展示了所有的用户列表”。靠精准的排版层级、间距与布局本身说话。
- **输入框占位符严禁废话**：姓名输入框默认就是“请输入姓名”，不要加“请在这里输入该员工的真实合法姓名”。

### 3. 排版高阶工程微细节 (Craftsmanship Details)

1. **暗色模式视网膜欺骗术 (Dark Mode Weight Compensation)**：
   - 人眼对“黑底白字”存在天然的光晕扩散错觉（Irradiation Phenomenon），导致深色背景下的字重看起来比浅色模式粗约 10%–15%，极易造成视觉发胖与刺眼疲劳；
   - **大厂规约**：切换为暗色模式（Dark Mode）时，代码层自动将全局主要字重**偷偷下调一档**（例如将 `font-medium (500)` 降为 `font-normal (400)`，`font-semibold (600)` 降为 `font-medium (500)`）。为了让人眼看起来一样粗，故意让代码参数不一样。
2. **等宽数字强制锁死 (Tabular Numerals 防抖)**：
   - B 端监控指标、KPI 看板、数据表格数值列、倒计时与金额统计，**必须全量启用等宽数字**：
     ```css
     .tabular-numbers {
       font-variant-numeric: tabular-nums;
     }
     ```
     在 Tailwind 中直接添加 `tabular-nums`。保证数字 0–9 拥有完全相等的排版物理宽度，彻底消灭数值动态递增、流式推送或筛选刷新时的左右横向乱抖。
3. **排版防孤字成行 (Text Wrap Balancing)**：
   - 页面主标题、卡片标题、表单引导文案统一启用 `text-wrap: balance` 或 `text-wrap: pretty`：
     ```css
     h1, h2, h3, .card-title {
       text-wrap: balance;
     }
     ```
     排版引擎自动平摊各行字数，绝不允许最后一行的末尾孤零零地掉下单字。
4. **行内图标 1/8 字高光学居中 (Inline Icon Optical Baseline)**：
   - 正文与按钮行内嵌图标（如 Lucide / Phosphor 图标）与相邻文字混合排版时，由于字体基线与图标盒模型的差异，图标重心往往偏上；
   - 统一对行内图标施加 `translate-y-[0.125em]` 或 `vertical-align: -0.125em`（即下移 1/8 个字高），使图标视觉质心与文字 x-height 精准咬合。

---

## 六、去 AI 味四大纯粹性铁律 (Anti-AI Taste & Tw93 Craftsmanship)

源自真实生产环境高频踩坑反思（EP20）：AI 自动生成的界面最容易陷入“五颜六色、卡片套卡片、大阴影发光”的廉价模板感，必须严格执行以下四大约束：

### 1. 页面默认平 (Zero Shadow on Cards)
- **页面不平是最大的 AI 味**：AI 最喜欢给每一个卡片都挂一层 `shadow-lg` 甚至外发光，导致页面漂浮杂乱。
- **规约**：页面所有常规卡片、表格容器、表单区域**一律默认纯平**，仅使用 `0.5px` 或 `1px` 微边框（`border border-border/40`）与微灰背景切分层级；
- **阴影的唯一合法归宿**：**阴影只留给离屏真实浮层**（如打开的下拉菜单 Dropdown、气泡卡片 Popover、弹出对话框 Modal、侧边抽屉 Drawer），绝不卡片套卡片。

### 2. 全页仅一个强调色 (Single Accent Rule)
- 严禁在同一屏内同时出现蓝主按钮、紫渐变标题、黄色卡片底纹与红绿混杂的标签；
- **一个界面只允许一个强调色**：用于唯一的主行动按钮（Primary Action），其余所有次要操作、标签、图标一律收敛为暖中性灰（Zinc/Stone）；只有在触发危险警告或成功终态时才允许出现少量的 Semantic 红/绿。

### 3. 灰用暖灰与字号 $\le 4$ 档
- **灰用暖灰**：严禁使用冷青灰（看起来像系统未响应死机）或纯黑底白字；优先采用带微温的暖灰阶（如 Zinc / Stone），呈现如纸张般的呼吸温润感；
- **字号严格 $\le 4$ 档**：坚决消灭只相差 1–2px 的杂乱层级。全页严格限定 4 档：**大数字 (24/28px) $\rightarrow$ 模块标题 (16px) $\rightarrow$ 正文与表格 (14px) $\rightarrow$ 辅助说明与标签 (12px)**。

### 4. 标题纯粹性与数字格式化
- **杜绝无意义悬顶小标签 (No Eyebrow)**：严禁在标题上方加一行无意义的大写灰小字（如 `DASHBOARD`、`ANALYTICS`）；靠排版层级直接说话；
- **杜绝标题内单词突兀着色**：严禁在标题中挑选一个单词刻意标蓝或倾斜（典型 AI 模板套路）；
- **数字必须带格式与物理单位**：所有金额、指标必须带千分位（如 `1,280,000.00`）并紧随单位（如“元”、“QPS”），严禁裸露无格式数字。
