"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (PROJECTS_PY)
 Module:
     SyncFiles.py

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
import platform

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pandas

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import lyrpy.LUConsole as LUConsole
import lyrpy.LUConst as LUConst
import lyrpy.LUDateTime as LUDateTime
import lyrpy.LUDecotators as LUDecotators
import lyrpy.LUDict as LUDict
import lyrpy.LUErrors as LUErrors
import lyrpy.LUFile as LUFile
import lyrpy.LUFileUtils as LUFileUtils
import lyrpy.LULog as LULog
import lyrpy.LUObjects as LUObjects
import lyrpy.LUObjectsYT as LUObjectsYT
import lyrpy.LUos as LUos
import lyrpy.LUParserARG as LUParserARG
import lyrpy.LUParserINI as LUParserINI
import lyrpy.LUProc as LUProc
import lyrpy.LUQThread as LUQThread
import lyrpy.LUQTimer as LUQTimer
import lyrpy.LUSheduler as LUSheduler
import lyrpy.LUStrDecode as LUStrDecode
import lyrpy.LUStrUtils as LUStrUtils
import lyrpy.LUSupport as LUSupport
import lyrpy.LUsys as LUsys
import lyrpy.LUThread as LUThread
import lyrpy.LUYouTube as LUYouTube
import lyrpy.LUDoc as LUDoc

if platform.system() == 'Windows':
    import lyrpy.LUNetwork as LUNetwork
    import lyrpy.LUNumUtils as LUNumUtils
    import lyrpy.LUTimer as LUTimer
    import lyrpy.LUVersion as LUVersion
    import lyrpy.LUParserREG
#endif

#------------------------------------------
#CONST
#------------------------------------------

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
    global GDirDest
    global GMask

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, s)
    #----------------------------------------------------------------
    GDir = LUParserARG.GetParam ('PDir', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = LUParserARG.GetParam ('PDirDest', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirDest = {GDirDest}')
    GMask = LUParserARG.GetParam ('PMask', "")
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    #----------------------------------------------------------------
    Lparser = argparse.ArgumentParser (description = 'Параметры', prefix_chars = '-/')
    Lparser.add_argument ('PDir', type = str, default='', help = 'PDir')
    Lparser.add_argument ('PDirDest', type = str, default='', help = 'PDirDest')
    Lparser.add_argument ('PMask', type = str, default='', help = 'PMask')
    # Lparser.add_argument ('-PDir', type = str, nargs = '?', default = '', dest = 'PDir', help = 'PDir')
    # Lparser.add_argument ('-PDirDest', type = str, nargs = '?', default = '', dest = 'PDirDest', help = 'PDirDest')
    # Lparser.add_argument ('-PMask', type = str, nargs = '?', default = '', dest = 'PMask', help = 'PMask')
    Largs = Lparser.parse_args ()
    GDir = Largs.PDir
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = Largs.PDirDest
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDirDest}')
    GMask = Largs.PMask
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')
    #----------------------------------------------------------------

    GDir = r'D:\WORK\08_SUBD\01_ORACLE\БИБЛИОТЕКИ'
    GDir = r'D:\WORK\08_SUBD\01_ORACLE\PROJECTS\oracle-db-examples'
    GDir = r'D:\WORK\08_SUBD'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDir = {GDir}')
    GDirDest = r'D:\WORK\SYNC\08_SUBD'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PDirDest = {GDirDest}')
    GMask = '.*'
    LULog.LoggerAPPS_AddLevel (LULog.TEXT, f'PMask = {GMask}')

    _Option = 0
    _OutFile = 'SyncFiles.txt'
    _OutFile = 'CONSOLE'
    # LUFile.FileDelete (_OutFile)

    LULog.LoggerTOOLS.setLevel(logging.INFO)
    # LULog.LoggerTOOLS.setLevel(logging.DEBUG)

    LUFileUtils.SyncFiles(GDir, GMask, GDirDest, _OutFile, _Option)

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
