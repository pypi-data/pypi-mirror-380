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


def eium_do_classpath(web_app_type, branch, alias, meta, project_folder="web-console"):
    siu_root, ops, branch_item = eclipse_eiumCommon.eium_lookup_branch(
        branch, web_app_type
    )
    build_context = thpe.eium_find_branch_build_context()
    if not alias:
        alias = web_app_type + "-" + build_context[thpe.EIUM_VERSION].replace(".", "")
    if branch_item:
        third_context = eclipse_eiumCommon.eium_user_libraries_for_3rd_in_eclipse(
            siu_root
        )
        context = eclipse_eiumCommon.eium_init_siu_context(
            siu_root, ops, branch_item, alias, project_folder, build_context
        )
        eium_make_classpath_file(third_context, context, branch_item)
        eium_make_user_libraries(context, branch_item, alias)
        eium_make_debug_launch(
            third_context, context, siu_root, ops, branch_item, alias
        )


"""
创建gwt lauch 文件
"""


def eium_make_debug_launch(third_context, context, siu_root, ops, branch_item, alias):
    current_path = context["PROJECT_ROOT"]
    target_file = f"{current_path}/{alias}.launch"
    # launch模板文件路径定义在eclipse.sample.yaml
    launch_params = tcontext.merge_design_runtime(ops, branch_item, "launch/gwtDevMode")
    classpath_value_for_list_entry = launch_params["classpathValueForListEntry"]
    classpath_kind_map = launch_params["classPathKindMap"]
    # classpath_kind_src = classpath_kind_map['src']
    # del classpath_kind_map['src']
    lines = tf.readlines(launch_params["template"], True, False)
    # eium, eium_branch_item = thpe.lookup_branch_by_type(branch_item['name'], 'install/eium')
    project_classpath_lines = []
    context["PROJECT_CLASSPATH"] = project_classpath_lines
    # PROJECT_CLASSPATH
    sorted_line_items = []
    webapp_classpath_entries = eium_get_webapp_classpath_entries(
        third_context, context, branch_item, True
    )
    for line_item in webapp_classpath_entries:
        if line_item["kind"] != "src" and line_item["kind"] in classpath_kind_map:
            sorted_line_items.append(line_item)
    for line_item in webapp_classpath_entries:
        if line_item["kind"] == "src" and not line_item["path"] == "test":
            sorted_line_items.append(line_item)
    THIRDPARTYROOT = context["THIRDPARTYROOT"]
    for line_item in sorted_line_items:
        line_item_kind = line_item["kind"]
        list_entry_attribute_map = classpath_kind_map[line_item_kind]
        list_entry_attribute = list_entry_attribute_map["name"]
        doc_path = line_item["sourcepath"] if "sourcepath" in line_item else None
        code_path = (
            f"/{alias}/{line_item['path']}"
            if "src" == line_item_kind
            else line_item["path"]
        )
        code_path = code_path.replace("${THIRDPARTYROOT}", THIRDPARTYROOT)
        code_source_root_path = "sourceRootPath=&quot;&quot; " if doc_path else ""
        java_project = (
            f"javaProject=&quot;{alias}&quot; "
            if "com.gwtplugins.gwt.eclipse.core.GWT_CONTAINER" == code_path
            else ""
        )
        list_entry_attr_path_value = (
            __eium_make_debug_launch_list_entry_attr_path_value(
                code_path, list_entry_attribute_map
            )
        )
        list_entry_attr_type_value = list_entry_attribute_map["type"]
        list_entry_attr_type = f"type=&quot;{list_entry_attr_type_value}&quot; "
        list_entry_attr_path = f"path=&quot;{list_entry_attr_path_value}&quot; "
        list_entry_value = (
            classpath_value_for_list_entry.replace(
                "${LIST_ENTRY_CODE}",
                __eium_make_debug_launch_list_entry_attribute(
                    list_entry_attribute, code_path
                ),
            )
            .replace(
                "${LIST_ENTRY_DOC}",
                __eium_make_debug_launch_list_entry_attribute(
                    "sourceAttachmentPath", doc_path
                ),
            )
            .replace("${LIST_ENTRY_PATH}", list_entry_attr_path)
            .replace("${LIST_ENTRY_TYPE}", list_entry_attr_type)
            .replace("${LIST_ENTRY_JAVA_PROJECT}", java_project)
            .replace("${LIST_ENTRY_DOC_ROOT_PATH}", code_source_root_path)
        )
        dict_items = {}
        dict_items["value"] = list_entry_value
        dict_items["TAG"] = "listEntry"
        project_classpath_lines.append(
            eclipse_metaFile.dict_to_line_with_tag("TAG", dict_items, 0, True) + "\n"
        )
    # PROJECT_WEB_APP_MODULES
    # project_web_app_modules_lines = []
    # context['PROJECT_WEB_APP_MODULES'] = project_web_app_modules_lines
    # excludings = tcontext.merge_design_runtime(eium, eium_branch_item, 'ops/excludings')
    # web_app_modules = thpe.eium_get_web_app_modules(siu_root, excludings)

    gwt_debug_xml = tcontext.load_item(branch_item, "launch/gwt")
    if not gwt_debug_xml:
        log.warning("no gwt Debug Xml found in launch/gwt " + branch_item["name"])
        gwt_debug_xml = "com.hp.usage.web.ConsoleDebug"
    log.info(f"startup from {gwt_debug_xml}")

    context["PROGRAM_ARGUMENTS"] = (
        tcontext.merge_design_runtime(ops, branch_item, "launch/arguments/program")
        .replace("${DEVROOT}", siu_root)
        .replace('"', "&quot;")
    )
    log.info(f'program with {context["PROGRAM_ARGUMENTS"]}')
    # if 'com.hp.usage.web.ConsoleDebug' in context['PROGRAM_ARGUMENTS']:
    #     log.error(f'invalid PROGRAM_ARGUMENTS')
    context["VM_ARGUMENTS"] = tcontext.merge_design_runtime(
        ops, branch_item, "launch/arguments/vm"
    )
    eclipse_eiumCommon.write_to_file_with_replace(target_file, lines, context)


