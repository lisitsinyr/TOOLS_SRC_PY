"""TEST_LUSheduler.py"""
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
     TEST_LUSheduler.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import threading
import logging
import time
import datetime

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import lyrpy.LUSheduler as LUSheduler
from lyrpy.LUDoc import *
import lyrpy.LUDateTime as LUDateTime

GShedulerThread = LUSheduler.TShedulerThread ()
GShedulerTimer = LUSheduler.TShedulerTimer (1,None)
GCounter = 0

def TEST_LUSheduler ():
    """TEST_LUSheduler"""
#beginfunction
    PrintInfoObject('---------TEST_LUSheduler----------')
    PrintInfoObject(TEST_LUSheduler)
    PrintInfoObject(LUSheduler)
#endfunction

# def __Action_ShedulerTEST1 ():
#     """__Action_ShedulerTEST1"""
# #beginfunction
#     PrintInfoObject('---------__Action_ShedulerTEST1----------')
#     print (GSheduler.OnShedulerEvent.NameEvent)
#     GSheduler.PrintEvent (GSheduler.OnShedulerEvent)
# #endfunction

# def __Action_ShedulerTEST2 ():
#     """__Action_ShedulerTEST2"""
# #beginfunction
#     PrintInfoObject('---------__Action_ShedulerTEST2----------')
#     print (GSheduler.OnShedulerEvent.NameEvent)
#     GSheduler.PrintEvent (GSheduler.OnShedulerEvent)
# #endfunction

def __Action_StartExecute (AEvent:LUSheduler.TShedulerEventItem):
    """__Action_StartExecute"""
    global GCounter
#beginfunction
    PrintInfoObject('---------__Action_StartExecute----------')
    # if AEvent is not None:
    #      GSheduler.PrintEvent (AEvent)
    # #endif
    GCounter += 1
    # if GSheduler.OnShedulerEvent is not None:
    #     if GSheduler.OnShedulerEvent.NameEvent == 'ShedulerTEST1':
    #         __Action_ShedulerTEST1 ()
    #     #endif
    #     if GSheduler.OnShedulerEvent.NameEvent == 'ShedulerTEST2':
    #         __Action_ShedulerTEST2 ()
    #     #endif
    # #endif
#endfunction

def TEST_ShedulerThreasd ():
    """TEST_ShedulerThreasd"""
    global GCounter
#beginfunction
    PrintInfoObject('---------TEST_ShedulerThreasd----------')
    PrintInfoObject(TEST_ShedulerThreasd)
    PrintInfoObject(LUSheduler.TSheduler)
    PrintInfoObject(LUSheduler.TShedulerEventItem)

    #-------------------------------
    # GShedulerThread
    #-------------------------------
    GShedulerThread.Sheduler.OnSheduler = __Action_StartExecute
    LEvent = GShedulerThread.Sheduler.AddEvent ('ShedulerTEST1', '* * * * *')
    # if LEvent is not None:
    #     GShedulerThread.Sheduler.PrintEvent (LEvent)
    # #endif
    LEvent = GShedulerThread.Sheduler.AddEvent ('ShedulerTEST2', '0 0 0 0 0')
    # if LEvent is not None:
    #      GShedulerThread.Sheduler.PrintEvent  (LEvent)
    # #endif
    LEvent = GShedulerThread.Sheduler.GetShedulerEventItem ('ShedulerTEST1')
    # if LEvent is not None:
    #      GShedulerThread.Sheduler.PrintEvent (LEvent)
    # #endif

    #---------------------------------------
    # GShedulerThread.Sheduler.DeleteEvent ('ShedulerTEST2')
    #---------------------------------------
    # print (len (GShedulerThread.Sheduler.ShedulerEvents))
    # GShedulerThread.Sheduler.DeleteEvent ('ShedulerTEST2')
    #---------------------------------------
    # print (len (GShedulerThread.Sheduler.ShedulerEvents))
    #---------------------------------------
    # LEvent = GShedulerThread.Sheduler.GetShedulerEventItem ('ShedulerTEST')
    # if LEvent is not None:
    #     GShedulerThread.Sheduler.PrintEvent (LEvent)
    #---------------------------------------

    PrintInfoObject('---------GShedulerThread.Sheduler.StartSheduler()----------')
    GShedulerThread.StartSheduler()

    # Ждем завершения работы всех потоков
    while len (threading.enumerate ()) > 1:
        if GCounter == 2:
            GShedulerThread.StopSheduler ()
        #endif
    #endwhile

    # Остался главный поток python
    for tread in threading.enumerate ():
        s = f'Остался главный поток python={tread}'
        LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, s)
    #endfor
#endfunction

def TEST_ShedulerTimer ():
    """TEST_ShedulerTimer"""
    global GCounter
#beginfunction
    PrintInfoObject('---------TEST_ShedulerTimer----------')
    PrintInfoObject(TEST_ShedulerTimer)
    PrintInfoObject(LUSheduler.TShedulerTimer)
    PrintInfoObject(LUSheduler.TShedulerEventItem)

    #-------------------------------
    # GShedulerTimer
    #-------------------------------
    GShedulerTimer.Sheduler.OnSheduler = __Action_StartExecute

    LEvent = GShedulerTimer.Sheduler.AddEvent ('ShedulerTEST1', '* * * * *')
    if LEvent is not None:
         GShedulerTimer.Sheduler.PrintEvent (LEvent)
    #endif
    LEvent = GShedulerTimer.Sheduler.AddEvent ('ShedulerTEST2', '0 0 0 0 0')
    if LEvent is not None:
         GShedulerTimer.Sheduler.PrintEvent  (LEvent)
    #endif
    LEvent = GShedulerTimer.Sheduler.GetShedulerEventItem ('ShedulerTEST1')
    if LEvent is not None:
         GShedulerTimer.Sheduler.PrintEvent (LEvent)
    #endif

    #---------------------------------------
    # GShedulerTimer.Sheduler.DeleteEvent ('ShedulerTEST2')
    #---------------------------------------
    # print (len (GShedulerTimer.ShedulerEvents))
    # GShedulerTimer.Sheduler.DeleteEvent ('ShedulerTEST2')
    #---------------------------------------
    # print (len (GShedulerTimer.Sheduler.ShedulerEvents))
    #---------------------------------------
    # LEvent = GShedulerTimer.Sheduler.GetShedulerEventItem ('ShedulerTEST')
    # if LEvent is not None:
    #     GShedulerTimer.Sheduler.PrintEvent (LEvent)
    #---------------------------------------

    PrintInfoObject('---------GSheduler.GShedulerTimer()----------')
    GShedulerTimer.StartSheduler()

    # Ждем завершения работы всех потоков
    while len (threading.enumerate ()) > 1:
        if GCounter == 100:
            GShedulerTimer.StopSheduler ()
            break
        #endif
    #endwhile

    # Остался главный поток python
    for tread in threading.enumerate ():
        s = f'Остался главный поток python={tread}'
        LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, s)
    #endfor
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_LUSheduler ()

    TEST_ShedulerThreasd ()
    TEST_ShedulerTimer ()
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

