import yaml
import sys, re, os, socket, json
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import calendar
import tutils.ttemplate as ttemplate
from tutils.tstr import (
    exist_in_object,
    print_similarity_history_data,
    exist_in_object_with_similarity,
    DiffTypeLiteral,
    DIFF_TYPE_SIMILARITY,
    DIFF_TYPE_CONTAIN,
)
from typing import Union
from datetime import date, datetime, timedelta
from pathlib import Path
from tutils.tjira_server_api import jira_search, jira_context
from typing import Literal


log = tl.log

# 判断当前 Python 版本
if sys.version_info >= (3, 10):
    # Python 3.10 及以上版本使用 | 符号
    OptionalDateType = date | None
else:
    # Python 3.9 及以下版本使用 Union
    OptionalDateType = Union[date, None]


def get_weeks_of_month(year: int, month: int):
    # 计算该月的第一天和最后一天
    first_day = date(year, month, 1)
    _, days_in_month = calendar.monthrange(year, month)
    last_day = date(year, month, days_in_month)

    weeks = []
    current = first_day

    # 找到第一个周一
    if current.weekday() != 0:  # weekday: Mon=0, Sun=6
        current -= timedelta(days=current.weekday())

    while current <= last_day:
        week_start = current
        week_end = current + timedelta(days=6)

        # 限制范围在本月
        real_start = max(week_start, first_day)
        real_end = min(week_end, last_day)

        weeks.append((real_start, real_end))
        current += timedelta(days=7)

    return weeks


# 常见艾宾浩斯复习间隔（单位：天）
EBBINGHAUS_INTERVALS = [1, 2, 4, 7, 15, 30]
MOMENT_ITEM_PLACEHOLDER = "占位"


def is_today_in_ebbinghaus_curve(date_str: str, today: OptionalDateType = None) -> bool:
    if today is None:
        today = date.today()

    # 拆分字符串 -> 转为 date 对象
    review_dates = sorted(
        [
            datetime.strptime(d.strip(), "%Y.%m.%d").date()
            for d in date_str.split(",")
            if d.strip()
        ]
    )
    review_dates_len = len(review_dates)
    if review_dates_len == 0:
        return True
    if review_dates_len > len(EBBINGHAUS_INTERVALS):
        return False

    # 取最近一次复习日期
    last_review = review_dates[-1]

    # 遍历艾宾浩斯间隔，计算下一个复习日
    for i, day in enumerate(EBBINGHAUS_INTERVALS):
        # 跳过已复习的日期
        if i < review_dates_len - 1:
            continue
        review_day = last_review + timedelta(days=day)
        if today == review_day:
            return True  # 今天要复习
    next_review_day = last_review + timedelta(
        days=EBBINGHAUS_INTERVALS[review_dates_len - 1]
    )
    return next_review_day < today


def generate_ebbinghaus_days(start: OptionalDateType = None):
    if start is None:
        start = date.today()

    review_dates = [(start + timedelta(days=i)) for i in EBBINGHAUS_INTERVALS]
    return review_dates


def generate_plan_markdown(full_month: str, type: Literal["plan", "moment"] = "plan"):
    if not full_month:
        raise ValueError("full_month is required, format is yyyy.mm")
    if type not in ("plan", "moment"):
        raise ValueError(f"type 只能是 plan 或 moment, 但接收到 {type}")
    year, month = full_month.split(".")
    markdown_project_folder = rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\{type}"
    markdown_template = thpe.load_template_yaml("markdown")
    context = thpe.create_env_context()
    plan_weekly_detail = []
    for week_section in get_weeks_of_month(int(year), int(month)):
        cloned_context = tcontext.deep_merge(context, {})
        real_start, real_end = week_section
        real_start_day = real_start.day
        real_end_day = real_end.day
        cloned_context["DATE_SECTION_ITEM"] = (
            f":octicons-arrow-right-16: {month}.{real_start_day}-{month}.{real_end_day}"
            if real_start_day == 1
            else f"{month}.{real_start_day}-{month}.{real_end_day}"
        )
        date_plan_items = []
        for i in range(real_start_day, real_end_day + 1):
            date_plan_items.append(f'=== "{month}.{i}"')
        cloned_context["list::DATE_PLAN_ITEM"] = date_plan_items
        plan_weekly_detail.append(
            "".join(
                ttemplate.handle_template_for_common_scripts(
                    markdown_project_folder,
                    tcontext.load_item(
                        markdown_template, f"{type}/ssz/template-weekly-detail"
                    ),
                    cloned_context,
                    comments="",
                    allow_escape_char=True,
                    skip_write_file=True,
                )
            )
        )
    cloned_context = tcontext.deep_merge(context, {})
    cloned_context["YEAR"] = year
    cloned_context["MONTH"] = month
    cloned_context["list::PLAN_WEEKLY_DETAIL"] = plan_weekly_detail
    ttemplate.handle_template_for_common_scripts(
        markdown_project_folder,
        tcontext.load_item(markdown_template, f"{type}/ssz/bo"),
        cloned_context,
        comments="",
        allow_escape_char=True,
    )


