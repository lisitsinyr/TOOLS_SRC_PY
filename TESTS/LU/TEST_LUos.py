"""TEST_LUos.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_LUos.py

 =======================================================
"""

import logging
#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
# import logging

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import lyrpy.LULog as LULog
import lyrpy.LUConst as LUConst
from lyrpy.LUDoc import *
import lyrpy.LUos as LUos

def TEST_LUos ():
    """TEST_LUos"""
#beginfunction
    PrintInfoObject('---------TEST_LUos----------')
    PrintInfoObject(TEST_LUos)
    s = 'os.name->',os.name
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = "os.environ['PYTHONPATH']->", os.environ['PYTHONPATH']
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetEnvVar ():
    """TEST_GetEnvVar"""
#beginfunction
    PrintInfoObject('---------TEST_GetEnvVar----------')
    PrintInfoObject(TEST_GetEnvVar)

    s = f'LUos.cHOME={LUos.GetEnvVar (LUos.cHOME)}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = f'LUos.cWINDIR={LUos.GetEnvVar (LUos.cWINDIR)}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_SetEnvVar ():
    """TEST_SetEnvVar"""
#beginfunction
    PrintInfoObject('---------TEST_SetEnvVar----------')
    PrintInfoObject(TEST_SetEnvVar)

    LUos.SetEnvVar(LUos.cTEST,'ValueTEST')
    s = LUos.GetEnvVar (LUos.cTEST)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, f'{LUos.cTEST}={s}')
#endfunction

def TEST_TFolders ():
    """TEST_TFolders"""
#beginfunction
    PrintInfoObject('---------TEST_TFolders----------')
    PrintInfoObject(TEST_TFolders)

    LULog.PrintHandlers (LULog.LoggerAPPS)

    LULog.LoggerAdd (LULog.LoggerAPPS, logging.DEBUG,'LULogger.debug')
    LTFolders = LUos.TFolders()
    s = f'LTFolders.cuDesktop={LTFolders.cuDesktop}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, s)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\LOGS',
                        'TEST_LUos.log',
                        'TEST_LUos_json.log')

    TEST_LUos ()
    TEST_GetEnvVar ()
    TEST_SetEnvVar ()

    if LUos.GOSInfo.system == 'Windows':
        TEST_TFolders ()
    #endif

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule

