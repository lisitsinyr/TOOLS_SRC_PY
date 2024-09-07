"""TEST_LUParserARG.py"""
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
     TEST_LUParserARG.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys
import argparse
import platform
#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import lyrpy.LUParserARG as LUParserARG
from lyrpy.LUDoc import *

def TEST_LUParserARG ():
    """TEST_LUParserARG"""
#beginfunction
    PrintInfoObject('---------TEST_LUParserARG----------')
    PrintInfoObject(TEST_LUParserARG)
    ...
#endfunction

def TEST_GetParam ():
    """TEST_GetParam"""
#beginfunction
    PrintInfoObject('---------TEST_GetParam----------')
    PrintInfoObject(TEST_GetParam)

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP1 = LUParserARG.GetParam('p1', "")
    s = f'p1 = {LP1}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP2 = LUParserARG.GetParam('P2', "")
    s = f'P2 = {LP2}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP3 = LUParserARG.GetParam('P3', "")
    s = f'P3 = {LP3}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP4 = LUParserARG.GetParam('P4', "")
    s = f'P4 = {LP4}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_ArgumentParser ():
    """TEST_GetParam_PY"""
#beginfunction
    PrintInfoObject('---------TEST_ArgumentParser----------')
    PrintInfoObject(TEST_ArgumentParser)

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    Lparser = argparse.ArgumentParser (description='Параметры', prefix_chars='-/')
    Lparser.add_argument ('FileName', type = str, default='', help = 'FileName')
    Lparser.add_argument ('-p1', type = str, nargs = '?', default = '', dest = 'p1', help = 'p1')
    Lparser.add_argument ('/P2', type = int, nargs = '?', default = -1, dest = 'P2', help = 'P2')
    Lparser.add_argument ('-P3', type = int, nargs = '?', default = -1, dest = 'P3', help = 'P3')
    Lparser.add_argument ('-P4', type = int, nargs = '?', default = -1, dest = 'P4', help = 'P4')
    Largs = Lparser.parse_args ()
    LP1 = Largs.p1
    s = f'p1 = {LP1}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP2 = Largs.P2
    s = f'P2 = {LP2}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP3 = Largs.P3
    s = f'P3 = {LP3}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP4 = Largs.P4
    s = f'P4 = {LP4}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_TArgParser ():
    """TEST_TArgParser"""
#beginfunction
    PrintInfoObject('---------TEST_TArgParser----------')
    PrintInfoObject(TEST_TArgParser)

    s = f'sys.argv = {sys.argv}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LArgParser = LUParserARG.TArgParser(description='Параметры', prefix_chars='-/')
    #-----------------------------------------------------------------
    # name - либо имя, либо список строк параметров, например. foo или -f, --foo.
    # type = int, float, argparse.FileType('w'), or callable function
    # default - значение, создаваемое, если аргумент отсутствует в командной строке
    # help - Краткое описание того, что делает аргумент.
    #-----------------------------------------------------------------
    # nargs = int, '?', '*', '+', or argparse.REMAINDER
    # dest - имя атрибута, который будет добавлен к объекту, возвращаемому функцией parse_args()
    # action = 'store', 'store_const', 'store_true', 'append', 'append_const', 'count', 'help', 'version'
    # const = None
    # choices = None
    # required = True or False
    # metavar = None
    #-----------------------------------------------------------------
    # LArg = LArgParser.add_argument ('FileName', type = str, default='', help = 'FileName')
    LArg = LArgParser.ArgParser.add_argument ('FileName', type = str, default='', help = 'FileName')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LArg)
    LArg = LArgParser.add_argument ('-p1', type = str, default='', help = 'p1')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LArg)
    LArg = LArgParser.add_argument ('/P2', type = int, default=-1, help = 'P2')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LArg)
    LArg = LArgParser.add_argument ('-P3', type = int, default=-1, help = 'P3')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LArg)
    LArg = LArgParser.add_argument ('-P4', type = int, default=-1, nargs = '?', help = 'P4')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LArg)

    # _StoreAction(option_strings=[], dest='FileName', nargs='?', const=None, default='', type=<class 'str'>, choices=None, required=False, help='FileName', metavar=None)
    # _StoreAction(option_strings=['-p1'], dest='p1', nargs='?', const=None, default='', type=<class 'str'>, choices=None, required=False, help='p1', metavar=None)
    # _StoreAction(option_strings=['/P2'], dest='P2', nargs='?', const=None, default=-1, type=<class 'int'>, choices=None, required=False, help='P2', metavar=None)
    # _StoreAction(option_strings=['-P3'], dest='P3', nargs='?', const=None, default=-1, type=<class 'int'>, choices=None, required=False, help='P3', metavar=None)
    # _StoreAction(option_strings=['-P4'], dest='P4', nargs='?', const=None, default=-1, type=<class 'int'>, choices=None, required=False, help='P4', metavar=None)

    # Largs = LArgParser.parse_args ()
    Largs = LArgParser.ArgParser.parse_args ()
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, Largs.__dict__)

    LFileName = Largs.FileName
    s = f'FileName = {LFileName}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP1 = Largs.p1
    s = f'p1 = {LP1}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP2 = Largs.P2
    s = f'P2 = {LP2}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP3 = Largs.P3
    s = f'P3 = {LP3}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LP4 = Largs.P4
    s = f'P4 = {LP4}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    # parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    #_StoreAction(option_strings=[], dest='integers', nargs='+', const=None, default=None, type=<class 'int'>, choices=None, required=True, help='an integer for the accumulator', metavar='N')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=max, help='sum the integers (default: find the max)')
    #_StoreConstAction(option_strings=['--sum'], dest='accumulate', nargs=0, const=<built-in function sum>, default=<built-in function max>, type=None, choices=None, required=False, help='sum the integers (default: find the max)', metavar=None)
    #Namespace(integers=[7, -1, 42], accumulate=<built-in function sum>)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    #FileName.txt -p1 "mn,mvnxsdv" /P2 3 -P3 5 -P4
    TEST_LUParserARG ()
    TEST_GetParam ()
    # TEST_ArgumentParser ()
    # TEST_TArgParser ()
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    if platform.system() == 'Windows':
        main ()
    #endif

    # from mounter.win import *
    # if sys.platform == "darwin":
    #     from mounter.osx import *
    # if sys.platform == "linux2":
    #     from mounter.linux import *

#endif

#endmodule

