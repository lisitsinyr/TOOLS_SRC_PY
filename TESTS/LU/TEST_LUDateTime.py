"""TEST_LUDateTime.py"""
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
     TEST_LUDateTime.py

 =======================================================
"""

import logging

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
# import LULog
# import LUConst
from lyrpy.LUDoc import *
import lyrpy.LUDateTime as LUDateTime

def TEST_LUDateTime ():
    """TEST_LUDateTime"""
#beginfunction
    PrintInfoObject('---------TEST_LUDateTime----------')
    PrintInfoObject(TEST_LUDateTime)
    PrintInfoObject(LUDateTime)
#endfunction

def TEST_LogDateStr ():
    """TEST_LogDateStr"""
#beginfunction
    PrintInfoObject ('---------TEST_LogDateStr----------')
    PrintInfoObject(TEST_LogDateStr)

    LToday = LUDateTime.Now ()

    PrintInfoObject (f'------------{LUDateTime.cFormatDateTimeLog01}')
    s1 = LUDateTime.DateTimeStr(False, LToday, LUDateTime.cFormatDateTimeLog01,Amsecs = True)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s1)

    s2 = LUDateTime.DateTimeStr(True, LToday, LUDateTime.cFormatDateTimeLog01,Amsecs = True)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s2)

    PrintInfoObject (f'------------{LUDateTime.cFormatDateTimeLog02}')
    s1 = LUDateTime.DateTimeStr(False, LToday, LUDateTime.cFormatDateTimeLog02,Amsecs = True)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s1)
    s2 = LUDateTime.DateTimeStr(True, LToday, LUDateTime.cFormatDateTimeLog02,Amsecs = True)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s2)

    PrintInfoObject (f'------------{LUDateTime.cFormatDateTimeLog05}')
    s1 = LUDateTime.DateTimeStr(False, LToday, LUDateTime.cFormatDateTimeLog05,Amsecs = True)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s1)
    s2 = LUDateTime.DateTimeStr(True, LToday, LUDateTime.cFormatDateTimeLog05,Amsecs = True)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s2)
#endfunction

def TEST_DecodeDate ():
    """TEST_DecodeDate"""
#beginfunction
    PrintInfoObject('---------TEST_DecodeDate----------')
    PrintInfoObject(TEST_DecodeDate)

    LYMD = LUDateTime.DecodeDate (LUDateTime.Now ())
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, LYMD)
#endfunction

def TEST_EncodeDate ():
    """TEST_EncodeDate"""
#beginfunction
    PrintInfoObject('---------TEST_EncodeDate----------')
    PrintInfoObject(TEST_EncodeDate)

    LYear, LMonth, LDay = LUDateTime.DecodeDate (LUDateTime.Now ())
    LDate = LUDateTime.EncodeDate(LYear, LMonth, LDay)
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, LDate)
#endfunction

def TEST_DayOfWeek ():
    """TEST_DayOfWeek"""
#beginfunction
    PrintInfoObject('---------TEST_DayOfWeek----------')
    PrintInfoObject(TEST_DayOfWeek)

    LYear, LMonth, LDay = LUDateTime.DecodeDate (LUDateTime.Now ())
    LDate = LUDateTime.EncodeDate(LYear, LMonth, LDay)
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, LDate)

    # LDayWeek = LUDateTime.DayOfWeek (LUDateTime.EncodeDate (LYear, LMonth, LDay))
    LDayWeek = LUDateTime.DayOfWeek (LDate)
    print(LDayWeek)

#endfunction


"""
DecodeTime (ADateTime: datetime.datetime):
EncodeTime (AHour: int, AMin: int, ASec: int, AMSec: int) -> datetime.time:
EncodeDateTime (AYear: int, AMonth: int, ADay: int, AHour: int, AMin: int, ASec: int, AMSec: int) -> datetime.datetime:
DayOfWeek (ADateTime: datetime.datetime):
DaysInMonth (AYear: int, AMonth: int):
IsLeapYear(AYear: int) -> bool:
DaysPerMonth(AYear: int, AMonth: int) -> int:
GenerateObjectIDStr (AObjectID: datetime.datetime) -> str:
"""

def TEST_GenerateObjectIDStr ():
    """TEST_GenerateObjectIDStr"""
#beginfunction
    PrintInfoObject('---------TEST_GenerateObjectIDStr----------')
    PrintInfoObject(TEST_GenerateObjectIDStr)

    LObjectIDStr = LUDateTime.GenerateObjectIDStr (LUDateTime.Now ())
    s = f'LObjectIDStr={LObjectIDStr}'
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, s)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_LogDateStr ()
    TEST_DecodeDate ()
    TEST_EncodeDate ()
    TEST_GenerateObjectIDStr ()

    TEST_DayOfWeek ()
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
