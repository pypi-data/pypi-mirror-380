# Word文档内容读取MCP服务

一个专门用于读取Word文档内容的MCP（Model Context Protocol）服务，提供五个核心的文档读取功能。

## 功能特性

- **文档信息获取**: 获取Word文档的基本信息（标题、作者、创建时间等）
- **文本提取**: 提取文档中的所有文本内容
- **大纲结构**: 获取文档的标题层次结构
- **段落读取**: 获取指定段落的文本内容
- **文本搜索**: 在文档中搜索指定文本并返回位置信息

## 安装和配置

### 使用uv（推荐）

项目使用uv进行依赖管理，无需手动安装依赖：

```bash
# 进入项目目录
cd python/Word文档内容读取

# uv会自动管理所有依赖
```

### MCP配置

将以下配置添加到Claude Desktop配置文件中：

```json
{
  "mcpServers": {
    "Word文档内容读取": {
      "timeout": 60,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "word-document-reader-mcp@1.0.1"
      ],
      "env": {}
    }
  }
}
```

**注意：** 请将 `/path/to/Word文档内容读取` 替换为项目的实际路径。

### Claude Desktop配置文件位置

- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/claude/claude_desktop_config.json`

## 使用方法

配置完成后，在Claude中可以使用以下功能：

### 1. 获取文档信息

```
请获取文档 "example.docx" 的信息
```

### 2. 提取文档文本

```
请提取文档 "example.docx" 的所有文本内容
```

### 3. 获取文档大纲

```
请获取文档 "example.docx" 的大纲结构
```

### 4. 获取段落文本

```
请获取文档 "example.docx" 第3段的文本
```

### 5. 查找文本

```
在文档 "example.docx" 中查找 "重要信息"
```

## 可用工具

- `get_document_info_tool`: 获取文档信息
- `get_document_text_tool`: 提取文档文本
- `get_document_outline_tool`: 获取文档大纲
- `get_paragraph_text_from_document_tool`: 获取段落文本
- `find_text_in_document_tool`: 查找文档文本

## 项目结构

```
word_document_reader/
├── __init__.py          # 包初始化
├── main.py             # MCP服务主程序
├── tools.py            # 核心工具函数
└── utils.py            # 辅助工具函数
```

## 依赖项

- `python-docx>=1.1.0`: Word文档处理
- `fastmcp>=2.8.1`: MCP服务框架

## 错误处理

所有函数都包含完善的错误处理机制：
- 文件不存在时返回相应错误信息
- 无效参数时返回参数错误提示
- 处理异常时返回详细错误描述

## 注意事项

1. 支持的文件格式：`.docx`（如果传入的文件名没有扩展名，会自动添加`.docx`）
2. 段落索引从0开始计数
3. 搜索功能支持区分大小写和全词匹配选项
4. 返回的JSON数据使用UTF-8编码，支持中文显示

## 许可证

MIT License