def eium_make_user_libraries(context: dict, branch_item: dict, alias: str):
    current_path = context["PROJECT_ROOT"]
    for user_lib in tcontext.load_item(branch_item, "buildPath/userLibraries"):
        tcontext.replace_object(context, user_lib)
        user_lib_root = user_lib["path"]
        context[f"{tcontext.CONTEXT_LIST_SCHEMA}{user_lib['name']}"] = user_lib_jars = (
            []
        )
        for filename in os.listdir(user_lib_root):
            jar_filename = tf.linuxPath(user_lib_root + "\\" + filename)
            user_lib_jars.append(jar_filename)
    eium_perference_file(current_path, context)


def eium_make_classpath_file(
    third_context: dict[str, str],
    context: dict[str, str],
    branch_item: dict[str, object],
):
    current_path = context["PROJECT_ROOT"]
    target_file = current_path + "/.classpath"
    lines = eclipse_metaFile.eclise_start_xml_file()
    lines.append("<classpath>")
    # line_item
    """ TAG: classpathentry
        kind: con
        path: org.eclipse.jdt.USER_LIBRARY/CIS_RT
        scope:  runtime
    """
    # prase classpath from build.properties
    for line_item in eium_get_webapp_classpath_entries(
        third_context, context, branch_item
    ):
        if eclipse_eiumCommon.is_eium_class_path_design_scope(line_item):
            lines.append(
                eclipse_eiumCommon.eium_make_classpath_tag_to_string(line_item)
            )

    lines.append("</classpath>")
    eclipse_eiumCommon.write_to_file_with_replace(target_file, lines, context)


