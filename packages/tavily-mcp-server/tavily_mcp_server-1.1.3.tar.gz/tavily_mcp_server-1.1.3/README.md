# Tavily MCP Server 简化版

🚀 **Tavily搜索MCP服务** - 为AI智能体提供网络搜索能力的简化实现

## 📖 简介

Tavily MCP Server简化版是一个基于FastMCP构建的轻量级搜索服务，集成了Tavily AI搜索引擎，为AI智能体提供网络搜索功能。该项目是原Tavily MCP Server的精简版本，保留了核心功能，移除了不必要的复杂性。

## ✨ 核心功能

- 🔍 **网络搜索** - 使用Tavily AI引擎进行网络搜索
- 🎯 **域名过滤** - 支持包含/排除特定域名
- 🔐 **API密钥验证** - 安全的API访问控制
- 📝 **日志记录** - 基本操作日志
- 💡 **简化实现** - 提供两种服务器实现方式：MCP服务器和简化版服务器

## 🚀 快速开始

### 环境配置

1. 创建 `.env` 文件并配置必要的环境变量：

```env
# Tavily API密钥 (必需)
TAVILY_API_KEY=your_tavily_api_key_here

# MCP API密钥 (必需)
MCP_API_KEY=your_mcp_api_key_here
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

### 启动服务

#### 方式1：使用MCP服务器

```bash
python -m tavily_mcp_server.server
```

#### 方式2：使用简化版服务器

```bash
python fixed_server.py
```

## 🔧 使用方法

### 测试搜索功能

项目提供了一个测试脚本 `final_test.py`，可以用来测试搜索功能：

```bash
python final_test.py
```

该脚本会构建一个搜索请求，发送到服务器，并显示搜索结果。

### 手动构建请求

你也可以手动构建JSON-RPC请求并发送到服务器：

```json
{
  "jsonrpc": "2.0",
  "method": "search",
  "params": {
    "query": "你的搜索关键词",
    "max_results": 5,
    "search_depth": "basic",
    "include_domains": [],
    "exclude_domains": []
  },
  "id": 1
}
```

## 🛠️ 项目结构

- `tavily_mcp_server/` - MCP服务器实现
  - `server.py` - 主服务器代码
- `fixed_server.py` - 简化版服务器实现
- `final_test.py` - 测试脚本
- `studio_config.json` - 各平台MCP配置
- `.env` - 环境变量配置

## 🔐 安全性

- 服务器需要有效的API密钥验证
- 环境变量中需要配置Tavily API密钥和MCP API密钥

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🔗 相关链接

- [Tavily API文档](https://docs.tavily.com/)
- [FastMCP文档](https://github.com/jlowin/fastmcp)

---

**为AI智能体提供简单高效的搜索能力！** 🚀