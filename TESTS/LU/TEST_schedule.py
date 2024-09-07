"""TEST_schedule.py"""
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
     TEST_schedule.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import schedule
import time
import threading

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
from lyrpy.LUDoc import *

def TEST_schedule ():
    """TEST_schedule"""
#beginfunction
    PrintInfoObject(TEST_schedule)
    PrintInfoObject(schedule)
#endfunction

def job():
    print("I'm working...")

def TEST_schedule_01 ():
    """TEST_schedule_01"""
#beginfunction
    PrintInfoObject(TEST_schedule_01)
    # Run job every 3 second/minute/hour/day/week,
    # Starting 3 second/minute/hour/day/week from now
    schedule.every (3).seconds.do (job)
    schedule.every (3).minutes.do (job)
    schedule.every (3).hours.do (job)
    schedule.every (3).days.do (job)
    schedule.every (3).weeks.do (job)

    # Run job every minute at the 23rd second
    schedule.every ().minute.at (":23").do (job)

    # Run job every hour at the 42rd minute
    schedule.every ().hour.at (":42").do (job)

    # Run jobs every 5th hour, 20 minutes and 30 seconds in.
    # If current time is 02:00, first execution is at 06:20:30
    schedule.every (5).hours.at ("20:30").do (job)

    # Run job every day at specific HH:MM and next HH:MM:SS
    schedule.every ().day.at ("10:30").do (job)
    schedule.every ().day.at ("10:30:42").do (job)

    # Run job on a specific day of the week
    schedule.every ().monday.do (job)
    schedule.every ().wednesday.at ("13:15").do (job)
    schedule.every ().minute.at (":17").do (job)

    while True:
        schedule.run_pending ()
        time.sleep (1)
#endfunction

def hello():
    print("hello, world")

def TEST_schedule_02 ():
    """TEST_schedule_01"""
#beginfunction
    PrintInfoObject(TEST_schedule_02)
    t = threading.Timer (5.0, hello)
    t.start ()
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_schedule ()
    TEST_schedule_01 ()
    TEST_schedule_02 ()
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

