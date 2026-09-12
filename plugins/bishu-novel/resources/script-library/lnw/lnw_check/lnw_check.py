#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lnw_check.py - 调用 long-novel-writer 进行章节校验
参数: sys.argv[1] = 章节文件路径, sys.argv[2] = 工作区路径
退出码: 0 = 校验通过, 1 = 校验失败或异常
"""
import subprocess
import sys
import os
import json
import shutil


def main():
    if len(sys.argv) < 3:
        print("Usage: lnw_check.py <chapter_file> <workspace>")
        sys.exit(1)

    chapter_file = sys.argv[1]
    workspace = sys.argv[2]

    if not os.path.isfile(chapter_file):
        print(f"Chapter file not found: {chapter_file}")
        sys.exit(1)

    # 读取章节内容
    try:
        with open(chapter_file, "r", encoding="utf-8") as f:
            chapter_content = f.read()
    except Exception as e:
        print(f"Failed to read chapter file: {e}")
        sys.exit(1)

    # 解析 npx 的真实路径（Windows 下是 npx.cmd）
    npx_path = shutil.which("npx")
    if not npx_path:
        print("npx not found. Please ensure Node.js is installed and in PATH.")
        sys.exit(1)

    # 构造传给 skill 的参数
    payload = json.dumps({
        "chapter_file": chapter_file,
        "chapter_content": chapter_content,
        "workspace": workspace
    }, ensure_ascii=False)

    # 调用 long-novel-writer skill
    cmd = [
        npx_path, "skills", "run",
        "jiaw-Zh/long-novel-writer",
        "-p", payload
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=600
        )
    except subprocess.TimeoutExpired:
        print("long-novel-writer validation timed out")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Failed to launch npx: {e}")
        sys.exit(1)

    # 输出 skill 的返回内容
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)

    # 根据返回码判断校验结果
    if result.returncode != 0:
        print(f"long-novel-writer validation failed for: {chapter_file}")
        sys.exit(1)

    print(f"long-novel-writer validation passed: {chapter_file}")
    sys.exit(0)


if __name__ == "__main__":
    main()