"""
任务查询模块

本模块为课程管理系统提供任务相关的查询功能,包括课程组任务列表、任务详情、学生答题情况等,供 MCP 工具调用.
"""

import json
import requests
from typing import Annotated
from pydantic import Field

from xiaoya_teacher_mcp_server.types.types import AnswerChecked


from ..utils.response import ResponseUtil
from ..config import MAIN_URL, TASK_URL, create_headers, MCP


@MCP.tool()
def query_group_tasks(
    group_id: Annotated[str, Field(description="课程组id")],
) -> dict:
    """查询课程组发布的全部任务(缺少public_id,只能获取卷子的文件id,是query_task_info的前置接口)"""
    try:
        response = requests.get(
            f"{TASK_URL}/group/task/queryTaskNotices",
            headers=create_headers(),
            params={"group_id": str(group_id)},
        ).json()
        if response.get("success"):
            tasks = response["data"]["teacher_tasks"]
            keep_keys = ["id", "node_id", "created_at", "end_time"]
            for task in tasks:
                task["paper_id"] = task["quote_id"]
            filtered_tasks = []

            for task in tasks:
                filtered_task = {key: task[key] for key in keep_keys}
                filtered_task["subgroups"] = [
                    {"group_name": sg["group_name"], "id": sg["id"]}
                    for sg in task["subgroups"]
                ]
                filtered_task["paper_id"] = task["quote_id"]
                filtered_tasks.append(filtered_task)

            return ResponseUtil.success(filtered_tasks, "任务查询成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def query_task_info(
    node_id: Annotated[
        str,
        Field(
            description="卷子的node_id(通过query_course_resources/query_group_tasks获取id)"
        ),
    ],
    group_id: Annotated[str, Field(description="课程组id")],
) -> dict:
    """查询指定卷子的全部任务信息(包含每个任务publish_id以及卷子的paper_id等)"""
    try:
        response = requests.get(
            f"{MAIN_URL}/resource/queryResource/v3",
            headers=create_headers(),
            params={"node_id": str(node_id), "group_id": str(group_id)},
        ).json()

        if response.get("success"):
            data = response["data"]
            task = {
                "paper_id": data["quote_id"],
                "id": data["id"],
                "parent_id": data["parent_id"],
                "name": data["name"],
                "type": data["type"],
                "path": data["path"],
                "created_at": data["created_at"],
                "updated_at": data["updated_at"],
                "link_tasks": [
                    {
                        "task_id": t["task_id"],
                        "start_time": t["start_time"],
                        "end_time": t["end_time"],
                        "publish_id": t["paper_publish_id"],
                    }
                    for t in data["link_tasks"]
                ],
            }
            return ResponseUtil.success(task, "任务id查询成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def query_test_result(
    group_id: Annotated[str, Field(description="课程组id")],
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    publish_id: Annotated[
        str,
        Field(
            description="发布id(需通过query_task_info/query_course_resources获取publish_id)"
        ),
    ],
) -> dict:
    """查询小测的学生答题情况(包含mark_mode_id)"""
    try:
        response = requests.get(
            f"{MAIN_URL}/survey/course/queryStuAnswerList/v2",
            headers=create_headers(),
            params={
                "group_id": str(group_id),
                "paper_id": str(paper_id),
                "publish_id": str(publish_id),
            },
        ).json()

        if response.get("success"):
            processed_data = {}

            if "lost_members" in response["data"]:
                keep_keys_lost = [
                    "class_id",
                    "class_name",
                    "nickname",
                    "student_number",
                ]
                processed_data["lost_members"] = [
                    {key: member[key] for key in keep_keys_lost if key in member}
                    for member in response["data"]["lost_members"]
                ]

            if "answer_records" in response["data"]:
                processed_data["answer_records"] = [
                    {
                        "record_id": record["id"],
                        "actual_score": record["actual_score"],
                        "answer_time": record["answer_time"],
                        "created_at": record["created_at"],
                        "nickname": record["nickname"],
                        "student_number": record["student_number"],
                        "class_id": record["class_id"],
                        "class_name": record["class_name"],
                        "answer_rate": record["answer_rate"],
                    }
                    for record in response["data"]["answer_records"]
                ]
                processed_data["mark_mode_id"] = response["data"]["mark_mode"][
                    "mark_mode_id"
                ]
            return ResponseUtil.success(processed_data, "小测答题情况查询成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))


@MCP.tool()
def query_preview_stu_paper(
    group_id: Annotated[str, Field(description="课程组id")],
    paper_id: Annotated[str, Field(description="试卷paper_id")],
    mark_mode_id: Annotated[
        str, Field(description="修改模式mark_mode_id(通过query_test_result获取)")
    ],
    publish_id: Annotated[
        str,
        Field(
            description="发布id(需通过query_task_info/query_course_resources获取publish_id)"
        ),
    ],
    record_id: Annotated[
        str, Field(description="答题记录id(通过query_test_result获取record_id)")
    ],
) -> dict:
    """查询学生答题预览信息"""
    try:
        response = requests.get(
            f"{MAIN_URL}/survey/course/queryMarkRecord",
            headers=create_headers(),
            params={
                "group_id": str(group_id),
                "paper_id": str(paper_id),
                "publish_id": str(publish_id),
                "mark_mode_id": str(mark_mode_id),
                "answer_record_id": str(record_id),
            },
        ).json()
        if response.get("success"):

            def parse_text(text):
                try:
                    return json.loads(text).get("blocks", [{}])[0].get("text", text)
                except Exception:
                    return text

            def parse_answer_items(answer_items):
                return [
                    {
                        k: v
                        for k, v in {
                            "id": item["id"],
                            "correct": AnswerChecked.get(item["answer_checked"]),
                            "answer": item["answer"] if item["answer"] else None,
                            "value": parse_text(item["value"])
                            if parse_text(item["value"])
                            else None,
                        }.items()
                        if v is not None
                    }
                    for item in answer_items
                ]

            record = response["data"]["answer_record"]
            questions = response["data"]["questions"]
            answer_map = {ans["question_id"]: ans for ans in record["answers"]}

            integrated_questions = []
            for q in questions:
                user_ans = answer_map[q["id"]]
                integrated_questions.append(
                    {
                        "id": q["id"],
                        "title": parse_text(q["title"]),
                        "description": parse_text(q["description"]),
                        "score": q["score"],
                        "options": parse_answer_items(q["answer_items"]),
                        "user_answer": parse_text(user_ans["answer"]),
                        "user_score": user_ans["score"],
                    }
                )

            return ResponseUtil.success(integrated_questions, "学生答题预览查询成功")
        else:
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )
    except Exception as e:
        return ResponseUtil.error(str(e))
