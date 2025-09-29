# Wallpaper MCP Server

[![PyPI version](https://badge.fury.io/py/wallpaper-mcp.svg)](https://badge.fury.io/py/wallpaper-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A cross-platform MCP (Model Context Protocol) server for setting desktop wallpapers on Windows, macOS, and Linux.

一个跨平台的 MCP 服务器，用于在 Windows、macOS 和 Linux 上设置桌面壁纸。

## Features / 功能特性

- 🖼️ **Set wallpaper from URL** - Download and set wallpaper from any image URL
- 📁 **Set wallpaper from local file** - Use local images as wallpaper
- 📱 **Get screen resolution** - Automatically detect current screen resolution
- 🎨 **Smart image processing** - Auto-resize and crop images to fit screen perfectly
- 🌍 **Cross-platform support** - Works on Windows, macOS, and Linux

## Installation / 安装

### From PyPI

```bash
pip install wallpaper-mcp
```

### From Source / 从源码安装

```bash
git clone https://github.com/mcpcn/wallpaper-mcp
cd wallpaper-mcp
pip install -e .
```

### Using uv

```bash
uv pip install wallpaper-mcp
```

## Usage / 使用方法

### With Claude Desktop

Add to your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "wallpaper": {
      "command": "wallpaper-mcp"
    }
  }
}
```

Or if using `uv`:

```json
{
  "mcpServers": {
    "wallpaper": {
      "command": "uv",
      "args": ["--directory", "/path/to/wallpaper-mcp", "run", "wallpaper-mcp"]
    }
  }
}
```

## Available Tools / 可用工具

### 1. set_wallpaper_from_url
Set desktop wallpaper from an image URL.

**Parameters:**
- `url` (required): Image URL to download and set as wallpaper
- `resolution` (optional): Target resolution as `{width, height}` object

**Example:**
```
Set this aurora image as my wallpaper:
https://example.com/aurora.jpg
```

### 2. set_wallpaper_from_file
Set desktop wallpaper from a local image file.

**Parameters:**
- `file_path` (required): Path to local image file
- `resolution` (optional): Target resolution as `{width, height}` object

**Example:**
```
Set ~/Pictures/sunset.jpg as my desktop wallpaper
```

### 3. get_current_resolution
Get the current screen resolution.

**Parameters:** None

**Example:**
```
What's my current screen resolution?
```

## Platform Support / 平台支持

| Platform | Status | Method |
|----------|---------|---------|
| macOS | ✅ Supported | AppleScript via `osascript` |
| Windows | ✅ Supported | Windows API via `ctypes` |
| Linux (GNOME) | ✅ Supported | `gsettings` |
| Linux (KDE) | ✅ Supported | `qdbus` |
| Linux (XFCE) | ✅ Supported | `xfconf-query` |
| Linux (MATE) | ✅ Supported | `gsettings` |
| Linux (Other) | ✅ Supported | `feh` fallback |

## Supported Image Formats / 支持的图片格式

- JPEG/JPG
- PNG
- BMP
- GIF (static)
- WEBP
- TIFF

## Requirements / 依赖

- Python 3.10+
- Pillow (for image processing)
- requests (for downloading images)
- mcp (for MCP protocol support)

## Troubleshooting / 故障排除

### macOS Permission Issues
Grant Terminal or your app appropriate permissions in System Preferences > Security & Privacy > Privacy.

### Linux Desktop Detection
If auto-detection fails, manually set the environment variable:
```bash
export DESKTOP_SESSION=gnome  # or kde, xfce, etc.
```

### Windows Administrator Rights
Some operations may require administrator privileges.

## Development / 开发

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/mcpcn/wallpaper-mcp
cd wallpaper-mcp

# Install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Format code
black src/

# Lint
ruff check src/
```

## License / 许可证

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing / 贡献

Contributions are welcome! Please feel free to submit a Pull Request.

欢迎贡献！请随时提交 Pull Request。

## Credits / 致谢

Developed by [MCP Chinese Community](https://github.com/mcpcn)

由 [MCP 中文社区](https://github.com/mcpcn) 开发