import sys, re, os, socket, copy
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.context_opt as tcontext
import tutils.thpe as thpe
import tutils.ttemplate as ttemplate
import tapps.eclipse.eiumExternalServer as eclipse_eiumExternalServer
import tapps.eclipse.eiumWebApp as eclipse_eiumWebApp
import tapps.eclipse.eiumRuntime as eclipse_eiumRuntime
import tapps.eclipse.eiumIde as eclipse_eiumIde
import tapps.eclipse.eiumCommon as eclipse_eiumCommon
import tapps.eclipse.workaround as eclipse_workaround

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
        [
            "eclipse",
            "eclipse/hello",
            "eclipse/ops",
            "eclipse/cis",
            "eclipse/opsdebug",
            "eclipse/externalium",
            "eclipse/ei",
            "eclipse/ide.eclipse",
            "eclipse/runtime",
            "eclipse/ri",
        ],
    ),
    (
        "a:",
        "alias=",
        "the project name of eclipse",
        ["eclipse", "eclipse/hello", "eclipse/ops", "eclipse/cis", "eclipse/cis1"],
    ),
    (
        "m:",
        "meta=",
        "relative meta folder",
        ["eclipse", "eclipse/hello", "eclipse/ops", "eclipse/cis"],
    ),
    (
        "d",
        "debug",
        "copy debug to product, or checkout --",
        "eclipse/opsdebug",
        "eclipse/license-portal-debug",
    ),
    (
        "i:",
        ["install_root=", "install-root=", "siu-install-root="],
        "local siu install home",
        "eclipse/externalium",
        "eclipse/ei",
    ),
    (
        "t:",
        ["app_type=", "app-type=", "web-app-type="],
        "app type,[ops,cis]",
        "eclipse/ei",
    ),
    (
        "t:",
        ["type=", "workaround-type="],
        "workaround type,[notest/junit]",
        "eclipse/workaround",
    ),
    ("r", "recursive", "Recursively workaround", "eclipse/workaround"),
    (
        "n:",
        "hostname=",
        "ssh hostname, default is eium-5888.ssz.hpqcorp.net",
        "eclipse/externalium",
        "eclipse/ei",
        "eclipse/runtime",
        "eclipse/ri",
    ),
    (
        "u:",
        "user=",
        "ssh user, default is snap[snap,snap90,snap90rogers,snap91,snap91ngr,snap92,snap105,snap106,snap107]",
        "eclipse/externalium",
        "eclipse/ei",
        "eclipse/runtime",
        "eclipse/ri",
    ),
    (
        "p:",
        "password=",
        "ssh password, default is snap",
        "eclipse/externalium",
        "eclipse/ei",
        "eclipse/runtime",
        "eclipse/ri",
    ),
    (
        "m:",
        ["module_type=", "module-type=", "module="],
        "module type, enum core or plugins",
        "eclipse/ide.eclipse",
    ),
    (
        "s",
        ["single_project", "single-project", "single"],
        "single project",
        "eclipse/ide.eclipse",
    ),
]

opp = OptParser(flags)


@cli_invoker("eclipse/|hello")  # first extension for eclipse, do some investigation
def eium_hello(branch=None, alias=None, meta=None):
    build_context = {}
    if not branch:
        build_context = thpe.eium_find_branch_build_context()
        branch = build_context[thpe.EIUM_VERSION]
    siu_root, modules, branch_item = eclipse_eiumCommon.eium_lookup_branch(
        branch, "module"
    )
    build_context["DEVROOT"] = tf.linuxPath(siu_root)
    third_context = eclipse_eiumCommon.eium_user_libraries_for_3rd_in_eclipse(siu_root)
    print(
        "hell third_context[library.jersey]",
        "library.hibernate-validator" in third_context,
        third_context["library.jersey"],
    )
    aaa = [1]
    bbb = [2]
    aaa += bbb
    print("merge list", aaa)


"""
    创建ops console Dev Meta info for eclipse
    相关配置文件
    sample.yaml:    sh/etc/eclipse.sample.yaml
    runtime.yaml:   ${hostname}/etc/eclipse.runtime.yaml
"""


@cli_invoker(
    "eclipse/ops"
)  # generate eclipse projecct for ops, please sure the current folder is web-console
def eium_classpath_for_ops(branch=None, alias=None, meta=None):
    eclipse_eiumWebApp.eium_do_classpath("ops", branch, alias, meta, "web-console")


@cli_invoker(
    "eclipse/cis"
)  # generate eclipse projecct for cis, please sure the current folder is vnfm-ui
def eium_classpath_for_cis(branch=None, alias=None, meta=False):
    eclipse_eiumWebApp.eium_do_classpath("cis", branch, alias, meta, "vnfm-ui")


