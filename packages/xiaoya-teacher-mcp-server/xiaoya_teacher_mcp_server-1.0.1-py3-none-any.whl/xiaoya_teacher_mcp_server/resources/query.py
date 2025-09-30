"""
资源查询MCP工具

此模块为从课程管理系统中查询教育资源和课程信息提供MCP工具.
"""

import requests
from typing import Annotated, Literal
from pydantic import Field

from ..utils.response import ResponseUtil
from ..config import MAIN_URL, create_headers, MCP


@MCP.tool()
def query_course_resources(
    group_id: Annotated[str, Field(description="课程组id")],
    format_type: Annotated[
        Literal["tree", "flat"],
        Field(
            description='返回格式("tree"为层级式,"flat"为列表式)',
            pattern="^(tree|flat)$",
        ),
    ],
) -> dict:
    """查询特定组的所有课程资源"""
    try:
        response = requests.get(
            f"{MAIN_URL}/resource/queryCourseResources/v2",
            headers=create_headers(),
            params={"group_id": str(group_id)},
        ).json()

        if not response.get("success"):
            return ResponseUtil.error(
                response.get("msg") or response.get("message", "未知错误")
            )

        resources = [
            {
                key: item[key]
                for key in [
                    "id",
                    "parent_id",
                    "quote_id",
                    "name",
                    "type",
                    "path",
                    "mimetype",
                    "sort_position",
                    "created_at",
                    "updated_at",
                ]
                if key in item
            }
            for item in response["data"]
        ]

        for idx, item in enumerate(response["data"]):
            if "link_tasks" in item and item["link_tasks"]:
                resources[idx]["link_tasks"] = [
                    {
                        (k if k != "paper_publish_id" else "publish_id"): t[k]
                        for k in [
                            "task_id",
                            "start_time",
                            "end_time",
                            "paper_publish_id",
                        ]
                        if k in t
                    }
                    for t in item["link_tasks"]
                ]

        for resource in resources:
            resource["is_folder"] = resource["mimetype"] is None
            resource["sort_position"] = resource["sort_position"]
            resource["level"] = len(resource["path"].split("/")) - 1
            if format_type == "tree" and resource["is_folder"]:
                resource["children"] = []
        resources.sort(key=lambda x: x["sort_position"])

        resource_map = {r["id"]: r for r in resources}

        def build_file_path(resource_id):
            if not resource_id or resource_id not in resource_map:
                return ""
            path_parts = []
            current = resource_map[resource_id]
            while current:
                path_parts.append(current["name"])
                parent_id = current["parent_id"]
                current = resource_map.get(parent_id) if parent_id else None
            return "/".join(reversed(path_parts))

        for resource in resources:
            resource["file_path"] = build_file_path(resource["id"])

        if format_type == "tree":
            root_resources = []
            for resource in resources:
                parent_id = resource["parent_id"]
                if parent_id in resource_map and resource_map[parent_id].get(
                    "is_folder"
                ):
                    resource_map[parent_id]["children"].append(resource)
                else:
                    root_resources.append(resource)
            return ResponseUtil.success(root_resources, "查询成功")

        return ResponseUtil.success(resources, "查询成功")
    except Exception as e:
        return ResponseUtil.error(str(e))
