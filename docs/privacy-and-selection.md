# Choosing an AI office tool: privacy and practical checks

[简体中文](#选择-ai-办公工具隐私与实用检查) · [Back to the directory](../README.en.md)

This is a checklist for comparing products, not a certification or a claim that any listed product meets these requirements. Check the current terms, settings, documentation and your organization's rules for the exact product, plan, region and configuration you intend to use.

## Before connecting work data

1. **Map the data flow.** Identify what the tool can read (prompts, files, email, calendars, meeting audio, search results and logs), which provider processes it, and which connected services or model providers receive it. Self-hosting an interface does not ensure that an external model or integration receives no data.
2. **Ask about retention and reuse.** For the relevant plan, check whether inputs or outputs may be used for model training or service improvement, the applicable default and opt-out, retention periods, deletion procedures, backups and subprocessors. Record a link and date for the policy you checked.
3. **Limit access.** Start with the minimum necessary account and resources; use read-only access where possible. Check administrative controls, shared-workspace permissions, audit logs and how to revoke a connection. Review an agent's proposed action, target and data before allowing it to send, change or delete anything consequential.
4. **Handle meetings carefully.** Check the applicable consent and workplace rules before recording or transcribing, notify participants as required, and review who can see and share the recording, transcript and summary.
5. **Use safe samples first.** Compare a few realistic tasks using synthetic or already-public material. Check output accuracy, citations, language support, permissions, export, human review and total cost. Never paste passwords, API keys, private customer records or confidential files into a public issue or pull request.
6. **Plan an exit.** Check export formats, how to revoke connected apps, and how to delete workspaces and associated data. Recheck the terms and permissions when the product or configuration changes.

## Compare the same task

For each candidate, keep a private record of the task, product and plan, date, source links, data recipients, permissions, retention and deletion terms, output quality and cost. Mark unknown answers as **unknown** rather than assuming a feature or policy. Share only a sanitized summary if you contribute findings to this public repository.

For example, to compare meeting tools, use a fictional transcript and ask each candidate for a summary and action items. Inspect errors and attribution, then separately check recording consent, retention and sharing controls in each vendor's current documentation. This example is a method, not a comparison result.

## Further reading

- [NIST Generative AI Risk Management Framework profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) — a broader framework for managing generative AI risks.
- [OWASP: sensitive information disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/) — data exposure risks in LLM applications.
- [OWASP: AI agent security](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) — least privilege and review of agent actions.

---

# 选择 AI 办公工具：隐私与实用检查

[English](#choosing-an-ai-office-tool-privacy-and-practical-checks) · [返回中文导航](../README.md)

这是一份选型检查清单，不代表任何收录产品已通过认证或满足这些要求。请针对实际使用的产品、版本、地区和配置，核对最新条款、设置、文档与所在组织的规定。

## 接入工作数据前

1. **梳理数据流。** 确认工具能够读取哪些内容（提示词、文件、邮件、日历、会议音频、搜索结果和日志），由谁处理，以及哪些模型供应商或连接的服务会收到数据。自行部署界面不等于外部模型或集成服务不会收到数据。
2. **核对保留和再利用。** 查看所选方案的输入和输出是否可能用于模型训练或服务改进、默认设置和退出方式、保留期限、删除流程、备份和分包处理方。记录所查政策的链接及日期。
3. **限制权限。** 从完成任务所需的最小账户和资源开始，能只读时优先只读。检查管理控制、团队共享权限、审计日志和连接撤销方式。允许智能体执行重要的发送、修改或删除操作前，核对操作、目标及涉及的数据。
4. **谨慎处理会议。** 录音或转录前核对适用的同意要求和组织规定，按要求告知参与者，并检查谁可以查看和分享录音、转录及摘要。
5. **先用安全样本。** 使用虚构或已公开的材料比较几个真实工作场景，检查准确性、引用、语言支持、权限、导出、人工复核及总成本。不要把密码、API 密钥、客户私人资料或机密文件提交到公开 Issue 或 PR。
6. **提前规划退出。** 检查导出格式、撤销应用连接的方法，以及工作空间和关联数据的删除方式。产品或配置发生变化时重新核对条款和权限。

## 用相同任务比较

针对每个候选产品，在私密位置记录任务、产品及方案、日期、来源链接、数据接收方、权限、保留与删除条款、输出质量和成本。不确定的项目标为**未知**，不要推测产品功能或政策。向本公开仓库贡献结果时，只分享去敏后的摘要。

例如，比较会议工具时，可用一份虚构的会议记录，分别要求生成摘要和待办事项，检查错误与归属；再单独查阅各厂商当前文档中的录音同意、保留及分享控制。这是比较方法，不是产品评测结果。

## 延伸阅读

- [NIST 生成式 AI 风险管理框架](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)：生成式 AI 风险管理的综合参考。
- [OWASP：敏感信息泄露](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/)：大模型应用中的数据泄露风险。
- [OWASP：AI 智能体安全](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html)：最小权限与智能体操作复核。
