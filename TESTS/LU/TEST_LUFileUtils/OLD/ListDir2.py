"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERNS_PY
     Python (PROJECTS_PY)
 Module:
     ListDir2.py

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
GLevel: int = 0
GMask: str = "*.*"
GLog: str = ""
GDir: str = ""
GShablon: str = ""

#------------------------------------------
DirName: str = ""
Shablon: str = ""
Shablon0: str = 'call arjd.bat \"{DirName}\"'
Shablon1: str = "{FullFileDir} {FileName} {FileTime} {FileSize}"
Shablon2: str = "{FileName={FullFileName}|{FullFileDir}|{FileDir}"
#------------------------------------------

#------------------------------------------
Format: int = 0
#------------------------------------------
NLevel = 0
#------------------------------------------

#------------------------------------------
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: str):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, ADir.path)
    Lstat = os.stat(ADir)
    # print('stat_name:',Lstat)
    # Lstat = os.stat(AFile.path)
    # print('stat_path:',Lstat)
    print (GLevel, NLevel)
    if GShablon == Shablon0:
        message = GShablon.format (DirName = ADir)
        print (message)
    #endif
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFile: str):
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

    global GDir
    global GLog
    global GShablon

    GDir = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY'
    # GDir = os.getcwd()
    match Format:
        case 1:
            GLog = 'sfile.ini'
            GShablon = Shablon1
        case 2:
            GLog = 'sfile.ini'
            GShablon = Shablon2
        case _:
            GLog = 'sdir.bat'
            GShablon = Shablon0
    #endmatch
    print ('GDir     = '+GDir)
    print ('GMask    = '+GMask)
    print ('GLog     = '+GLog)
    print ('GShablon = '+GShablon)

    print ('Format  = ',Format)
    print ('NLevel  = ',NLevel)

    _OutFile = 'ListDir2.txt'
    LUFile.FileDelete (_OutFile)

    LUFileUtils.__ListDir (GDir, GMask, '', True, _OutFile, 1, FuncDir, FuncFile)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')
    # LULog.LoggerTOOLS_AddLevel (LULog.TEXT, "Тест")
    # LULog.LoggerTOOLS_AddDebug ("debug")
    # LULog.LoggerTOOLS_AddLevel (logging.DEBUG, "debug")

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    Format = LUParserARG.GetParam ('Format', "")
    s = f'Format = {Format}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, Format)
    NLevel = LUParserARG.GetParam ('NLevel', "")
    s = f'NLevel = {NLevel}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, NLevel)

    # Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    # Lparser.add_argument ('-Format', type = int, nargs = '?', default = -1, dest = 'Format', help = 'Format')
    # Lparser.add_argument ('-NLevel', type = int, nargs = '?', default = -1, dest = 'NLevel', help = 'NLevel')
    # Largs = Lparser.parse_args ()
    # LFormat = Largs.Format
    # s = f'Format = {LFormat}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    # LNLevel = Largs.NLevel
    # s = f'NLevel = {LNLevel}'
    # LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)

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
