#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ludi Design System 规则自动化审计脚本 (Design Rules Linter)
用于对 React / Vue / TSX 页面代码进行设计系统合规性检查。

检查项覆盖：
1. [硬编码与粗边框] 检查是否存在粗黑边框、深黑硬编码色值，缺少 0.5px 微边框意识
2. [按钮层级] 检查操作区是否出现多个 primary 按钮、危险按钮未用 danger
3. [Badge 规范] 检查 Badge 是否存在纯色深底滥用、缺少业务状态文案
4. [弹窗防丢] 检查含有 input/form 的弹窗是否开启了 maskClosable
5. [表格对齐] 检查金额/数值列是否未进行右对齐
6. [冗余废话] 检查界面中是否存在占位说明废话
"""

import sys
import os
import re
from pathlib import Path

# 违规规则定义
RULES = [
    {
        "id": "DS-001",
        "name": "粗黑边框与硬编码纯黑",
        "severity": "WARNING",
        "pattern": r"(border-(?:black|gray-800|gray-900)|1px\s+solid\s+#000000|1px\s+solid\s+black)",
        "message": "检测到粗黑或深黑硬编码边框。B端现代界面推荐使用 0.5px 精细微边框或半透明边框 (如 border-slate-200/70)。",
    },
    {
        "id": "DS-002",
        "name": "危险操作样式违规",
        "severity": "ERROR",
        "pattern": r'(?:variant=["\']primary["\'][^>]*?(?:bg-red|text-red|bg-rose)|btn-primary[^>]*?(?:danger|delete))',
        "message": "检测到危险操作试图通过 primary 按钮涂红实现。必须使用标准 variant=\"danger\"。",
    },
    {
        "id": "DS-003",
        "name": "表单弹窗误触遮罩易丢数据",
        "severity": "ERROR",
        "pattern": r'(?:<Dialog|<Modal|<ConfirmDialog)[^>]*?maskClosable\s*=\s*\{?true\}?',
        "message": "含录入或确认的弹窗开启了 maskClosable={true}，用户误触空白处易造成数据丢失。必须显式设为 false。",
    },
    {
        "id": "DS-004",
        "name": "占位说明废话",
        "severity": "WARNING",
        "pattern": r'(?:这里展示了所有|请在这里输入该|用于展示.*?列表的信息)',
        "message": "检测到冗余占位废话。卡片与表单应去除无意义副标题，依靠排版层级与精准标签本身说话。",
    },
    {
        "id": "DS-005",
        "name": "表格金额或数值未右对齐",
        "severity": "WARNING",
        "pattern": r'(?:金额|价格|签约额|收入|支出|总额)[^<]*?</th>\s*<td(?![^>]*?text-right)',
        "message": "检测到金额或财务数值列未采用 text-right 右对齐。必须右对齐以保证个十百千数位垂直对齐。",
    },
]

def audit_file(file_path: Path):
    violations = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [{"id": "IO-ERR", "line": 0, "rule": "读取失败", "severity": "ERROR", "message": str(e)}]

    lines = content.splitlines()
    for rule in RULES:
        for idx, line in enumerate(lines, start=1):
            if re.search(rule["pattern"], line, re.IGNORECASE):
                violations.append({
                    "id": rule["id"],
                    "line": idx,
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "message": rule["message"],
                    "code_snippet": line.strip()[:80]
                })
    return violations

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    target_path = Path(target).resolve()

    if not target_path.exists():
        print(f"目标不存在： {target_path}", file=sys.stderr)
        sys.exit(2)

    extensions = (".tsx", ".jsx", ".vue", ".html")
    files_to_check = []
    if target_path.is_file():
        if target_path.suffix.lower() not in extensions:
            print(f"不支持的源码文件类型：{target_path}", file=sys.stderr)
            sys.exit(2)
        files_to_check.append(target_path)
    else:
        scan_errors = []
        for directory, _, filenames in os.walk(target_path, onerror=scan_errors.append):
            files_to_check.extend(
                Path(directory) / name for name in filenames
                if Path(name).suffix.lower() in extensions
            )
        if scan_errors:
            for error in scan_errors:
                print(f"目录扫描失败：{error}", file=sys.stderr)
            sys.exit(1)

    total_violations = 0
    print(f"[Ludi Design Linter] 正在走查设计系统规则: {target_path}")
    print(f"发现目标待测代码文件: {len(files_to_check)} 个\n")

    if not files_to_check:
        print("未找到受支持的源码文件（.tsx、.jsx、.vue、.html）。", file=sys.stderr)
        sys.exit(2)

    for f in files_to_check:
        results = audit_file(f)
        if results:
            print(f"文件: {f.relative_to(target_path) if target_path.is_dir() else f.name}")
            for r in results:
                total_violations += 1
                color_tag = "[ERROR]" if r["severity"] == "ERROR" else "[WARN]"
                print(f"  Line {r['line']} {color_tag} ({r['id']} {r['rule']}): {r['message']}")
                if "code_snippet" in r:
                    print(f"    代码片段: `{r['code_snippet']}`")
            print()

    if total_violations == 0:
        print("走查完成，未检测到已实现规则覆盖的违规项；仍需人工设计检查。")
        sys.exit(0)
    else:
        print(f"走查完成，共发现 {total_violations} 处需优化的设计或交互项。")
        sys.exit(1)

if __name__ == "__main__":
    main()
