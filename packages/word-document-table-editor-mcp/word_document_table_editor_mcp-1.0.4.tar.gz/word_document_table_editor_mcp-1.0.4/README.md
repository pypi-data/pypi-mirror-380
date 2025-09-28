# Word文档表格编辑 MCP服务

这是一个基于Model Context Protocol (MCP)的Word文档表格编辑服务，提供全面的表格格式化、单元格操作、对齐设置和尺寸调整功能。

## 功能特性

### 核心功能
- **表格格式化** - 设置边框、阴影和整体结构
- **单元格阴影** - 为特定单元格应用背景色和图案
- **交替行颜色** - 应用斑马纹效果提高可读性
- **标题高亮** - 为表格标题行应用特殊样式
- **单元格合并** - 支持矩形区域、水平和垂直合并
- **文本对齐** - 设置单元格内文本的水平和垂直对齐
- **文本格式化** - 格式化单元格内的文本样式
- **内边距设置** - 调整单元格的内边距
- **列宽管理** - 设置单列或多列宽度
- **表格宽度** - 调整整个表格的宽度
- **自动调整** - 根据内容自动调整列宽

### 技术特性
- 基于FastMCP框架构建
- 支持异步操作
- 完整的错误处理和验证
- 灵活的单位系统（点、英寸、厘米、百分比）
- 智能颜色解析（十六进制、颜色名称）
- 自动文件扩展名处理

## 安装要求

- Python 3.10+
- python-docx >= 1.1.0
- fastmcp >= 2.8.1

## 安装方法

使用uv安装依赖：

```bash
cd python/Word文档表格编辑
uv sync
```

或使用pip安装：

```bash
pip install python-docx fastmcp
```

## 使用方法

### 启动MCP服务器

```bash
# 使用uv运行
uv run python -m word_document_table_editor.main

# 或直接运行
python -m word_document_table_editor.main
```

### MCP配置

将以下配置添加到您的MCP客户端配置文件中：

```json
{
  "mcpServers": {
    "Word文档表格编辑": {
      "command": "uvx",
      "args": [
        "word-document-table-editor-mcp"
      ],
      "env": {}
    }
  }
}
```

### 在Claude中使用

配置完成后，在Claude中可以使用以下功能：

1. **格式化表格**
   ```
   请格式化文档 "example.docx" 中的第1个表格，设置为有标题行
   ```

2. **设置单元格阴影**
   ```
   请将文档 "example.docx" 第1个表格的第2行第3列单元格设置为红色背景
   ```

3. **应用交替行颜色**
   ```
   请为文档 "example.docx" 第1个表格应用交替行颜色，提高可读性
   ```

4. **合并单元格**
   ```
   请合并文档 "example.docx" 第1个表格中第1行的第2到4列
   ```

5. **格式化单元格文本**
   ```
   请将文档 "example.docx" 第1个表格第2行第1列的文本设为粗体蓝色
   ```

## API参考

### 表格格式化
```python
format_table_tool(filename: str, table_index: int, has_header_row: str = "",
                 border_style: str = "", shading: list = [])
```
- `has_header_row`: "true" 表示有标题行，"false" 表示无标题行，""表示不设置
- `border_style`: 边框样式名称，""表示不设置
- `shading`: 阴影颜色列表，[]表示不设置

### 单元格阴影
```python
set_table_cell_shading_tool(filename: str, table_index: int, row_index: int, 
                           col_index: int, fill_color: str, pattern: str = "clear")
```

### 交替行颜色
```python
apply_table_alternating_rows_tool(filename: str, table_index: int, 
                                color1: str = "FFFFFF", color2: str = "F2F2F2")
```

### 标题高亮
```python
highlight_table_header_tool(filename: str, table_index: int, 
                           header_color: str = "4472C4", text_color: str = "FFFFFF")
```

### 单元格合并
```python
# 矩形区域合并
merge_table_cells_tool(filename: str, table_index: int, start_row: int, start_col: int, 
                      end_row: int, end_col: int)

# 水平合并
merge_table_cells_horizontal_tool(filename: str, table_index: int, row_index: int, 
                                 start_col: int, end_col: int)

# 垂直合并
merge_table_cells_vertical_tool(filename: str, table_index: int, col_index: int, 
                               start_row: int, end_row: int)
```

### 文本对齐
```python
# 单个单元格对齐
set_table_cell_alignment_tool(filename: str, table_index: int, row_index: int, col_index: int,
                             horizontal: str = "left", vertical: str = "top")

# 整个表格对齐
set_table_alignment_all_tool(filename: str, table_index: int, 
                           horizontal: str = "left", vertical: str = "top")
```

