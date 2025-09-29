import yaml
import sys, re, os, socket, json
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import calendar
import tutils.ttemplate as ttemplate

from typing import Union
from datetime import date, datetime, timedelta
from pathlib import Path
from tutils.tsyno_server_api import (
    syno_context,
    syno_note_list,
    syno_webapi_list,
    syno_note_latest_list,
    syno_note_notebook_list,
    syno_note_stack_list,
    syno_note_content,
    syno_note_notebook_content,
)
from typing import Literal


log = tl.log

# 判断当前 Python 版本
if sys.version_info >= (3, 10):
    # Python 3.10 及以上版本使用 | 符号
    OptionalDateType = date | None
else:
    # Python 3.9 及以下版本使用 Union
    OptionalDateType = Union[date, None]

notebook_list_file = os.path.join(os.path.expanduser("~"), ".syno_notebook_list.yaml")
notebook_backup_doc_folder = r"C:\usr\ssz\workspace\git\app\syno-notes\docs"


def safe_filename(name: str, max_length=100, replacement="-") -> str:
    """
    将任意字符串转换为安全文件名
    - 去掉不合法字符
    - 限制最大长度
    """
    # 1. 替换非法字符
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1F]', replacement, name)

    # 2. 去掉首尾空格和点（Windows 不允许文件名以点或空格结尾）
    safe = safe.strip(" .")

    # 3. 限制长度（保留扩展名）
    if len(safe) > max_length:
        base, ext = os.path.splitext(safe)
        safe = base[: max_length - len(ext)] + ext

    return safe


def syno_notes_note_to_markdown(context: dict, stack: str):
    notebook_map = tf.yaml_load(notebook_list_file)
    if stack in notebook_map:  # type: ignore
        for notebook in notebook_map[stack]:  # type: ignore
            notebook_title = notebook["title"]
            notebook_folder = os.path.join(
                notebook_backup_doc_folder, stack, notebook_title
            )
            tf.mkdir_if_absent(notebook_folder)
            for note_object_id in notebook["items"]:
                data = syno_note_content(context, note_object_id, dataReturn=True)
                title = data["title"]
                content = data["content"]
                markdown_file = os.path.join(
                    notebook_folder, f"{safe_filename(title)}.md"
                )
                tf.writelines(markdown_file, [content])


SYNO_ENCREPT_FLAG = " - 加密"


def syno_notes_note_to_markdown_one_note(context: dict, note: dict):
    notebook_map: dict = tf.yaml_load(notebook_list_file)
    target_note_object_id = note["object_id"]
    for stack, notebooks in notebook_map.items():  # type: ignore
        for notebook in notebooks:  # type: ignore
            notebook_title = notebook["title"]
            notebook_folder = os.path.join(
                notebook_backup_doc_folder, stack, notebook_title
            )
            for note_object_id in notebook["items"]:
                if note_object_id == target_note_object_id:
                    data = syno_note_content(context, note_object_id, dataReturn=True)
                    title = data["title"]

                    old_title = (
                        title.replace(SYNO_ENCREPT_FLAG, "")
                        if title.endswith(SYNO_ENCREPT_FLAG)
                        else f"{title}{SYNO_ENCREPT_FLAG}"
                    )
                    content = data["content"]
                    markdown_file = os.path.join(
                        notebook_folder, f"{safe_filename(title)}.md"
                    )
                    tf.remove_if_present(
                        os.path.join(notebook_folder, f"{safe_filename(old_title)}.md")
                    )
                    tf.mkdir_if_absent(notebook_folder)
                    tf.writelines(markdown_file, [content])


def syno_notes_notebooks_to_yaml(context: dict):
    notebook_no = 1
    notebook_map = {}
    for syno_note in syno_note_notebook_list(context, limit=1000):
        title = syno_note["title"]
        stack = syno_note["stack"]
        if not stack:
            stack = "未命名书架"
        if not title:
            title = f"未命名笔记本-{notebook_no}"
            notebook_no += 1
        items = syno_note["items"]
        if stack not in notebook_map:
            notebook_map[stack] = []
        notebook_map[stack].append(
            {
                "title": title,
                "items": items,
            }
        )
    tf.yaml_dump(notebook_list_file, notebook_map)


def syno_notes_handle():
    context = syno_context()
    syno_notes_notebooks_to_yaml(context)
    syno_notes_note_to_markdown(context, "运维")


def syno_notes_latest_handle():
    context = syno_context()
    syno_notes_notebooks_to_yaml(context)
    for note in syno_note_latest_list(context, limit=6):
        print("----", note)
        syno_notes_note_to_markdown_one_note(context, note)


def syno_webapi_list_handle():
    context = syno_context()
    for webapi_key, webapi_body in syno_webapi_list(context).items():
        webapi_prefix = f'{webapi_body["path"]}?api={webapi_key}&version={webapi_body["maxVersion"]}'
        print("----", webapi_prefix)
