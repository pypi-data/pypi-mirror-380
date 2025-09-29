import tapps.deploy.synology as deploy_syno
from tio.tcli import OptParser, cli_invoker
import tlog.tlogging as tl

flags = [
    ("c", "commit", "automatically commit", ["vilink/check-git-commit"]),
    ("n:", "name=", "message for commit", ["vilink/commit-push"]),
]

opp = OptParser(flags)

log = tl.log


@cli_invoker(
    "install/syno-notes"
)  # generate plan and memory task from jira issue daily
def deploy_syno_notes_handler():
    deploy_syno.syno_notes_handle()


@cli_invoker(
    "install/syno-notes-latest"
)  # generate plan and memory task from jira issue daily
def deploy_syno_notes_latest_handler():
    deploy_syno.syno_notes_latest_handle()


@cli_invoker("install/syno-webapis")  # list avaiable webapis
def deploy_syno_webapi_list_handler():
    deploy_syno.syno_webapi_list_handle()
