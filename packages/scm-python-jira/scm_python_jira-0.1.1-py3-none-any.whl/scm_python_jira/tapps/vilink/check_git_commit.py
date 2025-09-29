from __future__ import annotations
import numbers
import yaml

# import aspose.words as aw
import sys, os, datetime, math, re
import tempfile
import requests
import json
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
from .interface import ScheduleJob
from typing import Union
from tutils.tjira_server_api import (
    jira_search,
    jira_issue,
    jira_issue_comment,
    jira_issue_original_estimate,
    jira_issue_story_point,
    jira_issue_log_time,
    jira_context,
    jira_board,
    jira_sprint,
    jira_get_epic_link,
    jira_get_original_estimate,
    jira_get_story_point,
    jira_get_log_time_hour,
    jira_is_cross_repository_summary,
    jira_get_cross_repository_issue_type,
    jira_get_components,
    jira_get_labels,
    jira_get_sprint,
    jira_get_fix_versions,
    jira_issue_components,
    jira_issue_sprint,
    jira_issue_fix_versions,
)
from typing import Literal

log = tl.log

JIRA_ISSUE_TYPES = ("Bug", "Story", "Task", "Epic", "Sub-task", "")
JiraIssueTypeLiteral = Literal["Bug", "Story", "Task", "Epic", "Sub-task", ""]
JIRA_TASKM_DEFAULT_EPIC_LINK = "TASKM-33"
JIRA_EPIC_LINK = "EPIC_LINK"
JIRA_ARCHIVE = "archive"


class Commit_Push_Param:
    ISSUE_TYPE = "issue_type"
    SUMMARY = "summary"
    EPIC_DICT = {}

    def __init__(self, summary: str, issue_type: str):
        self.summary = summary if "True" != summary else ""
        self.issue_type = issue_type
        self.__child: Commit_Push_Param = None  # type: ignore

    @classmethod
    def issue_key_is_epic(cls, issue_key: str) -> bool:
        return issue_key in cls.EPIC_DICT

    @classmethod
    def set_epic_for_issue_key(cls, issue_key: str):
        cls.EPIC_DICT[issue_key] = True

    def is_sub_task(self) -> bool:
        return "Sub-task" == self.issue_type

    def is_epic(self) -> bool:
        return "Epic" == self.issue_type

    def is_issue_type_not_confirm(self) -> bool:
        return self.issue_type == ""

    def get_issue_type(self) -> str:
        return self.issue_type

    def set_issue_type(self, issue_type: str):
        self.issue_type = issue_type

    def get_summary(self) -> str:
        return self.summary

    def set_summary(self, summary: str):
        self.summary = summary

    def set_child(self, child: Commit_Push_Param):
        self.__child = child

    def get_child(self) -> Commit_Push_Param:
        return self.__child  # type: ignore


def get_aggregation_definition(jira_template="search-issue-open"):
    result: list = []
    summary_set = set()
    params_dict = {}
    for jira_issue_type in JIRA_ISSUE_TYPES:
        if not jira_issue_type:
            continue
        params_dict[jira_issue_type] = "1"
    if response_json := jira_search(jira_context(ISSUE_TYPE="Task"), jira_template):
        issues = response_json["issues"]
        if len(issues) > 0:
            for issue in issues:
                summary = issue["fields"]["summary"]
                foo_strs = summary.split(" - ", 2)
                summary = (foo_strs[2] if len(foo_strs) > 2 else foo_strs[-1]).strip()
                if summary not in summary_set:
                    result.append(
                        {
                            "name": summary,
                            "params": params_dict,
                        }
                    )
                    summary_set.add(summary)

    return result


# -params=Epic=true,Story=story,Subtask=sub-task
def parse_params_for_commit_and_push(params: str) -> Commit_Push_Param:
    result: Commit_Push_Param = Commit_Push_Param("", "")
    tmp_value: Commit_Push_Param = result  # type: ignore
    for option_key_value in params.split(","):
        issue_type, summary = option_key_value.split("=")
        if issue_type == "Subtask":
            issue_type = "Sub-task"
        if summary == "true" and result.is_issue_type_not_confirm():
            result.set_issue_type(issue_type)
        # known issue: ssz,2025.9.28 CLI 参数处理会删除所有的'-'
        else:
            tmp_value.set_child(Commit_Push_Param(summary, issue_type))
            tmp_value = tmp_value.get_child()
    # known issue: ssz,2025.9.28 一定会生成一个Root
    return result


