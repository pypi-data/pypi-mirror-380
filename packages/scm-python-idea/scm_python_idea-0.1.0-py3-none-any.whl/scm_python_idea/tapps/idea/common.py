import yaml
import sys, re, os, socket, copy
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import tutils.ttemplate as ttemplate

log = tl.log


"""
there only be varaibles in build_share.propertis, so have no dependencis other files
they are in core/${module_name}, plugins, apps, apps/web
"""


def idea_common_1(siu_root, build_context: dict, module_type):
    print("idea_common_1")


def idea_get_config_home():
    context = thpe.create_env_context()
    jetBrains_root = tcontext.replace_by_context(
        context, "${env:USERPROFILE}\\AppData\\Roaming\\JetBrains"
    )
    return tf.search_dirs(jetBrains_root, f"IntelliJIdea2023*")[0]


"""
首先往上找.idea目录,如果找不到往下找
"""


def idea_get_workspace():
    return os.path.join(os.path.abspath("."), ".idea")
