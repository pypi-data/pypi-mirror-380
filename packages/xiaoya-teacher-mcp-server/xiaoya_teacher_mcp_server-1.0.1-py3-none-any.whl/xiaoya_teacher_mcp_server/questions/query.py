"""
题目查询MCP工具

此模块为在线测试系统中查询试卷和题目提供MCP工具.
"""

import requests
from typing import Annotated
from pydantic import Field

from xiaoya_teacher_mcp_server.types.types import AnswerChecked

from ..utils.response import ResponseUtil
from ..config import MAIN_URL, create_headers, MCP
import json


@MCP.tool()
def query_paper(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    group_id: Annotated[str, Field(description="组id")],
) -> dict:
    """查询试卷编辑缓冲区信息"""
    try:
        response = requests.get(
            f"{MAIN_URL}/survey/queryPaperEditBuffer",
            headers=create_headers(),
            params={"paper_id": str(paper_id), "group_id": str(group_id)},
        ).json()
        if response.get("success"):
            data = response["data"]
            questions = {
                "question_shuffle": data["random"],
                "option_shuffle": data["question_random"],
                "id": data["id"],
                "paper_id": data["paper_id"],
                "title": data["title"],
                "updated_at": data["updated_at"],
            }

            def parse_text(text):
                try:
                    return json.loads(text).get("blocks", [{}])[0].get("text", text)
                except Exception:
                    return text

            def parse_answer_items(answer_items):
                return [
                    {
                        "answer": item["answer"],
                        "value": parse_text(item["value"]),
                        "id": item["id"],
                        "correct": AnswerChecked.get(item["answer_checked"]),
                    }
                    for item in answer_items
                ]

            questions["questions"] = [
                {
                    "id": q["id"],
                    "title": parse_text(q["title"]),
                    "description": q["description"],
                    "score": q["score"],
                    "required": q["required"],
                    "is_split_answer": q["is_split_answer"],
                    "automatic_type": q["automatic_type"],
                    "automatic_stat": q["automatic_stat"],
                    "answer_items_sort": q["answer_items_sort"],
                    "answer_items": parse_answer_items(q["answer_items"]),
                }
                for q in data["questions"]
            ]
            return ResponseUtil.success(questions, "试卷查询成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))