def parse_args_as_long_dict(args: list[str]):
    result: Commit_Push_Param = Commit_Push_Param("", "")
    tmp_value: Commit_Push_Param = result
    long_option_dict = {}
    long_option = None
    # ['jira', 'server', 'integration', '--Epic', '--Bug', 'fix bug in auto create jira issue', '--Sub-task', 'create jira issue']
    print("---parse_args_as_long_dict", args)

    for option_or_value in args:
        if option_or_value.startswith("--"):
            long_option = option_or_value.replace("--", "")
            long_option_dict[long_option] = True
            # known issue: ssz,2025.9.28 首次出现的issue_type是没有message的
            if (
                long_option in JIRA_ISSUE_TYPES
                and result.is_issue_type_not_confirm()
                and long_option != "Sub-task"
            ):
                result.set_issue_type(long_option)
        else:
            value = option_or_value
            if long_option not in JIRA_ISSUE_TYPES:
                continue
            if tmp_value:
                tmp_value.set_child(Commit_Push_Param(value, long_option))
                tmp_value = tmp_value.get_child()
            else:
                # known issue: ssz,2025.9.28 此时只允许Sub-task存在, parent_issue_type待定
                if long_option != "Sub-task":
                    raise ValueError(f"请输入一个Sub-task")
                tmp_value = Commit_Push_Param("", "")
                result = tmp_value
                tmp_value.set_child(Commit_Push_Param(value, long_option))
    return long_option_dict, result


def start_check(automatic_commit=False):
    context = thpe.create_env_context()
    hostname = tcontext.replace_by_context(context, "${env:COMPUTERNAME}")
    for job in thpe.load_yaml_from_install("vilink/jobs", "vilink"):  # type: ignore
        schedule_job = ScheduleJob(job)

        for folder in schedule_job.get_folders():
            if os.path.exists(folder):
                # --ignore-submodules=all,必须要加否则有子模块(C:\usr\ssz\workspace\git\app\bulletin) 会影响结果,认定为此repo一直有更新
                status_result = ts.call(f"cd {folder} && git status --porcelain -uall --ignore-submodules=all")  # type: ignore
                # 如果有结果代表内容有改变
                if len(status_result) > 0:
                    if automatic_commit:
                        ts.raw_detail(f"cd {folder} && git add --all")
                        ts.raw_detail(
                            f'cd {folder} && git commit -a -m "NOCR: committed by shell from {hostname} for {folder}'
                        )
                    else:
                        print(folder, status_result)
                status_result = ts.call(
                    f'cd {folder} && git status |grep "Your branch is ahead"'  # type: ignore
                )
                # 如果有结果代表提交有内容
                if len(status_result) > 0:
                    ts.raw_detail(f"cd {folder} && git pull --rebase")
                    ts.raw_detail(f"cd {folder} && git push && echo 1")


def no_any_cli_handler(aggregation_command: str, args: list[str]):
    print("---no_any_cli_handler", aggregation_command, args)
    long_option_dict, param = parse_args_as_long_dict(args)
    skip_commit = False
    param.set_summary(aggregation_command)
    if "Epic" in long_option_dict:
        log.warning("Epic不会触发提交动作且它不属于任何Repository")
        skip_commit = True
    if "Skip-Commit" in long_option_dict:
        log.warning("用户选择不提交代码,但还是会包含Repository前缀")
        skip_commit = True
    entrypoint_to_commit_and_push(
        param,
        skip_commit=skip_commit,
    )  # type: ignore


def commit_and_push_create_jira_issue_handler(
    git_repo_name: str,
    issue_key: str,
    to_create_jira_issue_summary: str,
    issue_type: str,
    parent_task_key: str,
    additional_context: dict,
):
    # known issue: ssz,2025.9.28, 此处是为了性能优化,查询过这个Issue已创建,不要删除
    if not issue_key:
        issue_key = create_jira_issue(
            to_create_jira_issue_summary,
            issue_type,  # type: ignore
            parent_task_key,
            additional_context=additional_context,
            git_repo_name=git_repo_name,
        )
        print(
            f"-----commit_and_push 新JIRA {issue_type}",
            to_create_jira_issue_summary,
        )
        if issue_key and "Epic" == issue_type:
            Commit_Push_Param.set_epic_for_issue_key(issue_key)

    return issue_key


