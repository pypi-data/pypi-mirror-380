import tapps.eclipse.eiumWebApp as eclipse_eiumWebApp
import tapps.exercise.lib_webapp as exercise_lib_webapp
import tlog.tlogging as tl
from tio.tcli import *

log = tl.log
flags = []

opp = OptParser(flags)


@cli_invoker(
    "exercise/lib-webapp"
)  # generate eclipse projecct for ops, please sure the current folder is web-console
def exercise_lib_webapp_handler():
    exercise_lib_webapp.exercise_lib_webapp_handler()
