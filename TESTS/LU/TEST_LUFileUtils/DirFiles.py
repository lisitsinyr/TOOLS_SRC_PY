"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     DirFiles.py

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
import stat
import platform

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКИ lyrpy.LU
#------------------------------------------
# import lyrpy.LUConsole
# import lyrpy.LUConst
# import lyrpy.LUDateTime
# import lyrpy.LUDecotators
# import lyrpy.LUDict
# import lyrpy.LUErrors
import lyrpy.LUFile as LUFile
import lyrpy.LUFileUtils as LUFileUtils
import lyrpy.LUDoc as LUDoc
import lyrpy.LULog as LULog
# import lyrpy.LUObjects
# import lyrpy.LUObjectsYT
# import lyrpy.LUos
import lyrpy.LUParserARG as LUParserARG
# import lyrpy.LUParserINI
# import lyrpy.LUProc
# import lyrpy.LUQThread
# import lyrpy.LUQTimer
# import lyrpy.LUSheduler
# import lyrpy.LUStrDecode
# import lyrpy.LUStrUtils
# import lyrpy.LUSupport
# import lyrpy.LUsys
# import lyrpy.LUThread
# import lyrpy.LUYouTube

if platform.system() == 'Windows':
    import lyrpy.LUNetwork as LUNetwork
    import lyrpy.LUNumUtils as LUNumUtils
    import lyrpy.LUTimer as LUTimer
    import lyrpy.LUVersion as LUVersion
    import lyrpy.LUParserREG as LUParserREG
#endif

#------------------------------------------
#CONST
#------------------------------------------

#------------------------------------------
# FuncDir ()
#------------------------------------------
def FuncDir (ADir: str, APathDest: str):
    """FuncDir"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    Lstat = os.stat(ADir)
    LAttr = (LUFile.GetFileAttr (ADir))
    LDirSize = LUFile.GetDirectoryTreeSize (ADir)
    LDirDateTime = LUFile.GetDirDateTime (ADir)
    s = f'{LDirDateTime[2]:%d.%m.%Y  %H:%M} {LDirDateTime[3]:%d.%m.%Y  %H:%M} {LDirSize:d}'
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, s)
#endfunction

#------------------------------------------
# FuncFile ()
#------------------------------------------
def FuncFile (AFileName: str, APathDest: str):
    """FuncFile"""
#beginfunction
    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    Lstat = os.stat(AFileName)
    LAttr = LUFile.GetFileAttr(AFileName)
    # Lflags = stat.FILE_ATTRIBUTE_SYSTEM | stat.FILE_ATTRIBUTE_HIDDEN | stat.FILE_ATTRIBUTE_READONLY
    # lyrpy.LUFile.SetFileAttr (AFileName, Lflags, True)

    LPureWindowsPath = LUFile.GetPureWindowsPath (AFileName)
    LPureWindowsPath = LUFile.GetPureWindowsPath ('TEST_LUFileUtils\\')
    # print ('LPureWindowsPath:', LPureWindowsPath)
    LWindowsPath = LUFile.GetWindowsPath (AFileName)
    LWindowsPath = LUFile.GetPureWindowsPath ('TEST_LUFileUtils\\')
    # print ('LWindowsPath:', LWindowsPath)

    LFileSize = LUFile.GetFileSize (AFileName)
    LFileDateTime = LUFile.GetFileDateTime (AFileName)
    s = f'{LFileDateTime[2]:%d.%m.%Y  %H:%M} {LFileDateTime[2]:%d.%m.%Y  %H:%M} {LFileSize:d}'
    LULog.LoggerTOOLS_AddLevel (LULog.TEXT, s)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # print ('DEBUG: function ',sys._getframe (0).f_code.co_name, '...')
    LUDoc.PrintInfoObject('-----main----')
    LUDoc.PrintInfoObject(main)

    global GDir
    global GMask

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GDir = LUParserARG.GetParam ('PDir', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = LUParserARG.GetParam ('PMask', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    Largs = Lparser.parse_args ()
    GDir = Largs.PDir
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GMask = Largs.PMask
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    # GDir = r'D:\WORK\!!HISTORY'
    # lyrpy.LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    # GMask = '.*'
    # lyrpy.LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')

    _Option = 1
    _OutFile = 'DirFiles.txt'
    _OutFile = 'CONSOLE'
    # lyrpy.LUFile.FileDelete (_OutFile)

    LULog.LoggerTOOLS.setLevel(logging.INFO)
    # lyrpy.LULog.LoggerTOOLS.setLevel(logging.DEBUG)

    LUFileUtils.DirFiles(GDir, GMask, True, _OutFile, _Option, FuncDir, FuncFile)

    LULog.STOPLogging ()
#endfunction

#------------------------------------------
# DirFiles
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