def eium_get_webapp_classpath_entries(
    third_context, context, branch_item, include_runtime=False
):
    handled_jars: list[str] = []
    classpath_line_items: list[str] = []
    classpath_entries: list[str] = [] + branch_item["classpath"]
    # define classpath in eclipse.sample.yaml
    if "fromBuildProperties" not in branch_item:
        return classpath_entries
    log.info(
        f"load classpath from build.properties because fromBuildProperties set in eclipse.sample.yaml"
    )
    classpath_entries = [
        line_item
        for line_item in classpath_entries
        if not include_runtime
        or eclipse_eiumCommon.is_eium_class_path_runtime_scope(line_item)
    ]
    first_list = classpath_entries[:]
    con_list = []
    from_build_properties = branch_item["fromBuildProperties"]
    skip_jars = (
        from_build_properties["skipJar"] if "skipJar" in from_build_properties else []
    )
    # container classpath should be put in the list at the end
    for line_item in classpath_entries:
        class_path = line_item["path"]
        filename = os.path.basename(class_path)
        if array_startswith(skip_jars, filename):
            first_list.remove(line_item)
        elif line_item["kind"] in ["output", "con"]:
            first_list.remove(line_item)
            con_list.append(line_item)
    # to scan build.properties to generate the classpath
    for line_item in (
        first_list
        + eium_classpath_defined_in_build_properteis(
            third_context, context, branch_item, skip_jars, include_runtime
        )
        + con_list
    ):
        path = line_item["path"]
        runtime_line_items = []
        # temporary list to put classpath, including repeated classpath
        if path in third_context:
            for path_from_ant in third_context[path].split(","):
                line_item_from_ant = tcontext.deep_merge({}, line_item)
                line_item_from_ant["path"] = (
                    path_from_ant
                    if path_from_ant.startswith("IUM_3RD")
                    else f"IUM_3RD/3rdParty/{path_from_ant}"
                )
                runtime_line_items.append(line_item_from_ant)
        else:
            runtime_line_items.append(line_item)
        for runtime_line_item in runtime_line_items:
            path = runtime_line_item["path"]
            # skip the repeated classpath
            if path not in handled_jars:
                # log.info(f'handle runtime_line {path}')
                handled_jars.append(path)
                classpath_line_items.append(runtime_line_item)
    return classpath_line_items


def eium_classpath_defined_in_build_properteis_load_build_share_properties(
    third_context, current_path
):
    build_share_properties = tf.properties(
        os.path.join(current_path, "..", "build-share.properties")
    )
    tcontext.replace_object(third_context, build_share_properties)
    tcontext.replace_object(build_share_properties, build_share_properties)
    return build_share_properties


def eium_classpath_defined_in_build_properteis_load_build_properties(
    third_context, build_share_properties, current_path
):
    runtime_context = tcontext.deep_merge(third_context, build_share_properties)
    build_properties = tf.properties(os.path.join(current_path, "build.properties"))
    tcontext.replace_object(runtime_context, build_properties)
    tcontext.replace_object(build_properties, build_properties)
    return build_properties


def optional_array_in_properties(build_properties, package_name):
    # build_properties[package_name] = gwt-2.8.2/gwt-user.jar,gwt-2.8.2/gwt-dev.jar,gwt-2.8.2/validation-api-1.0.0.GA.jar,gwt-2.8.2/validation-api-1.0.0.GA-sources.jar
    # ,${library.slf4j.run.1.7.16}
    return (
        build_properties[package_name].split(",")
        if package_name in build_properties
        else []
    )


def array_startswith(skip_jars: list[str], filename: str):
    for jar in skip_jars:
        if filename.startswith(jar):
            return True
    return False


