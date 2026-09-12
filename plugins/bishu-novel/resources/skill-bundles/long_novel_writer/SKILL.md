---
name: long_novel_writer
description: |
  长篇网络小说的一体化创作与项目管理技能。用于用户提出长篇、开书、选题、榜单/趋势扫描、拆书、写大纲、
  黄金三章、章节续写、批量正文、去 AI 痕迹、质量检查、导入旧稿或跨会话续写时；
  覆盖市场证据、读者契约、人物与关系、世界观、冲突/爽点/情感线、卷纲与章纲、正文交付、状态台账和一致性验证。
metadata:
  display_name: 长篇小说写作
  version: 1.0.0
  category: writing
  workflow_only: true
---

  # 长篇小说写作

  把每部长篇当作可恢复、可验证、可持续迭代的项目，而不是一次性文本。保持用户语言、类型、叙事视角和已确认设定。

  ## 路由请求

| 用户意图                 | 先做        | 随后做                         |
| ------------------------ | ----------- | ------------------------------ |
| "开书、写长篇、从零开始" | Phase 1–3   | 建档后按需进入正文             |
| "扫描榜单、找趋势、选题" | Phase 1     | 输出带来源日期的候选矩阵       |
| "拆这本书/分析样章"      | Phase 2     | 输出商业三角、结构与可迁移机制 |
| "做设定/人物/世界观"     | Phase 3     | 更新故事圣经与读者契约         |
| "写大纲/卷纲/章纲"       | Phase 3     | 同步伏笔、时间线和章节承诺     |
| "写第 N 章/续写/批量写"  | Phase 4     | 每章后更新状态并执行 Phase 5   |
| "改稿/去 AI 味/质检"     | Phase 5–6   | 输出修改稿与问题清单           |
| "导入旧小说/接着写"      | Phase I1–I5 | 重建状态后续写，不重置已知事实 |

  ## Phase 5：质量检查

  执行三维检查：

  1. **情绪交付**：本章让目标读者期待、紧张、满足或心疼的具体位置是什么？回报是否兑现或合理延期？
  2. **契约安全**：是否偏离题材承诺、人物底线、视角、世界规则和平台尺度？
  3. **一致性**：时间、地点、称谓、能力、物品、伤势、知情范围、关系与伏笔是否连续？

  检查脚本只提供线索，不做机械删改。把严重问题、证据片段、建议动作和复核结果写入 `analysis/qa-report.md`。

  第 6 章检查一次新鲜度衰减，之后每 10 章做冷读与跨章重复检查；每卷做读者承诺、角色弧、问题/承诺、伏笔、节奏和 Canon 冲突审计。正文因果链保持顺序写作，审校视角可并行。相同失败出现两次，就把它沉淀为规则或确定性测试。

  黄金三章逐章做通俗复述：目标读者若不能用一句口语说清"主角要什么、遇到什么麻烦、这章赢或输了什么"，本章判为读者体验失败。反馈优先级高于自动评分。

  ## Phase 6：去 AI 痕迹七道门

  依次执行并保留剧情事实：

  1. **禁用词门**：删除空泛套话和高频过渡词串。
  2. **句法套路门**：打散同构排比、连续"不是…而是…"和均匀句长。
  3. **心理解释门**：把情绪标签改为动作、选择、误判或身体反应。
  4. **节奏门**：允许必要的短促、停顿、跳切和留白，避免段段总结。
  5. **对话门**：删除礼貌完整答句，加入回避、抢话、错位回应与角色口癖。
  6. **结尾门**：停止升华、感悟和主题总结，以新信息/动作/代价/决定收束。
  7. **解释腔门**：信任读者；同一信息只保留最有力量的一次。

  修改后重跑 Phase 5，防止去痕破坏连续性。

  ## 输出纪律

  - 保留用户已确认事实；新假设集中列出，不悄悄改设定。
  - 区分"证据""推断""建议"。实时扫描附来源与日期，文本分析附章节或片段位置。
  - 交付正文时先给正文，再给不超过必要程度的检查摘要。
  - 不在正文插入写作说明、占位符、模型自评或工具日志。
  - 修改已有稿件时保存原稿或生成新版本，并列出改动范围。
  - 每次行动产生文件、章节、报告、状态更新或明确决策之一。

  ## Human cold-read priority

  When a reader reports composition-like prose, weak continuation desire, platform mismatch, or hard-to-evaluate opening, freeze production, and rewrite chapter 1. Automated metrics are preflight only.

  ## Production hard gates

  - New projects target 2400-3200 Chinese characters per chapter; below 2000 blocks submission.
  - Before commit every chapter must complete: prose checks -> chapter cold review -> chapter-facts -> foreshadowing-reconcile -> fact projections -> quality-brief. Missing evidence keeps the transaction open.
  - At chapters 10, 30, 100, and 400 the runner pauses on longform-gate until the cross-chapter review exists, quality history is complete, repair debt is closed, and longform-health has no stall/fatigue/upgrade-decay warning.
