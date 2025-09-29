import tlog.tlogging as tl
import requests
import json
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext


log = tl.log


JIRA_SERVER_API_BASE_URL = "https://de.vicp.net:6586/rest/api/2"
JIRA_SERVER_AGILE_API_BASE_URL = "https://de.vicp.net:6586/rest/agile/1.0"
GITLAB_API_EMBED_FILE_EXT_LIST = [".xml", ".yaml", ".json"]
JIRA_SPRINT_CACHE = {}


def jira_server_authorization_header():
    token = tf.dotenv("jira-ssz-person-access-token")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    return headers


def jira_context(**kwargs):
    context = thpe.create_env_context()
    extends_dict = {}
    for key, value in kwargs.items():
        if key.endswith("_LIST") and isinstance(value, list):
            key = f'list::{key.replace("_LIST", "")}'
        extends_dict[key] = value
    return tcontext.deep_merge(context, extends_dict)


def jira_number_data_json_handler(context: dict, origin_data: dict, field_name: str):
    if field_name in origin_data:
        component_str = origin_data[field_name]
        if isinstance(component_str, str):
            print("---jira_number_data_json_handler", component_str)
            origin_data[field_name] = json.loads(component_str)


def jira_number_data_context_variable_value_handler(
    context: dict,
    origin_data: dict,
    field_name: str,
    variable: str,
):
    if field_name in origin_data:
        component_str = origin_data[field_name]
        if isinstance(component_str, str):
            origin_data[field_name] = context[variable]


def jira_number_data_handler(context: dict, data: dict):
    for key, value in data.items():
        if isinstance(value, dict):
            jira_number_data_handler(context=context, data=value)
    origin_data = data
    jira_number_data_context_variable_value_handler(
        context, origin_data, "customfield_10100", "SPRINT"
    )
    jira_number_data_context_variable_value_handler(
        context, origin_data, "customfield_10106", "STORY_POINT"
    )
    jira_number_data_context_variable_value_handler(
        context, origin_data, "customfield_10203", "STORY_POINT"
    )
    jira_number_data_json_handler(context, origin_data, "components")
    jira_number_data_json_handler(context, origin_data, "labels")
    jira_number_data_json_handler(context, origin_data, "fixVersions")


def jira_post(context: dict, jira_template_key: str, api_cmd: str, data_hander=None):
    url = f"{JIRA_SERVER_API_BASE_URL}/{api_cmd}"

    data = thpe.load_yaml_from_install(
        f"vilink/jira-template/{jira_template_key}", "vilink"
    )
    tcontext.replace_object(context, data)
    if data_hander:
        data_hander(context, data)
    print("-----jira_post", api_cmd, data)
    response = requests.post(
        url,
        headers=jira_server_authorization_header(),
        data=json.dumps(data),
        verify=thpe.SSZ_ROOT_CA,
    )  # verify=False 对应 -k
    if response.status_code in (200, 201):
        return response.json()
    else:
        raise Exception(response.text)


def jira_put(
    context: dict, jira_template_key: str, api_cmd: str, data_hander=None
) -> bool:
    url = f"{JIRA_SERVER_API_BASE_URL}/{api_cmd}"

    data = thpe.load_yaml_from_install(
        f"vilink/jira-template/{jira_template_key}", "vilink"
    )
    tcontext.replace_object(context, data)
    if data_hander:
        data_hander(context, data)
    print("-----jira_put", data)
    response = requests.put(
        url,
        headers=jira_server_authorization_header(),
        json=data,
        verify=thpe.SSZ_ROOT_CA,
    )  # verify=False 对应 -k
    if response.status_code in (200, 204):
        return True
    else:
        raise Exception(response.text)