def commit_and_push_sub_task_handler(
    git_repo_name: str,
    parent_task_key: str,
    message: str,
    additional_context: dict,
):
    # known issues: ssz,2025.9.24 只有Sub-task是无法判定parent issue type的,强制认定为Task
    task_key = parent_task_key
    issue_type = "Sub-task"
    # known issues: ssz,2025.9.24, 跨repository,不允许创建sub-task
    issue_key, _ = search_jira_issue_sub_task_by_summary(
        commit_and_push_get_search_issue_summary_handler(
            git_repo_name=git_repo_name, issue_type=issue_type, message=message
        ),
        task_key,
    )
    to_create_jira_issue_summary = (
        commit_and_push_get_create_jira_issue_summary_handler(
            git_repo_name=git_repo_name, issue_type=issue_type, message=message
        )
    )
    issue_key = commit_and_push_create_jira_issue_handler(
        git_repo_name=git_repo_name,
        issue_key=issue_key,
        to_create_jira_issue_summary=to_create_jira_issue_summary,
        issue_type=issue_type,
        parent_task_key=task_key,
        additional_context=additional_context,
    )
    return issue_key, to_create_jira_issue_summary


def commit_and_push_issue_handler(
    git_repo_name: str,
    parent_task_key: str,
    issue_key: str,
    message: str,
    issue_type: str,
    is_cross_repository: bool,
    additional_context: dict,
):
    # known issues: ssz,2025.9.24,如果用户输入的issue_type类型和jira中已存在的不一样,还会查询一次
    if not issue_key:
        issue_key, _ = search_jira_issue_by_summary(
            commit_and_push_get_search_issue_summary_handler(
                git_repo_name=git_repo_name,
                issue_type=issue_type,
                message=message,
                is_cross_repository=is_cross_repository,
            )
        )
        if issue_key and "Epic" == issue_type:
            Commit_Push_Param.set_epic_for_issue_key(issue_key)

    to_create_jira_issue_summary = (
        commit_and_push_get_create_jira_issue_summary_handler(
            git_repo_name=git_repo_name,
            issue_type=issue_type,
            message=message,
            is_cross_repository=is_cross_repository,
        )
    )
    issue_key = commit_and_push_create_jira_issue_handler(
        git_repo_name=git_repo_name,
        issue_key=issue_key,
        to_create_jira_issue_summary=to_create_jira_issue_summary,
        issue_type=issue_type,
        parent_task_key=parent_task_key,
        additional_context=additional_context,
    )
    return issue_key, to_create_jira_issue_summary


def commit_and_push_epic_handler(
    git_repo_name: str,
    message: str,
    additional_context: dict,
):
    issue_type = "Epic"
    issue_key, _ = search_jira_issue_by_summary(
        commit_and_push_get_search_issue_summary_handler(
            git_repo_name=git_repo_name, issue_type=issue_type, message=message
        )
    )
    if issue_key and "Epic" == issue_type:
        Commit_Push_Param.set_epic_for_issue_key(issue_key)

    to_create_jira_issue_summary = (
        commit_and_push_get_create_jira_issue_summary_handler(
            git_repo_name=git_repo_name, issue_type=issue_type, message=message
        )
    )
    issue_key = commit_and_push_create_jira_issue_handler(
        git_repo_name=git_repo_name,
        issue_key=issue_key,
        to_create_jira_issue_summary=to_create_jira_issue_summary,
        issue_type=issue_type,
        parent_task_key="",
        additional_context=additional_context,
    )
    return issue_key, to_create_jira_issue_summary


def commit_and_push_get_search_issue_summary_handler(
    git_repo_name: str,
    issue_type: str,
    message: str,
    is_cross_repository=False,
):
    if "Epic" == issue_type:
        return f"{issue_type} - {message}"
    if is_cross_repository:
        return f"{issue_type} - {message}"
    return f"{git_repo_name} - {issue_type} - {message}"


