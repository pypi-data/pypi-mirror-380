这是一个 mcp server 的代码，以前用的是 paraformer-v2 模型识别，现在要切换到 qwen-3-asr-flash 模型识别，API 说明文档在 context/qwen-3-asr-flash.md

请你根据 API 说明文档，修改 douyin_mcp_server/server.py 代码，实现 qwen-3-asr-flash 模型识别，请将 ASR 识别作为一个单独的代码模块，可以同时支持传入 url 或者 本地音频识别，同时支持传递增强上下文提高识别准确率，将原来的 paraformer-v2 模型识别代码替换为 qwen-3-asr-flash 模型识别代码。

其他功能不变。