### 文本格式化
```python
format_table_cell_text_tool(filename: str, table_index: int, row_index: int, col_index: int,
                           text_content: str = "", bold: str = "", italic: str = "",
                           underline: str = "", color: str = "", font_size: int = 0,
                           font_name: str = "")
```
- `text_content`: 单元格文本内容，""表示不修改
- `bold`: "true" 表示粗体，"false" 表示非粗体，""表示不改变
- `italic`: "true" 表示斜体，"false" 表示非斜体，""表示不改变
- `underline`: "true" 表示下划线，"false" 表示无下划线，""表示不改变
- `color`: 文本颜色，""表示不改变
- `font_size`: 字体大小（磅），0表示不改变
- `font_name`: 字体名称，""表示不改变

### 内边距设置
```python
set_table_cell_padding_tool(filename: str, table_index: int, row_index: int, col_index: int,
                           top: float = 0.0, bottom: float = 0.0, left: float = 0.0,
                           right: float = 0.0, unit: str = "points")
```
- `top, bottom, left, right`: 内边距值，0.0表示不设置
- `unit`: 单位（"points", "inches", "cm"等）

### 列宽管理
```python
# 单列宽度
set_table_column_width_tool(filename: str, table_index: int, col_index: int, 
                           width: float, width_type: str = "points")

# 多列宽度
set_table_column_widths_tool(filename: str, table_index: int, widths: list, 
                           width_type: str = "points")

# 表格宽度
set_table_width_tool(filename: str, table_index: int, width: float, 
                   width_type: str = "points")

# 自动调整
auto_fit_table_columns_tool(filename: str, table_index: int)
```

## 使用示例

### 创建专业表格
```python
# 1. 应用交替行颜色
result = apply_table_alternating_rows_tool("report.docx", 0, "FFFFFF", "F0F0F0")

# 2. 高亮标题行
result = highlight_table_header_tool("report.docx", 0, "4472C4", "FFFFFF")

# 3. 设置列宽
widths = [100, 150, 200, 120]  # 点为单位
result = set_table_column_widths_tool("report.docx", 0, widths, "points")

# 4. 居中对齐所有内容
result = set_table_alignment_all_tool("report.docx", 0, "center", "center")
```

### 合并单元格创建复杂布局
```python
# 合并标题行的前三列
result = merge_table_cells_horizontal_tool("document.docx", 0, 0, 0, 2)

# 合并第一列的多行作为分类标题
result = merge_table_cells_vertical_tool("document.docx", 0, 0, 1, 3)
```

### 格式化特定单元格
```python
# 设置单元格背景色
result = set_table_cell_shading_tool("document.docx", 0, 1, 2, "FFE6E6")

# 格式化单元格文本
result = format_table_cell_text_tool("document.docx", 0, 1, 2, 
                                    text_content="重要数据", 
                                    bold=True, color="FF0000", font_size=12)
```

## 支持的参数

### 对齐方式
- **水平对齐**: "left", "center", "right", "justify"
- **垂直对齐**: "top", "center", "bottom"

### 单位类型
- **points**: 点（默认）
- **inches**: 英寸
- **cm**: 厘米
- **percent**: 百分比（部分功能）

### 颜色格式
- **十六进制**: "FF0000", "#FF0000"
- **颜色名称**: "red", "blue", "green"等

### 阴影图案
- **clear**: 纯色填充（默认）
- **solid**: 实心填充
- **pct10**, **pct20**: 百分比图案

## 错误处理

服务提供完整的错误处理：

- 文件存在性和权限检查
- 表格和单元格索引验证
- 参数类型和范围验证
- 颜色格式验证
- 详细的错误信息返回

## 参数说明

### 布尔参数处理
由于MCP框架的类型限制，布尔参数使用字符串表示：
- `"true"` - 启用该格式（如设为粗体）
- `"false"` - 禁用该格式（如取消粗体）
- `""` (空字符串) - 不改变该格式

### 其他可选参数
- 字符串参数：空字符串 `""` 表示不改变
- 数值参数：`0` 或 `0.0` 表示不改变
- 列表参数：空列表 `[]` 表示不设置
- 所有参数都有合理的默认值，可以省略不填

## 注意事项

1. 确保Word文档存在且可写
2. 文档不能被其他程序打开
3. 表格和单元格索引从0开始
4. 合并操作不可撤销
5. 某些格式可能依赖于Word版本
6. 复杂的边框样式需要额外处理

## 许可证

MIT License

## 作者

Word MCP Services
