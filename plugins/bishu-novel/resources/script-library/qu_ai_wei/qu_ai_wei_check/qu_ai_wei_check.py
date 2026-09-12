#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
qu_ai_wei_check.py - 调用 qu-ai-wei 对章节正文进行去 AI 味处理
参数: sys.argv[1] = 输入文件路径, sys.argv[2] = 输出文件路径
退出码: 0 = 成功, 1 = 失败
"""
import subprocess
import sys
import os
import json


def main():
    if len(sys.argv) < 3:
        print("Usage: qu_ai_wei_check.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Input file not found: {input_file}")
        sys.exit(1)

    # 读取输入文件内容
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text_content = f.read()
    except Exception as e:
        print(f"Failed to read input file: {e}")
        sys.exit(1)

    if not text_content.strip():
        print(f"Input file is empty: {input_file}")
        sys.exit(1)

    # 构造传给 skill 的参数
    payload = json.dumps({
        "input": text_content
    }, ensure_ascii=False)

    # 调用 qu-ai-wei skill
    cmd = [
        "npx", "skills", "run",
        "hardydai-cell/qu-ai-wei",
        "--skill", "去AI味",
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
        print("qu-ai-wei processing timed out")
        sys.exit(1)
    except FileNotFoundError:
        print("npx not found. Please ensure Node.js is installed and in PATH.")
        sys.exit(1)

    if result.returncode != 0:
        print(f"qu-ai-wei processing failed: {result.stderr}")
        sys.exit(1)

    # 将处理后的文本写入输出文件
    processed_text = result.stdout.strip()
    if not processed_text:
        print("qu-ai-wei returned empty output")
        sys.exit(1)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(processed_text)
    except Exception as e:
        print(f"Failed to write output file: {e}")
        sys.exit(1)

    print(f"qu-ai-wei processing completed: {input_file} -> {output_file}")
    sys.exit(0)


if __name__ == "__main__":
    main()