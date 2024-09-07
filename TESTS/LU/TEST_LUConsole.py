"""TEST_LUConsole.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023-2024
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (PROJECTS_PY)
 Module:
     TEST_LUConsole.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys
import time
import logging

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import rich
import rich.progress
# from rich.progress import FileSizeColumn, Progress, TotalFileSizeColumn, Console
# from rich.progress import track

# from rich import print
# from rich.console import Console

# from progress.bar import IncrementalBar
import progress.bar

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import lyrpy.LULog as LULog
import lyrpy.LUConst as LUConst
from lyrpy.LUDoc import *
import lyrpy.LUConsole as LUConsole
import lyrpy.LUSupport as LUSupport

#------------------------------------------
# TEST_LUConsole ()
#------------------------------------------
def TEST_LUConsole ():
    """TEST_LUConsole"""
#beginfunction
    PrintInfoObject('---------TEST_LUConsole----------')
    PrintInfoObject(TEST_LUConsole)
    PrintInfoObject(LUConsole)

    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, sys.stdout.encoding)
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, sys.stdout.name)
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, sys.stdout.isatty())
    LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, sys.stdout.mode)
    # if sys.stdout.isatty ():
    if LUSupport.IsTerminal ():
        LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, 'Это терминал WINDOWS')
    else:
        LULog.LoggerAdd (LULog.LoggerAPPS, logging.INFO, 'Это терминал piped or redirected')
    #endif
#endfunction

def TEST_Write ():
    """TEST_Write"""
#beginfunction
    PrintInfoObject('---------TEST_Write----------')
    PrintInfoObject(TEST_Write)

    s1 = 'ТЕСТ1'
    LUConsole.Write (s1)
    LUConsole.Write (s1, AStyles=(LUConsole.cS_BOLD,LUConsole.cS_ITALIC), AFG8=LUConsole.cFG8_RED, ABG8=LUConsole.cBG8_WHITE)
    LUConsole.WriteLN ('')
#endfunction

def TEST_WriteLN ():
    """TEST_WriteLN"""
#beginfunction
    PrintInfoObject('---------TEST_WriteLN----------')
    PrintInfoObject(TEST_WriteLN)

    s1 = 'ТЕСТ2'
    # LUConsole.WriteLN(s1, AStyles=LUConsole.cS_BOLD,  AFG8=LUConsole.cFG8_GREEN, ABG8=LUConsole.cBG8_CYAN)
    LUConsole.WriteLN(s1, AStyles=LUConsole.cStyles.BOLD.value,  AFG8=LUConsole.cFG8.GREEN.value, ABG8=LUConsole.cBG8.CYAN.value)
    #
    s1 = 'ТЕСТ3'
    LUConsole.WriteLN(s1, AESC='\033[01;03;04;07;38;05;222;48;05;22m')
    s1 = 'ТЕСТ4'
    LUConsole.WriteLN (s1, AStyles = '', AFG8 = LUConsole.cFG8.GREEN.value, ABG8 = LUConsole.cBG8.BLACK.value)
#endfunction

def TEST_WriteLN_FULL ():
    """TEST_WriteLN_FULL"""
#beginfunction
    PrintInfoObject('---------TEST_WriteLN_FULL----------')
    PrintInfoObject(TEST_WriteLN_FULL)

    for Style in LUConsole.cStyles:
        for BG in LUConsole.cBG8:
            for FG in LUConsole.cFG8:
                s1 = str(Style.value)+str(FG.value)+str(BG.value)
                LUConsole.Write(s1, AStyles=Style.value, AFG8=FG.value, ABG8=BG.value)
            #endfor
            LUConsole.WriteLN ('')
        #endfor
    #endfor
#endfunction

#------------------------------------------------------
# TEST_WriteLN_flush ():
#------------------------------------------------------
def TEST_WriteLN_flush ():
    """TEST_WriteLN_flush"""
#beginfunction
    PrintInfoObject('---------TEST_WriteLN_flush----------')
    PrintInfoObject(TEST_WriteLN_flush)

    # for i in range(0, 101, 10):
    #     print ('\r>> You have finished %d%%' % i)
    #     sys.stdout.flush()
    #     time.sleep(0.5)
    print('sys.stdout.write...')
    for x in range (10):
        LUConsole.ClearLine()
        # sys.stdout.write ('\r' + 'xxxxxxxxxxxx='+str (x))
        sys.stdout.write ('xxxxxxxxxxxx=' + str (x))
        sys.stdout.flush ()
        time.sleep (0.5)
    #endfor
    LUConsole.WriteLN ('')

    print('LUConsole.Write...')
    for x in range (10):
        LUConsole.ClearLine()
        # s1 = '\r' + 'xxxxxxxxxxxx='+str (x)
        s1 = 'xxxxxxxxxxxx=' + str (x)
        LUConsole.Write (s1, AStyles = LUConsole.cS_BOLD, AFG8 = LUConsole.cFG8_GREEN, ABG8 = LUConsole.cBG8_CYAN)
        time.sleep (0.5)
    #endfor
    LUConsole.WriteLN ('')
#endfunction

#------------------------------------------------------
# TEST_Rich_Progress ():
#------------------------------------------------------
def TEST_Rich_Progress ():
    """TEST_Rich_Progress"""
#beginfunction
    PrintInfoObject('---------TEST_Rich_Progress----------')
    PrintInfoObject(TEST_Rich_Progress)

    LMax = 100
    LFileSizeColumn = rich.progress.FileSizeColumn ()
    LTotalFileSizeColumn = rich.progress.TotalFileSizeColumn ()
    prog = rich.progress.Progress (LFileSizeColumn, ('/'), LTotalFileSizeColumn)
    # global task
    task = prog.add_task ("downloading...", total=LMax)

    def show_progress_bar (bytes_remaining):
    #beginfunction
        # print(bytes_remaining)
        prog.update (task, completed = LMax - bytes_remaining)
    #endfunction

    prog.start()

    for i in range(0,LMax,10):
        # print(i)
        time.sleep(0.2)
        show_progress_bar(LMax-i)
    #endfor

    prog.remove_task(task)
    prog.stop()
#endfunction

def TEST_Rich_ERROR ():
    """TEST_Rich_ERROR"""
#beginfunction
    PrintInfoObject('---------TEST_Rich_ERROR----------')
    PrintInfoObject(TEST_Rich_ERROR)

    rich.print('[bold red]Ошибка[/bold red]')

    def process_data():
    #beginfunction
        time.sleep(0.1)
    #endfunction

    for _ in rich.progress.track (range (50), description = '[green]Processing data'):
        process_data ()
    #endfor

    print('Hello, [bold magenta]World[/bold magenta]!', ":vampire:", locals())

    # console.log (f"[green]Finish fetching data[/green] {num}")

    console = rich.progress.Console()
    console.print('==> Mismatches were found in one or more platforms <==', style='bold red')

    console = rich.progress.Console(color_system="windows")
    print(console.color_system)
    console.print('==> Mismatches were found in one or more platforms <==', style='bold red')

    rich.reconfigure(force_terminal=True)
    rich.print("[1, 2, ..., 3, 4]")
#endfunction

def TEST_progress ():
    """TEST_progress"""
#beginfunction
    PrintInfoObject('---------TEST_progress----------')
    PrintInfoObject(TEST_progress)

    mylist = [1,2,3,4]
    bar = progress.bar.IncrementalBar('Countdown', max = len(mylist))
    for item in mylist:
        bar.next()
        time.sleep(1)
    #endfor

    # bar.hide_cursor = False
    # bar.finish()
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    print (f'ISTerminal={LUSupport.IsTerminal ()}')

    TEST_LUConsole ()
    TEST_Write ()
    TEST_WriteLN ()
    TEST_WriteLN_FULL ()
    TEST_WriteLN_flush ()
    TEST_Rich_Progress ()
    TEST_Rich_ERROR ()
    TEST_progress ()
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

