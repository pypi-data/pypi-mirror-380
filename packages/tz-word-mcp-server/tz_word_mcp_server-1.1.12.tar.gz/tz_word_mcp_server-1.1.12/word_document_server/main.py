"""
Main entry point for the Word Document MCP Server.
Acts as the central controller for the MCP server that handles Word document operations.
Supports multiple transports: stdio, sse, and streamable-http using standalone FastMCP.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
print("Loading configuration from .env file...")
load_dotenv()
# Set required environment variable for FastMCP 2.8.1+
os.environ.setdefault('FASTMCP_LOG_LEVEL', 'INFO')
from fastmcp import FastMCP
from word_document_server.tools import (
    document_tools,
    content_tools,
    format_tools,
    protection_tools,
    footnote_tools,
    extended_document_tools,
    comment_tools
)
from word_document_server.tools.content_tools import replace_paragraph_block_below_header_tool
from word_document_server.tools.content_tools import replace_block_between_manual_anchors_tool

def get_transport_config():
    """
    Get transport configuration from environment variables.
    
    Returns:
        dict: Transport configuration with type, host, port, and other settings
    """
    # Default configuration
    config = {
        'transport': 'stdio',  # Default to stdio for backward compatibility
        'host': '0.0.0.0',
        'port': 8000,
        'path': '/mcp',
        'sse_path': '/sse'
    }
    
    # Override with environment variables if provided
    transport = os.getenv('MCP_TRANSPORT', 'stdio').lower()
    print(f"Transport: {transport}")
    # Validate transport type
    valid_transports = ['stdio', 'streamable-http', 'sse']
    if transport not in valid_transports:
        print(f"Warning: Invalid transport '{transport}'. Falling back to 'stdio'.")
        transport = 'stdio'
    
    config['transport'] = transport
    config['host'] = os.getenv('MCP_HOST', config['host'])
    config['port'] = int(os.getenv('MCP_PORT', config['port']))
    config['path'] = os.getenv('MCP_PATH', config['path'])
    config['sse_path'] = os.getenv('MCP_SSE_PATH', config['sse_path'])
    
    return config


def setup_logging(debug_mode):
    """
    Setup logging based on debug mode.
    
    Args:
        debug_mode (bool): Whether to enable debug logging
    """
    import logging
    
    if debug_mode:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        print("Debug logging enabled")
    else:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )


# Initialize FastMCP server
mcp = FastMCP("Word Document Server")


def register_tools():
    """Register all tools with the MCP server using FastMCP decorators."""
    
    # Document tools (create, copy, info, etc.)
    @mcp.tool()
    def create_document(filename: str, title: str = None, author: str = None):
        """创建一个新的Word文档，并可选择性地添加元数据信息。

        此函数用于创建一个全新的Word文档（.docx格式），可以选择性地设置文档标题和作者信息。
        创建的文档将是一个空白文档，包含基本的文档结构和属性。

        Args:
            filename (str): 新文档的文件名（应包含.docx扩展名）
            title (str, optional): 文档标题，设置后将显示在文档属性中
            author (str, optional): 文档作者，设置后将显示在文档属性中

        Returns:
            dict: 包含创建结果的字典，包含文档基本信息和操作状态

        Example:
            >>> create_document("report.docx", "季度报告", "张三")
        """
        return document_tools.create_document(filename, title, author)
    
    @mcp.tool()
    def copy_document(source_filename: str, destination_filename: str = None):
        """复制一个Word文档到新位置。

        此函数用于创建一个现有Word文档的完整副本，包括所有内容、格式、样式和元数据。
        如果目标文件名未指定，将使用源文件名加"_copy"后缀创建副本。

        Args:
            source_filename (str): 源文档的文件名（需要包含在当前目录中）
            destination_filename (str, optional): 目标文档的文件名。如果未指定，
                将自动生成如"source_copy.docx"的文件名

        Returns:
            dict: 包含复制操作结果的字典，包含源文件、目标文件路径和操作状态

        Example:
            >>> copy_document("document.docx", "backup.docx")
            >>> copy_document("report.docx")  # 自动生成 "report_copy.docx"
        """
        return document_tools.copy_document(source_filename, destination_filename)
    
    @mcp.tool()
    def get_document_info(filename: str):
        """获取Word文档的详细信息。

        此函数用于获取Word文档的各种元数据和统计信息，包括文档属性、页数、段落数、
        字符数等基本信息，帮助用户了解文档的基本特征。

        Args:
            filename (str): 要分析的Word文档文件名

        Returns:
            dict: 包含文档详细信息的字典，包含以下字段：
                - filename: 文档文件名
                - title: 文档标题
                - author: 文档作者
                - created_date: 创建日期
                - modified_date: 修改日期
                - pages: 页数
                - paragraphs: 段落数
                - characters: 字符数
                - words: 单词数
                - size: 文件大小（字节）

        Example:
            >>> get_document_info("report.docx")
        """
        return document_tools.get_document_info(filename)
    
    @mcp.tool()
    def get_document_text(filename: str):
        """提取Word文档中的所有文本内容。

        此函数用于从Word文档中提取所有纯文本内容，包括段落、标题、表格内容等。
        提取的文本将保持原有的段落结构和顺序，但不包含格式信息。

        Args:
            filename (str): 要提取文本的Word文档文件名

        Returns:
            dict: 包含提取结果的字典，包含以下字段：
                - filename: 文档文件名
                - text: 提取的完整文本内容
                - paragraphs: 按段落分割的文本列表
                - word_count: 总单词数
                - character_count: 总字符数

        Example:
            >>> get_document_text("report.docx")
        """
        return document_tools.get_document_text(filename)
    
    @mcp.tool()
    def get_document_outline(filename: str):
        """获取Word文档的结构大纲。

        此函数用于分析Word文档的层次结构，提取所有标题、子标题及其层级关系，
        生成文档的结构化大纲，帮助用户快速了解文档的组织架构和内容框架。

        Args:
            filename (str): 要分析结构的Word文档文件名

        Returns:
            dict: 包含文档结构信息的字典，包含以下字段：
                - filename: 文档文件名
                - outline: 按层级组织的标题结构列表
                - headings: 所有标题的详细信息（文本、层级、位置）
                - max_heading_level: 最大标题层级
                - total_headings: 标题总数

        Example:
            >>> get_document_outline("report.docx")
        """
        return document_tools.get_document_outline(filename)
    
    @mcp.tool()
    def list_available_documents(directory: str = "."):
        """列出指定目录中的所有Word文档文件。

        此函数用于扫描指定目录（包括子目录）中的所有.docx格式的Word文档文件，
        返回包含详细文件信息的列表，帮助用户了解当前可用的文档资源。

        Args:
            directory (str): 要扫描的目录路径，默认为当前目录(".")

        Returns:
            dict: 包含文档列表的字典，包含以下字段：
                - directory: 扫描的目录路径
                - documents: 找到的Word文档文件列表，每个文档包含：
                    - filename: 文件名
                    - filepath: 完整文件路径
                    - size: 文件大小（字节）
                    - modified_date: 最后修改日期
                    - created_date: 创建日期
                - total_count: 文档总数

        Example:
            >>> list_available_documents(".")  # 扫描当前目录
            >>> list_available_documents("documents/")  # 扫描documents子目录
        """
        return document_tools.list_available_documents(directory)
    
    @mcp.tool()
    def get_document_xml(filename: str):
        """获取Word文档的原始XML结构。

        此函数用于提取Word文档的完整XML结构，包括文档.xml、styles.xml等各个组件的
        原始XML内容。这对于高级用户和开发者非常有用，可以直接查看和分析文档的
        内部结构和格式定义。

        Args:
            filename (str): 要提取XML结构的Word文档文件名

        Returns:
            dict: 包含文档XML结构的字典，包含以下字段：
                - filename: 文档文件名
                - document_xml: 主文档XML内容
                - styles_xml: 样式定义XML内容
                - numbering_xml: 编号定义XML内容（如果存在）
                - footnotes_xml: 脚注XML内容（如果存在）
                - endnotes_xml: 尾注XML内容（如果存在）
                - comments_xml: 评论XML内容（如果存在）
                - relationships: 文档关系定义

        Example:
            >>> get_document_xml("report.docx")
        """
        return document_tools.get_document_xml_tool(filename)
    
    @mcp.tool()
    def insert_header_near_text(filename: str, target_text: str = None, header_title: str = None, position: str = 'after', header_style: str = 'Heading 1', target_paragraph_index: int = None):
        """在指定文本或段落附近插入标题。

        此函数用于在Word文档中的特定位置插入标题，可以通过文本内容定位或直接指定段落索引。
        支持在目标位置之前或之后插入，并可以指定标题样式和层级。

        Args:
            filename (str): Word文档文件名
            target_text (str, optional): 用于定位的目标文本内容，如果提供将搜索此文本
            header_title (str): 要插入的标题文本内容
            position (str): 插入位置，'before'表示在目标之前，'after'表示在目标之后
            header_style (str): 标题样式，默认为'Heading 1'，可选择'Heading 1'到'Heading 9'
            target_paragraph_index (int, optional): 目标段落索引，如果提供将直接使用此位置

        Returns:
            dict: 包含操作结果的字典，包含插入的标题信息和文档更新状态

        Example:
            >>> insert_header_near_text("doc.docx", target_text="Introduction", header_title="Chapter 1", position="before")
            >>> insert_header_near_text("doc.docx", target_paragraph_index=5, header_title="New Section", header_style="Heading 2")
        """
        return content_tools.insert_header_near_text_tool(filename, target_text, header_title, position, header_style, target_paragraph_index)
    
    @mcp.tool()
    def insert_line_or_paragraph_near_text(filename: str, target_text: str = None, line_text: str = None, position: str = 'after', line_style: str = None, target_paragraph_index: int = None):
        """在指定文本或段落附近插入行或段落。

        此函数用于在Word文档中的特定位置插入新的文本行或段落，可以通过文本内容定位
        或直接指定段落索引。支持在目标位置之前或之后插入，并可以指定文本样式。

        Args:
            filename (str): Word文档文件名
            target_text (str, optional): 用于定位的目标文本内容，如果提供将搜索此文本
            line_text (str): 要插入的文本内容
            position (str): 插入位置，'before'表示在目标之前，'after'表示在目标之后
            line_style (str, optional): 要应用的文本样式，如果不指定将使用匹配的样式
            target_paragraph_index (int, optional): 目标段落索引，如果提供将直接使用此位置

        Returns:
            dict: 包含操作结果的字典，包含插入的文本信息和文档更新状态

        Example:
            >>> insert_line_or_paragraph_near_text("doc.docx", target_text="Introduction", line_text="New content here", position="after")
            >>> insert_line_or_paragraph_near_text("doc.docx", target_paragraph_index=3, line_text="Additional text", line_style="Normal")
        """
        return content_tools.insert_line_or_paragraph_near_text_tool(filename, target_text, line_text, position, line_style, target_paragraph_index)
    
    @mcp.tool()
    def insert_numbered_list_near_text(filename: str, target_text: str = None, list_items: list = None, position: str = 'after', target_paragraph_index: int = None):
        """在指定文本或段落附近插入编号列表。

        此函数用于在Word文档中的特定位置插入编号列表，可以通过文本内容定位
        或直接指定段落索引。支持在目标位置之前或之后插入编号列表。

        Args:
            filename (str): Word文档文件名
            target_text (str, optional): 用于定位的目标文本内容，如果提供将搜索此文本
            list_items (list): 要插入的列表项内容，每个元素是一项列表内容
            position (str): 插入位置，'before'表示在目标之前，'after'表示在目标之后
            target_paragraph_index (int, optional): 目标段落索引，如果提供将直接使用此位置

        Returns:
            dict: 包含操作结果的字典，包含插入的编号列表信息和文档更新状态

        Example:
            >>> insert_numbered_list_near_text("doc.docx", target_text="Steps", list_items=["First step", "Second step", "Third step"], position="after")
            >>> insert_numbered_list_near_text("doc.docx", target_paragraph_index=5, list_items=["Item 1", "Item 2"], position="before")
        """
        return content_tools.insert_numbered_list_near_text_tool(filename, target_text, list_items, position, target_paragraph_index)
    # Content tools (paragraphs, headings, tables, etc.)
    @mcp.tool()
    def add_paragraph(filename: str, text: str, style: str = None):
        """向Word文档添加一个段落。

        此函数用于在Word文档末尾添加一个新的文本段落。可以选择性地指定段落样式，
        使段落具有特定的格式和外观。

        Args:
            filename (str): Word文档文件名
            text (str): 要添加的段落文本内容
            style (str, optional): 要应用的段落样式，如果不指定将使用默认样式

        Returns:
            dict: 包含操作结果的字典，包含添加的段落信息和文档更新状态

        Example:
            >>> add_paragraph("document.docx", "This is a new paragraph.")
            >>> add_paragraph("document.docx", "Styled paragraph", style="Heading 2")
        """
        return content_tools.add_paragraph(filename, text, style)
    
    @mcp.tool()
    def add_heading(filename: str, text: str, level: int = 1):
        """向Word文档添加标题。

        此函数用于在Word文档末尾添加一个标题，可以指定标题层级（1-9级）。
        标题将自动应用相应的格式样式，并建立文档的层次结构。

        Args:
            filename (str): Word文档文件名
            text (str): 标题文本内容
            level (int): 标题层级，1-9之间，默认为1（最高层级）

        Returns:
            dict: 包含操作结果的字典，包含添加的标题信息和文档更新状态

        Example:
            >>> add_heading("document.docx", "Main Title", level=1)
            >>> add_heading("document.docx", "Subsection", level=2)
        """
        return content_tools.add_heading(filename, text, level)
    
    @mcp.tool()
    def add_picture(filename: str, image_path: str, width: float = None):
        """向Word文档添加图片。

        此函数用于在Word文档末尾插入图片。可以选择性地指定图片宽度，
        图片将以指定的宽度显示，保持原始宽高比。

        Args:
            filename (str): Word文档文件名
            image_path (str): 图片文件路径（支持jpg、png、gif等格式）
            width (float, optional): 图片显示宽度（磅值），如果不指定将使用图片原始尺寸

        Returns:
            dict: 包含操作结果的字典，包含添加的图片信息和文档更新状态

        Example:
            >>> add_picture("document.docx", "image.jpg", width=300.0)
            >>> add_picture("document.docx", "logo.png")  # 使用原始尺寸
        """
        return content_tools.add_picture(filename, image_path, width)
    
    @mcp.tool()
    def add_table(filename: str, rows: int, cols: int, data: list = None):
        """向Word文档添加表格。

        此函数用于在Word文档末尾创建一个新的表格。可以选择性地提供表格数据，
        用于填充表格内容。如果提供了数据，将按行优先的顺序填充表格单元格。

        Args:
            filename (str): Word文档文件名
            rows (int): 表格行数，必须大于0
            cols (int): 表格列数，必须大于0
            data (list, optional): 表格数据，二维列表格式，每行数据为一个子列表。
                如果不提供，将创建空表格

        Returns:
            dict: 包含操作结果的字典，包含创建的表格信息和文档更新状态

        Example:
            >>> add_table("document.docx", rows=3, cols=2)
            >>> add_table("document.docx", rows=2, cols=3, data=[["Name", "Age", "City"], ["John", "25", "New York"]])
        """
        return content_tools.add_table(filename, rows, cols, data)
    
    @mcp.tool()
    def add_page_break(filename: str):
        """在Word文档中添加分页符。

        此函数用于在Word文档末尾插入分页符，强制后续内容在新页面开始。
        这对于控制文档布局和页面分隔非常有用。

        Args:
            filename (str): Word文档文件名

        Returns:
            dict: 包含操作结果的字典，包含分页符信息和文档更新状态

        Example:
            >>> add_page_break("document.docx")
        """
        return content_tools.add_page_break(filename)
    
    @mcp.tool()
    def delete_paragraph(filename: str, paragraph_index: int):
        """从Word文档中删除指定段落。

        此函数用于删除Word文档中指定索引位置的段落。段落索引从0开始计数，
        删除操作将完全移除该段落及其内容。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 要删除的段落索引（从0开始计数）

        Returns:
            dict: 包含操作结果的字典，包含删除操作信息和文档更新状态

        Example:
            >>> delete_paragraph("document.docx", paragraph_index=2)
        """
        return content_tools.delete_paragraph(filename, paragraph_index)
    
    @mcp.tool()
    def search_and_replace(filename: str, find_text: str, replace_text: str):
        """在Word文档中搜索并替换所有匹配的文本。

        此函数用于在整个Word文档中搜索指定的文本内容，并将所有匹配项替换为新的文本。
        替换操作将影响文档中的所有段落、标题、表格等位置。

        Args:
            filename (str): Word文档文件名
            find_text (str): 要搜索的文本内容
            replace_text (str): 用于替换的文本内容

        Returns:
            dict: 包含操作结果的字典，包含替换的匹配数量和文档更新状态

        Example:
            >>> search_and_replace("document.docx", "old text", "new text")
        """
        return content_tools.search_and_replace(filename, find_text, replace_text)
    
    # Format tools (styling, text formatting, etc.)
    @mcp.tool()
    def create_custom_style(filename: str, style_name: str, bold: bool = None,
                          italic: bool = None, font_size: int = None,
                          font_name: str = None, color: str = None,
                          base_style: str = None):
        """在Word文档中创建自定义样式。

        此函数用于创建一个新的自定义样式，可以设置字重、斜体、字体大小、字体名称、
        颜色等格式属性。可以基于现有样式创建新样式，也可以创建全新的样式。

        Args:
            filename (str): Word文档文件名
            style_name (str): 新样式名称，必须唯一
            bold (bool, optional): 是否粗体，True为粗体，False为非粗体，None为继承
            italic (bool, optional): 是否斜体，True为斜体，False为非斜体，None为继承
            font_size (int, optional): 字体大小（磅值），None为继承默认大小
            font_name (str, optional): 字体名称，如"Times New Roman"，None为继承
            color (str, optional): 字体颜色，如"FF0000"（红色），None为继承
            base_style (str, optional): 基础样式名称，新样式将基于此样式创建

        Returns:
            dict: 包含操作结果的字典，包含创建的样式信息和文档更新状态

        Example:
            >>> create_custom_style("doc.docx", "MyStyle", bold=True, font_size=12, font_name="Arial", color="0000FF")
            >>> create_custom_style("doc.docx", "SubStyle", base_style="Heading 1", italic=True)
        """
        return format_tools.create_custom_style(
            filename, style_name, bold, italic, font_size, font_name, color, base_style
        )
    
    @mcp.tool()
    def format_text(filename: str, paragraph_index: int, start_pos: int, end_pos: int,
                   bold: bool = None, italic: bool = None, underline: bool = None,
                   color: str = None, font_size: int = None, font_name: str = None):
        """格式化段落中特定范围的文本。

        此函数用于对Word文档中指定段落的特定文本范围应用格式设置。可以设置
        粗体、斜体、下划线、颜色、字体大小和字体名称等格式属性。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 目标段落索引（从0开始计数）
            start_pos (int): 格式化起始位置（字符索引）
            end_pos (int): 格式化结束位置（字符索引）
            bold (bool, optional): 是否粗体，True为粗体，False为非粗体，None为不改变
            italic (bool, optional): 是否斜体，True为斜体，False为非斜体，None为不改变
            underline (bool, optional): 是否下划线，True为下划线，False为非下划线，None为不改变
            color (str, optional): 字体颜色，如"FF0000"（红色），None为不改变
            font_size (int, optional): 字体大小（磅值），None为不改变
            font_name (str, optional): 字体名称，如"Times New Roman"，None为不改变

        Returns:
            dict: 包含操作结果的字典，包含格式化信息和文档更新状态

        Example:
            >>> format_text("doc.docx", paragraph_index=1, start_pos=0, end_pos=10, bold=True, color="FF0000")
            >>> format_text("doc.docx", paragraph_index=2, start_pos=5, end_pos=15, font_size=14, font_name="Arial")
        """
        return format_tools.format_text(
            filename, paragraph_index, start_pos, end_pos, bold, italic,
            underline, color, font_size, font_name
        )
    
    @mcp.tool()
    def format_table(filename: str, table_index: int, has_header_row: bool = None,
                    border_style: str = None, shading: list = None):
        """格式化Word文档中的表格。

        此函数用于对Word文档中指定表格应用格式设置，包括边框样式、底纹和结构设置。
        可以设置表格是否有标题行、边框样式和底纹颜色等。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            has_header_row (bool, optional): 是否将第一行设置为标题行，None为不改变
            border_style (str, optional): 边框样式，如"single", "double", "thick"等，None为不改变
            shading (list, optional): 底纹设置，包含颜色和图案信息，None为不改变

        Returns:
            dict: 包含操作结果的字典，包含表格格式化信息和文档更新状态

        Example:
            >>> format_table("doc.docx", table_index=0, has_header_row=True, border_style="single")
            >>> format_table("doc.docx", table_index=1, shading=["CCCCCC", "solid"])
        """
        return format_tools.format_table(filename, table_index, has_header_row, border_style, shading)
    
    # New table cell shading tools
    @mcp.tool()
    def set_table_cell_shading(filename: str, table_index: int, row_index: int,
                              col_index: int, fill_color: str, pattern: str = "clear"):
        """为指定表格单元格应用底纹/填充。

        此函数用于为Word文档中表格的特定单元格设置底纹颜色和填充图案，
        增强表格的可视化效果和可读性。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            row_index (int): 行索引（从0开始计数）
            col_index (int): 列索引（从0开始计数）
            fill_color (str): 填充颜色，如"FFFF00"（黄色）、"4472C4"（蓝色）
            pattern (str): 填充图案，默认为"clear"，可选择"solid", "clear"等

        Returns:
            dict: 包含操作结果的字典，包含单元格底纹设置信息和文档更新状态

        Example:
            >>> set_table_cell_shading("doc.docx", table_index=0, row_index=1, col_index=2, fill_color="FFFF00", pattern="solid")
        """
        return format_tools.set_table_cell_shading(filename, table_index, row_index, col_index, fill_color, pattern)
    
    @mcp.tool()
    def apply_table_alternating_rows(filename: str, table_index: int,
                                   color1: str = "FFFFFF", color2: str = "F2F2F2"):
        """为表格应用交替行颜色以提高可读性。

        此函数用于为Word文档中指定表格的所有行应用交替的底纹颜色，
        通常用于提高表格的可读性和视觉效果。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            color1 (str): 奇数行使用的颜色，默认为"FFFFFF"（白色）
            color2 (str): 偶数行使用的颜色，默认为"F2F2F2"（浅灰色）

        Returns:
            dict: 包含操作结果的字典，包含交替行颜色设置信息和文档更新状态

        Example:
            >>> apply_table_alternating_rows("doc.docx", table_index=0, color1="FFFFFF", color2="F0F0F0")
        """
        return format_tools.apply_table_alternating_rows(filename, table_index, color1, color2)
    
    @mcp.tool()
    def highlight_table_header(filename: str, table_index: int,
                             header_color: str = "4472C4", text_color: str = "FFFFFF"):
        """为表格标题行应用特殊高亮效果。

        此函数用于为Word文档中指定表格的标题行（第一行）应用特殊的背景色和文本颜色，
        使其在视觉上与其他行区分开来，提高表格的可读性。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            header_color (str): 标题行背景颜色，默认为"4472C4"（蓝色）
            text_color (str): 标题行文本颜色，默认为"FFFFFF"（白色）

        Returns:
            dict: 包含操作结果的字典，包含标题行高亮设置信息和文档更新状态

        Example:
            >>> highlight_table_header("doc.docx", table_index=0, header_color="4472C4", text_color="FFFFFF")
        """
        return format_tools.highlight_table_header(filename, table_index, header_color, text_color)
    
    # Cell merging tools
    @mcp.tool()
    def merge_table_cells(filename: str, table_index: int, start_row: int, start_col: int,
                        end_row: int, end_col: int):
        """合并表格中矩形区域内的单元格。

        此函数用于将Word文档中表格的指定矩形区域内的所有单元格合并为一个单元格。
        合并后的单元格将跨越多行多列，内容将保留在合并区域的起始位置。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            start_row (int): 起始行索引（从0开始计数）
            start_col (int): 起始列索引（从0开始计数）
            end_row (int): 结束行索引（从0开始计数）
            end_col (int): 结束列索引（从0开始计数）

        Returns:
            dict: 包含操作结果的字典，包含单元格合并信息和文档更新状态

        Example:
            >>> merge_table_cells("doc.docx", table_index=0, start_row=0, start_col=0, end_row=1, end_col=2)
        """
        return format_tools.merge_table_cells(filename, table_index, start_row, start_col, end_row, end_col)
    
    @mcp.tool()
    def merge_table_cells_horizontal(filename: str, table_index: int, row_index: int,
                                   start_col: int, end_col: int):
        """在表格单行中水平合并单元格。

        此函数用于将Word文档中表格指定行内的多个连续单元格水平合并为一个单元格。
        合并后的单元格将跨越多列，内容将保留在合并区域的起始位置。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            row_index (int): 行索引（从0开始计数）
            start_col (int): 起始列索引（从0开始计数）
            end_col (int): 结束列索引（从0开始计数）

        Returns:
            dict: 包含操作结果的字典，包含单元格水平合并信息和文档更新状态

        Example:
            >>> merge_table_cells_horizontal("doc.docx", table_index=0, row_index=1, start_col=0, end_col=2)
        """
        return format_tools.merge_table_cells_horizontal(filename, table_index, row_index, start_col, end_col)
    
    @mcp.tool()
    def merge_table_cells_vertical(filename: str, table_index: int, col_index: int,
                                 start_row: int, end_row: int):
        """在表格单列中垂直合并单元格。

        此函数用于将Word文档中表格指定列内的多个连续单元格垂直合并为一个单元格。
        合并后的单元格将跨越多行，内容将保留在合并区域的起始位置。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            col_index (int): 列索引（从0开始计数）
            start_row (int): 起始行索引（从0开始计数）
            end_row (int): 结束行索引（从0开始计数）

        Returns:
            dict: 包含操作结果的字典，包含单元格垂直合并信息和文档更新状态

        Example:
            >>> merge_table_cells_vertical("doc.docx", table_index=0, col_index=1, start_row=0, end_row=2)
        """
        return format_tools.merge_table_cells_vertical(filename, table_index, col_index, start_row, end_row)
    
    # Cell alignment tools
    @mcp.tool()
    def set_table_cell_alignment(filename: str, table_index: int, row_index: int, col_index: int,
                               horizontal: str = "left", vertical: str = "top"):
        """设置指定表格单元格的文本对齐方式。

        此函数用于设置Word文档中表格特定单元格的文本水平和垂直对齐方式，
        控制文本在单元格内的位置和排列方式。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            row_index (int): 行索引（从0开始计数）
            col_index (int): 列索引（从0开始计数）
            horizontal (str): 水平对齐方式，默认为"left"，可选择"left", "center", "right", "justify"
            vertical (str): 垂直对齐方式，默认为"top"，可选择"top", "center", "bottom"

        Returns:
            dict: 包含操作结果的字典，包含单元格对齐设置信息和文档更新状态

        Example:
            >>> set_table_cell_alignment("doc.docx", table_index=0, row_index=1, col_index=2, horizontal="center", vertical="center")
        """
        return format_tools.set_table_cell_alignment(filename, table_index, row_index, col_index, horizontal, vertical)
    
    @mcp.tool()
    def set_table_alignment_all(filename: str, table_index: int,
                              horizontal: str = "left", vertical: str = "top"):
        """设置表格中所有单元格的文本对齐方式。

        此函数用于批量设置Word文档中指定表格的所有单元格的文本水平和垂直对齐方式，
        统一控制表格中所有文本的位置和排列方式。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            horizontal (str): 水平对齐方式，默认为"left"，可选择"left", "center", "right", "justify"
            vertical (str): 垂直对齐方式，默认为"top"，可选择"top", "center", "bottom"

        Returns:
            dict: 包含操作结果的字典，包含表格整体对齐设置信息和文档更新状态

        Example:
            >>> set_table_alignment_all("doc.docx", table_index=0, horizontal="center", vertical="center")
        """
        return format_tools.set_table_alignment_all(filename, table_index, horizontal, vertical)
    
    # Protection tools
    @mcp.tool()
    def protect_document(filename: str, password: str):
        """为Word文档添加密码保护。

        此函数用于为Word文档设置密码保护，保护文档不被未经授权的用户打开或修改。
        设置密码后，用户需要输入正确的密码才能打开文档。

        Args:
            filename (str): Word文档文件名
            password (str): 保护密码，建议使用强密码组合

        Returns:
            dict: 包含操作结果的字典，包含密码保护设置信息和文档更新状态

        Example:
            >>> protect_document("document.docx", "MySecurePassword123")
        """
        return protection_tools.protect_document(filename, password)
    
    @mcp.tool()
    def unprotect_document(filename: str, password: str):
        """移除Word文档的密码保护。

        此函数用于移除Word文档的密码保护，允许用户在没有密码的情况下打开文档。
        需要提供正确的密码才能成功移除保护。

        Args:
            filename (str): Word文档文件名
            password (str): 当前用于保护文档的密码

        Returns:
            dict: 包含操作结果的字典，包含密码保护移除信息和文档更新状态

        Example:
            >>> unprotect_document("document.docx", "MySecurePassword123")
        """
        return protection_tools.unprotect_document(filename, password)
    
    # Footnote tools
    @mcp.tool()
    def add_footnote_to_document(filename: str, paragraph_index: int, footnote_text: str):
        """在Word文档指定段落中添加脚注。

        此函数用于在Word文档指定段落的末尾添加脚注。脚注将以标准格式显示，
        包含引用标记和脚注内容。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 目标段落索引（从0开始计数）
            footnote_text (str): 脚注文本内容

        Returns:
            dict: 包含操作结果的字典，包含脚注添加信息和文档更新状态

        Example:
            >>> add_footnote_to_document("document.docx", paragraph_index=2, footnote_text="This is a footnote.")
        """
        return footnote_tools.add_footnote_to_document(filename, paragraph_index, footnote_text)
    
    @mcp.tool()
    def add_footnote_after_text(filename: str, search_text: str, footnote_text: str,
                               output_filename: str = None):
        """在指定文本后添加脚注并确保正确的上标格式。

        此增强函数用于在Word文档中查找特定文本，并在该文本后添加脚注。
        脚注将以正确的上标格式显示，确保符合Word文档的格式标准。

        Args:
            filename (str): Word文档文件名
            search_text (str): 要搜索的文本内容，将在此文本后添加脚注
            footnote_text (str): 脚注文本内容
            output_filename (str, optional): 输出文件名，如果不指定将覆盖原文件

        Returns:
            dict: 包含操作结果的字典，包含脚注添加信息和文档更新状态

        Example:
            >>> add_footnote_after_text("doc.docx", "important point", "See reference [1] for details.")
        """
        return footnote_tools.add_footnote_after_text(filename, search_text, footnote_text, output_filename)
    
    @mcp.tool()
    def add_footnote_before_text(filename: str, search_text: str, footnote_text: str,
                                output_filename: str = None):
        """在指定文本前添加脚注并确保正确的上标格式。

        此增强函数用于在Word文档中查找特定文本，并在该文本前添加脚注。
        脚注将以正确的上标格式显示，确保符合Word文档的格式标准。

        Args:
            filename (str): Word文档文件名
            search_text (str): 要搜索的文本内容，将在此文本前添加脚注
            footnote_text (str): 脚注文本内容
            output_filename (str, optional): 输出文件名，如果不指定将覆盖原文件

        Returns:
            dict: 包含操作结果的字典，包含脚注添加信息和文档更新状态

        Example:
            >>> add_footnote_before_text("doc.docx", "important point", "See reference [1] for details.")
        """
        return footnote_tools.add_footnote_before_text(filename, search_text, footnote_text, output_filename)
    
    @mcp.tool()
    def add_footnote_enhanced(filename: str, paragraph_index: int, footnote_text: str,
                             output_filename: str = None):
        """在Word文档指定段落末尾添加增强型脚注，确保正确的上标格式。

        此增强函数用于在Word文档指定段落的末尾添加脚注，并保证脚注引用标记具有正确的上标格式。
        脚注将以标准格式显示，包含引用标记和脚注内容，具有完整的样式处理功能。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 目标段落索引（从0开始计数）
            footnote_text (str): 脚注文本内容
            output_filename (str, optional): 输出文件名，如果不指定将覆盖原文件

        Returns:
            dict: 包含操作结果的字典，包含脚注添加信息和文档更新状态

        Example:
            >>> add_footnote_enhanced("document.docx", paragraph_index=2, footnote_text="这是增强型脚注内容。")
        """
        return footnote_tools.add_footnote_enhanced(filename, paragraph_index, footnote_text, output_filename)
    
    @mcp.tool()
    def add_endnote_to_document(filename: str, paragraph_index: int, endnote_text: str):
        """在Word文档指定段落中添加尾注。

        此函数用于在Word文档指定段落的末尾添加尾注。尾注将以标准格式显示，
        包含引用标记和尾注内容，尾注通常显示在文档末尾或章节末尾。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 目标段落索引（从0开始计数）
            endnote_text (str): 尾注文本内容

        Returns:
            dict: 包含操作结果的字典，包含尾注添加信息和文档更新状态

        Example:
            >>> add_endnote_to_document("document.docx", paragraph_index=2, endnote_text="这是尾注内容。")
        """
        return footnote_tools.add_endnote_to_document(filename, paragraph_index, endnote_text)
    
    @mcp.tool()
    def customize_footnote_style(filename: str, numbering_format: str = "1, 2, 3",
                                start_number: int = 1, font_name: str = None,
                                font_size: int = None):
        """自定义Word文档中脚注的编号格式和样式。

        此函数用于自定义Word文档中脚注的编号格式、起始编号、字体名称和字体大小等样式属性。
        可以灵活控制脚注的外观和编号方式，使其符合特定的格式要求。

        Args:
            filename (str): Word文档文件名
            numbering_format (str): 编号格式，默认为"1, 2, 3"，可选择其他格式如"a, b, c", "i, ii, iii"等
            start_number (int): 起始编号，默认为1，表示从1开始编号
            font_name (str, optional): 字体名称，如"Times New Roman"，None为使用默认字体
            font_size (int, optional): 字体大小（磅值），None为使用默认大小

        Returns:
            dict: 包含操作结果的字典，包含脚注样式自定义信息和文档更新状态

        Example:
            >>> customize_footnote_style("doc.docx", numbering_format="a, b, c", start_number=1, font_name="Arial", font_size=10)
            >>> customize_footnote_style("doc.docx", numbering_format="i, ii, iii", start_number=5)
        """
        return footnote_tools.customize_footnote_style(
            filename, numbering_format, start_number, font_name, font_size
        )
    
    @mcp.tool()
    def delete_footnote_from_document(filename: str, footnote_id: int = None,
                                     search_text: str = None, output_filename: str = None):
        """从Word文档中删除脚注。

        此函数用于从Word文档中删除指定的脚注。可以通过脚注ID（1, 2, 3等）或搜索附近的文本来识别要删除的脚注。
        删除操作将完全移除脚注引用标记和脚注内容。

        Args:
            filename (str): Word文档文件名
            footnote_id (int, optional): 要删除的脚注ID（从1开始计数），如果提供将直接使用此ID
            search_text (str, optional): 用于定位脚注的搜索文本，如果提供将在附近搜索脚注
            output_filename (str, optional): 输出文件名，如果不指定将覆盖原文件

        Returns:
            dict: 包含操作结果的字典，包含脚注删除信息和文档更新状态

        Example:
            >>> delete_footnote_from_document("doc.docx", footnote_id=1)
            >>> delete_footnote_from_document("doc.docx", search_text="important point", output_filename="output.docx")
        """
        return footnote_tools.delete_footnote_from_document(
            filename, footnote_id, search_text, output_filename
        )
    
    # Robust footnote tools - Production-ready with comprehensive validation
    @mcp.tool()
    def add_footnote_robust(filename: str, search_text: str = None,
                           paragraph_index: int = None, footnote_text: str = "",
                           validate_location: bool = True, auto_repair: bool = False):
        """使用强大的验证和Word兼容性添加脚注。

        这是具有全面错误处理的生产就绪版本。可以基于搜索文本或段落索引定位脚注位置，
        提供位置验证和自动修复功能，确保脚注添加的准确性和Word文档的兼容性。

        Args:
            filename (str): Word文档文件名
            search_text (str, optional): 用于定位的搜索文本，如果提供将在此文本附近添加脚注
            paragraph_index (int, optional): 目标段落索引（从0开始计数），如果提供将直接使用此位置
            footnote_text (str): 脚注文本内容，默认为空字符串
            validate_location (bool): 是否验证脚注位置，默认为True
            auto_repair (bool): 是否自动修复位置问题，默认为False

        Returns:
            dict: 包含操作结果的字典，包含脚注添加信息、验证结果和文档更新状态

        Example:
            >>> add_footnote_robust("doc.docx", search_text="important point", footnote_text="这是脚注内容。")
            >>> add_footnote_robust("doc.docx", paragraph_index=2, footnote_text="段落脚注", validate_location=True, auto_repair=True)
        """
        return footnote_tools.add_footnote_robust_tool(
            filename, search_text, paragraph_index, footnote_text,
            validate_location, auto_repair
        )
    
    @mcp.tool()
    def validate_document_footnotes(filename: str):
        """验证Word文档中所有脚注的一致性和合规性。

        此函数用于验证Word文档中所有脚注的完整性和正确性，返回详细的验证报告。
        检查内容包括ID冲突、孤立内容、缺失样式等问题，确保脚注的完整性和规范性。

        Args:
            filename (str): Word文档文件名

        Returns:
            dict: 包含验证结果的字典，包含以下字段：
                - filename: 文档文件名
                - total_footnotes: 脚注总数
                - validation_results: 验证结果列表，包含每个脚注的验证状态
                - id_conflicts: ID冲突报告
                - orphaned_content: 孤立内容报告
                - missing_styles: 缺失样式报告
                - overall_status: 整体验证状态（"valid", "warning", "error"）

        Example:
            >>> validate_document_footnotes("document.docx")
        """
        return footnote_tools.validate_footnotes_tool(filename)
    
    @mcp.tool()
    def delete_footnote_robust(filename: str, footnote_id: int = None,
                              search_text: str = None, clean_orphans: bool = True):
        """使用全面清理和孤立内容移除功能删除脚注。

        此函数用于从Word文档中彻底删除指定的脚注，并确保从document.xml、footnotes.xml和
        关系文件中完全移除。提供孤立内容清理功能，确保删除操作的完整性和文档的清洁性。

        Args:
            filename (str): Word文档文件名
            footnote_id (int, optional): 要删除的脚注ID（从1开始计数），如果提供将直接使用此ID
            search_text (str, optional): 用于定位脚注的搜索文本，如果提供将在附近搜索脚注
            clean_orphans (bool): 是否清理孤立内容，默认为True

        Returns:
            dict: 包含操作结果的字典，包含脚注删除信息、清理报告和文档更新状态

        Example:
            >>> delete_footnote_robust("doc.docx", footnote_id=1, clean_orphans=True)
            >>> delete_footnote_robust("doc.docx", search_text="important point", clean_orphans=True)
        """
        return footnote_tools.delete_footnote_robust_tool(
            filename, footnote_id, search_text, clean_orphans
        )
    
    # Extended document tools
    @mcp.tool()
    def get_paragraph_text_from_document(filename: str, paragraph_index: int):
        """从Word文档中获取指定段落的文本内容。

        此函数用于提取Word文档中指定段落的纯文本内容。段落索引从0开始计数，
        可以获取特定段落的完整文本，便于对文档内容进行分析和处理。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 要获取文本的段落索引（从0开始计数）

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - paragraph_index: 段落索引
                - text: 段落文本内容
                - character_count: 字符数
                - word_count: 单词数

        Example:
            >>> get_paragraph_text_from_document("document.docx", paragraph_index=2)
        """
        return extended_document_tools.get_paragraph_text_from_document(filename, paragraph_index)
    
    @mcp.tool()
    def find_text_in_document(filename: str, text_to_find: str, match_case: bool = True,
                             whole_word: bool = False):
        """在Word文档中查找特定文本的所有出现位置。

        此函数用于在Word文档中搜索指定的文本内容，并返回所有匹配的位置和上下文信息。
        支持区分大小写和整词匹配选项，可以精确控制搜索行为和结果。

        Args:
            filename (str): Word文档文件名
            text_to_find (str): 要查找的文本内容
            match_case (bool): 是否区分大小写，默认为True
            whole_word (bool): 是否整词匹配，默认为False

        Returns:
            dict: 包含搜索结果的字典，包含以下字段：
                - filename: 文档文件名
                - search_text: 搜索的文本内容
                - matches: 匹配结果列表，每个匹配包含：
                    - paragraph_index: 段落索引
                    - start_pos: 起始位置
                    - end_pos: 结束位置
                    - text_context: 上下文文本
                    - matched_text: 匹配的文本
                - total_matches: 总匹配数量
                - search_options: 搜索选项设置

        Example:
            >>> find_text_in_document("doc.docx", "important", match_case=True, whole_word=False)
            >>> find_text_in_document("doc.docx", "Word", match_case=False, whole_word=True)
        """
        return extended_document_tools.find_text_in_document(
            filename, text_to_find, match_case, whole_word
        )
    
    @mcp.tool()
    def convert_to_pdf(filename: str, output_filename: str = None):
        """将Word文档转换为PDF格式。

        此函数用于将Word文档（.docx格式）转换为PDF格式文件。转换将保留文档的格式、布局、
        字体和样式，确保转换后的PDF文件与原Word文档具有相同的视觉效果。

        Args:
            filename (str): 要转换的Word文档文件名
            output_filename (str, optional): 输出PDF文件名，如果不指定将自动生成

        Returns:
            dict: 包含转换结果的字典，包含以下字段：
                - filename: 原文档文件名
                - output_filename: 输出PDF文件名
                - conversion_status: 转换状态（"success", "error"）
                - file_size: 输出文件大小（字节）
                - pages: PDF页数

        Example:
            >>> convert_to_pdf("document.docx", "document.pdf")
            >>> convert_to_pdf("report.docx")  # 自动生成 "report.pdf"
        """
        return extended_document_tools.convert_to_pdf(filename, output_filename)

    @mcp.tool()
    def replace_paragraph_block_below_header(filename: str, header_text: str, new_paragraphs: list, detect_block_end_fn=None):
        """替换标题下方段落块，避免修改目录表。

        此函数用于替换Word文档中指定标题下方的一组段落内容。可以精确控制替换的范围，
        避免影响文档的目录表（TOC），确保文档结构的完整性。

        Args:
            filename (str): Word文档文件名
            header_text (str): 标题文本，用于定位要替换的段落块
            new_paragraphs (list): 新的段落内容列表，每个元素是一个段落文本
            detect_block_end_fn (function, optional): 检测段落块结束位置的函数，如果不提供将使用默认逻辑

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - header_text: 目标标题文本
                - paragraphs_replaced: 被替换的段落数量
                - new_paragraphs_count: 新段落数量
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> replace_paragraph_block_below_header("doc.docx", "Chapter 1", ["New paragraph 1", "New paragraph 2"])
        """
        return replace_paragraph_block_below_header_tool(filename, header_text, new_paragraphs, detect_block_end_fn)

    @mcp.tool()
    def replace_block_between_manual_anchors(filename: str, start_anchor_text: str, new_paragraphs: list, end_anchor_text: str = None, match_fn=None, new_paragraph_style: str = None):
        """替换两个手动锚点之间的所有内容（如果未提供结束锚点则替换到下一个逻辑标题）。

        此函数用于替换Word文档中两个锚点文本之间（或从开始锚点到下一个逻辑标题之间）的所有内容。
        支持自定义匹配函数和新的段落样式，可以精确控制替换的范围和格式。

        Args:
            filename (str): Word文档文件名
            start_anchor_text (str): 开始锚点文本，用于定位替换的起始位置
            new_paragraphs (list): 新的段落内容列表，每个元素是一个段落文本
            end_anchor_text (str, optional): 结束锚点文本，如果不提供将替换到下一个逻辑标题
            match_fn (function, optional): 自定义匹配函数，用于更精确的文本匹配
            new_paragraph_style (str, optional): 新段落的样式，如果不指定将使用默认样式

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - start_anchor: 开始锚点文本
                - end_anchor: 结束锚点文本（如果提供）
                - paragraphs_replaced: 被替换的段落数量
                - new_paragraphs_count: 新段落数量
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> replace_block_between_manual_anchors("doc.docx", "Start Here", ["New content 1", "New content 2"], "End Here")
            >>> replace_block_between_manual_anchors("doc.docx", "Chapter 1", ["Updated content"], new_paragraph_style="Normal")
        """
        return replace_block_between_manual_anchors_tool(filename, start_anchor_text, new_paragraphs, end_anchor_text, match_fn, new_paragraph_style)

    # Comment tools
    @mcp.tool()
    def get_all_comments(filename: str):
        """从Word文档中提取所有评论。

        此函数用于提取Word文档中的所有评论内容，包括每个评论的作者、日期、位置和内容。
        返回完整的评论列表，帮助用户了解文档中的所有审阅和批注信息。

        Args:
            filename (str): Word文档文件名

        Returns:
            dict: 包含评论提取结果的字典，包含以下字段：
                - filename: 文档文件名
                - comments: 评论列表，每个评论包含：
                    - id: 评论ID
                    - author: 评论作者
                    - date: 评论日期
                    - paragraph_index: 关联段落索引
                    - comment_text: 评论内容
                    - resolved: 是否已解决
                - total_comments: 评论总数
                - authors: 作者列表

        Example:
            >>> get_all_comments("document.docx")
        """
        return comment_tools.get_all_comments(filename)
    
    @mcp.tool()
    def get_comments_by_author(filename: str, author: str):
        """从Word文档中提取指定作者的评论。

        此函数用于提取Word文档中特定作者的所有评论内容。可以按作者姓名筛选评论，
        帮助用户查看特定审阅者提出的所有反馈和建议。

        Args:
            filename (str): Word文档文件名
            author (str): 评论作者姓名，用于筛选评论

        Returns:
            dict: 包含评论提取结果的字典，包含以下字段：
                - filename: 文档文件名
                - author: 指定的作者姓名
                - comments: 该作者的评论列表，每个评论包含：
                    - id: 评论ID
                    - author: 评论作者（应与指定作者一致）
                    - date: 评论日期
                    - paragraph_index: 关联段落索引
                    - comment_text: 评论内容
                    - resolved: 是否已解决
                - total_comments: 该作者的评论总数

        Example:
            >>> get_comments_by_author("document.docx", "张三")
            >>> get_comments_by_author("report.docx", "李四")
        """
        return comment_tools.get_comments_by_author(filename, author)
    
    @mcp.tool()
    def get_comments_for_paragraph(filename: str, paragraph_index: int):
        """从Word文档中提取指定段落的评论。

        此函数用于提取Word文档中特定段落的所有评论内容。可以按段落索引筛选评论，
        帮助用户查看特定段落相关的所有审阅反馈和批注信息。

        Args:
            filename (str): Word文档文件名
            paragraph_index (int): 段落索引（从0开始计数），用于筛选该段落的评论

        Returns:
            dict: 包含评论提取结果的字典，包含以下字段：
                - filename: 文档文件名
                - paragraph_index: 指定的段落索引
                - comments: 该段落的评论列表，每个评论包含：
                    - id: 评论ID
                    - author: 评论作者
                    - date: 评论日期
                    - paragraph_index: 关联段落索引（应与指定段落一致）
                    - comment_text: 评论内容
                    - resolved: 是否已解决
                - total_comments: 该段落的评论总数

        Example:
            >>> get_comments_for_paragraph("document.docx", paragraph_index=2)
            >>> get_comments_for_paragraph("report.docx", paragraph_index=5)
        """
        return comment_tools.get_comments_for_paragraph(filename, paragraph_index)
    # New table column width tools
    @mcp.tool()
    def set_table_column_width(filename: str, table_index: int, col_index: int,
                              width: float, width_type: str = "points"):
        """设置指定表格列的宽度。

        此函数用于设置Word文档中表格特定列的宽度。可以精确控制列的宽度，
        支持不同的宽度单位（磅值、百分比等），以适应不同的布局需求。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            col_index (int): 列索引（从0开始计数）
            width (float): 列宽度值
            width_type (str): 宽度单位，默认为"points"，可选择"points", "percentage"等

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - table_index: 表格索引
                - col_index: 列索引
                - width: 设置的宽度值
                - width_type: 宽度单位
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> set_table_column_width("doc.docx", table_index=0, col_index=1, width=100.0, width_type="points")
            >>> set_table_column_width("doc.docx", table_index=1, col_index=0, width=50.0, width_type="percentage")
        """
        return format_tools.set_table_column_width(filename, table_index, col_index, width, width_type)

    @mcp.tool()
    def set_table_column_widths(filename: str, table_index: int, widths: list,
                               width_type: str = "points"):
        """批量设置表格多列的宽度。

        此函数用于批量设置Word文档中表格多个列的宽度。可以同时为多列设置不同的宽度值，
        支持不同的宽度单位，提高操作效率，适用于需要调整多个列宽的场景。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            widths (list): 宽度值列表，每个元素对应一列的宽度
            width_type (str): 宽度单位，默认为"points"，可选择"points", "percentage"等

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - table_index: 表格索引
                - widths: 设置的宽度值列表
                - width_type: 宽度单位
                - columns_updated: 更新的列数量
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> set_table_column_widths("doc.docx", table_index=0, widths=[100.0, 150.0, 120.0], width_type="points")
            >>> set_table_column_widths("doc.docx", table_index=1, widths=[25.0, 35.0, 40.0], width_type="percentage")
        """
        return format_tools.set_table_column_widths(filename, table_index, widths, width_type)

    @mcp.tool()
    def set_table_width(filename: str, table_index: int, width: float,
                       width_type: str = "points"):
        """设置表格的整体宽度。

        此函数用于设置Word文档中指定表格的整体宽度。可以控制表格的总宽度，
        支持不同的宽度单位，帮助调整表格在文档中的布局和显示效果。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            width (float): 表格宽度值
            width_type (str): 宽度单位，默认为"points"，可选择"points", "percentage"等

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - table_index: 表格索引
                - width: 设置的宽度值
                - width_type: 宽度单位
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> set_table_width("doc.docx", table_index=0, width=400.0, width_type="points")
            >>> set_table_width("doc.docx", table_index=1, width=80.0, width_type="percentage")
        """
        return format_tools.set_table_width(filename, table_index, width, width_type)

    @mcp.tool()
    def auto_fit_table_columns(filename: str, table_index: int):
        """根据内容自动调整表格列宽。

        此函数用于自动调整Word文档中指定表格的列宽，使其根据单元格内容自动适应。
        系统会自动计算每列的最佳宽度，确保内容完整显示且表格布局美观。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - table_index: 表格索引
                - columns_adjusted: 调整的列数量
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> auto_fit_table_columns("doc.docx", table_index=0)
            >>> auto_fit_table_columns("report.docx", table_index=1)
        """
        return format_tools.auto_fit_table_columns(filename, table_index)

    # New table cell text formatting and padding tools
    @mcp.tool()
    def format_table_cell_text(filename: str, table_index: int, row_index: int, col_index: int,
                               text_content: str = None, bold: bool = None, italic: bool = None,
                               underline: bool = None, color: str = None, font_size: int = None,
                               font_name: str = None):
        """格式化指定表格单元格内的文本。

        此函数用于格式化Word文档中表格特定单元格内的文本。可以设置文本内容、字体样式（粗体、斜体、下划线）、
        颜色、字体大小和字体名称等格式属性，为表格内容提供丰富的视觉效果。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            row_index (int): 行索引（从0开始计数）
            col_index (int): 列索引（从0开始计数）
            text_content (str, optional): 要设置的文本内容，如果不提供将保留原内容
            bold (bool, optional): 是否粗体，True为粗体，False为非粗体，None为不改变
            italic (bool, optional): 是否斜体，True为斜体，False为非斜体，None为不改变
            underline (bool, optional): 是否下划线，True为下划线，False为非下划线，None为不改变
            color (str, optional): 字体颜色，如"FF0000"（红色），None为不改变
            font_size (int, optional): 字体大小（磅值），None为不改变
            font_name (str, optional): 字体名称，如"Times New Roman"，None为不改变

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - table_index: 表格索引
                - row_index: 行索引
                - col_index: 列索引
                - formatting_applied: 应用的格式设置
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> format_table_cell_text("doc.docx", table_index=0, row_index=1, col_index=2, bold=True, color="FF0000")
            >>> format_table_cell_text("doc.docx", table_index=1, row_index=0, col_index=1, font_size=12, font_name="Arial")
        """
        return format_tools.format_table_cell_text(filename, table_index, row_index, col_index,
                                                   text_content, bold, italic, underline, color, font_size, font_name)

    @mcp.tool()
    def set_table_cell_padding(filename: str, table_index: int, row_index: int, col_index: int,
                               top: float = None, bottom: float = None, left: float = None,
                               right: float = None, unit: str = "points"):
        """为指定表格单元格设置内边距/外边距。

        此函数用于为Word文档中表格的特定单元格设置内边距（填充），可以分别控制上、下、左、右四个方向的间距。
        适当的内边距可以改善文本的可读性和表格的视觉效果，支持不同的度量单位。

        Args:
            filename (str): Word文档文件名
            table_index (int): 表格索引（从0开始计数）
            row_index (int): 行索引（从0开始计数）
            col_index (int): 列索引（从0开始计数）
            top (float, optional): 上内边距值，None为不改变
            bottom (float, optional): 下内边距值，None为不改变
            left (float, optional): 左内边距值，None为不改变
            right (float, optional): 右内边距值，None为不改变
            unit (str): 度量单位，默认为"points"，可选择"points", "inches", "cm"等

        Returns:
            dict: 包含操作结果的字典，包含以下字段：
                - filename: 文档文件名
                - table_index: 表格索引
                - row_index: 行索引
                - col_index: 列索引
                - padding_applied: 应用的内边距设置
                - unit: 使用的度量单位
                - operation_status: 操作状态（"success", "error"）

        Example:
            >>> set_table_cell_padding("doc.docx", table_index=0, row_index=1, col_index=2, top=5.0, bottom=5.0, left=10.0, right=10.0)
            >>> set_table_cell_padding("doc.docx", table_index=1, row_index=0, col_index=1, left=8.0, right=8.0, unit="points")
        """
        return format_tools.set_table_cell_padding(filename, table_index, row_index, col_index,
                                                   top, bottom, left, right, unit)



def run_server():
    """Run the Word Document MCP Server with configurable transport."""
    # Get transport configuration
    config = get_transport_config()
    
    # Setup logging
    # setup_logging(config['debug'])
    
    # Register all tools
    register_tools()
    
    # Print startup information
    transport_type = config['transport']
    print(f"Starting Word Document MCP Server with {transport_type} transport...")
    
    # if config['debug']:
    #     print(f"Configuration: {config}")
    
    try:
        if transport_type == 'stdio':
            # Run with stdio transport (default, backward compatible)
            print("Server running on stdio transport")
            mcp.run(transport='stdio')
            
        elif transport_type == 'streamable-http':
            # Run with streamable HTTP transport
            print(f"Server running on streamable-http transport at http://{config['host']}:{config['port']}{config['path']}")
            mcp.run(
                transport='streamable-http',
                host=config['host'],
                port=config['port'],
                path=config['path']
            )
            
        elif transport_type == 'sse':
            # Run with SSE transport
            print(f"Server running on SSE transport at http://{config['host']}:{config['port']}{config['sse_path']}")
            mcp.run(
                transport='sse',
                host=config['host'],
                port=config['port'],
                path=config['sse_path']
            )
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as e:
        print(f"Error starting server: {e}")
        if config['debug']:
            import traceback
            traceback.print_exc()
        sys.exit(1)
    
    return mcp


def main():
    """Main entry point for the server."""
    run_server()


if __name__ == "__main__":
    main()