def get_moment_update_history_data(year: int, month: int):
    history_data = {}

    def update_item(item: str, date_str: str):
        if MOMENT_ITEM_PLACEHOLDER == item:
            return
        if item in history_data:
            if date_str not in history_data[item]:
                history_data[item] = date_str + "," + history_data[item]
        else:
            history_data[item] = date_str

    def parse_markdown_file(current_year, file_path: str):
        if not os.path.exists(file_path):
            return
        text = Path(file_path).read_text(encoding="utf-8")
        print(f"---------parse_markdown_file({file_path})")
        # 匹配 <!-- ... --> 之间的内容
        comments = re.findall(r"<!--(.*?)-->", text, flags=re.DOTALL)
        for comment in comments:
            # 去掉前后空白行和空格
            for line in comment.splitlines():
                line = line.strip()
                if "::" in line:
                    key, value = map(str.strip, line.rsplit("::", 1))
                    if key not in history_data:
                        history_data[key] = value
        content = Path(file_path).read_text(encoding="utf-8").splitlines()
        date_pattern = re.compile(r'^\s*===\+?\s*"(\d{1,2}\.\d{1,2})"\s*$')
        item_pattern = re.compile(r"^\s*-\s+(.+)\s*$")
        date_str = ""
        for line in content:
            if date_pattern_match := date_pattern.match(line):
                date_str = date_pattern_match.group(1)
            elif item_pattern_match := item_pattern.match(line):
                item_str = item_pattern_match.group(1)
                update_item(item_str, f"{current_year}.{date_str}")

    def update_history_data(current_year, current_month, month_num=1):
        if month_num >= 0:
            current_markdown_file = rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\moment\{current_year}.{current_month}.md"
            parse_markdown_file(current_year, current_markdown_file)
            previous_month = current_month - 1 if current_month > 1 else 12
            previous_year = current_year - 1 if previous_month == 12 else current_year
            update_history_data(previous_year, previous_month, month_num - 1)

    update_history_data(year, month, 1)
    return history_data


def update_moment_ebbinghaus_daily(days: Literal[0, 1] = 0):
    if days not in (0, 1):
        raise ValueError(f"days 只能是 0 或 1, 但接收到 {days}")
    time = datetime.now() - timedelta(days=days)
    year = time.year
    month = time.month
    day = time.day
    today = datetime.strptime(f"{year}.{month}.{day}", "%Y.%m.%d").date()
    markdown_file = (
        rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\moment\{year}.{month}.md"
    )
    history_data = get_moment_update_history_data(year, month)
    for item, date_str in history_data.items():
        if is_today_in_ebbinghaus_curve(date_str, today):
            add_moment_to_markdown(markdown_file, item, f"{month}.{day}")

    def overwrite_html_comments(file_path: str):
        path = Path(file_path)
        text = path.read_text(encoding="utf-8")

        # 生成新的注释块
        new_block = "\n".join(f"{k} :: {v}" for k, v in history_data.items())
        new_comment = f"<!--\n{new_block}\n-->"
        if re.search(r"<!--.*?-->", text, flags=re.DOTALL):
            # 用 lambda 返回替换内容，避免 re.sub 解析反斜杠
            new_text = re.sub(
                r"<!--.*?-->", lambda m: new_comment, text, flags=re.DOTALL
            )
        else:
            # 没有注释块 → 直接追加
            new_text = text.rstrip() + "\n\n" + new_comment + "\n"

        path.write_text(new_text, encoding="utf-8")
        print(f"✅ 已更新文件: {file_path}")

    overwrite_html_comments(markdown_file)


