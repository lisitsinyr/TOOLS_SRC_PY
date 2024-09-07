"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     ScanDir.py

 =======================================================
"""
#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime
import logging
import argparse

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LUConsole
import LUConst
import LUDateTime
import LUDecotators
import LUDict
from LUDoc import *
#import LUDoc
import LUErrors
import LUFile
import LUFileUtils
import LULog
import LUNetwork
import LUNumUtils
import LUObjects
import LUObjectsYT
import LUos
import LUParserARG
import LUParserINI
#import LUParserREG
import LUProc
import LUQThread
import LUQTimer
import LUSheduler
import LUStrDecode
import LUStrUtils
import LUSupport
import LUsys
import LUThread
#import LUTimer
import LUVersion
import LUYouTube

#------------------------------------------
#CONST
#------------------------------------------
GDirSource =''
GDirDest = ''
GMask = ''

#------------------------------------------
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: str):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, ADir.path)
    # Lstat = os.stat(AFile.name)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFile: str, _Older: int):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, AFile.path)
    Lstat = os.stat(AFile)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    ...
#endfunction

#------------------------------------------
# TEST_01 ()
#------------------------------------------
def TEST_01 ():
    """TEST_"""
#beginfunction
    print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    PrintInfoObject('-----TEST_01----')
    PrintInfoObject(TEST_01)

    _OutFile = 'ListDir.txt'
    LUFile.FileDelete (_OutFile)

    LUFileUtils.ScanDir(GDirSource, GDirDest, GMask,
                         True, '',False, None, False, None)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    global GDirSource
    global GDirDest
    global GMask

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

    #----------------------------------------------------------------
    # LPDir = LUParserARG.GetParam ('PDir', "")
    # s = f'Format = {LPDir}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LPDir)
    # LPMask = LUParserARG.GetParam ('PMask', "")
    # s = f'PMask = {LPMask}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, LPMask)
    #----------------------------------------------------------------

    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDirSource', type = str, default='', help = 'PDirSource')
    Lparser.add_argument ('PDirDest', type = str, default='', help = 'PDirDest')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    # Lparser.add_argument ('-PDirSource', type = str, nargs = '?', default = '', dest = 'PDirSource', help = 'PDirSource')
    # Lparser.add_argument ('-PDirDest', type = str, nargs = '?', default = '', dest = 'PDirDest', help = 'PDirDest')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    # Largs = Lparser.parse_args ()
    # GDirSource = Largs.PDirSource
    # GDirDest = Largs.PDirDest
    # GMask = Largs.PMask

    GDirSource = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    GDirDest = 'D:\\WORK\\TESTS_PY'
    GMask = '.*'

    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirSource = {GDirSource}')
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirDest = {GDirDest}')
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')

    TEST_01 ()

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
# ListDir2
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
