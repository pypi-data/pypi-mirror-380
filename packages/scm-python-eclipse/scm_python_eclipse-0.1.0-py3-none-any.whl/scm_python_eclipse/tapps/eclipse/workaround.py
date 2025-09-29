import yaml
import sys, re, os
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tutils.context_opt as tcontext
import tutils.thpe as thpe
import tutils.ttemplate as ttemplate
import tapps.eclipse.eiumCommon as eclipse_eiumCommon
import tapps.eclipse.eiumType as eclipse_eiumType
import tapps.eclipse.metaFile as eclipse_metaFile

log = tl.log


def do_handler(type: str, recursive=False):
    eclipse_template = java_template = thpe.load_template_yaml("eclipse")
    module_definition = tcontext.load_item(eclipse_template, f"workaroud/{type}")
    if recursive:
        search_file_name = module_definition["search"]
        for classpath in tf.search(".", search_file_name, exact=True):
            workround_hander(os.path.dirname(classpath), module_definition)
    else:
        project_folder = os.path.abspath(".")
        workround_hander(project_folder, module_definition)


def workround_hander(project_folder: str, module_definition):
    go_condition = (
        "exists" in module_definition
        and os.path.exists(os.path.join(project_folder, module_definition["exists"]))
        or "exists" not in module_definition
    )
    if go_condition:
        context = thpe.create_env_context()
        cloned_context = tcontext.deep_merge({}, context)
        ttemplate.handle_template_for_common_scripts(
            project_folder,
            module_definition,
            cloned_context,
            comments=None,
            allow_escape_char=True,
        )
