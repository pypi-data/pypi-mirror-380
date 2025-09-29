import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log


def eium_do_config_with_external_server(
    siu_root, siu_install_root, ops, branch_item, hostname, user, password
):
    log.info(f"eium_do_config_with_external_server {siu_root}")
    if siu_install_root:
        siu_install_root = f"D:\SIU_{siu_install_root}"
    else:
        vm_arugments = tcontext.load_item(branch_item, "launch/arguments/vm")
        # -DSIUINI=d:\SIU_snap106\SIU.ini
        siu_ini_item = "SIUINI"
        siu_ini_start_index = vm_arugments.find("-D" + siu_ini_item + "=")
        vm_arguments_right_part = vm_arugments[
            siu_ini_start_index + len(siu_ini_item) + 3 :
        ]
        siu_ini_flag = "/SIU.ini" if thpe.is_linux else "\SIU.ini"
        siu_install_root = vm_arguments_right_part[
            0 : vm_arguments_right_part.find(siu_ini_flag)
        ]
    ip = socket.getaddrinfo(hostname, None)[0][4][0]
    log.info(f"put siu into {siu_install_root}")
    if not os.path.exists(os.path.join(siu_install_root, "SIU.ini")):
        print(siu_install_root)
        log.info("TODO: create external environment")
        eium_config_with_external_server_new(
            siu_install_root, hostname, ip, user, password
        )
    if branch_item["name"].startswith("9.0"):
        __eium_do_config_with_external_server_corba(
            siu_install_root, hostname, ip, user, password
        )
    else:
        __eium_do_config_with_external_server_http(siu_install_root, hostname, ip)


def eium_config_with_external_server_new(
    siu_install_root, hostname, ip, user, password
):
    tf.mkdir_if_absent(siu_install_root)
    tf.mkdir_if_absent(os.path.join(siu_install_root, "plugins"))
    tf.mkdir_if_absent(os.path.join(siu_install_root, "var", "cache"))
    remote_siu_root = f"{user}@{hostname}:/opt/SIU_{user}"
    remote_siu_root_etc = f"{user}@{hostname}:/etc/opt/SIU_{user}"
    remote_siu_root_var = f"{user}@{hostname}:/var/opt/SIU_{user}"
    prefix_call = "" if thpe.is_linux else "call "
    cmds = ["source /etc/profile"] if thpe.is_linux else []
    # lib目录貌似也不需要同步,只要SIU.ini文件
    # cmds.append(f'{prefix_call}sshcli get -r --remote="{remote_siu_root}/lib" --local="{siu_install_root}" --passwd={password}')
    # 如果加上这句会导致classpath检查, 以至于所有的plugins都要存在
    # cmds.append(f'call sshcli get -r --remote="{remote_siu_root}/plugins/com.hp.usage.jmx_*/" --local="{siu_install_root}\\plugins" --passwd={password}')
    cmds.append(
        f'{prefix_call}sshcli get --remote="{remote_siu_root_etc}/SIU.ini" --local="{siu_install_root}" --passwd={password}'
    )
    cmds.append(
        f'{prefix_call}sshcli get --remote="{remote_siu_root_var}/ConfigServer.ior" --local="{siu_install_root}/var" --passwd={password}'
    )
    cmds.append(
        f'{prefix_call}sshcli get --remote="{remote_siu_root_var}/cache/csaddress.txt" --local="{siu_install_root}/var/cache" --passwd={password}'
    )
    cmds.append(
        f'{prefix_call}sshcli get --remote="{remote_siu_root_var}/cache/PluginRegistry.cache" --local="{siu_install_root}/var/cache" --passwd={password}'
    )
    ts.pipeline(*cmds)
    if thpe.is_linux:
        # siu_home = siu_install_root[siu_install_root.find('/') + 1:]
        _siu_root = siu_install_root
        siu_root = f"{siu_install_root}/"
        siu_var = f"{siu_root}var/"
        siu_ini_file = f"{siu_root}SIU.ini"
        ior_file = f"{siu_var}ConfigServer.ior"
    else:
        # siu_home = siu_install_root[siu_install_root.find('\\') + 1:]
        siu_install_root = tf.linuxPath(siu_install_root)
        _siu_root = siu_install_root
        siu_root = f"{siu_install_root}/"
        siu_var = f"{siu_root}var/"
        siu_ini_file = f"{siu_install_root}/SIU.ini"
        ior_file = f"{siu_var}ConfigServer.ior"

    def __replace_path(item):
        if item.startswith("IORURL"):
            return f"IORURL=file\:{ior_file}\n"
        elif item.startswith("BINROOT"):
            return "BINROOT=" + _siu_root + "\n"
        elif item.startswith("DATAFILE"):
            return "DATAFILE=" + siu_var + "config.db\n"
        elif item.startswith("VARROOT"):
            return "VARROOT=" + siu_var + "\n"
        elif item.startswith("CFGROOT"):
            return "CFGROOT=" + siu_var + "\n"
        elif item.startswith("IORFILE"):
            return "IORFILE=" + siu_var + "ConfigServer.ior\n"
        elif item.startswith("SIUJAVAINI"):
            return "SIUJAVAINI=" + siu_root + "SIUJava.ini\n"
        elif item.startswith("LICENSEFILE"):
            return "LICENSEFILE=" + siu_root + "license.config\n"
        return item

    with open(siu_ini_file, "r") as f1:
        list1 = f1.readlines()
    list2 = map(__replace_path, list1)
    with open(siu_ini_file, "w") as f1:
        f1.writelines(list2)
    log.info("complete new server")


def __eium_do_config_with_external_server_corba(
    siu_install_root, hostname, ip, user, password
):
    tf.replace(
        os.path.join(siu_install_root, "SIU.ini"), "HOSTID=.+", f"HOSTID={hostname}"
    )
    tf.replace(
        os.path.join(siu_install_root, "var", "cache", "csaddress.txt"),
        ".+",
        f"{ip},8300,8158,{hostname}",
    )
    cmds = [
        f'sshcli get --remote="{user}@{hostname}:/var/opt/SIU_{user}/ConfigServer.ior" --local="{siu_install_root}/var" --passwd={password}'
    ]
    ts.pipeline(*cmds)


def __eium_do_config_with_external_server_http(siu_install_root, hostname, ip):
    siu_init_file = os.path.join(siu_install_root, "SIU.ini")
    tf.replace(siu_init_file, "HOSTID=.+", f"HOSTID={hostname}")
    tf.replace(siu_init_file, "CSURL=", f"CSURL=rpc://{ip}:8158")
