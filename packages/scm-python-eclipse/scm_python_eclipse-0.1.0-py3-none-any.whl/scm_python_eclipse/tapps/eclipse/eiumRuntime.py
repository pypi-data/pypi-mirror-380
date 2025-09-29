import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext

log = tl.log


def eium_sync_runtime_dependency(hostname, user, password, cache_lib, overrides=None):
    if not overrides:
        overrides = []
    tf.mkdir_if_absent(f"{cache_lib}/com.hp.usage.jmx")
    remote_siu_root = f"{user}@{hostname}:/opt/SIU_{user}"
    cmds = []
    cmds.append(
        f'{thpe.PREFIX_CALL}sshcli get -r --remote="{remote_siu_root}/lib/*.jar" --local="{cache_lib}" --passwd={password}'
    )
    cmds.append(
        f'{thpe.PREFIX_CALL}sshcli get -r --remote="{remote_siu_root}/plugins/com.hp.usage.jmx_*/*.jar" --local="{cache_lib}/com.hp.usage.jmx" --passwd={password}'
    )
    ts.pipeline(*cmds)
    for override in overrides:
        tf.copy(override["from"], os.path.join(cache_lib, override["to"]))
