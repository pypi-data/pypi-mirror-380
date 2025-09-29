import tapps.vilink.check_git_commit as vilink_check_git_commit
from tio.tcli import OptParser, cli_invoker
import tlog.tlogging as tl

flags = [
    ("c", "commit", "automatically commit", ["vilink/check-git-commit"]),
    ("n:", "name=", "message for commit", ["vilink/commit-push"]),
]

opp = OptParser(flags)

"""
    启动一个python process来执行检查哪些repo没有提交
    相关配置文件
    sample.yaml:    sh/etc/install.sample.yaml
    runtime.yaml:   ${hostname}/etc/vilink.install.runtime.yaml
"""

log = tl.log


# check all repo defined in vilink/job, if have uncommit, commit it
@cli_invoker("vilink/check-git-commit")
def vilink_check_git_commit_handler(commit=False):
    log.info("start vilink check uncommit in git repo")
    vilink_check_git_commit.start_check(automatic_commit=commit)


"""
    完成代码提交,检查JIRA task是否创建,如果没有则自动创建
    不允许提交Epic, 只创建, Epic没有Repository Path
    相关配置文件
    sample.yaml:    sh/etc/install.sample.yaml
    runtime.yaml:   ${hostname}/etc/vilink.install.runtime.yaml
"""


# git commit and pull --rebase and push with check JIRA task creation
@cli_invoker(
    "vilink/commit-push",
    arggreation=lambda: vilink_check_git_commit.get_aggregation_definition(
        "search-issue-all"
    ),
    no_any_cli_handler=vilink_check_git_commit.no_any_cli_handler,
    command_is_match_handler=lambda aggregation_command_list, aggregation_command_name: " ".join(
        aggregation_command_list
    )
    == aggregation_command_name,
)
def vilink_git_commit_push_handler(name=None, params=""):
    log.info(f"--message={name} -params={params}")
    parsed_param = vilink_check_git_commit.parse_params_for_commit_and_push(params)
    parsed_param.set_summary(name)
    if not name:
        addition_sub_cmd_json_file = os.path.join(
            os.path.expanduser("~"), ".ium", f"pycli-vilink-commit-push.json"
        )
        with open(addition_sub_cmd_json_file, "w") as outfile:
            json.dump(
                vilink_check_git_commit.get_aggregation_definition("search-issue-open"),
                outfile,
            )
    else:
        vilink_check_git_commit.entrypoint_to_commit_and_push(parsed_param)


@cli_invoker("vilink/hello-world")  # to test meaninglessly
def vilink_hello_world_handler():
    # vilink_check_git_commit.update_jira_issue_story_point_by_project("TASKM")
    # vilink_check_git_commit.list_jira_board()
    # vilink_check_git_commit.create_jira_issue_log_time("TASKM-107", log_time_hour=0.05)
    # print(vilink_check_git_commit.jira_get_updated_line_number())
    # vilink_check_git_commit.list_jira_issue_component_is_empty()
    # vilink_check_git_commit.list_jira_issue_label_is_empty()
    # vilink_check_git_commit.list_jira_issue_fix_version_is_empty()
    vilink_check_git_commit.list_jira_issue_sprint_is_empty()
    # exist_object = []
    # for index in range(1, 100):
    #     exist_object.append(
    #         "Jira jql中不能直接含--xxx类似字符",
    #     )
    # with ts.Timer():
    #     for index in range(1, 100):
    #         print(
    #             tstr.exist_in_object_with_similarity(
    #                 "Jira jql中不能直接含--xxx类似字符,会报错,意味着summary中也不能包含--xxx,或者用--xxx包裹起来",
    #                 exist_object,
    #             )
    #         )
