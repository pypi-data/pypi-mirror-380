import sys, re, os, socket, copy
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.context_opt as tcontext
import tutils.thpe as thpe
import tutils.ttemplate as ttemplate
import tapps.idea.module as idea_module
import tapps.idea.settings_color as idea_settings_color
import tapps.idea.settings_keymaps as idea_settings_keymaps
import tapps.idea.workspace_maven as idea_workspace_maven
from tio.tcli import *

log = tl.log
# use for eclipse helper, for example user library and classpathVariable

# name= means that name follow string parameter
# mandatory is by func with default parameter
flags = [
    (
        "r:",
        "branch=",
        "which branch, sample branch [90/91/92/103/104/105]",
        ["idea", "idea/hello"],
    ),
    ("a:", "alias=", "the project name of idea", ["idea", "idea/hello"]),
    ("m:", "meta=", "relative meta folder", ["idea", "idea/hello"]),
]
opp = OptParser(flags)


@cli_invoker("idea/|hello")  # first extension for eclipse, do some investigation
def eium_hello(branch=None, alias=None, meta=None):
    print("merge list")


"""
    创建module for idea, 每个workspace都要修改
    相关配置文件
    sample.yaml:    sh/etc/ide.template.sample.yaml
    runtime.yaml:   ${hostname}/etc/ide.template.runtime.yaml
"""


@cli_invoker("idea/module")  # generate idea module file
def idea_module_entry(branch=None, alias=None, meta=None):
    project_folder = os.path.abspath(".")
    idea_module.idea_module_handler(project_folder)


"""
    创建color settings for idea, 全局
    相关配置文件
    sample.yaml:    sh/etc/ide.template.sample.yaml
    runtime.yaml:   ${hostname}/etc/ide.template.runtime.yaml
"""


@cli_invoker("idea/settings-color")  # set idea color
def idea_setting_color():
    idea_settings_color.idea_settings_color_handler()


"""
    创建keymaps settings for idea, 全局
    相关配置文件
    sample.yaml:    sh/etc/ide.template.sample.yaml
    runtime.yaml:   ${hostname}/etc/ide.template.runtime.yaml
"""


@cli_invoker("idea/settings-keymaps")  # set idea color
def idea_setting_keymaps():
    idea_settings_keymaps.idea_settings_keymaps_handler()


"""
    创建maven settings for idea, 每个workspace都要修改
    相关配置文件
    sample.yaml:    sh/etc/ide.template.sample.yaml
    runtime.yaml:   ${hostname}/etc/ide.template.runtime.yaml
"""


@cli_invoker("idea/workspace-maven")  # set idea maven in the workspace
def idea_workspace_maven_handler():
    idea_workspace_maven.idea_workspace_maven_handler()
