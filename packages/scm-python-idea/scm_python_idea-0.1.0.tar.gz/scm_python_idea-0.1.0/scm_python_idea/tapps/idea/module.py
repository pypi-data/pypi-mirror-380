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
there only be varaibles in build_share.propertis, so have no dependencis other files
they are in core/${module_name}, plugins, apps, apps/web
"""


def idea_module_handler(project_folder: str):
    context = thpe.create_env_context()
    ide_template = thpe.load_template_yaml("ide")
    for pom_file in tf.search(project_folder, f"pom.xml", exact=True):
        java_project_folder = os.path.dirname(pom_file)
        expexpected_match_count = (
            2
            if tf.find_context_in_file(pom_file, "<parent>", expected_match_count=1)
            else 1
        )
        project_name = tf.find_context_in_file(
            pom_file,
            "<artifactId>(.+)</artifactId>",
            expected_match_count=expexpected_match_count,
        )
        idea_iml = os.path.join(java_project_folder, f"{project_name}.iml")
        if os.path.exists(idea_iml):
            log.warning(f"{idea_iml} exists, skip it")
        else:
            cloned_context = tcontext.deep_merge(context, {})
            cloned_context["project_name"] = project_name
            ttemplate.handle_template_for_common_scripts(
                java_project_folder,
                tcontext.load_item_support_dot(ide_template, f"idea.setting.module"),
                cloned_context,
                comments="",
                allow_escape_char=True,
            )
