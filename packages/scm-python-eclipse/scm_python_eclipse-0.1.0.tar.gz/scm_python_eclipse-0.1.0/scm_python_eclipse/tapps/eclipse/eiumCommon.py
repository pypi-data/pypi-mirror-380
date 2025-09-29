import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import tapps.eclipse.eiumType as eclipse_eiumType
import tapps.eclipse.metaFile as eclipse_metaFile

log = tl.log
BUILD_PROPERTIES_FILE = "build.properties"
PLUGIN_PROPERTIES_FILE = "plugin.properties"
BUILD_SHARE_PROPERTIES_FILE = "build-share.properties"
PROJECT_TEST_DEPENDENCIES = "project.test.dependencies"
THE_3RD_DEPENDENCIES = "3rd-party.dependencies"
THE_3RD_TEST_DEPENDENCIES = "3rd-party.test.dependencies"


def eium_class_path_scope(line_item: dict) -> eclipse_eiumType.EiumClassPathScope:
    scope = line_item["scope"] if "scope" in line_item and line_item["scope"] else "all"
    return eclipse_eiumType.EiumClassPathScope(scope)


def is_eium_class_path_runtime_scope(line_item: dict) -> bool:
    scope = eium_class_path_scope(line_item)
    return (
        scope == eclipse_eiumType.EiumClassPathScope.All
        or scope == eclipse_eiumType.EiumClassPathScope.Runtime
    )


def is_eium_class_path_design_scope(line_item: dict) -> bool:
    scope = eium_class_path_scope(line_item)
    return (
        scope == eclipse_eiumType.EiumClassPathScope.All
        or scope == eclipse_eiumType.EiumClassPathScope.Design
    )


def eium_nested_import_plugins(
    abs_folder: str, import_plugins: list, project_dependencies: str
):
    build_properties_file = os.path.join(abs_folder, BUILD_PROPERTIES_FILE)
    build_properties = tf.properties(build_properties_file)
    tmp_import_plugins = []
    tf.merge_properity_array(build_properties, tmp_import_plugins, project_dependencies)
    for import_plugin in tmp_import_plugins:
        if import_plugin.startswith("com.") and import_plugin not in import_plugins:
            eium_nested_import_plugins(
                os.path.join(os.path.dirname(abs_folder), import_plugin),
                import_plugins,
                project_dependencies,
            )
    tf.merge_properity_array(build_properties, import_plugins, project_dependencies)
    # siu\plugins\com.hp.usage.ccf.encapsulator\build.properties
    # nme.impl=\
    #   com.hp.usage.nme.registrar,\
    #   com.hp.usage.array
    #   com.hp.usage.datastruct.nme
    if "com.hp.usage.arraycom.hp.usage.datastruct.nme" in import_plugins:
        import_plugins.remove("com.hp.usage.arraycom.hp.usage.datastruct.nme")
        import_plugins.append("com.hp.usage.array")
        import_plugins.append("com.hp.usage.datastruct.nme")
    if "../core/scripting/engine" in import_plugins:
        import_plugins.remove("../core/scripting/engine")
        import_plugins.append("../core/scripting/api")
    thpe.list_set(import_plugins)


def eium_init_siu_context(
    siu_root,
    root_item,
    branch_item,
    project_name=None,
    project_folder=None,
    build_context=None,
):
    context = {}
    context["THIRDPARTYROOT"] = os.environ.get("THIRDPARTYROOT")
    context["DEVROOT"] = tf.linuxPath(siu_root)
    if build_context:
        context["COMPILE_VERSION"] = build_context[thpe.EIUM_COMPILE_VERSION]
    if project_folder:
        context["PROJECT_ROOT"] = os.path.join(
            siu_root, "siu", "apps", "web", project_folder
        )
        context["PLUGINS_ROOT"] = os.path.join(siu_root, "siu", "plugins")
        context["CORE_ROOT"] = os.path.join(siu_root, "siu", "core")
    if project_name:
        context["PROJECT_NAME"] = project_name
    # 导入全局配置,减少相同的配置
    eclise_item: dict = thpe.load_eclipse_yaml()
    varaiables = {}
    refer_context_str: str = (
        root_item["REFER_CONTEXT"] if "REFER_CONTEXT" in root_item else None
    )
    log.info(f"define refer context in {refer_context_str} by REFER_CONTEXT")
    if refer_context_str:
        varaiables = tcontext.merge_design_runtime(
            varaiables,
            tcontext.load_item(eclise_item, refer_context_str),
            "fromBuildProperties/varaiables",
        )
    varaiables = tcontext.deep_merge(
        varaiables, tcontext.load_item(branch_item, "fromBuildProperties/varaiables")
    )
    if varaiables:
        return tcontext.deep_merge(context, varaiables)
    return context