def commit_and_push_get_create_jira_issue_summary_handler(
    git_repo_name: str,
    issue_type: str,
    message: str,
    is_cross_repository=False,
):
    if "Epic" == issue_type:
        return f"{issue_type} - {message}"
    if is_cross_repository:
        return f"{issue_type} - {message}"
    return f"[{git_repo_name}] - {issue_type} - {message}"


def commit_and_push_cross_repository_handler(
    message: str,
    issue_type: str,
):
    is_cross_repository = (
        True if "Epic" == issue_type else jira_is_cross_repository_summary(message)
    )
    return is_cross_repository


def commit_and_push_run_git_cmd_handler(
    git_repo_name: str,
    issue_key: str,
    to_create_jira_issue_summary: str,
    issue_type: str,
):
    if not issue_key or not issue_key.startswith("TASKM"):
        raise ValueError(f"提交时候必须要指定issue_key或格式不正确{issue_key}")
    commit_messages = ts.call_cmd(
        f'git commit -a -m "{issue_key} {to_create_jira_issue_summary}" && git pull --rebase && git push && echo done'
    )
    if "done" == commit_messages[-1]:
        jira_comments = ts.call_cmd("git show --name-status --pretty=fuller HEAD")
        comment_id = jira_comments[0]
        jira_comments.insert(
            0,
            comment_id.replace(
                "commit ", f"https://de.vicp.net:58443/{git_repo_name}/-/commit/"
            ),
        )
        jira_comments.insert(
            0,
            comment_id.replace(
                "commit ", f"https://github.shao.sh/{git_repo_name}/commit/"
            ),
        )
        total_updated_line_number = jira_get_updated_line_number()
        log_time_hour = jira_get_log_time_hour(
            issue_type, total_updated_line_number, git_repo_name=git_repo_name
        )
        jira_comments.insert(
            2,
            f"total changed code line number is {total_updated_line_number}, work time is {log_time_hour}h\n",
        )
        print("\n".join(jira_comments))
        create_jira_issue_comment(issue_key, "\n".join(jira_comments))
        create_jira_issue_log_time(
            issue_key,
            log_time_hour,
        )


def entrypoint_to_commit_and_push(
    param: Commit_Push_Param,
    skip_commit=False,
):
    status_result = ts.call_cmd(f"git config --get remote.origin.url")
    url = status_result[0]
    match = re.search(r"([^/]+/[^/]+)\.git$", url)
    if match:
        git_repo_name = match.group(1)
        additional_context = {}
        epic_link = jira_get_epic_link(git_repo_name)
        additional_context[JIRA_EPIC_LINK] = epic_link.split(" ")[0]
        parent_task_key = ""
        parent_message = ""
        while param:
            issue_type = param.get_issue_type()
            if issue_type not in JIRA_ISSUE_TYPES:
                raise ValueError(
                    f"issue_type should be in {JIRA_ISSUE_TYPES}, but get {issue_type}"
                )
            message = param.get_summary()
            is_cross_repository = commit_and_push_cross_repository_handler(
                message=message,
                issue_type=issue_type,
            )
            print(
                "---entrypoint_to_commit_and_push",
                message,
                "issue_type=",
                issue_type,
                Commit_Push_Param.EPIC_DICT,
            )
            # fix skip issue creatation if three layer exists
            issue_key = ""
            if parent_task_key and Commit_Push_Param.issue_key_is_epic(parent_task_key):
                additional_context[JIRA_EPIC_LINK] = parent_task_key
            if param.is_epic():
                issue_key, to_create_jira_issue_summary = commit_and_push_epic_handler(
                    git_repo_name=git_repo_name,
                    message=message,
                    additional_context=additional_context,
                )
            elif param.is_sub_task():
                issue_key, to_create_jira_issue_summary = (
                    commit_and_push_sub_task_handler(
                        git_repo_name=git_repo_name,
                        parent_task_key=parent_task_key,
                        message=message,
                        additional_context=additional_context,
                    )
                )
            else:
                if param.is_issue_type_not_confirm():
                    issue_key, issue_type = search_jira_parent_issue_by_summary(
                        message=message, git_repo_name=git_repo_name
                    )
                    if not issue_type:
                        issue_type = jira_get_cross_repository_issue_type("")
                    if issue_key and "Epic" == issue_type:
                        Commit_Push_Param.set_epic_for_issue_key(issue_key)

                issue_key, to_create_jira_issue_summary = commit_and_push_issue_handler(
                    git_repo_name=git_repo_name,
                    parent_task_key=parent_task_key,
                    issue_key=issue_key,
                    message=message,
                    is_cross_repository=is_cross_repository,
                    issue_type=issue_type,
                    additional_context=additional_context,
                )
            parent_task_key = issue_key
            parent_message = message
            param = param.get_child()
        if skip_commit:
            return
        commit_and_push_run_git_cmd_handler(
            git_repo_name=git_repo_name,
            issue_key=issue_key,
            to_create_jira_issue_summary=to_create_jira_issue_summary,
            issue_type=issue_type,
        )
    else:
        raise Exception("未匹配到Repository")


