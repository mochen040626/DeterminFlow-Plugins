#!/bin/bash
# qu_ai_wei_check.sh - 调用 qu-ai-wei 对章节正文进行去 AI 味处理
# 参数: $1 = 输入文件路径（章节正文）, $2 = 输出文件路径（处理后的章节正文）

INPUT_FILE=$1
OUTPUT_FILE=$2

# 读取输入文件内容
if [ ! -f "$INPUT_FILE" ]; then
  echo "Input file not found: $INPUT_FILE"
  exit 1
fi

# 读取文件内容并转义为 JSON 字符串
TEXT_CONTENT=$(cat "$INPUT_FILE" | python -c "import sys, json; print(json.dumps(sys.stdin.read()))")

# 调用 qu-ai-wei skill
npx skills run hardydai-cell/qu-ai-wei --skill "去AI味" -p "{\"input\": $TEXT_CONTENT}"

# 检查处理结果
if [ $? -ne 0 ]; then
  echo "qu-ai-wei processing failed for: $INPUT_FILE"
  exit 1
fi

# 注意：上述命令的输出会直接打印到 stdout，而不是自动写入文件。
# 如果你需要将输出写入文件，请根据实际输出格式调整。通常建议使用重定向：
# npx skills run hardydai-cell/qu-ai-wei --skill "去AI味" -p "{\"input\": $TEXT_CONTENT}" > "$OUTPUT_FILE"

echo "qu-ai-wei processing completed: $INPUT_FILE"
exit 0