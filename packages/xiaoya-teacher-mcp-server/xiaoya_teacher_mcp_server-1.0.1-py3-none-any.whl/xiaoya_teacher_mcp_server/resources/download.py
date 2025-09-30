"""
文件下载MCP工具

此模块为在线测试系统中下载文件提供MCP工具.
支持通过文件id和文件名下载文件并转换为markdown格式.
"""

import tempfile
import requests
from markitdown import MarkItDown
from urllib.parse import quote
from pathlib import Path
from typing import Annotated, Optional
from pydantic import Field

from ..utils.response import ResponseUtil
from ..config import DOWNLOAD_URL, create_headers, MCP


@MCP.tool()
def download_file(
    quote_id: Annotated[str, Field(description="文件quote_id")],
    filename: Annotated[str, Field(description="文件名")],
    save_path: Annotated[
        Optional[str],
        Field(description="文件保存路径[默认临时文件夹]", default=None),
    ] = None,
) -> dict:
    """获取下载链接并自动下载文件内容"""
    try:
        url = f"{DOWNLOAD_URL}/cloud/file_down/{quote_id}/v2?filename={quote(filename)}"
        response = requests.get(url, headers=create_headers()).json()
        if not response.get("success"):
            return ResponseUtil.error(
                f"获取下载链接失败: {filename},{response.get('msg').get('message', '未知错误')}"
            )

        download_response = requests.get(response["data"]["download_url"], stream=True)
        download_response.raise_for_status()

        file_path = (
            save_path
            if save_path
            else tempfile.NamedTemporaryFile(delete=False, suffix=f"_{filename}").name
        )

        with open(file_path, "wb") as f:
            f.write(download_response.content)

        return ResponseUtil.success(
            {
                "filename": filename,
                "file_path": file_path,
                "content_type": download_response.headers["Content-Type"],
            },
            f"文件下载成功: {file_path}",
        )
    except Exception as e:
        return ResponseUtil.error(f"下载文件{filename}失败: {str(e)}")


@MCP.tool()
def read_file_by_markdown(
    quote_id: Annotated[Optional[str], Field(description="文件quote_id", default=None)],
    filename: Annotated[Optional[str], Field(description="文件名", default=None)],
    file_path: Annotated[
        Optional[str], Field(description="本地文件路径", default=None)
    ],
) -> dict:
    """使用markitdown工具,通过文件id和文件名下载文件并转换为markdown格式,或直接转换本地文件,读取文本内容"""
    try:
        if file_path:
            result = MarkItDown().convert(Path(file_path))
            return ResponseUtil.success(
                {"content": result.text_content},
                f"本地文件转换为markdown成功: {file_path}",
            )
        elif quote_id and filename:
            url = f"{DOWNLOAD_URL}/cloud/file_down/{quote_id}/v2?filename={quote(filename)}"
            response = requests.get(url, headers=create_headers()).json()
            if not response.get("success"):
                return ResponseUtil.error(f"获取下载链接失败: {filename}")

            download_response = requests.get(response["data"]["download_url"])
            download_response.raise_for_status()
            result = MarkItDown().convert(download_response)
            return ResponseUtil.success(
                {"content": result.text_content},
                f"文件下载且转换为markdown成功: {filename}",
            )
        else:
            return ResponseUtil.error("请提供file_path或者同时提供file_id和filename")

    except Exception as e:
        return ResponseUtil.error(f"处理文件失败: {str(e)}")
