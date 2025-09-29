import yaml
import sys, re, os, socket, copy
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import tutils.ttemplate as ttemplate
import tapps.eclipse.eiumCommon as eclipse_eiumCommon
import tapps.eclipse.metaFile as eclipse_metaFile
import tapps.eclipse.eiumType as eclipse_eiumType

log = tl.log


"""
there only be varaibles in build_share.propertis, so have no dependencis other files
they are in core/${module_name}, plugins, apps, apps/web
"""


def eium_inject_build_share_properties(siu_root, build_context: dict, module_type):
    build_share_properties_file = None
    if eclipse_eiumType.EiumModuleType.Plugins.value == module_type:
        build_share_properties_file = os.path.join(
            siu_root, "siu", "plugins", eclipse_eiumCommon.BUILD_SHARE_PROPERTIES_FILE
        )
        build_context["plugins-share.basedir"] = "IUM_CODE/siu/plugins"
    elif eclipse_eiumType.EiumModuleType.Core.value == module_type:
        build_context["core-share.basedir"] = "IUM_CODE/siu/core"
    if build_share_properties_file:
        prop = tf.properties(build_share_properties_file)
        tcontext.replace_object(build_context, prop)
        tcontext.replace_object(prop, prop)
        build_context.update(prop)


def eium_all_project_abs_folder_by_module_type(siu_root: str, module_type: str):
    modules_root = os.path.join(siu_root, "siu", module_type)
    result_list: list[str] = []
    if eclipse_eiumType.EiumModuleType.Plugins.value == module_type:
        return [
            os.path.join(modules_root, folder) for folder in os.listdir(modules_root)
        ]
    if eclipse_eiumType.EiumModuleType.Core.value == module_type == module_type:
        for folder0 in os.listdir(modules_root):
            core_module_abs_folder = os.path.join(modules_root, folder0)
            if os.path.isdir(core_module_abs_folder):
                result_list += [
                    os.path.join(core_module_abs_folder, folder)
                    for folder in os.listdir(core_module_abs_folder)
                ]
        return result_list
    return result_list


def eium_projects_in_eclipse(
    siu_root: str,
    module_type: str,
    context: dict,
    third_context: dict,
    modules,
    branch_item: dict,
):
    for abs_folder in eium_all_project_abs_folder_by_module_type(siu_root, module_type):
        eium_projects_in_eclipse_for_single_project(
            siu_root, abs_folder, context, third_context, modules, branch_item
        )


"""
generate meta files(.project/.classpath) for single core/plugin project
siu_root=
abs_folder=
context=
third_context=
modules=
branch_item=
"""


def eium_projects_in_eclipse_for_single_project(
    siu_root: str,
    abs_folder: str,
    context: dict,
    third_context: dict,
    modules: dict,
    branch_item: dict,
):
    folder = os.path.basename(abs_folder)
    if _is_eium_build_folder(abs_folder):
        if _is_eium_project(abs_folder):
            context["THIRDPARTYROOT"] = os.environ.get("THIRDPARTYROOT")
            context["PROJECT_NAME"] = folder
            context["PROJECT_MODULE_NAME"] = folder
            context["PROJECT_MODULE_PATH"] = abs_folder.replace(siu_root, "")
            import_plugins = __eium_project_file_in_eclipse(
                context, folder, abs_folder, modules, branch_item
            )
            __eium_classpath_file_in_eclipse(
                context,
                third_context,
                folder,
                abs_folder,
                import_plugins,
                modules,
                branch_item,
            )
            __eium_prefs_file_in_eclipse(
                context, folder, abs_folder, modules, branch_item
            )
        else:
            eium_projects_in_eclipse(
                siu_root, abs_folder, context, third_context, modules, branch_item
            )


def _is_eium_project(abs_folder):
    return (
        os.path.isdir(abs_folder)
        and os.path.exists(os.path.join(abs_folder, "src"))
        and os.path.exists(
            os.path.join(abs_folder, eclipse_eiumCommon.BUILD_PROPERTIES_FILE)
        )
    )


def _is_eium_build_folder(abs_folder):
    return os.path.isdir(abs_folder) and os.path.exists(
        os.path.join(abs_folder, eclipse_eiumCommon.BUILD_PROPERTIES_FILE)
    )


def __eium_prefs_file_in_eclipse(context, folder, abs_folder, modules, branch_item):
    log.info("to finish work on the prefs file in ./settings")
    cloned_context = tcontext.deep_merge(context, {})
    ttemplate.handle_template_for_common_scripts(
        abs_folder,
        tcontext.load_item(thpe.load_template_yaml("eclipse"), f"hpe/cms/eium/plugins"),
        cloned_context,
    )


