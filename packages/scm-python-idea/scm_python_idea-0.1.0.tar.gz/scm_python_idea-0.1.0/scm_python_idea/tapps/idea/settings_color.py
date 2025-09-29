import yaml
import sys, re, os, socket, copy
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import tutils.ttemplate as ttemplate
import tapps.idea.common as idea_common

log = tl.log


"""
color settings
"""


def idea_settings_color_handler():
    context = thpe.create_env_context()
    idea_root = idea_common.idea_get_config_home()
    ide_template = thpe.load_template_yaml("ide")
    cloned_context = tcontext.deep_merge(context, {})
    ttemplate.handle_template_for_common_scripts(
        os.path.join(idea_root, "colors"),
        tcontext.load_item_support_dot(ide_template, f"idea.setting.colors"),
        cloned_context,
        comments="",
        allow_escape_char=True,
    )