@cli_invoker(
    "eclipse/ide.eclipse"
)  # generate eclipse projecct for plugins or core, please sure the current folder is web-console
def eium_core_or_plugin_meta_files(
    branch=None, module_type="plugins", single_project=False
):
    build_context = {}
    if not branch:
        build_context = thpe.eium_find_branch_build_context()
        branch = build_context[thpe.EIUM_VERSION]
    siu_root, modules, branch_item = eclipse_eiumCommon.eium_lookup_branch(
        branch, "module"
    )
    build_context["DEVROOT"] = tf.linuxPath(siu_root)
    eclipse_eiumIde.eium_inject_build_share_properties(
        siu_root, build_context, module_type
    )
    third_context = eclipse_eiumCommon.eium_user_libraries_for_3rd_in_eclipse(
        siu_root, modules, branch_item
    )
    if single_project:
        eclipse_eiumIde.eium_projects_in_eclipse_for_single_project(
            siu_root,
            os.path.abspath("."),
            build_context,
            third_context,
            modules,
            branch_item,
        )
    else:
        eclipse_eiumIde.eium_projects_in_eclipse(
            siu_root, module_type, build_context, third_context, modules, branch_item
        )


@cli_invoker(
    "eclipse/opsdebug"
)  # use compatible gwt file to replace product, or checkout
def debug_rdm(branch=None, debug=False):
    siu_root, ops, branch_item = eclipse_eiumCommon.eium_lookup_branch(branch, "ops")
    if branch_item:
        if debug:
            for target in tcontext.merge_design_runtime(ops, branch_item, "debug"):
                target_path = target["target"]
                for from_file in target["froms"]:
                    tf.copy(from_file, siu_root + "\\" + target_path)
        else:
            cmds = ["cd " + siu_root]
            for target in tcontext.merge_design_runtime(ops, branch_item, "debug"):
                target_path = tf.linuxPath(target["target"])
                for from_file in target["froms"]:
                    [dirname, filename] = os.path.split(from_file)
                    cmds.append("git checkout -- " + target_path + "/" + filename)
            ts.pipeline(*cmds)


@cli_invoker(
    "eclipse/license-portal-debug"
)  # use compatible gwt file to replace product, or checkout
def debug_license_portal(debug=False):
    branch_item = thpe.lookup_project_in_eclipse("license")
    if branch_item:
        if debug:
            for target in tcontext.load_item(branch_item, "debug"):
                target_path = target["target"]
                for from_file in target["froms"]:
                    [dirname, filename] = os.path.split(from_file)
                    dirname = os.path.basename(dirname)
                    abs_target_path = os.path.join(target_path, dirname)
                    tf.copy(from_file, abs_target_path)
        else:
            for target in tcontext.load_item(branch_item, "debug"):
                target_path = tf.linuxPath(target["target"])
                cmds = ["cd " + target_path]
                for from_file in target["froms"]:
                    [dirname, filename] = os.path.split(from_file)
                    dirname = os.path.basename(dirname)
                    cmds.append(f"git checkout -- {target_path}/{dirname}/{filename}")
            ts.pipeline(*cmds)


"""
    从远程服务器下载相关的配置信息到c:/delegates, 主要是SIU.ini
    相关配置文件
    sample.yaml:    sh/etc/eclipse.sample.yaml
    runtime.yaml:   ${hostname}/etc/eclipse.runtime.yaml
"""


@cli_invoker(
    "eclipse/externalium|ei"
)  # change config in D disk to connect to external IUM, support EIUM 9.0+
def eium_config_with_external_server(
    branch=None,
    install_root=None,
    hostname="eium-5888.ssz.hpqcorp.net",
    user="snap",
    password=None,
    app_type="ops",
):
    log.info(f"app_type is {app_type}")
    if not password:
        password = user
    siu_root, ops, branch_item = eclipse_eiumCommon.eium_lookup_branch(branch, app_type)
    eclipse_eiumExternalServer.eium_do_config_with_external_server(
        siu_root, install_root, ops, branch_item, hostname, user, password
    )


"""
    从远程服务器下载相关的配置信息到c:/usr/cache/ium-lib, 主要是LIB目录下的jar
    相关配置文件
    sample.yaml:    sh/etc/eclipse.sample.yaml
    runtime.yaml:   ${hostname}/etc/eclipse.runtime.yaml
"""


@cli_invoker(
    "eclipse/runtime|ri"
)  # sync runtime SIU_LIB from remote ium server, support EIUM 9.0+
def eium_sync_runtime_dependency_entry(
    branch=None, hostname="eium-5888.ssz.hpqcorp.net", user="snap", password=None
):
    if not password:
        password = user
    siu_root, ops, branch_item = eclipse_eiumCommon.eium_lookup_branch(branch)
    overrides = tcontext.load_item(branch_item, "buildPath/override_SIU_LIB")
    context = eclipse_eiumCommon.eium_init_siu_context(siu_root, ops, branch_item)
    for user_lib in tcontext.load_item(branch_item, "buildPath/userLibraries"):
        tcontext.replace_object(context, user_lib)
        if "SIU_LIB" == user_lib["name"]:
            eclipse_eiumRuntime.eium_sync_runtime_dependency(
                hostname, user, password, user_lib["path"], overrides
            )


@cli_invoker("eclipse/test")  # eclipse test
def eium_test():
    log.info("do test for eclipse module")


"""
    创建ops console Dev Meta info for eclipse
    相关配置文件
    sample.yaml:    sh/etc/eclipse.template.sample.yaml
    runtime.yaml:   ${hostname}/etc/eclipse.template.runtime.yaml
"""


@cli_invoker(
    "eclipse/workaround"
)  # generate eclipse projecct for ops, please sure the current folder is web-console
def eium_workaround(type="notest", recursive=False):
    eclipse_workaround.do_handler(type, recursive)