def search_jira_issue_by_summary(summary: str):
    return search_jira_issue_by_summary_handler(summary, "search-issue-by-summary")


def search_jira_parent_issue_by_summary(message: str, git_repo_name=""):

    return search_jira_issue_by_summary_handler(
        message,
        "search-parent-issue-by-summary",
        additional_dict={"GIT_REPO_NAME": git_repo_name},
        result_handler=lambda result: (
            result["key"],
            get_jira_mapping_issue_type(result["fields"]["issuetype"]["name"]),
        ),
    )


def search_jira_issue_sub_task_by_summary(summary: str, parent_key: str):
    return search_jira_issue_by_summary_handler(
        summary, "search-issue-Sub-task-by-summary", parent_key
    )


def search_jira_issue_by_summary_handler(
    summary: str,
    jira_template="search-issue-by-summary",
    parent_key="",
    additional_dict={},
    result_handler=None,
):
    if response_json := jira_search(
        jira_context(SUMMARY=summary, ISSUE_KEY=parent_key, **additional_dict),
        jira_template,
    ):
        issues = response_json["issues"]
        if len(issues) == 0:
            return ("", "")
        result = issues[0]
        return (
            result_handler(result)
            if result_handler
            else (result["key"], result["fields"]["summary"])
        )
    else:
        return ("", "")


def search_jira_issue_original_estimate_is_empty_by_project(project_key="TASKM"):
    return search_jira_issue_by_project_generic_handler(
        "search-issue-original-estimate-is-empty-by-project", project_key
    )


def search_jira_issue_story_point_is_empty_by_project(project_key="TASKM"):
    return search_jira_issue_by_project_generic_handler(
        "search-issue-story-point-is-empty-by-project", project_key
    )


def search_jira_issue_component_is_empty_by_project(project_key="TASKM"):
    return search_jira_issue_by_project_generic_handler(
        "search-issue-component-is-empty-by-project", project_key
    )


def search_jira_issue_fix_version_is_empty_by_project(project_key="TASKM"):
    return search_jira_issue_by_project_generic_handler(
        "search-issue-fix-version-is-empty-by-project", project_key
    )


def search_jira_issue_by_project_generic_handler(
    jira_template: str, project_key="TASKM"
):
    if response_json := jira_search(
        jira_context(PROJECT_KEY=project_key),
        jira_template,
    ):
        issues = response_json["issues"]
        return issues
    else:
        return []


def search_jira_issue_label_is_empty_by_project(project_key="TASKM"):
    return search_jira_issue_by_project_generic_handler(
        "search-issue-label-is-empty-by-project", project_key
    )


def search_jira_issue_sprint_is_empty_by_project(project_key="TASKM"):
    return search_jira_issue_by_project_generic_handler(
        "search-issue-sprint-is-empty-by-project", project_key
    )


