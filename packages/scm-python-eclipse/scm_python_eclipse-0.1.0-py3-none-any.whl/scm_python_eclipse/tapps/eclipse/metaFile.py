import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log


def eium_classpathentry_plugin(import_plugin: str, test=False):
    path = "test/classes" if test else "classes"
    sourcepath = "test" if test else "src"
    return {
        "TAG": "classpathentry",
        "kind": "var",
        "path": f"IUM_CODE/siu/plugins/{import_plugin}/build/{path}",
        "sourcepath": f"IUM_CODE/siu/plugins/{import_plugin}/{sourcepath}",
    }


def eium_classpathentry_jar(jar_file: str):
    return {"TAG": "classpathentry", "kind": "var", "path": f"{jar_file}"}


def eium_classpathentry_jre():
    return {
        "TAG": "classpathentry",
        "kind": "con",
        "path": "org.eclipse.jdt.launching.JRE_CONTAINER",
    }


def eium_classpathentry_output():
    return {"TAG": "classpathentry", "kind": "output", "path": "build/classes"}


def eclise_start_xml_file():
    return ['<?xml version="1.0" encoding="UTF-8"?>']


def dict_to_line_with_tag(
    tag_name: str,
    line: dict,
    tNum=1,
    close=True,
    excluded_attributes: list[str] = ["scope"],
) -> str:
    tag = line[tag_name]
    text = __tNumToString(tNum) + "<" + tag
    for k, v in line.items():
        if k != tag_name and k not in excluded_attributes:
            text += " " + k + '="' + v + '"'
    return text + (" />" if close else " >")


def __tNumToString(tNum: int) -> str:
    text = ""
    foo = tNum
    while foo > 0:
        foo -= 1
        text += "\t"
    return text


def __isPrimitve(item):
    return item and not (isinstance(item, list) or isinstance(item, dict))


def __noAttrToString(lines, item, tNum=0):
    if not item:
        return
    if isinstance(item, list):
        for list1 in item:
            __noAttrToString(lines, list1, tNum)
    elif isinstance(item, dict):
        for k, v in item.items():
            if __isPrimitve(v):
                lines.append(
                    __tNumToString(tNum) + "<" + k + ">" + str(v) + "</" + k + ">"
                )
            else:
                lines.append(__tNumToString(tNum) + "<" + k + ">")
                __noAttrToString(lines, v, tNum + 1)
                lines.append(__tNumToString(tNum) + "</" + k + ">")


def __updateLine(lines, line_item):
    if not line_item:
        return
    index = 0
    catagoryIndex = -1
    matchIndex = -1
    attrName = line_item[0 : line_item.find("=")]
    catagory = attrName[0 : attrName.find(".", len("org.eclipse.jdt.core") + 1)]
    for line in lines:
        # attr_name_2 = line[0: line_item.find('=')]
        if attrName == (attr_name_2 := line[0 : line_item.find("=")]):
            matchIndex = index
            break
        if attr_name_2.startswith(catagory):
            catagoryIndex = index
        index += 1
    if matchIndex > -1:
        lines.pop(matchIndex)
        lines.insert(matchIndex, line_item)
        return
    if catagoryIndex == -1:
        catagoryIndex = index
    lines.insert(catagoryIndex, line_item)


def __classpathVariable(classpathVariable):
    if not classpathVariable:
        log.error("classpathVariable is not found in buildPath.classpathVariables")
        return
    return (
        "org.eclipse.jdt.core.classpathVariable."
        + classpathVariable["name"]
        + "="
        + __reversePath(classpathVariable["path"])
    )


def __reversePath(path):
    return path[0:1] + "\\" + path[1:]


def __userLibrary(userLibrary):
    if not userLibrary:
        log.error("userLibrary is not found in buildPath.userLibraries")
        return
    target_path = userLibrary["path"]
    if not os.path.exists(target_path):
        log.error(target_path + " is not exists")
        return
    text = (
        "org.eclipse.jdt.core.userLibrary."
        + userLibrary["name"]
        + '=<?xml version\\="1.0" encoding\\="UTF-8"?>\\r\\n<userlibrary systemlibrary\\="false" version\\="2">\\r\\n'
    )
    reversedPath = __reversePath(target_path)
    for filename in os.listdir(target_path):
        if os.path.isfile(target_path + "/" + filename):
            text += (
                '\\t<archive path\\="' + reversedPath + "/" + filename + '" />\\r\\n'
            )
    text += "</userlibrary>\\r\\n"
    return text
