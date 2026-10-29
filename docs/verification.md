# Verification notes / 核验记录

[Directory](../README.md) · [中文导航](../README.zh-CN.md)

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