def jira_get(context: dict, jira_template_key: str, api_cmd: str, filed_name: str = ""):
    jira_rest_api_url = (
        JIRA_SERVER_AGILE_API_BASE_URL
        if jira_template_key.startswith("agile_")
        else JIRA_SERVER_API_BASE_URL
    )
    url = f"{jira_rest_api_url}/{api_cmd}"
    log.info(f"{url}")

    # data = thpe.load_yaml_from_install(
    #     f"vilink/jira-template/{jira_template_key}", "vilink"
    # )

    # tcontext.replace_object(context, data)
    response = requests.get(
        url,
        headers=jira_server_authorization_header(),
        verify=thpe.SSZ_ROOT_CA,
    )  # verify=False 对应 -k
    if response.status_code in (200, 201):
        return response.json()[filed_name] if filed_name else response.json()
    else:
        raise Exception(response.text)


def jira_search_escape_jql(context: dict, data):
    if "jql" in data:
        data["jql"] = data["jql"].replace("\n", "")


def jira_search(context: dict, jira_template_key: str):
    return jira_post(
        context, jira_template_key, "search", data_hander=jira_search_escape_jql
    )


def jira_issue(context: dict, jira_template_key: str):
    return jira_post(
        context, jira_template_key, "issue", data_hander=jira_number_data_handler
    )


def jira_issue_comment(context: dict, jira_template_key: str, issue_key: str):
    return jira_post(context, jira_template_key, f"issue/{issue_key}/comment")


def jira_issue_log_time(context: dict, issue_key: str):
    return jira_post(context, "update-issue-log-time", f"issue/{issue_key}/worklog")


def jira_issue_original_estimate(context: dict, jira_template_key: str, issue_key: str):
    return jira_put(context, jira_template_key, f"issue/{issue_key}")


def jira_issue_components(context: dict, jira_template_key: str, issue_key: str):
    return jira_put(
        context,
        jira_template_key,
        f"issue/{issue_key}",
        data_hander=jira_number_data_handler,
    )


def jira_issue_fix_versions(context: dict, jira_template_key: str, issue_key: str):
    return jira_put(
        context,
        jira_template_key,
        f"issue/{issue_key}",
        data_hander=jira_number_data_handler,
    )


def jira_issue_sprint(context: dict, jira_template_key: str, issue_key: str):
    return jira_put(
        context,
        jira_template_key,
        f"issue/{issue_key}",
        data_hander=jira_number_data_handler,
    )


def jira_issue_story_point(context: dict, jira_template_key: str, issue_key: str):
    return jira_put(
        context,
        jira_template_key,
        f"issue/{issue_key}",
        data_hander=jira_number_data_handler,
    )


def jira_board(context: dict):
    return jira_get(context, "agile_board", "board", "values")


def jira_sprint(context: dict, board_id: str):
    return jira_get(context, "agile_sprint", f"board/{board_id}/sprint", "values")


def jira_get_log_time_hour(
    issue_type: str, total_updated_line_number=0, git_repo_name=""
):
    timetracking_elector_dict: dict = thpe.load_yaml_from_install(
        "vilink/jira-template/timetracking-selector",
        "vilink",
        skip_replace=True,
    )  # type: ignore
    update_line_number_per_hour = (
        jira_get_log_time_hour_update_line_number_per_hour_handler(
            timetracking_elector_dict, git_repo_name
        )
    )
    runtime_hour = total_updated_line_number / update_line_number_per_hour
    max_work_load_hour = jira_get_log_time_hour_this_max_work_load_hour_handler(
        timetracking_elector_dict, issue_type, git_repo_name
    )
    # -----jira_post issue/TASKM-42/worklog {'timeSpent': '0.01h'}
    # {"errorMessages":["工作日志无效。"],"errors":{"timeLogged":"无效的工作持续时间。"}}
    # jira中默认单位是分,假设单位为0.02h = 1m, < 0.05都不行
    return max(min(runtime_hour, max_work_load_hour), 0.05)