def eium_lookup_branch(branch, web_app_type="ops"):
    if not branch:
        build_context = thpe.eium_find_branch_build_context()
        branch = build_context[thpe.EIUM_VERSION]
    return thpe.lookup_branch_by_type(
        branch, web_app_type, "siu", thpe.load_eclipse_yaml()
    )


def write_to_file_with_replace(target_file, lines, context):
    # tf.backup(target_file)
    with open(target_file, "w") as fw:
        log.info("save to " + target_file)
        for line in lines:
            line = tcontext.replace_by_context(context, line)
            if isinstance(line, list):
                for sub_line in line:
                    if sub_line.endswith("\n"):
                        fw.write(sub_line)
                    else:
                        fw.write(sub_line + "\n")
                    log.debug(str(line))
            else:
                if line.endswith("\n"):
                    fw.write(line)
                else:
                    fw.write(line + "\n")
                log.debug(line)


def eium_user_libraries_for_3rd_in_eclipse(siu_root, modules=None, branch_item={}):
    third_party_file = os.path.join(siu_root, "siu", "3rd-party.properties")
    props = tf.properties(third_party_file)

    def replace_variable(variable):
        # ${maven:org.apache.poi:poi:3.17:jar}, in 10.0 format
        if variable.startswith("maven:"):
            foo = variable.split(":")
            package = foo[1].replace(".", "/")
            return f"IUM_3RD/.m2/repository/{package}/{foo[2]}/{foo[3]}/{foo[2]}-{foo[3]}.{foo[4]}"
        return props[variable] if variable in props else variable

    for key_item in props.keys():
        replace_count = 0
        while tcontext.has_variable(props[key_item]) and replace_count <= 100:
            replace_count += 1
            props[key_item] = tcontext.replace(replace_variable, props[key_item])
    lines = eclipse_metaFile.eclise_start_xml_file()
    lines.append('<eclipse-userlibraries version="2">')
    third_repo_root = os.environ.get("THIRDPARTYROOT")
    for key_item in props.keys():
        __eclipse_user_libraries_library_item(lines, key_item)
        for jar_file in props[key_item].split(","):
            jar_file = jar_file.strip()
            if jar_file.startswith("IUM_3RD"):
                jar_file = jar_file.replace("IUM_3RD", third_repo_root, 1)
            else:
                jar_file = f"{third_repo_root}/3rdParty/{jar_file}"
            __eclipse_user_libraries_library_archive_item(lines, tf.linuxPath(jar_file))
        lines.append("\t</library>")
    lines.append("</eclipse-userlibraries>")
    target_file = os.path.join(siu_root, "siu", "user-libraries-python.xml")
    write_to_file_with_replace(target_file, lines, {})
    return props


def eium_make_classpath_tag_to_string(line: dict, tNum=1):
    return eclipse_metaFile.dict_to_line_with_tag("TAG", line, tNum)


def eium_prop_item_varaible(jar_file):
    return jar_file.startswith("IUM_") or jar_file.startswith("$")


def eium_prop_item_path(jar_file):
    jar_file = jar_file.strip()
    if not eium_prop_item_varaible(jar_file):
        jar_file = f"IUM_3RD/3rdParty/{jar_file}"
    return jar_file


def __eclipse_user_libraries_library_archive_item(lines, jar_filename):
    dict_items = {}
    dict_items["TAG"] = "archive"
    dict_items["path"] = jar_filename
    lines.append(eclipse_metaFile.dict_to_line_with_tag("TAG", dict_items, 2, True))


def __eclipse_user_libraries_library_item(lines, name):
    dict_items = {}
    dict_items["name"] = name
    dict_items["systemlibrary"] = "false"
    dict_items["TAG"] = "library"
    lines.append(eclipse_metaFile.dict_to_line_with_tag("TAG", dict_items, 1, False))


def eium_is_embed_in_jdk(context: dict, jar_file: str):
    jdk_9_embed_jars = ["xml-apis"]
    java_compile_version = context[thpe.EIUM_COMPILE_VERSION]
    if java_compile_version == "11":
        for embed_jar in jdk_9_embed_jars:
            if embed_jar in jar_file:
                return True
    return False
