# Contributing / 贡献指南

Thank you for helping keep this directory useful. English and Chinese contributions are welcome, including tool suggestions, corrections, translations, and broken-link reports.

感谢你帮助维护这个导航。欢迎使用中文或英文推荐工具、纠错、翻译及反馈失效链接。

## Before you post / 提交前请注意

**Issues, pull requests, comments, and commit history are public.** Do not submit API keys, passwords, access tokens, personal information, private messages, customer documents, or logs containing sensitive data. Use fictional or anonymized examples and check links for credentials, personal identifiers, tracking parameters, or affiliate codes. Link only to information that is already public and that you are entitled to share.

**Issue、Pull Request、评论和提交历史都是公开的。** 请勿提交 API 密钥、密码、访问令牌、个人信息、私人消息、客户文件或含敏感信息的日志。使用虚构或匿名化示例，并检查链接中是否包含凭据、个人标识、跟踪参数或推广联盟代码。只链接已公开且你有权分享的信息。

Do not submit private dashboards, account-specific links, or material that requires someone else's login. Maintainers assess public evidence; they do not need access to your account or private files. Removing a public comment or file may not remove it from Git history or other copies.

请勿提交私人控制台、账号专属链接或需要他人登录才能查看的资料。维护者依据公开证据审核，无需访问你的账号或私人文件。删除公开评论或文件不一定能清除 Git 历史或其他副本。

## Suggest a tool / 推荐工具

[Open a tool suggestion](https://github.com/ct-jaryn/awesome-ai-office-tools/issues/new/choose) or submit a pull request with:

1. Product name and official, public product URL.
2. The best-fitting category and a short, factual description of its workplace use.
3. A public official source supporting the description, and a note on your affiliation, if any. Self-submissions are welcome.
4. A short explanation of why it belongs in the directory.

请提供产品名称、公开官网、适合的分类、简短的办公用途描述、可核实的公开官方来源及推荐理由；如与产品有关联请说明，欢迎自荐。

## Review criteria / 收录与复核标准

- The product should have a clear knowledge-work use within an existing category, a public official page or repository, and enough current documentation to support the description. General model lists, unrelated developer infrastructure, and duplicate products are outside this directory's scope.
- Prefer a specific use case over a slogan. Do not present vendor claims as independent tests or rankings. Cite public evidence for claims that are not apparent from the linked product page; note when access or availability could not be verified.
- Review reported changes, broken links, shutdowns, archived repositories, and duplicates against current evidence. A timeout or access restriction alone does not prove a product has shut down. Correct or remove an entry when the evidence warrants it.

- 产品应有符合现有分类的明确知识工作用途、公开官网或仓库，以及足以支持描述的当前文档。通用模型清单、无关的开发基础设施和重复产品不属于本导航范围。
- 优先描述具体用途，不使用宣传口号；不要将厂商说法写成独立测试或排名。产品页面无法直接支持的描述应附公开证据；无法验证访问或可用性时请注明。
- 根据当前证据处理变更、失效链接、停服、归档仓库及重复项的反馈。超时或访问受限本身不能证明产品已经停服；证据充分时修正或移除条目。

## Pull requests / 提交 PR

- Search both READMEs and existing issues to avoid duplicates. 检查双语页面及现有 Issue，避免重复。
- Add or update the same item in the Chinese `README.md` and English `README.en.md`, preserving category and order. If translation is difficult, a suggestion in an issue is welcome. 请同步中文 `README.md` 与英文 `README.en.md` 的分类、顺序和内容；翻译有困难可先提交 Issue。
- Link to public official sources; use neutral descriptions, avoid unverifiable claims, tracking or affiliate links, and unsupported pricing or privacy promises. 使用公开官方来源与客观描述，避免无法核实的说法、跟踪或推广联盟链接，以及未经证实的价格或隐私承诺。
- Explain the change and disclose affiliation. By contributing original content you agree to its distribution under [CC BY 4.0](LICENSE). 说明修改并披露关联；提交原创内容即同意按 CC BY 4.0 分发。

If you have Python 3.9 or newer, run `python3 scripts/check_directory.py` before submitting. The check is offline: it checks categories, link order, local Markdown links and some common tracking parameters, but cannot verify external links, product claims, translation quality or all privacy risks. For checker changes, also run `python3 -m unittest discover -s scripts -p 'test_*.py' -v`. When adding or renaming a category, update `CATEGORY_HEADINGS` in the checker as well.

如已安装 Python 3.9 或更新版本，提交前请运行 `python3 scripts/check_directory.py`。该检查不联网，检查分类、链接顺序、本地 Markdown 链接及部分常见跟踪参数，但不能验证外链、产品事实、翻译质量或所有隐私风险。修改检查器时还需运行 `python3 -m unittest discover -s scripts -p 'test_*.py' -v`；新增或重命名分类时，也请更新检查器中的 `CATEGORY_HEADINGS`。

Maintainers review relevance, public evidence, link validity, clarity, and duplication. Inclusion is at maintainer discretion; the featured placement of Baizhi Office is editorial and is not a ranking. Respect the [Code of Conduct](CODE_OF_CONDUCT.md).

维护者根据相关性、公开证据、链接、表述与重复情况审核，是否收录由维护者决定。百智办公的置顶属于编辑安排，并非排名。请遵守[行为准则](CODE_OF_CONDUCT.md)。
