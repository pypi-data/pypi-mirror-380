# News MCP Server

基于MCP协议的新闻获取服务器，支持热点新闻获取和新闻搜索功能。

## 功能特性

- 🔥 获取热点新闻（多个分类）
- 🔍 搜索新闻
- 🌐 RESTful API 接口
- 🐳 Docker 容器化部署
- 📊 健康检查

## API接口

### 健康检查
GET /health

### 获取新闻分类
GET /news/categories


### 获取热点新闻
GET /news/hot?category=general&limit=10

### 搜索新闻
GET /news/search?keyword=科技&limit=10


### MCP接口
/mcp


## 本地测试


1. 安装依赖：
```bash
pip install -r requirements.txt
运行测试：

bash
python src/mcp_server.py
启动服务器：

bash
python app.py