def class_path_entries_for_plugin_from_properties(
    build_properties,
    skip_plugin=[],
    used_plugins=[],
    attributes=["project.dependencies"],
):
    class_path_entries = []
    for attribute_name in attributes:
        for class_path in optional_array_in_properties(
            build_properties, attribute_name
        ):
            if not class_path:
                continue
            filename = os.path.basename(class_path)
            if array_startswith(skip_plugin, filename):
                continue
            # log.info(f'plugin_from_properties {class_path}')
            if class_path.startswith("${plugin.root}") or class_path.startswith(
                "${core.root}"
            ):
                relative_path = class_path.replace(
                    "${plugin.root}", "IUM_CODE/siu/plugins"
                )
                relative_path = relative_path.replace(
                    "${core.root}", "IUM_CODE/siu/core"
                )
                if class_path.startswith("${plugin.root}"):
                    plugin_name = class_path.replace("${plugin.root}/", "")
                    if plugin_name not in skip_plugin:
                        used_plugins.append(plugin_name)
                class_path_entries.append(
                    {
                        "TAG": "classpathentry",
                        "kind": "var",
                        "path": f"{relative_path}/build/classes",
                        "sourcepath": f"{relative_path}/src",
                    }
                )
            # log.info(f'------ {class_path}')
            # the following item is entity for class_path
            # ${plugin.root}, ${core.root} defined in siu\apps\build-share.properties
            # ------ ${plugin.root}/com.hp.usage.opsmodel
            # ------ ${core.root}/security/httpclient
    return class_path_entries


"""
    from build-webapp.xm
    <path refid="project.dependencies.classpath"/>
    <path refid="3rd-party.build.dependencies.path"/>
    <path refid="ext.3rd-party.build.dependencies.path"/>
    <path refid="3rd-party.run.dependencies.path"/>
    <path refid="ext.3rd-party.run.dependencies.path"/>
"""


def class_path_entries_for_jar_from_properties(
    build_properties,
    skip_jars=[],
    attributes=["3rd-party.dependencies", "3rd-party.run.dependencies"],
):
    class_path_entries = []
    for package_name in attributes:
        for class_path in optional_array_in_properties(build_properties, package_name):
            if not class_path:
                continue
            if "gwt-" in class_path or "${" in class_path:
                continue
            filename = os.path.basename(class_path)
            if array_startswith(skip_jars, filename):
                continue
            # log.info(f'------ {class_path}')
            # the following item is entity for class_path
            # IUM_3RD/.m2/repository/org/javassist/javassist/3.24.0-GA/javassist-3.24.0-GA.jar
            # scannotation-1.0.2/scannotation-1.0.2.jar
            class_path_entries.append(
                {
                    "TAG": "classpathentry",
                    "kind": "var",
                    "path": eclipse_eiumCommon.eium_prop_item_path(class_path),
                }
            )
    return class_path_entries


"""
third_context come from 3rd-party.properties
context come from embed properties running in python
"""