def entrypoint_to_flag_plan_item(item: str, days: int, minutes: int):
    print("---entrypoint_to_flag_plan_item", item, days, minutes)
    now = datetime.now() - timedelta(days=days)
    year = now.year
    month = now.month
    day = now.day
    markdown_file = (
        rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\plan\{year}.{month}.md"
    )
    add_task_to_markdown(
        markdown_file,
        item,
        task_status=True,
        task_time_minutes=minutes,
        date=f"{month}.{day}",
        skip_write_file_if_new=True,
        diff_type=DIFF_TYPE_CONTAIN,
    )


def entrypoint_to_create_plan_item(
    item: str, days: int, minutes: int, completed: bool, started: int
):
    print("---entrypoint_to_create_plan_item", item, days, minutes, completed)
    for day_index in range(days):
        now = datetime.now() + timedelta(days=day_index + started)
        year = now.year
        month = now.month
        day = now.day
        markdown_file = (
            rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\plan\{year}.{month}.md"
        )
        add_task_to_markdown(
            markdown_file,
            item,
            task_status=completed,
            task_time_minutes=minutes,
            date=f"{month}.{day}",
        )


def entrypoint_to_create_moment_item(item: str):
    time = datetime.now()
    year = time.year
    month = time.month
    day = time.day
    markdown_file = (
        rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\moment\{year}.{month}.md"
    )
    history_data = get_moment_update_history_data(year, month)
    add_moment_to_markdown(
        markdown_file, item, f"{month}.{day}", history_data=history_data
    )
    print_similarity_history_data()


def entrypoint_to_update_plan_jira_task_daily(days: Literal[0, 1] = 1):
    if days not in (0, 1):
        raise ValueError(f"days 只能是 0 或 1, 但接收到 {days}")
    time_flag = "yesterday" if 1 == days else "today"
    now = datetime.now() - timedelta(days=days)
    year = now.year
    month = now.month
    day = now.day
    markdown_file = (
        rf"C:\usr\ssz\workspace\git\app\draft\docs\ssz\plan\{year}.{month}.md"
    )
    if response_json := jira_search(
        jira_context(SUMMARY="foo", ISSUE_TYPE="Task"),
        f"search-issue-updated-{time_flag}",
    ):
        for issue in response_json["issues"]:
            add_task_to_markdown(
                markdown_file,
                f'{issue["key"]} {issue["fields"]["summary"]}',
                task_status=True,
                date=f"{month}.{day}",
            )


def add_moment_to_markdown(markdown_file, task_name="XXX", date="9.2", history_data={}):
    task_pattern = re.compile(r"-\s+(.*)")

    def match_handler(existing_tasks, line, foo_index):
        match = task_pattern.match(line.strip())
        if match:
            last_task_name_str = match.group(1)
            existing_tasks[last_task_name_str] = foo_index
            # print('---add_moment_to_markdown', last_task_name_str, existing_tasks[last_task_name_str])

    def item_line_handler(existing_tasks):
        merged_existing_task = tcontext.deep_merge(existing_tasks, history_data)
        if exist_in_object_with_similarity(
            task_name,
            merged_existing_task,
            passed_similarity=0.7,
            passed_dist=100,
            enable_similarity_str_len=10,
        ):
            return -2, None
        if MOMENT_ITEM_PLACEHOLDER in existing_tasks:
            return existing_tasks[MOMENT_ITEM_PLACEHOLDER], task_name
        return (
            -1,
            task_name,
        )

    add_item_to_markdown(
        markdown_file, match_handler, item_line_handler, task_name, date
    )


def add_task_to_markdown(
    markdown_file,
    task_name="XXX",
    task_status=False,
    task_time_minutes=5,
    date="9.2",
    diff_type: DiffTypeLiteral = DIFF_TYPE_SIMILARITY,
    skip_write_file_if_new=False,
):
    task_pattern = re.compile(
        r"-\s*(:(?:[a-zA-Z0-9_\-]+):)\s+__(.*?)__\s+(\d+(?:minutes|分钟|分))\s+(.*)"
    )
    print(
        "---add_task_to_markdown diff_type=",
        diff_type,
        "skip_write_file_if_new=",
        skip_write_file_if_new,
    )

    def match_handler(existing_tasks, line, foo_index):
        match = task_pattern.match(line.strip())
        if match:
            flag, status_text, task_time_minutes_str, task_name_str = match.groups()
            existing_tasks[task_name_str] = (
                foo_index,
                flag,
                status_text,
                task_time_minutes_str,
            )
            # print('---add_task_to_markdown match_handler', task_name_str, existing_tasks[task_name_str])

    def item_line_handler(existing_tasks):
        insert_idx = -1
        updated_task_name = task_name
        if exist_task_item := exist_in_object(task_name, existing_tasks, diff_type):
            exist_task_name, exist_task_cache = exist_task_item
            _, _, status_text, _ = exist_task_cache
            updated_task_name = exist_task_name
            print("----item_line_handler", exist_task_cache)
            if (
                task_status
                and status_text == "完成"
                or (not task_status and status_text == "待完成")
            ) and re.match(rf"^{task_time_minutes}(minutes|分钟|分)", exist_task_name):
                return -2, None
            else:
                print(f"任务 '{updated_task_name}'", exist_task_cache)
                insert_idx = exist_task_cache[0]

        # 增量添加任务，如果该日期下没有任务行，则直接插到日期行下面
        task_status_format = (
            ":material-check: __完成__" if task_status else ":x: __待完成__"
        )
        return (
            insert_idx,
            f"{task_status_format} {task_time_minutes}minutes {updated_task_name}",
        )

    add_item_to_markdown(
        markdown_file,
        match_handler,
        item_line_handler,
        task_name,
        date,
        skip_write_file_if_new,
    )