def create_jira_issue(
    summary: str,
    issue_type: JiraIssueTypeLiteral = "Task",
    task_key="",
    additional_context: dict = {},
    git_repo_name="",
) -> str:
    default_epic_link = tcontext.get_field(
        additional_context, JIRA_EPIC_LINK, JIRA_TASKM_DEFAULT_EPIC_LINK
    )

    if response_json := jira_issue(
        jira_context(
            PROJECT_KEY="TASKM",
            SUMMARY=summary,
            ISSUE_TYPE=issue_type,
            ISSUE_KEY=task_key,
            LIST_SPLIT_COMPONENT=",",
            COMPONENT_LIST=jira_get_components(git_repo_name),
            LIST_SPLIT_LABEL=",",
            SPRINT=jira_get_sprint(git_repo_name),
            FIX_VERSION_LIST=jira_get_fix_versions(git_repo_name),
            LIST_SPLIT_FIX_VERSION=",",
            LABEL_LIST=jira_get_labels(git_repo_name),
            ORIGINAL_ESTIMATE=f"{jira_get_original_estimate(issue_type)}",
            STORY_POINT=jira_get_story_point(issue_type),
            EPIC_LINK="" if issue_type == "Epic" else default_epic_link,
        ),
        (
            "create-epic-without-description"
            if issue_type == "Epic"
            else (
                "create-sub-task-without-description"
                if issue_type == "Sub-task"
                else "create-issue-without-description"
            )
        ),
    ):
        print(f"✅ JIRA ISSUE {issue_type} 创建成功")
        return response_json["key"]
    return ""


def create_jira_issue_comment(issue_key: str, comment: str):
    if response_json := jira_issue_comment(
        jira_context(
            COMMENT=comment,
        ),
        "create-issue-comment",
        issue_key,
    ):
        print("✅ JIRA ISSUE COMMENT 创建成功")
        print(response_json)


def create_jira_issue_log_time(issue_key: str, log_time_hour: float = 1):
    if log_time_hour < 1:
        log.warning("the change is too small, skip log time for it")
    if response_json := jira_issue_log_time(
        jira_context(
            LOG_TIME_HOUR=log_time_hour,
        ),
        issue_key,
    ):
        print(f"✅ JIRA ISSUE Log Time {log_time_hour}h成功")
        print(response_json)


def get_jira_mapping_issue_type(issue_type: str):
    issue_type_mapping = {
        "故障": "Bug",
        "故事": "Story",
        "任务": "Task",
        "子任务": "Sub-task",
    }
    if issue_type in issue_type_mapping:
        issue_type = issue_type_mapping[issue_type]
    return issue_type


def update_jira_issue_original_estimate_by_project(project_key="TASKM"):

    for issue in search_jira_issue_original_estimate_is_empty_by_project(project_key):
        issue_type = issue["fields"]["issuetype"]["name"]
        issue_type = get_jira_mapping_issue_type(issue_type)
        issue_key = issue["key"]
        work_time_hour = jira_get_original_estimate(issue_type)
        update_jira_issue_original_estimate(issue_key, work_time_hour)


def update_jira_issue_story_point_by_project(project_key="TASKM"):

    for issue in search_jira_issue_story_point_is_empty_by_project(project_key):
        issue_type = issue["fields"]["issuetype"]["name"]
        issue_type = get_jira_mapping_issue_type(issue_type)
        issue_summary = issue["fields"]["summary"]
        issue_key = issue["key"]
        story_point = jira_get_story_point(issue_type)
        print(issue_key, issue_summary, issue)
        update_jira_issue_story_point(issue_key, story_point)


def update_jira_issue_story_point(issue_key: str, time_unit_hour=1):
    if response_json := jira_issue_story_point(
        jira_context(
            STORY_POINT=time_unit_hour,
        ),
        "update-issue-story-point",
        issue_key,
    ):
        print(f"✅ JIRA ISSUE {issue_key} 更新StoryPoint成功")
        print(response_json)


def update_jira_issue_original_estimate(issue_key: str, time_unit_hour=1):
    if response_json := jira_issue_original_estimate(
        jira_context(
            ORIGINAL_ESTIMATE=f"{time_unit_hour}",
        ),
        "update-issue-original-estimate",
        issue_key,
    ):
        print(f"✅ JIRA ISSUE {issue_key} 更新初始工时成功")
        print(response_json)


def update_jira_issue_components(issue_key: str, git_repo_name=""):
    if response_json := jira_issue_components(
        jira_context(
            LIST_SPLIT_COMPONENT=",",
            COMPONENT_LIST=jira_get_components(git_repo_name),
        ),
        "update-issue-components",
        issue_key,
    ):
        print(f"✅ JIRA ISSUE {issue_key} 更新Components成功")
        print(response_json)