def eium_classpath_defined_in_build_properteis(
    third_context, context, branch_item, skip_jars, include_runtime
):
    # current_path=C:\git\integration-10.8.x\siu\apps\web\web-console
    current_path = context["PROJECT_ROOT"]
    plugin_widgets_path = os.path.join(context["PLUGINS_ROOT"], "com.hp.usage.widgets")
    build_share_properties = (
        eium_classpath_defined_in_build_properteis_load_build_share_properties(
            third_context, current_path
        )
    )
    build_properties = eium_classpath_defined_in_build_properteis_load_build_properties(
        third_context, build_share_properties, current_path
    )
    plugin_widgets_build_properties = (
        eium_classpath_defined_in_build_properteis_load_build_properties(
            third_context, {}, plugin_widgets_path
        )
    )
    # com.hp.usage.opsmodel 的build目录下会生成临时java.security,而且是错误的,需要删除它的依赖
    # com.hp.usage.widgets 必须要删除,它已经被加入了src,否则热部署不成功,一直用build/classes里的代码
    skip_plugins = ["com.hp.usage.opsmodel", "com.hp.usage.widgets"]
    # the jars defined in com.hp.usage.widgets are required to append into the classpath
    class_path_entries_for_jar = class_path_entries_for_jar_from_properties(
        plugin_widgets_build_properties, skip_jars, ["3rd-party.dependencies"]
    )
    print("plugin_widgets_build_properties", class_path_entries_for_jar)
    class_path_entries_for_plugin = []
    print("--- skip jar, skip_plugins", skip_jars, skip_plugins)
    # the class path entry order is required, so use two array to ensure it
    used_plugins = []
    for module in optional_array_in_properties(
        build_properties, "web.app.dependencies"
    ):
        module_path = os.path.abspath(os.path.join(current_path, "..", module))
        # dependency module = C:\git\integration-dt-on-10.7.x\siu\apps\web\decisiontable-ui from C:\git\integration-dt-on-10.7.x\siu\apps\web\decisiontable-ui
        log.info(f"dependency module = {module_path} from {module_path}")
        build_properties_1 = (
            eium_classpath_defined_in_build_properteis_load_build_properties(
                third_context, build_share_properties, module_path
            )
        )
        class_path_entries_for_jar += class_path_entries_for_jar_from_properties(
            build_properties_1, skip_jars
        )
        class_path_entries_for_plugin += class_path_entries_for_plugin_from_properties(
            build_properties_1, skip_plugins, used_plugins
        )
    class_path_entries_for_jar += class_path_entries_for_jar_from_properties(
        build_properties, skip_jars
    )
    class_path_entries_for_plugin += class_path_entries_for_plugin_from_properties(
        build_properties, skip_plugins
    )
    if include_runtime:
        print("--- used plugins", list(set(used_plugins)))
        used_plugin_path = os.path.join(
            context["PLUGINS_ROOT"], "com.hp.usage.decisiontable"
        )
        build_properties_1 = (
            eium_classpath_defined_in_build_properteis_load_build_properties(
                third_context, build_share_properties, used_plugin_path
            )
        )
        class_path_entries_for_jar += class_path_entries_for_jar_from_properties(
            build_properties_1, skip_jars
        )
    return class_path_entries_for_plugin + class_path_entries_for_jar


def __eium_make_debug_launch_list_entry_attribute(attribute_name, attribute_value=None):
    return f"{attribute_name}=&quot;{attribute_value}&quot; " if attribute_value else ""


def __eium_make_debug_launch_list_entry_attr_path_value(
    code_path: str, list_entry_attribute_map
):
    if code_path.startswith("org.eclipse.jdt.USER_LIBRARY"):
        return 1
    return list_entry_attribute_map["path"]


def eium_perference_file(plugin_folder: str, context: dict):
    current_path = context["PROJECT_ROOT"]
    project_folder = os.path.basename(current_path)
    cloned_context = tcontext.deep_merge(context, {})
    cloned_context["IUM_LIB"] = "C:/usr/cache/ium-lib"
    cloned_context["THIRDPARTYROOT"] = tf.linuxPath(cloned_context["THIRDPARTYROOT"])
    ttemplate.handle_template_for_common_scripts(
        plugin_folder,
        tcontext.load_item(thpe.load_template_yaml("eclipse"), f"hpe/cms/eium/webapp"),
        cloned_context,
        skip_predicate=lambda file_path: os.path.basename(file_path)
        == "ConsoleDebug.gwt.xml"
        and (
            project_folder == "vnfm-ui"
            or (
                project_folder == "web-console"
                and os.path.exists(os.path.join(plugin_folder, file_path))
            )
        ),
        allow_escape_char=True,
    )
    project_context = tcontext.load_item(
        thpe.load_template_yaml("eclipse"), f"hpe/cms/eium/{project_folder}"
    )
    if project_context:
        ttemplate.handle_template_for_common_scripts(
            plugin_folder,
            project_context,
            cloned_context,
            skip_predicate=False,
            allow_escape_char=True,
        )
    ttemplate.handle_template_for_common_scripts(
        plugin_folder,
        tcontext.load_item(thpe.load_template_yaml("eclipse"), f"hpe/cms/eium/plugins"),
        cloned_context,
    )
