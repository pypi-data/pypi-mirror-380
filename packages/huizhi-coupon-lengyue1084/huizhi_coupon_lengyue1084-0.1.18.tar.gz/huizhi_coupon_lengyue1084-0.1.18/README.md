一个简单的计算工具包，提供基本的数学运算和问候功能。

## 功能特性
- 提供幸运星计算功能
- 支持两个数字的加法运算
- 提供自定义问候功能

## 安装方法
```bash
pip install huizhi_coupon_lengyue1084
```

## 使用示例
```python
from calculate import lucky_star, num_add, greeting

# 计算幸运星
result1 = lucky_star(5)  # 返回: 500

# 计算两个数字的和
result2 = num_add(10, 20)  # 返回: 30

# 获取问候语
result3 = greeting("World")  # 返回: "Hello, World!"
```

## 服务器运行
```bash
python -m src.main
```

## 依赖项
- fastapi>=0.116.2
- uvicorn>=0.35.0



配置方法
要使用此服务，您需要在应用中添加以下MCP配置。服务支持三种传输方式：stdio（默认）、sse 和 streamable-http。

stdio 传输（默认）
直接在客户端配置如下MCP Server即可。

{
    "mcpServers": {
        "amap-mcp-server": {
            "command": "uvx",
            "args": [
                "amap-mcp-server"
            ],
            "env": {
                "AMAP_MAPS_API_KEY": "your valid amap maps api key"
            }
        }
    }
}
SSE 传输
SSE传输支持实时数据推送，适合远程部署MCP Server。

本地以SSE运行 amap-mcp-server：

$ export AMAP_MAPS_API_KEY=你的有效API Key
$ uv run server.py  sse  9009

INFO:     Started server process [50125]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
MCP客户端配置：

{
    "mcpServers": {
        "amap-mcp-server": {
            "url": "http://0.0.0.0:8000/sse"
        }
    }
}
Streamable HTTP 传输
本地以Streamable HTTP运行 amap-mcp-server：

$ export AMAP_MAPS_API_KEY=你的有效API Key
$ uvx amap-mcp-server streamable-http

INFO:     Started server process [50227]
INFO:     Waiting for application startup.
StreamableHTTP session manager started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
MCP客户端配置：

{
    "mcpServers": {
        "amap-mcp-server": {
            "url": "http://localhost:8000/mcp"
        }
    }
}

您可以在高德开放平台注册并获取API密钥。