import yaml
import sys, re, os, socket
import tempfile
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
from enum import Enum

log = tl.log


class EiumModuleType(Enum):
    Plugins = "plugins"
    Core = "core"


"""
EiumClassPathScope('Runtime')
"""


class EiumClassPathScope(Enum):
    All = "all"
    Design = "design"
    Runtime = "runtime"
