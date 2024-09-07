"""TEST_LUsys.py"""
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
     TEST_LUSupport.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import logging
from subprocess import CompletedProcess, run, Popen, PIPE
from sys import executable
# Значение executable в Python
#   это абсолютный путь к исполняемому файлу интерпретатора Python. Оно потребуется для запуска кода.
# python import local file

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU
#------------------------------------------
import lyrpy.LUSupport as LUSupport
from lyrpy.LUDoc import *

"""
Синтаксис subprocess.run
    subprocess.run(args, *, stdin, input, stdout,  stderr,
               capture_output, shell, cwd, timeout,
               check, encoding, errors, text, env,
               universal_newlines)
Аргумент args
    обязательный, через него передается запускаемая программа с аргументами.
Параметры stdin, input, stdout и stderr
    отвечают за потоки данных, которые передаются в процесс или выходят из него. Здесь stdout — поток вывода (результат работы), stderr — поток ошибок, которые возникли при выполнении. По умолчанию их значения — None.
capture_output
    по умолчанию False, отвечает за захват результата работы процесса (вывода).
Параметр shell
    отвечает за способ передачи в процесс программы и ее аргументов — если они представлены как одна строка, следует указать True. По умолчанию False.
cwd
    используется, если требуется указать абсолютный путь к каталогу с запускаемой программой.
timeout
    время в секундах, по истечении которого процесс завершится. При этом возникает исключение.
check
    если имеет значение True, то вызывает исключение, если во время выполнения возникли ошибки. По умолчанию False.
encoding
    отвечает за декодирование вывода.
errors
    если указан, то ошибки кодировки будут вызывать исключение.
text, universal_newlines
    текстовые режимы для потоков ввода, вывода и ошибок. По умолчанию false.
env
    переменные среды для нового процесса.

"""

def TEST_LUSupport ():
    """TEST_LUSupport"""
#beginfunction
    PrintInfoObject(TEST_LUSupport)
    PrintInfoObject(LUSupport)
#endfunction

def TEST_01 ():
    """TEST_01"""
#beginfunction
    PrintInfoObject(TEST_01)
    print ('01.-----------------------------')
    # CompletedProcess (args = "echo 'Subprocesses are cool!", returncode = 0)
    LCompletedProcess = run (r'C:\startup866.cmd', shell = True)
    LCompletedProcess = run ("echo 'Subprocesses are cool!", shell = True)
    LCompletedProcess = run ("echo 'Это по русски!", shell = True, encoding = 'cp866')

    print ('02.-----------------------------')
    """
    Но что если мы хотим получить не только статус выполнения, но и какие-то данные вывода?
    Для этого нам необходимо установить параметр capture_output = True:
    """
    # LCompletedProcess = run ('ping localhost', shell = True, capture_output = True, encoding = 'cp866')
    # print("stdout:", LCompletedProcess.stdout)
    # print("stderr:", LCompletedProcess.stderr)

    print ('03.-----------------------------')
    # LCompletedProcess = run ('notepad.exe')

    print ('04.-----------------------------')
    # LCompletedProcess = run ('regedit.exe')
#endfunction

def TEST_05 ():
    """TEST_05"""
#beginfunction
    PrintInfoObject(TEST_05)
    #encoding = 'cp866' encoding='utf-8'
    p1 = Popen ('dir', shell = True, stdin = None, stdout = PIPE, stderr = PIPE)
    p2 = Popen ('sort /R', shell = True, stdin = p1.stdout)
    out, err = p2.communicate ()
    p1.stdout.close ()
    # print("stdout:", out)
    # print("stderr:", err)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_LUSupport ()
    TEST_01 ()
    TEST_05 ()
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

