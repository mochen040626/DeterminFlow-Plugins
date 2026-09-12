#!/bin/bash
# lnw-check.sh - 调用 long-novel-writer 进行章节校验
# 参数: $1 = 章节文件路径, $2 = 工作区路径

CHAPTER_FILE=$1
WORKSPACE=$2

# 设置 long-novel-writer 需要的环境变量（请替换为你的实际配置）
export NOVEL_API_KEY="sk-xxx"
export NOVEL_API_BASE_URL="https://your-api.com/v1"
export NOVEL_MODEL="your-model-name"

# 调用校验命令
# 具体命令需要根据 long-novel-writer 的实际 CLI 文档调整
npx skills run Da-loong/long-novel-writer --check "$CHAPTER_FILE" --workspace "$WORKSPACE"

# 如果校验不通过，脚本返回非零退出码，触发 DeterminFlow 的重试机制
if [ $? -ne 0 ]; then
  echo "Long-novel-writer validation failed for chapter: $CHAPTER_FILE"
  exit 1
fi

exit 0