def __eium_project_file_in_eclipse(
    context: dict, module_name: str, abs_folder: str, modules: dict, branch_item: dict
):
    target_file = os.path.join(abs_folder, ".project")
    module_item = copy.deepcopy(modules)
    # 3rd-party.dependencies=, all 3rd-party dependencies
    # 3rd-party.misc.dependencies, all core dependencies
    # build_properties_file = os.path.join(abs_folder,'build.properties')
    # imports=, all plugin dependencies
    plugins_properties_file = os.path.join(
        abs_folder, eclipse_eiumCommon.PLUGIN_PROPERTIES_FILE
    )  # ium 10.x
    plugins_xml_file = os.path.join(abs_folder, "plugin.xml.template")  # ium 9.x
    plugins_properties = {}
    import_plugins = []
    if os.path.exists(plugins_properties_file):
        plugins_properties = tf.properties(plugins_properties_file)
        if "imports" in plugins_properties and plugins_properties["imports"]:
            import_plugins = plugins_properties["imports"].split(",")
            # for plugin_name in import_plugins:
            #     link_item = { 'link': {
            #         'name': 'classes',
            #         'type': 2,
            #         'locationURI': f'IUM_ROOT/siu/plugins/{plugin_name}/src'
            #     }}
            #     linked_resources.append(link_item)
    elif os.path.exists(plugins_xml_file):
        ns = {"ium": "http://ov.hp.com/ium/namespace/plugin"}
        import_plugins = [
            plugin["plugin"]
            for plugin in tf.xml_attribs(
                plugins_xml_file, "ium:requires/ium:import", ns
            )
        ]

    linked_resources = tcontext.load_item(
        module_item, "project/projectDescription/linkedResources"
    )
    lines = eclipse_metaFile.eclise_start_xml_file()
    eclipse_metaFile.__noAttrToString(lines, module_item["project"])
    eclipse_eiumCommon.write_to_file_with_replace(target_file, lines, context)
    return list(set(import_plugins))


def __eium_classpath_file_in_eclipse(
    context: dict,
    third_context: dict,
    module_name: str,
    abs_folder: str,
    import_plugins: list[str],
    modules: dict,
    branch_item: dict,
):
    target_file = os.path.join(abs_folder, ".classpath")
    module_item = copy.deepcopy(modules)
    lines = eclipse_metaFile.eclise_start_xml_file()
    lines.append("<classpath>")
    build_properties_file = os.path.join(
        abs_folder, eclipse_eiumCommon.BUILD_PROPERTIES_FILE
    )
    build_properties = tf.properties(build_properties_file)
    classpath_list: list = tcontext.load_item(module_item, "classpath")
    import_test_plugins = []
    eclipse_eiumCommon.eium_nested_import_plugins(
        abs_folder, import_test_plugins, eclipse_eiumCommon.PROJECT_TEST_DEPENDENCIES
    )
    import_plugins = thpe.list_trims(import_plugins)
    for import_plugin in import_plugins:
        classpath_list.append(
            eclipse_metaFile.eium_classpathentry_plugin(import_plugin)
        )
        classpath_list.append(
            eclipse_metaFile.eium_classpathentry_plugin(import_plugin, True)
        )
    for import_plugin in [
        import_plugin0
        for import_plugin0 in import_test_plugins
        if import_plugin0 not in import_plugins
    ]:
        classpath_list.append(
            eclipse_metaFile.eium_classpathentry_plugin(import_plugin)
        )
        classpath_list.append(
            eclipse_metaFile.eium_classpathentry_plugin(import_plugin, True)
        )
    libraries = []
    tf.merge_properity_array(
        build_properties, libraries, eclipse_eiumCommon.THE_3RD_DEPENDENCIES
    )
    tf.merge_properity_array(
        build_properties, libraries, eclipse_eiumCommon.THE_3RD_TEST_DEPENDENCIES
    )
    handled_jars = []
    for library_name in libraries:
        for jar_file in tcontext.replace_by_context(third_context, library_name).split(
            ","
        ):
            jar_file = eclipse_eiumCommon.eium_prop_item_path(jar_file)
            if eclipse_eiumCommon.eium_is_embed_in_jdk(context, jar_file):
                continue
            if jar_file in handled_jars:
                continue
            handled_jars.append(jar_file)
            classpath_list.append(eclipse_metaFile.eium_classpathentry_jar(jar_file))

    classpath_list.append(eclipse_metaFile.eium_classpathentry_jre())
    classpath_list.append(eclipse_metaFile.eium_classpathentry_output())
    for line_item in classpath_list:
        if eclipse_eiumCommon.is_eium_class_path_design_scope(line_item):
            lines.append(
                eclipse_eiumCommon.eium_make_classpath_tag_to_string(line_item)
            )
    lines.append("</classpath>")
    eclipse_eiumCommon.write_to_file_with_replace(target_file, lines, context)