def add_item_to_markdown(
    markdown_file,
    match_handler,
    item_line_handler,
    task_name="XXX",
    date="9.2",
    skip_write_file_if_new=False,
):
    """
    向 Markdown 文件指定日期增量添加任务
    :param markdown_file: Markdown 文件路径
    :param task_name: 任务名称，例如 "5分钟力量锻炼"
    :param date: 增加任务的日期段，例如 "9.1"
    """
    md_path = Path(markdown_file)
    if not md_path.exists() or not md_path.is_file():
        raise FileNotFoundError(f"{markdown_file} 不存在或不是文件")
    skip_write_file = False
    # 读取文件内容
    content = md_path.read_text(encoding="utf-8").splitlines()
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    enable_tab_flag = True if f"{month}.{day}" == date else False
    # 同时匹配 ===+ "9.2" 或 === "9.2"
    # 忽略行首空格，同时匹配 ===+ 或 ===
    date_line_idx = None
    date_sections_line_idx = 1
    for i, line in enumerate(content):
        if re.match(
            r'===\+? ".*?(\d{1,2}\.\d{1,2}(?:-\d{1,2}\.\d{1,2})?-\d{1,2}\.\d{1,2}(?:-\d{1,2}\.\d{1,2})?)"',
            line,
        ):
            date_sections_line_idx = i

        if re.match(rf'^\s*===\+?\s*"{re.escape(date)}"', line):
            if enable_tab_flag:
                content[i] = content[i].replace("=== ", "===+ ")
                content[date_sections_line_idx] = content[
                    date_sections_line_idx
                ].replace("=== ", "===+ ")
            date_line_idx = i
            break
        elif re.match(rf'^\s*===\+\s*"', line):
            if enable_tab_flag:
                content[i] = content[i].replace("===+", "===")

    if date_line_idx is None:
        raise ValueError(f"未找到日期 {date} 的段落")

    # 找到该日期下已有任务行的最后一行
    tasks_start_idx = date_line_idx + 1
    tasks_end_idx = tasks_start_idx
    for i in range(tasks_start_idx, len(content)):
        line = content[i]
        if re.match(r"^\s*===", line):  # 下一个日期段落
            break
        if line.strip().startswith("-"):
            tasks_end_idx = i + 1

    # 收集已有任务内容，避免重复
    existing_tasks = {}
    foo_index = tasks_start_idx
    for line in content[tasks_start_idx:tasks_end_idx]:
        match_handler(existing_tasks, line, foo_index)
        foo_index += 1
    insert_idx, item_line = item_line_handler(existing_tasks)
    if insert_idx == -2:
        print(f"任务 '{task_name}' 已存在，不重复添加")
        return
    new_task_line = f"        - {item_line}"
    if insert_idx == -1:
        insert_idx = (
            tasks_end_idx if tasks_end_idx > tasks_start_idx else tasks_start_idx
        )
        content.insert(insert_idx, new_task_line)
        print(f"新增任务 '{task_name}' 到日期 {date}")
        if skip_write_file_if_new:
            skip_write_file = True
    else:
        content[insert_idx] = new_task_line
        print(f"更新任务 '{new_task_line}' 到日期 {date}")

    # 写回 Markdown
    if skip_write_file:
        print("-----add_item_to_markdown", "跳过写文件")
    else:
        md_path.write_text("\n".join(content), encoding="utf-8")
