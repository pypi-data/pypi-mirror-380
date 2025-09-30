"""
题目更新MCP工具

此模块为在线测试系统中更新题目及其选项提供MCP工具.
"""

import json
import requests
import random
import string
from typing import Annotated, List, Optional
from pydantic import Field

from ..utils.response import ResponseUtil
from ..config import MAIN_URL, create_headers, MCP
from ..types.types import (
    AnswerChecked,
    AutoScoreType,
    QuestionScoreType,
    RequiredType,
    AutoStatType,
    RandomizationType,
)


@MCP.tool()
def update_question(
    question_id: Annotated[str, Field(description="题目id")],
    title: Annotated[Optional[str], Field(description="题目陈述")] = None,
    score: Annotated[Optional[int], Field(description="题目分值", ge=0)] = None,
    description: Annotated[
        Optional[str],
        Field(
            description="答案解析(答案请提供足够详细解析,避免过于简短或过长,注意不要搞错成题目陈述)"
        ),
    ] = None,
    required: Annotated[
        Optional[RequiredType], Field(description="是否必答 1=否, 2=是")
    ] = None,
    is_split_answer: Annotated[
        Optional[bool], Field(description="是否允许多个答案(仅填空题)")
    ] = None,
    automatic_stat: Annotated[
        Optional[AutoStatType],
        Field(description="自动评分设置(仅填空题) 1=关闭, 2=开启"),
    ] = None,
    automatic_type: Annotated[
        Optional[AutoScoreType],
        Field(
            description="""填空题自动评分类型(仅填空题)[必须严格根据题目情况选择]:
                        - 1=精确匹配+有序排序: 答案必须完全匹配且顺序一致,适用于每个空只有一个正确答案的情况;
                        - 2=部分匹配+有序排序: 答案部分匹配且顺序一致,适用于每个空有多个正确答案的情况;
                        - 11=精确匹配+无序排序: 答案必须完全匹配但顺序不限,适用于每个空只有一个正确答案且答案顺序不重要的情况;
                        - 12=部分匹配+无序排序: 答案部分匹配且顺序不限,适用于每个空有多个正确答案且答案顺序不重要的情况;
                    """.replace("\n", " ").strip(),
        ),
    ] = None,
) -> dict:
    """更新题目设置"""
    try:
        url = f"{MAIN_URL}/survey/updateQuestion"
        response = requests.post(
            url,
            json={
                "question_id": str(question_id),
                **(
                    {
                        "title": json.dumps(
                            {"blocks": [{"text": title}], "entityMap": {}}
                        )
                    }
                    if title is not None
                    else {}
                ),
                **({"description": description} if description is not None else {}),
                **({"required": required} if required is not None else {}),
                **({"score": score} if score is not None else {}),
                **(
                    {"is_split_answer": is_split_answer}
                    if is_split_answer is not None
                    else {}
                ),
                **(
                    {"automatic_stat": automatic_stat}
                    if automatic_stat is not None
                    else {}
                ),
                **(
                    {"automatic_type": automatic_type}
                    if automatic_type is not None
                    else {}
                ),
            },
            headers=create_headers(),
        ).json()

        if response.get("success"):
            return ResponseUtil.success(None, "题目更新成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def update_question_options(
    question_id: Annotated[str, Field(description="题目id")],
    answer_item_id: Annotated[str, Field(description="选项id")],
    option_text: Annotated[Optional[str], Field(description="选项文本内容")] = None,
    is_answer: Annotated[Optional[bool], Field(description="是否为正确答案")] = False,
) -> dict:
    """更新单选或多选题的选项内容"""
    try:
        key = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
        payload = {
            "question_id": str(question_id),
            "answer_item_id": str(answer_item_id),
        }
        if option_text is not None:
            payload["value"] = json.dumps(
                {
                    "blocks": [
                        {
                            "key": key,
                            "text": option_text,
                            "type": "unstyled",
                            "depth": 0,
                            "inlineStyleRanges": [],
                            "entityRanges": [],
                            "data": {},
                        }
                    ],
                    "entityMap": {},
                }
            )
        if is_answer:
            payload["answer_checked"] = 2

        response = requests.post(
            url=f"{MAIN_URL}/survey/updateAnswerItem",
            json=payload,
            headers=create_headers(),
        ).json()

        if response.get("success"):
            simplified_data = [
                {
                    "id": item["id"],
                    "question_id": item["question_id"],
                    "answer": item["value"],
                    "correct": AnswerChecked.get(item["answer_checked"]),
                }
                for item in response["data"]
            ]
            return ResponseUtil.success(simplified_data, "选项更新成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def update_fill_blank_options(
    question_id: Annotated[str, Field(description="题目id")],
    answer_item_id: Annotated[str, Field(description="选项id")],
    answer: Annotated[str, Field(description="选项文本内容")],
) -> dict:
    """更新填空题的选项内容"""
    try:
        response = requests.post(
            url=f"{MAIN_URL}/survey/updateAnswerItem",
            json={
                "question_id": str(question_id),
                "answer_item_id": str(answer_item_id),
                "value": answer,
            },
            headers=create_headers(),
        ).json()

        if response.get("success"):
            simplified_data = [
                {
                    "id": item["id"],
                    "question_id": item["question_id"],
                    "answer": item["answer"],
                }
                for item in response["data"]
            ]
            return ResponseUtil.success(simplified_data, "选项更新成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def update_fill_blank_answer(
    question_id: Annotated[str, Field(description="题目id")],
    answer_item_id: Annotated[str, Field(description="答案项id")],
    answer_text: Annotated[str, Field(description="答案文本内容")],
) -> dict:
    """更新填空答案"""
    try:
        response = requests.post(
            f"{MAIN_URL}/survey/updateAnswerItem",
            json={
                "question_id": str(question_id),
                "answer_item_id": str(answer_item_id),
                "answer": answer_text,
            },
            headers=create_headers(),
        ).json()
        return ResponseUtil.success(response, "填空答案更新成功")
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def update_true_false_answer(
    question_id: Annotated[str, Field(description="题目id")],
    answer_item_id: Annotated[str, Field(description="答案项id")],
) -> dict:
    """更新判断题答案,将选项id对应的选项设为正确答案"""
    try:
        response = requests.post(
            f"{MAIN_URL}/survey/updateAnswerItem",
            json={
                "question_id": str(question_id),
                "answer_item_id": str(answer_item_id),
                "answer_checked": 2,
            },
            headers=create_headers(),
        ).json()
        return ResponseUtil.success(response, "判断题答案更新成功")
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def update_paper_randomization(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question_shuffle: Annotated[
        RandomizationType, Field(description="是否启用题目随机化,1为关闭,2为开启")
    ] = RandomizationType.DISABLED,
    option_shuffle: Annotated[
        RandomizationType, Field(description="是否启用选项随机化,1为关闭,2为开启")
    ] = RandomizationType.DISABLED,
    question_score_type: Annotated[
        QuestionScoreType, Field(description="题目评分类型 1=严格计分, 2=宽分模式")
    ] = QuestionScoreType.LENIENT,
) -> dict:
    """更新试卷的题目和选项随机化设置"""
    try:
        response = requests.post(
            f"{MAIN_URL}/survey/updatePaper",
            json={
                "paper_id": str(paper_id),
                "question_random": option_shuffle,
                "random": question_shuffle,
                "question_score_type": question_score_type,
            },
            headers=create_headers(),
        ).json()

        if response.get("success"):
            return ResponseUtil.success(None, "试卷随机化设置更新成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def move_answer_item(
    question_id: Annotated[str, Field(description="题目id")],
    answer_item_ids: Annotated[
        list[str], Field(description="按新顺序排列的选项id列表", min_length=1)
    ],
) -> dict:
    """调整题目选项顺序"""
    try:
        response = requests.post(
            f"{MAIN_URL}/survey/moveAnswerItem",
            json={
                "question_id": str(question_id),
                "answer_item_ids": answer_item_ids,
            },
            headers=create_headers(),
        ).json()
        if response.get("success"):
            return ResponseUtil.success(None, "选项顺序调整成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def update_paper_question_order(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question_ids: Annotated[
        List[str], Field(description="按新顺序排列的题目id列表", min_length=1)
    ],
) -> dict:
    """更新试卷的题目顺序"""
    try:
        response = requests.post(
            f"{MAIN_URL}/survey/moveQuestion",
            json={
                "paper_id": str(paper_id),
                "question_ids": [str(qid) for qid in question_ids],
            },
            headers=create_headers(),
        ).json()
        if response.get("success"):
            filtered_data = {
                k: response["data"][k] if k != "questions_sort" else response["data"][k].split(',')
                for k in ["id", "title", "updated_at", "questions_sort"]
                if k in response["data"]
            }
            return ResponseUtil.success(filtered_data, "试卷题目顺序更新成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))
