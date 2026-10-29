# Verification notes / 核验记录

[Directory](../README.en.md) · [中文导航](../README.md)

## Initial review / 首轮核验 · 2026-10-29

The 29 product descriptions were checked against public official product pages, documentation or repositories. This verifies that the stated use is described by the provider; it is **not** a hands-on evaluation, security assessment or endorsement. Products and policies change. Entries link to their official product page or source; the sources below give additional context where the name or description needed clarification.

通过公开的官方产品页面、文档或仓库核对了 29 个产品的用途描述。这只能说明厂商资料支持所写用途，**不代表上手评测、安全审计或背书**。产品和政策可能变化。条目本身链接至官网或源码；以下资料补充说明需要特别澄清的名称或用途。

- **Baizhi Office / 百智办公:** [official source and product overview](https://github.com/chaitin/MonkeyCode).
- **Claude / Cowork:** [official product page](https://claude.com/product/cowork) describes the transition into Claude; rollout varies by plan.
- **Microsoft Copilot:** [official product page](https://www.microsoft.com/en-us/copilot) describes work content and Microsoft 365 app integration.
- **Gemini Notebook / NotebookLM:** [Google's rename announcement](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/) and [source-based answers and citations](https://support.google.com/gemininotebook/answer/16269187).
- **ZoomMate:** [Zoom's announcement](https://www.zoom.com/en/blog/zoom-ai-companion-zoommate/) distinguishes ZoomMate from previous AI Companion offerings.
- **Doubao Work Companion / 豆包工作伙伴:** [official guide](https://aily.feishu.cn/hc/1u7kleqg_3d5z9ttt) describes workplace context and connected tasks.
- **DingTalk AI Assistant / 钉钉 AI 助理:** [official product page](https://page.dingtalk.com/wow/dingtalk/default/dingtalk/AIzhuli) describes messages, scheduling, documents and meetings.
- **Perplexity, Consensus and Otter:** their official help pages provide additional context on [search and sources](https://www.perplexity.ai/help-center/en/articles/10352903-what-is-pro-search), [research search](https://help.consensus.app/en/articles/9922660-how-to-search-best-practices), and [meeting notes](https://help.otter.ai/hc/en-us/articles/4425393298327-Otter-Notetaker-Overview).

An unauthenticated HTTP check of the 30 product and source links in the directory returned HTTP 200 for 27; ChatGPT, Microsoft Copilot and Gamma returned HTTP 403 to the automated client. A 403 does not establish that a page is unavailable to a normal browser. The check does not verify individual features, user access, privacy practices, or future availability.

对目录中的 30 个产品与源码链接进行未登录的 HTTP 检查：27 个返回 HTTP 200，ChatGPT、Microsoft Copilot 和 Gamma 对自动客户端返回 HTTP 403。403 不能证明普通浏览器无法访问。这项检查不能验证具体功能、用户访问权限、隐私实践或未来可用性。

## Work-agent expansion / 办公智能体扩充 · 2026-10-29

The following 15 additions and the updated Perplexity entry were checked against the public sources linked below. These are provider or project descriptions, not hands-on tests, security audits, or guarantees of availability. The earlier HTTP figures apply only to the initial 29-product snapshot above; they are not a link-check result for this expansion.

以下 15 个新增条目及更新后的 Perplexity 条目依据所列公开资料核对。资料来自产品或项目方，不代表上手实测、安全审计或可用性保证。上方 HTTP 数字只适用于首轮 29 个产品的快照，不是本轮扩充的链接检查结果。

An unauthenticated HTTP check of the 18 distinct links in the new or changed directory rows returned 200 for 17; Genspark returned 403 to the automated client, while its public page was readable through a separate web source. A 403 alone does not establish that the page is unavailable.

对本轮新增或修改的目录行中的 18 个不同链接进行未登录 HTTP 检查：17 个返回 200，Genspark 对自动客户端返回 403，但通过另一公开网页来源可读取其产品页面。403 本身不能证明该页面不可用。

- [Kimi Work](https://www.kimi.com/products/kimi-work) — desktop work with files and browser tasks / 本地文件与浏览器工作。
- [Alibaba Wukong](https://wukong.dingtalk.com/) and its [FAQ](https://wukong.dingtalk.com/docs/faq/) — computer tasks and DingTalk integration; its sources differ on invitation requirements, so check current access / 电脑任务与钉钉集成；不同资料对邀请码的说明不一致，请核对当前开放情况。
- [Skywork Desktop](https://skywork.ai/desktop/en/index.html) — office deliverables and desktop workflows / 办公交付物与桌面工作流。
- [Loomy](https://loomy.xunfei.cn/) — office files, data and connected tools / 办公文件、数据与工具连接。
- [OfficeAce](https://www.huaweicloud.com/product/officeace.html) — research and workplace content / 调研与办公内容。
- [AutoClaw](https://autoclaw.zhipuai.cn/docs/getting-started/what-is-autoclaw/) — desktop agent and multi-step work / 桌面智能体与多步骤工作。
- [Genspark Super App](https://superapp.genspark.ai/) — AI workspace, chat, email and office tools / AI 工作空间、聊天、邮件及办公工具。
- [Lindy](https://www.lindy.ai/) — meetings, connected apps and scheduled work / 会议、应用连接与定时工作。
- [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/desktop) — desktop interface; see also [messaging platforms](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/) / 桌面界面；另见消息平台文档。
- [Interpreter Workstation](https://github.com/openinterpreter/interpreter-workstation) — local or remote computer workspaces and model configuration / 本地或远程电脑工作台与模型配置。
- [PawWork](https://github.com/Astro-Han/pawwork) — office skills, scheduling, and model-key setup / 办公技能、定时任务与模型密钥配置。
- [Open Duet](https://github.com/Anil-matcha/open-duet) — agent delegation, routines and experimental status / 智能体委派、定时任务与实验性状态。
- [Comma](https://comma.surf/) — connected app tasks and self-hosting / 连接应用的任务与自托管。
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio/) — desktop agents and document handling / 桌面智能体与文档处理。
- [AStudio](https://agent.xfyun.cn/studio-guide/features) — workbench tasks, project folders and artifact preview / 工作台任务、项目文件夹及成果预览。
- [Perplexity Computer](https://www.perplexity.ai/products/computer) — research, connected workflows and plan availability / 调研、连接工具的工作流与方案适用范围。

## Scenarios and features expansion / 场景与功能扩充 · 2026-10-29

Fifteen products were added and the existing 44 entries were rewritten to distinguish intended uses and main features. Their descriptions draw on the linked public product pages and official documents below, including the earlier reviews. Sources describe provider or project claims, not independent testing or security assessment. Availability and configuration can change.

本轮新增 15 项，并为原有 44 项补充适用场景和主要功能。描述依据条目中的公开官网、以下官方资料及前述核验记录；这些是厂商或项目方资料，不代表独立实测或安全审计。产品可用性和配置可能变化。

The 16 distinct new product and source URLs were checked without authentication: 15 returned HTTP 200; Box returned HTTP 403 to the automated client, while its public product page was readable through a web source. A 403 alone does not establish that a page is unavailable.

本轮 16 个不同的新增产品与源码链接经未登录 HTTP 检查，15 个返回 200；Box 对自动客户端返回 403，但可通过网页来源读取其公开产品页。403 本身不能证明页面不可用。

### New entries / 新增条目

- [Baidu DuMate](https://cloud.baidu.com/product/dumate.html).
- [TRAE (TraeWork)](https://www.trae.cn/).
- [QoderWork](https://docs.qoder.com/qoderwork/introduction).
- [LobsterAI](https://lobsterai.youdao.com/) · [Source](https://github.com/netease-youdao/LobsterAI).
- [QwenPaw](https://github.com/agentscope-ai/QwenPaw).
- [Lingxi AI Assistant](https://ai.soho.komect.com/).
- [WorkDSH](https://github.com/techflag/workdsh).
- [GoodBuddy](https://mesalogo.github.io/goodbuddy/).
- [Kowork](https://getkowork.com/).
- [Open Cowork](https://github.com/coasty-ai/open-cowork).
- [OpenWorker](https://github.com/andrewyng/openworker).
- [Box Agent](https://www.box.com/agents).
- [Relevance AI](https://relevanceai.com/).
- [Asana AI Teammates](https://asana.com/product/ai/ai-teammates).
- [ClickUp Super Agents](https://clickup.com/brain/agents).

Additional context / 补充资料： [TRAE migration / 升级说明](https://docs.trae.cn/work_traework-to-traecode-data-migration) · [QoderWork introduction / 简介](https://docs.qoder.com/zh/qoderwork/introduction) · [QwenPaw browser beta / 浏览器测试版](https://github.com/agentscope-ai/QwenPaw/blob/main/website/public/docs/browser.en.md) · [ClickUp Super Agents / 官方说明](https://help.clickup.com/hc/en-us/articles/31010910371991-What-are-Super-Agents) · [Relevance AI documentation / 文档](https://relevanceai.com/docs/get-started/introduction).

### Further sources for updated entries / 原有条目补充资料

- Gamma: [official source 1](https://help.gamma.app/en/articles/7838093-how-do-i-create-a-new-presentation-document-or-webpage-in-gamma).
- Grammarly: [official source 1](https://www.grammarly.com/business/overview-one-pager.pdf).
- Canva: [official source 1](https://www.canva.com/help/using-magic-presentations/) · [official source 2](https://www.canva.com/help/about-magic-write/).
- WPS: [official source 1](https://ai.wps.cn/cms/Eluo8eI8.html).
- Perplexity: [official source 1](https://www.perplexity.ai/help-center/en/articles/10352903-what-is-pro-search) · [official source 2](https://www.perplexity.ai/products/computer).
- Gemini Notebook: [official source 1](https://support.google.com/gemininotebook/answer/16215270).
- Notion AI: [official source 1](https://www.notion.com/help/enterprise-search).
- Glean: [official source 1](https://docs.glean.com/user-guide/about/what-is-glean).
- Elicit: [official source 1](https://support.elicit.com/en/articles/14757543-getting-started-with-elicit-which-workflow-should-i-use).
- Consensus: [official source 1](https://help.consensus.app/en/articles/9922673-how-consensus-works).
- ZoomMate: [official source 1](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0083738).
- Otter: [official source 1](https://help.otter.ai/hc/en-us/articles/9156381229079-Meeting-Summary-Overview).
- Fireflies: [official source 1](https://fireflies.ai/).
- Fathom: [official source 1](https://help.fathom.video/en/articles/6049729).
- Zapier: [official source 1](https://help.zapier.com/hc/en-us/articles/22234847450893-Zap-workflows-quick-start-guide).
- Make: [official source 1](https://help.make.com/whats-a-scenario-and-which-type-should-you-use).
- n8n: [official source 1](https://docs.n8n.io/).
- Dify: [official source 1](https://docs.dify.ai/en/home).

## Further workbench additions / 工作台补充 · 2026-10-29

The eight additions below were checked against public provider or project documentation. These sources describe product capabilities, not independent testing, security assessments, or guarantees; features can depend on configuration or plan.

以下八个新增条目依据厂商或项目方的公开资料核对，不代表独立实测、安全审计或任何保证；功能可能因配置或方案而异。

An unauthenticated HTTP check returned 200 for all eight new directory links. This does not verify user access or product behavior.

八个新增目录链接经未登录 HTTP 检查均返回 200；这不代表已验证用户访问权限或产品实际表现。

- [QwenWork / 千问办公](https://help.aliyun.com/zh/qwenwork/) · [product introduction / 产品介绍](https://qwenwork.cn/docs/product-introduction).
- [Coze / 扣子](https://docs.coze.cn/) · [desktop guide / 桌面端指南](https://docs.coze.cn/quick-start-coze-desktop).
- [AionUi](https://github.com/iOfficeAI/AionUi/) · [中文说明](https://github.com/iOfficeAI/AionUi/blob/main/docs/readme/readme_ch.md).
- [Eigent](https://www.eigent.ai/) · [source / 源码](https://github.com/eigent-ai/eigent).
- [CoWork OS](https://coworkosapp.com/) · [getting started / 入门](https://github.com/CoWork-OS/CoWork-OS/blob/main/docs/getting-started.md).
- [Pipali](https://github.com/khoj-ai/pipali) — beta / 测试阶段。
- [Nexus](https://github.com/nexus-research-lab/nexus) · [中文说明](https://github.com/nexus-research-lab/nexus/blob/main/README_zh.md).
- [LaborAny](https://github.com/laborany/laborany) · [project site / 项目主页](https://laborany.github.io/).

## Workbench additions / 办公工作台补充 · 2026-10-29

The following entries are based on public official product or project information, not independent tests or privacy assurances. Capabilities and availability may vary by plan, region, or configuration.

以下条目依据公开的官方产品或项目资料整理，不代表独立实测或隐私保证。功能和可用性可能因方案、地区或配置而异。

The ten new directory links returned HTTP 200 in an unauthenticated check; this does not verify feature access or product behavior.

十个新增目录链接经未登录 HTTP 检查均返回 200；这不代表已验证功能访问权限或产品实际表现。

- [TeleAgent / 星辰超级智能体](https://www.teleai.com.cn/product/teleagent).
- [Dume Cowork](https://www.dume.ai/cowork).
- [Adamant](https://adamantcore.ai/).
- [OpenWork](https://openworklabs.com/) · [source / 源码](https://github.com/different-ai/openwork/).
- [AnythingLLM](https://anythingllm.com/) · [documentation / 文档](https://docs.anythingllm.com/).
- [Abacus AI Desktop](https://abacus.ai/teams/desktop).
- [Nano Work / 纳米 Work](https://work.n.cn/) · [360 product information / 官方产品资讯](https://weishi.360.cn/n/13047.html).
- [ASI:Work](https://asi1.ai/work).
- [Abu / 阿布](https://github.com/PM-Shawn/Abu-Cowork) · [project site / 项目主页](https://abuwork.com/).
- [Kun](https://github.com/KunAgent/Kun) — review license terms / 使用前核对许可条款。
