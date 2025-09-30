"""
题目创建MCP工具

此模块为在线测试系统中创建各种类型的题目提供MCP工具.
支持单选题、多选题、填空题、判断题、简答题和编程题.
"""

import requests
from typing import Annotated, List, Optional
from pydantic import Field

from ..questions.update import (
    update_fill_blank_answer,
    update_question,
    update_question_options,
    update_true_false_answer,
)
from ..questions.delete import delete_questions
from ..types.types import (
    QuestionType,
    QuestionData,
    SingleChoiceQuestion,
    MultipleChoiceQuestion,
    TrueFalseQuestion,
    FillBlankQuestion,
)
from typing import Union
from ..utils.response import ResponseUtil
from ..config import MAIN_URL, create_headers, MCP


@MCP.tool()
def create_single_choice_question(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question: Annotated[SingleChoiceQuestion, Field(description="单选题信息")],
) -> dict:
    """创建单选题"""
    question_id = None
    try:
        question_id, answer_items = _create_question_base(
            QuestionType.SINGLE_CHOICE, paper_id, question.score
        )

        _update_question_base(
            question_id,
            question.title,
            question.description,
            paper_id,
            required=question.required,
        )

        for _ in range(len(answer_items), len(question.options)):
            resp = create_answer_item(paper_id, question_id)
            if not resp.get("success"):
                raise ValueError(resp.get("msg") or resp.get("message", "未知错误"))
            answer_items.append(resp["data"])

        for item, option in zip(answer_items, question.options):
            result = update_question_options(
                question_id, item["id"], option.text, option.answer
            )
            if not result["success"]:
                raise ValueError(result.get("msg") or result.get("message", "未知错误"))

        return ResponseUtil.success(None, "题目创建成功")
    except Exception as e:
        if question_id:
            delete_questions(paper_id, [question_id])
        return ResponseUtil.error(str(e))


@MCP.tool()
def create_multiple_choice_question(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question: Annotated[MultipleChoiceQuestion, Field(description="多选题信息")],
) -> dict:
    """创建多选题"""
    question_id = None
    try:
        question_id, answer_items = _create_question_base(
            QuestionType.MULTIPLE_CHOICE, paper_id, question.score
        )

        _update_question_base(
            question_id,
            question.title,
            question.description,
            paper_id,
            required=question.required,
        )

        for _ in range(len(answer_items), len(question.options)):
            resp = create_answer_item(paper_id, question_id)
            if not resp.get("success"):
                raise ValueError(resp.get("msg") or resp.get("message", "未知错误"))
            answer_items.append(resp["data"])

        for item, option in zip(answer_items, question.options):
            result = update_question_options(
                question_id, item["id"], option.text, option.answer
            )
            if not result["success"]:
                raise ValueError(result.get("msg") or result.get("message", "未知错误"))

        return ResponseUtil.success(None, "题目创建成功")
    except Exception as e:
        if question_id:
            delete_questions(paper_id, [question_id])
        return ResponseUtil.error(str(e))


@MCP.tool()
def create_fill_blank_question(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question: Annotated[FillBlankQuestion, Field(description="填空题信息")],
) -> dict:
    """创建填空题"""
    question_id = None
    try:
        question_id = _create_question_base(
            QuestionType.FILL_BLANK, paper_id, question.score
        )[0]

        _validate_fill_blank_question(question.title, len(question.options))
        count = question.title.count("____")

        result = create_blank_answer_items(paper_id, question_id, count)
        if not result["success"]:
            raise ValueError(result.get("msg") or result.get("message", "未知错误"))
        answer_items = result["data"]

        _update_question_base(
            question_id,
            question.title,
            question.description,
            paper_id,
            required=question.required,
            is_split_answer=question.is_split_answer,
            automatic_stat=question.automatic_stat,
            automatic_type=question.automatic_type,
        )

        for item, option in zip(answer_items, question.options):
            result = update_fill_blank_answer(question_id, item["id"], option.text)
            if not result["success"]:
                raise ValueError(result.get("msg") or result.get("message", "未知错误"))

        return ResponseUtil.success(None, "题目创建成功")
    except Exception as e:
        if question_id:
            delete_questions(paper_id, [question_id])
        return ResponseUtil.error(str(e))


@MCP.tool()
def create_true_false_question(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question: Annotated[TrueFalseQuestion, Field(description="判断题信息")],
) -> dict:
    """创建判断题"""
    question_id = None
    try:
        question_id, answer_items = _create_question_base(
            QuestionType.TRUE_FALSE, paper_id, question.score
        )

        _update_question_base(
            question_id,
            question.title,
            question.description,
            paper_id,
            required=question.required,
        )

        result = update_true_false_answer(
            question_id, answer_items[question.answer]["id"]
        )
        if not result["success"]:
            raise ValueError(result.get("msg") or result.get("message", "未知错误"))

        return ResponseUtil.success(None, "题目创建成功")
    except Exception as e:
        if question_id:
            delete_questions(paper_id, [question_id])
        return ResponseUtil.error(str(e))


