import sys, re, os, socket, unittest
import tlog.tlogging as tl
import tutils.thpe as thpe
import tapps.eclipse.eiumWebApp as eclipse_eiumWebApp

log = tl.log
UT = unittest.TestCase()


def exercise_lib_webapp_handler():
    log.info("exercise_lib_webapp_handler")
    context = {
        "THIRDPARTYROOT": "a",
        "PROJECT_NAME": "b",
        "PROJECT_ROOT": "b",
        "DEVROOT": "b",
        "list::SIU_LIB": ["1", "2"],
        "list::gwt2.8.2patch": ["3", "4"],
    }
    if not thpe.is_linux:
        eclipse_eiumWebApp.eium_perference_file(
            eium_web_project_folder := "C:\\usr\\ssz\\tmp", context
        )
        UT.assertTrue(os.path.exists(os.path.join(eium_web_project_folder, ".project")))
        UT.assertTrue(
            os.path.exists(os.path.join(eium_web_project_folder, "b.userlibraries"))
        )
        UT.assertTrue(
            os.path.exists(
                os.path.join(eium_web_project_folder, "perference_webapp.epf")
            )
        )
