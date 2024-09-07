"""
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     PATTERNS_PY
     Python (PROJECTS_PY)
 Module:
     TEST_LULog_START.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime
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
# TEST_01 ()
#------------------------------------------
def TEST_01 ():
    """TEST_"""
#beginfunction
    print (sys._getframe (0).f_code.co_name, '...')
    # print (inspect.currentframe().f_code.co_name, '...')
    # print (inspect.stack () [0] [3], '...')
    # print (traceback.extract_stack () [-1].name, '...')
    LUDoc.PrintInfoObject('-----TEST_01----')
    LUDoc.PrintInfoObject(TEST_01)
#endfunction

#------------------------------------------
# main ()
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')
    LULog.LoggerAdd (LULog.LoggerTOOLS, LULog.TEXT, "Тест")
    TEST_01 ()
    LULog.STOPLogging ()

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslCONFIG, 'LOG_CONFIG',
                        'LOGGING_FILECONFIG.log','LOGGING_FILECONFIG_json.log')
    LULog.LoggerAdd (LULog.LoggerTOOLS, LULog.TEXT, "Тест")
    TEST_01 ()
    LULog.STOPLogging ()

    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslYAML, 'LOG_YAML',
                        'LOGGING_FILEYAML.log','LOGGING_FILEYAML_json.log')
    LULog.LoggerAdd (LULog.LoggerTOOLS, LULog.TEXT, "Тест")
    TEST_01 ()
    LULog.STOPLogging ()

#endfunction

#------------------------------------------
# PATTERNS_PY
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
