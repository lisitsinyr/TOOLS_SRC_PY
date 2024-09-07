"""TEST_LU.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023-2024
 Author:
     Lisitsin Y.R.
 Project:
     TESTS_PY
     Python (LU)
 Module:
     TEST_LUFileUtils.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import logging

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU
#------------------------------------------
import lyrpy.LUConst as LUConst
import lyrpy.LULog as LULog
import lyrpy.LUFile as LUFile
from lyrpy.LUDoc import *

#------------------------------------------
# TEST_re ()
#------------------------------------------
def TEST_re (AFileName, AComment, AMask):
    """TEST_re"""
#beginfunction
    print ('LFileName:', AFileName)
    print ('LComment:', AComment)
    print ('LMask:', AMask)
    Lresult = LUFile.CheckFileNameMask (AFileName, AMask)
    if Lresult :
        LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, AFileName + ' ok!')
    else:
        LULog.LoggerAdd (LULog.LoggerAPPS, logging.ERROR, AFileName + ' not match')
    #endif
#endfunction

def TEST_01 ():
    """TEST_"""
#beginfunction
    PrintInfoObject('-----TEST_01----')
    PrintInfoObject(TEST_01)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(только латинские буквы и цифры) (расширение) .py'
    LMask = '^[a-zA-Z0-9]+.py'
    TEST_re (LFileName, LComment, LMask)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(все символы) (расширение) .*'
    LMask = '.*'
    TEST_re (LFileName, LComment, LMask)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(все символы) (расширение) .*'
    LMask = '.*.'
    TEST_re (LFileName, LComment, LMask)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(все символы) (расширение) .*'
    LMask = '.*.*'
    TEST_re (LFileName, LComment, LMask)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(все символы) (расширение) .py'
    LMask = '.*.py'
    TEST_re (LFileName, LComment, LMask)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(все символы + пробелы) (расширение) .py'
    LMask = '[\\S ]*.py'
    TEST_re (LFileName, LComment, LMask)

    LFileName = 'LUNu  mUt  ils.py'
    LComment = '(только латинские буквы и цифры + пробелы) (расширение) .py'
    LMask = '[a-zA-Z0-9 ]*.py'
    TEST_re (LFileName, LComment, LMask)

#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')
    TEST_01 ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