# 新增的简化批量创建函数
@MCP.tool()
def batch_create_questions(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    questions: Annotated[
        List[
            Union[
                SingleChoiceQuestion,
                MultipleChoiceQuestion,
                TrueFalseQuestion,
                FillBlankQuestion,
            ]
        ],
        Field(description="题目列表", min_length=1),
    ],
) -> dict:
    """批量创建题目(非官方接口),不稳定但功能更强大"""
    success_count, failed_count, results = 0, 0, []

    for i, question in enumerate(questions, 1):
        try:
            if isinstance(question, SingleChoiceQuestion):
                result = create_single_choice_question(paper_id, question)
            elif isinstance(question, MultipleChoiceQuestion):
                result = create_multiple_choice_question(paper_id, question)
            elif isinstance(question, TrueFalseQuestion):
                result = create_true_false_question(paper_id, question)
            elif isinstance(question, FillBlankQuestion):
                result = create_fill_blank_question(paper_id, question)
            if result["success"]:
                success_count += 1
                results.append(f"第{i}题: 创建成功 - {question.title}")
            else:
                failed_count += 1
                results.append(f"第{i}题: 创建失败 - {result['message']}")
        except Exception as e:
            failed_count += 1
            results.append(f"第{i}题: 创建异常 - {str(e)}")

    summary = f"批量创建完成: 成功 {success_count} 题,失败 {failed_count} 题, 总计 {len(questions)} 题"
    return ResponseUtil.success({"details": results}, summary)


@MCP.tool()
def office_create_questions(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    questions: Annotated[
        List[QuestionData],
        Field(description="题目列表", min_length=1),
    ],
) -> dict:
    """批量导入题目(官方接口),稳定性强"""
    url = f"{MAIN_URL}/survey/question/import"
    try:
        for i, question in enumerate(questions, 1):
            if question.type == QuestionType.FILL_BLANK:
                try:
                    _validate_fill_blank_question(
                        question.title, len(question.standard_answers)
                    )
                except ValueError as e:
                    return ResponseUtil.error(f"第{i}题: {str(e)}")

        response = requests.post(
            url,
            json={
                "paper_id": str(paper_id),
                "questions": [question.model_dump() for question in questions],
            },
            headers=create_headers(),
        ).json()
        if response.get("success"):
            return ResponseUtil.success(response["data"], "题目导入成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(f"题目导入失败: {str(e)}")


@MCP.tool()
def create_question(
    type_number: Annotated[int, Field(description="题目类型编号")],
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    score: Annotated[int, Field(description="题目分数", gt=0)],
    insert_question_id: Annotated[
        Optional[str], Field(description="插入指定题目ID后面")
    ] = None,
) -> dict:
    """在试卷中创建新题目(空白题目)"""
    try:
        response = requests.post(
            f"{MAIN_URL}/survey/addQuestion",
            json={
                "type": type_number,
                "paper_id": str(paper_id),
                "score": score,
                **(
                    {"insert_question_id": insert_question_id}
                    if insert_question_id is not None
                    else {}
                ),
            },
            headers=create_headers(),
        )
        response = response.json()["data"]
        return ResponseUtil.success(response, "题目创建成功")
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def create_blank_answer_items(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question_id: Annotated[str, Field(description="题目id")],
    count: Annotated[int, Field(description="空白答案项数量", gt=0)],
) -> dict:
    """创建空白答案项"""

    try:
        response = requests.post(
            f"{MAIN_URL}/survey/createBlankAnswerItems",
            json={
                "paper_id": str(paper_id),
                "question_id": str(question_id),
                "count": count,
            },
            headers=create_headers(),
        )
        response = response.json()["data"]["answer_items"]
        return ResponseUtil.success(response, "空白答案项创建成功")
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def create_answer_item(
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    question_id: Annotated[str, Field(description="题目id")],
) -> dict:
    """创建答案项"""

    try:
        response = requests.post(
            f"{MAIN_URL}/survey/createAnswerItem",
            json={"paper_id": str(paper_id), "question_id": str(question_id)},
            headers=create_headers(),
        ).json()["data"]
        return ResponseUtil.success(response, "答案项创建成功")
    except Exception as e:
        return ResponseUtil.error(str(e))


def _create_question_base(
    question_type: QuestionType,
    paper_id: str,
    score: int,
    insert_question_id: Optional[str] = None,
) -> tuple:
    """创建题目基础信息并返回question_id和answer_items"""
    data = create_question(question_type.value, paper_id, score, insert_question_id)
    if not data["success"]:
        raise ValueError(data.get("msg") or data.get("message", "未知错误"))
    return data["data"]["id"], data["data"]["answer_items"]


def _update_question_base(
    question_id: str, title: str, description: str, paper_id: str, **kwargs
) -> None:
    """更新题目基础信息，失败时清理题目"""
    result = update_question(
        question_id, title=title, description=description, **kwargs
    )
    if not result["success"]:
        delete_questions(paper_id, [question_id])
        raise ValueError(result.get("msg") or result.get("message", "未知错误"))


def _validate_fill_blank_question(title: str, answers_count: int) -> None:
    """验证填空题的格式是否正确"""
    if "____" not in title:
        raise ValueError("填空题标题必须包含空白标记'____'")

    blank_count = title.count("____")
    if blank_count != answers_count:
        raise ValueError(
            f"空白标记数量({blank_count})与答案数量({answers_count})不匹配"
        )