def jira_get_log_time_hour_this_max_work_load_hour_handler(
    timetracking_elector_dict: dict, issue_type: str, git_repo_name=""
):
    time_spent_dict = timetracking_elector_dict["timeSpent"]
    if git_repo_name not in time_spent_dict:
        git_repo_name = "default"
    time_spent_dict = tcontext.get_field(time_spent_dict, git_repo_name, {})
    return tcontext.get_field(time_spent_dict, issue_type, 1)


def jira_get_labels(git_repo_name="") -> list[str]:
    return jira_get_generic_handler(git_repo_name, "labels-selector")


def jira_get_sprint(git_repo_name="") -> int:
    jira_update_sprint_cache()
    sprint_name = jira_get_generic_handler(git_repo_name, "sprint-selector")
    return JIRA_SPRINT_CACHE[sprint_name]


def jira_update_sprint_cache():
    if not JIRA_SPRINT_CACHE:
        context = jira_context()
        for board in jira_board(context):
            board_id = board["id"]
            board_name = board["name"]
            print("--------", board_name, board_id)
            for sprint in jira_sprint(context, board_id):
                sprint_id = sprint["id"]
                sprint_name = sprint["name"]
                JIRA_SPRINT_CACHE[sprint_name] = sprint_id
                print("\t--------", sprint_name, sprint_id)


def jira_get_fix_versions(git_repo_name="") -> list[str]:
    return jira_get_generic_handler(git_repo_name, "fix-versions-selector")


def jira_get_components(git_repo_name="") -> list[str]:
    return jira_get_generic_handler(git_repo_name, "components-selector")


def jira_get_generic_handler(git_repo_name, selector: str) -> list[str]:
    component_selector_dict: dict = thpe.load_yaml_from_install(
        f"vilink/jira-template/{selector}",
        "vilink",
        skip_replace=True,
    )  # type: ignore
    if git_repo_name not in component_selector_dict:
        git_repo_name = "default"
    component_list: list[str] = tcontext.get_field(
        component_selector_dict, git_repo_name, []
    )
    return component_list


def jira_get_log_time_hour_update_line_number_per_hour_handler(
    timetracking_elector_dict: dict, git_repo_name=""
):
    update_line_number_per_hour_dict = timetracking_elector_dict[
        "updateLineNumberPerHour"
    ]
    if git_repo_name not in update_line_number_per_hour_dict:
        git_repo_name = "default"
    return tcontext.get_field(update_line_number_per_hour_dict, git_repo_name, 20)


def jira_is_cross_repository_summary(summary: str):
    timetracking_elector_list: list[str] = thpe.load_yaml_from_install(
        "vilink/jira-template/cross-repository-issue-summary-selector",
        "vilink",
        skip_replace=True,
    )  # type: ignore
    return summary in timetracking_elector_list


def jira_get_cross_repository_issue_type(parent_issue_type: str):
    return parent_issue_type if parent_issue_type else "Task"


def jira_get_story_point(issue_type: str):
    timetracking_elector_dict: dict = thpe.load_yaml_from_install(
        "vilink/jira-template/timetracking-selector/storyPoint",
        "vilink",
        skip_replace=True,
    )  # type: ignore
    return timetracking_elector_dict[issue_type]


def jira_get_original_estimate(issue_type: str):
    timetracking_elector_dict: dict = thpe.load_yaml_from_install(
        "vilink/jira-template/timetracking-selector/originalEstimate",
        "vilink",
        skip_replace=True,
    )  # type: ignore
    return timetracking_elector_dict[issue_type]


def jira_get_epic_link(git_repo_name: str):
    epic_selector_dict: dict = thpe.load_yaml_from_install(
        "vilink/jira-template/epic-selector", "vilink", skip_replace=True
    )  # type: ignore
    if git_repo_name in epic_selector_dict:
        epic_link = epic_selector_dict[git_repo_name]
    elif "default" in epic_selector_dict:
        epic_link = epic_selector_dict["default"]
    return epic_link