def update_jira_issue_fix_version(issue_key: str, git_repo_name=""):
    if response_json := jira_issue_fix_versions(
        jira_context(
            FIX_VERSION_LIST=jira_get_fix_versions(git_repo_name),
            LIST_SPLIT_FIX_VERSION=",",
        ),
        "update-issue-fix-versions",
        issue_key,
    ):
        print(f"✅ JIRA ISSUE {issue_key} 更新Fix Version成功")
        print(response_json)


def update_jira_issue_labels(issue_key: str, git_repo_name=""):
    if response_json := jira_issue_components(
        jira_context(
            LIST_SPLIT_LABEL=",",
            LABEL_LIST=jira_get_labels(git_repo_name),
        ),
        "update-issue-labels",
        issue_key,
    ):
        print(f"✅ JIRA ISSUE {issue_key} 更新Labels成功")
        print(response_json)


def update_jira_issue_sprint(issue_key: str, git_repo_name=""):
    if response_json := jira_issue_sprint(
        jira_context(
            SPRINT=jira_get_sprint(git_repo_name),
        ),
        "update-issue-sprint",
        issue_key,
    ):
        print(f"✅ JIRA ISSUE {issue_key} 更新Sprint成功")
        print(response_json)


def list_jira_board():
    context = jira_context()
    for board in jira_board(context):
        board_id = board["id"]
        board_name = board["name"]
        print("--------", board_name, board)
        for sprint in jira_sprint(context, board_id):
            sprint_id = sprint["id"]
            sprint_name = sprint["name"]
            print("\t--------", sprint_name, sprint)


def list_jira_issue_component_is_empty():
    for issue in search_jira_issue_component_is_empty_by_project():
        key = issue["key"]
        summary = issue["fields"]["summary"]
        print("---list_jira_issue_component_is_empty", key, summary)
        match = re.search(r"\[(.*?)\]", summary)
        if match:
            git_repo_name = match.group(1)
            print(git_repo_name, jira_get_components(git_repo_name=git_repo_name))
            update_jira_issue_components(key, git_repo_name)


def list_jira_issue_fix_version_is_empty():
    for issue in search_jira_issue_fix_version_is_empty_by_project():
        key = issue["key"]
        summary = issue["fields"]["summary"]
        print("---list_jira_issue_fix_version_is_empty", key, summary)
        match = re.search(r"\[(.*?)\]", summary)
        if match:
            git_repo_name = match.group(1)
            print(git_repo_name, jira_get_fix_versions(git_repo_name=git_repo_name))
            update_jira_issue_fix_version(key, git_repo_name)
        elif jira_issue_is_archive(summary):
            update_jira_issue_fix_version(key, JIRA_ARCHIVE)


def jira_issue_is_archive(summary: str):
    match = re.search(r"^(Epic|Bug|Story|Sub-task|Task) -", summary)
    return not match


def list_jira_issue_label_is_empty():
    for issue in search_jira_issue_label_is_empty_by_project():
        key = issue["key"]
        summary = issue["fields"]["summary"]
        print("---list_jira_issue_label_is_empty", key, summary)
        match = re.search(r"\[(.*?)\]", summary)
        if match:
            git_repo_name = match.group(1)
            print(git_repo_name, jira_get_labels(git_repo_name=git_repo_name))
            update_jira_issue_labels(key, git_repo_name)
        elif jira_issue_is_archive(summary):
            update_jira_issue_labels(key, JIRA_ARCHIVE)


def list_jira_issue_sprint_is_empty():
    for issue in search_jira_issue_sprint_is_empty_by_project():
        key = issue["key"]
        summary = issue["fields"]["summary"]
        print("---list_jira_issue_sprint_is_empty", key, summary)
        match = re.search(r"\[(.*?)\]", summary)
        if match:
            git_repo_name = match.group(1)
            print(git_repo_name, jira_get_sprint(git_repo_name=git_repo_name))
        elif jira_issue_is_archive(summary):
            update_jira_issue_sprint(key, JIRA_ARCHIVE)


def jira_get_updated_line_number():
    total_line_number = 0
    for line in ts.call_cmd(f'git show --numstat --format=""'):
        parts = line.split()
        total_line_number += int(parts[0]) + int(parts[1])
    return total_line_number
