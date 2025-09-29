from tio.tcli import OptParser, cli_invoker
import tlog.tlogging as tl
import tio.tfile as tf
import tapps.deploy.plan as deploy_plan

flags = [
    (
        "i:",
        "item=",
        "项目内容",
        ["install/plan-item", "install/plan-flag-item", "install/moment-item"],
    ),
]

opp = OptParser(flags)

"""
    启动一个python process来执行检查哪些repo没有提交
    相关配置文件
    sample.yaml:    sh/etc/install.sample.yaml
    runtime.yaml:   ${hostname}/etc/vilink.install.runtime.yaml
"""

log = tl.log


@cli_invoker("install/plan-task-daily")  # generate plan task from jira issue daily
def deploy_plan_task_daily_handler():
    deploy_plan.entrypoint_to_update_plan_jira_task_daily()
    deploy_plan.entrypoint_to_update_plan_jira_task_daily(0)


@cli_invoker(
    "install/plan-item"
)  # create a plan item, today started is 0, yesterday is 1
def deploy_plan_item_handler(item: str, days=1, minutes=5, completed=False, started=0):
    deploy_plan.entrypoint_to_create_plan_item(
        item, int(days), int(minutes), completed=completed, started=int(started)
    )


@cli_invoker(
    "install/plan-flag-item"
)  # flag a plan item, yesterday days is 1, today is 0
def deploy_plan_flag_item_handler(item: str, days=0, minutes=5):
    deploy_plan.entrypoint_to_flag_plan_item(item, int(days), int(minutes))


@cli_invoker("install/moment-daily")  # update memory ebbinghaus item daily
def deploy_moment_daily_handler():
    deploy_plan.update_moment_ebbinghaus_daily()


@cli_invoker("install/moment-item")  # create a memory item
def deploy_moment_item_handler(item: str):
    deploy_plan.entrypoint_to_create_moment_item(item)


@cli_invoker("install/plan-markdown")  # generate plan and memory markdown file by month
def deploy_plan_markdown_handler(month: str = ""):
    tf.USE_LOCAL_FILE_FOR_DOC_TEMPLATE = True
    # deploy_plan.generate_plan_markdown("2025.9", type="memory")
    # deploy_plan.generate_plan_markdown("2025.10", type="memory")
    for type in ("plan", "moment"):
        deploy_plan.generate_plan_markdown(month, type=type)
