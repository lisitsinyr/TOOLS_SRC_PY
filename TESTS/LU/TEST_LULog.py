"""TEST_LULog.py"""
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
     TEST_LULog.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import traceback
import logging
import argparse

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
# import lyrpy.LULog as LULog

from lyrpy.LUDoc import *
import lyrpy.LUos as LUos
import lyrpy.LUFile as LUFile
import lyrpy.LUDateTime as LUDateTime

from lyrpy.LUParserARG import GArgParser
from lyrpy.LUParserINI import GINIFile

def TEST_LULog ():
    """ TEST_LULog """
#beginfunction
    PrintInfoObject('---------TEST_LULog----------')
    PrintInfoObject(TEST_LULog)
    PrintInfoObject(LULog)
#endfunction

def TEST_GetLogFileName ():
    """TEST_GetLogFileName"""
#beginfunction
    PrintInfoObject('---------TEST_GetLogFileName----------')
    PrintInfoObject(TEST_GetLogFileName)

    s = LULog.GetLogFileName()
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetLogFileNameSufix ():
    """TEST_GetLogFileNameSufix"""
#beginfunction
    PrintInfoObject('---------TEST_GetLogFileNameSufix----------')
    PrintInfoObject(TEST_GetLogFileNameSufix)

    s = LULog.GetLogFileNameSufix('sufix')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_Log_KIX ():
    """TEST_Log_KIX"""
#beginfunction
    PrintInfoObject('---------TEST_Log_KIX----------')
    PrintInfoObject(TEST_Log_KIX)

    #------------------------------------------------------
    # $LogDir, $Log, $LogFile
    #------------------------------------------------------
    """
    LLog = 2    # консоль
    LLog = 1    # файл
    LLog = 10   # файл (при первом обращении будет удален)
    LLog = 3    # файл + консоль
    LLog = 30   # файл (при первом обращении будет удален) + консоль
    """
    LLog = 30
    LLog = 3
    LLogDir: str = 'LOG'
    LLogDir = LUFile.ExpandFileName(LLogDir)
    LLogFile: str = ''
    if not LUFile.DirectoryExists(LLogDir):
        LUFile.ForceDirectories(LLogDir)
    #endif
    LLogFile = LULog.LogFileName (LLog, LLogDir, LLogFile)
    s = f'{LLog} {LLogDir} {LLogFile}'
    # LULog.LogAdd(LLog, LLogFile, 'I', s)

    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsNOTSET, '---- " " Это tlsNOTSET ---------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsDEBUG, '---- "D" Это tlsDebug ------------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsINFO, '---- Это информация ---------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsWARNING, '---- "W" Это tlsWarning -------------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsERROR, '---- Это ОШИБКА -------------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsCRITICAL, '---- "C" Это tlsCritical ------------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsBEGIN, '---- ">" Это tlsBegin ---------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsEND, '---- "<" Это tlsEnd ---------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsPROCESS, '---- Это процесс ------------')
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsTEXT, '---- "" Это tlsText ------------')

    # LFileName = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\TEST_LUsys.py'
    LFileName = 'TEST_LUSupport.py'
    LFileName = 'TEST_LUsys.py'
    LULog.LogAdd(LLog, LLogFile, LULog.TTypeLogString.tlsINFO, LFileName)
    LULog.LogAddFile (LLog, LLogFile, LULog.TTypeLogString.tlsTEXT, LFileName)
#endfunction

def TEST_Log_LU ():
    """TEST_Log_LU"""
#beginfunction
    PrintInfoObject('---------TEST_Log_LU----------')
    PrintInfoObject(TEST_Log_LU)

    # -------------------------------
    # Журнал
    # -------------------------------
    # LAPPLog: LULog.TFileMemoLog = LULog.TFileMemoLog ()
    LULog.FileMemoLog.Name = 'TEST_Log_LU'
    LULog.FileMemoLog.MemoLog = None
    LULog.FileMemoLog.TruncateDays = LULog.TruncLog
    LLogDir = LUFile.IncludeTrailingBackslash (LUos.APPWorkDir()) + 'LOG'
    LLogDir = LUFile.GetDirNameYYMM (LLogDir, LUDateTime.Now())
    LLogDir = LUFile.ExpandFileName (LLogDir)
    LProjectName = 'TEST_Log_LU'

    LULog.FileMemoLog.FileName = LUFile.IncludeTrailingBackslash (LLogDir) + LProjectName + '_' + LULog.GetLogFileName()

    s = f'{LLogDir}'
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsTEXT, s)
    s = f'{LULog.FileMemoLog.FileName}'
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsTEXT, s)

    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsNOTSET, '---- " " Это tlsNOTSET ---------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsDEBUG, '---- "D" Это tlsDebug ------------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsINFO, '---- "I" Это tlsInfo ---------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsWARNING, '---- "W" Это tlsWarning -------------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsERROR, '---- "E" Это tlsError -------------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsCRITICAL, '---- "C" Это tlsCritical ------------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsBEGIN, '---- ">" Это tlsBegin ---------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsEND, '---- "<" Это tlsEnd ---------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsPROCESS, '---- "P" Это tlsProcess ------------')
    LULog.FileMemoLog.AddLog (LULog.TTypeLogString.tlsTEXT, '---- "" Это tlsText ------------')

    LULog.FileMemoLog.AddLogFile ('logging.ini')
#endfunction

def TEST_PrintLogger (ALogger):
    """TEST_PrintLogger"""
#beginfunction
    PrintInfoObject('---------TEST_PrintLogger----------')
    PrintInfoObject(TEST_PrintLogger)

    # When set on a logger, indicates that ancestor loggers are to be consulted to determine the effective level. If that still resolves to NOTSET, then all events are logged. When set on a handler, all events are handled.
    # logging.NOTSET 0
    # Detailed information, typically only of interest to a developer trying to diagnose a problem.
    # logging.DEBUG 10
    # Confirmation that things are working as expected.
    # logging.INFO 20
    # An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected.
    # logging.WARNING 30
    # Due to a more serious problem, the software has not been able to perform some function.
    # logging.ERROR 40
    # A serious error, indicating that the program itself may be unable to continue running.
    # logging.CRITICAL 50

    # LULog.LoggerTOOLS.level = logging.NOTSET
    # LULog.LoggerTOOLS.level = logging.DEBUG
    # LULog.LoggerTOOLS.level = logging.INFO
    # LULog.LoggerTOOLS.level = logging.WARNING
    # LULog.LoggerTOOLS.level = logging.ERROR
    # LULog.LoggerTOOLS.level = logging.CRITICAL
    # LULog.LoggerTOOLS.level = logging.FATAL

    # LULog.LoggerTOOLS.level = logging.INFO
    # LULog.LoggerTOOLS.setLevel (logging.INFO)

    LULog.LoggerTOOLS.debug ('DEBUG.')
    LULog.LoggerTOOLS.info ('INFO.')
    LULog.LoggerTOOLS.warning ('WARNING.')
    LULog.LoggerTOOLS.error ('ERROR.')
    LULog.LoggerTOOLS.critical ('CRITICAL.')
    LULog.LoggerTOOLS.fatal ('FATAL.')
    LULog.LoggerTOOLS.log (logging.WARNING, 'WARNING.')

    
    s = f'Logger={ALogger}'
    ALogger.info (s)
    s = f'Logger.name={ALogger.name}'
    ALogger.info (s)

    ALogger.debug ('DEBUG message. Русский')
    ALogger.info ('INFO message')

    # ?????????????????????????????????????
    # ALogger.info ('INFO message', UserWarning)

    # ?????????????????????????????????????
    # LUserField = "LUserField"
    # ALogger.info ('INFO message', extra={"LUserField=":LUserField})

    ALogger.warning ('WARNING message')
    ALogger.error ('ERROR message')
    # ALogger.exception ('exception')
    ALogger.critical ('CRITICAL message')
    ALogger.log (LULog.DEBUGTEXT,'DEBUGTEXT message')
    ALogger.log (LULog.BEGIN,'BEGIN message')
    ALogger.log (LULog.END,'END message')
    ALogger.log (LULog.PROCESS,'PROCESS message')
    ALogger.log (LULog.TEXT,'TEXT message')

    # ------------------------------------------------
    # exception
    # ------------------------------------------------
    try:
        1 / 0
    except:
        ALogger.exception ('exception = 1 / 0')
        # logging.exception ('exception = 1 / 0')

    # ------------------------------------------------
    # error
    # Логирование исключений
    # -------------------------------
    # Чтобы logging.error перехватывала трассировку, установите sys.exc_info в True
    # ------------------------------------------------
    # ------------------------------------------------
    # Перехват необработанных исключений
    # -------------------------------
    # Вы не можете предвидеть и обработать все исключения, но можете логировать необработанные исключения,
    # чтобы исследовать их позже.
    # Необработанное исключение возникает вне try...except или, когда вы не включаете нужный тип исключения в except.
    # Например, если приложение обнаруживает TypeError, а ваш except обрабатывает только NameError,
    # исключение передаётся в другие try, пока не встретит нужный тип.
    # Если ничего не встретилось, исключение становится необработанным.
    # Интерпретатор вызывает sys.excepthook с тремя аргументами:
    # класс исключения, его экземпляр и трассировка. Эта информация обычно появляется в sys.stderr,
    # но если вы настроили свой лог для вывода в файл, traceback не логируется.
    # ------------------------------------------------
    try:
        1 / 0
    except OSError as e:
        # ALogger.error (e)
        ALogger.error (e, exc_info = True)
        ...
    except:
        ALogger.error ("необработанное exception: %s", traceback.format_exc ())
        ...
    # exception
    try:
        1 / 0
    except Exception as e:
        ALogger.error ("Exception occurred", exc_info = True)

    # ------------------------------------------------
    # Using LogRecord.getMessage()
    # ------------------------------------------------
    PrintInfoObject('-----------------Using LogRecord.getMessage()------------------------')
    # Create LogRecord object
    Llogrec = logging.LogRecord ('Mylogger', 10, '/home/fahmida/python/example2.py', 4,
                                'Python Logging Tutorial', (), None)
    #Call getMessage() to print message
    ALogger.info (Llogrec.getMessage ())

    # ------------------------------------------------
    # Using LogRecord attributes — args
    # ------------------------------------------------
    PrintInfoObject('------------------Using LogRecord attributes — args------------------')
    #Create custom log record
    #(self, name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None, **kwargs):
    logRecord = logging.LogRecord ('MyNewLog', 30, 'python/code/example1.py', 6,
                                   'Python Logging Tutorial', tuple(['test']), None)
    ALogger.info (logRecord.args)

    # ------------------------------------------------
    # Using logging.disable
    # ------------------------------------------------
    PrintInfoObject ('------------------Using logging.disable------------------')
    logging.disable (logging.DEBUG)

    # ------------------------------------------------
    # Using Adapter
    # ------------------------------------------------
    PrintInfoObject ('------------------Using Adapter------------------')
    # Новый атрибут с фиксированным значением
    LLogger = logging.LoggerAdapter (ALogger, {"app": "тестовое приложение"})
    LLogger.info ("Программа стартует")
    LLogger.info ("Программа завершила работу")

    # Новый атрибут с динамическим значением
    LLogger = LULog.TAdapter (logger = ALogger, extra = {"id": None})
    LLogger.info ('ID предоставлен', id = '1234')
    LLogger.info ('ID предоставлен', id = '5678')
    LLogger.info ('Отсутствует информация об ID')

    # ----------------------------------------------
    #2. Создавайте определенные пользователем атрибуты объектов класса LogRecord, используя класс Filter
    # ----------------------------------------------
    PrintInfoObject ('------------------Using Filter------------------')
    ALogger.addFilter (LULog.TFilter (name = 'Filter'))
    ALogger.debug ("сообщение для отладки, цвет — зеленый")
    ALogger.info ("информационное сообщение, цвет — зеленый")
    ALogger.warning ("предупреждающее сообщение, цвет — желтый")
    ALogger.error ("сообщение об ошибке, цвет — красный")
    ALogger.critical ("сообщение о критической ошибке, цвет — красный")

    # ----------------------------------------------
    # ALogger.isEnabledFor
    # ----------------------------------------------
    ALogger.info ('logging.NOTSET='+str(ALogger.isEnabledFor (logging.NOTSET)))
    ALogger.info ('logging.DEBUG='+str(ALogger.isEnabledFor (logging.DEBUG)))
    ALogger.info ('logging.INFO='+str(ALogger.isEnabledFor (logging.INFO)))
    ALogger.info ('logging.WARNING='+str(ALogger.isEnabledFor (logging.WARNING)))
    ALogger.info ('logging.ERROR='+str(ALogger.isEnabledFor (logging.ERROR)))
    ALogger.info ('logging.CRITICAL='+str(ALogger.isEnabledFor (logging.CRITICAL)))

    ALogger.info ('LULog.DEBUGTEXT='+str(ALogger.isEnabledFor (LULog.DEBUGTEXT)))
    ALogger.info ('LULog.BEGIN='+str(ALogger.isEnabledFor (LULog.BEGIN)))
    ALogger.info ('LULog.END='+str(ALogger.isEnabledFor (LULog.END)))
    ALogger.info ('LULog.PROCESS='+str(ALogger.isEnabledFor (LULog.PROCESS)))
    ALogger.info ('LULog.TEXT='+str(ALogger.isEnabledFor (LULog.TEXT)))
#endfunction

def TEST_Log_TLogger ():
    """TEST_Log_TLogger"""
#beginfunction
    PrintInfoObject('---------TEST_Log_TLogger----------')
    PrintInfoObject(TEST_Log_TLogger)

    # -------------------------------
    # Журнал
    # -------------------------------
    # LEVEL
    LULog.LoggerTLogger.debug (str(logging.DEBUG)+'-'+logging.getLevelName (logging.DEBUG))
    LULog.LoggerTLogger.info (str(logging.INFO)+'-'+logging.getLevelName (logging.INFO))
    LULog.LoggerTLogger.warning (str(logging.WARNING)+'-'+logging.getLevelName (logging.WARNING))
    LULog.LoggerTLogger.error (str(logging.ERROR)+'-'+logging.getLevelName (logging.ERROR))
    LULog.LoggerTLogger.critical (str(logging.CRITICAL)+'-'+logging.getLevelName (logging.CRITICAL))

    LULog.LoggerTLogger.log (LULog.DEBUGTEXT,str(LULog.DEBUGTEXT)+'-'+logging.getLevelName (LULog.DEBUGTEXT))
    LULog.LoggerTLogger.log (LULog.BEGIN,str(LULog.BEGIN)+'-'+logging.getLevelName (LULog.BEGIN))
    LULog.LoggerTLogger.log (LULog.END,str(LULog.END)+'-'+logging.getLevelName (LULog.END))
    LULog.LoggerTLogger.log (LULog.PROCESS,str(LULog.PROCESS)+'-'+logging.getLevelName (LULog.PROCESS))
    LULog.LoggerTLogger.log (LULog.TEXT,str(LULog.TEXT)+'-'+logging.getLevelName (LULog.TEXT))

    # УСТАНОВИТЬ LEVEL для GLogger
    s = 'GLogger.level=', LULog.LoggerTLogger.level
    LULog.LoggerTLogger.info (s)

    # LULog.LoggerTLogger.setLevel(logging.NOTSET)
    # s = 'LULog.LoggerTLogger.level=', GLogger.level
    # LULog.LoggerTLogger.setLevel(logging.NOTSET)

    # FILE
    PrintInfoObject('=========FILE===========================')
    LLogDir = LUFile.IncludeTrailingBackslash (LUos.APPWorkDir()) + 'LOG'
    LLogDir = LUFile.GetDirNameYYMM (LLogDir, LUDateTime.Now())
    LLogDir = LUFile.ExpandFileName (LLogDir)
    
    s = f'LogDir={LLogDir}'
    LULog.LoggerTLogger.log (LULog.TEXT, s)
    
    LProjectName = 'TEST_Log_logging'
    LFileName = LUFile.IncludeTrailingBackslash (LLogDir) + LProjectName + '_' + LULog.GetLogFileName()
    LULog.LoggerTLogger.AddHandlerFILE(LFileName, logging.DEBUG)
    LULog.LoggerTLogger.debug ('GLogger.AddHandlerFILE(LFileName, logging.DEBUG)')
    PrintInfoObject('========================================')

    # # FILE JSON
    # print ('=========FILE===========================')
    # LLogDir = IncludeTrailingBackslash (APPWorkDir()) + 'LOG'
    # LLogDir = GetDirNameYYMM (LLogDir, Now())
    # LLogDir = ExpandFileName (LLogDir)
    # print (f'LogDir={LLogDir}')
    # LProjectName = 'TEST_Log_logging_JSON'
    # LFileName = IncludeTrailingBackslash (LLogDir) + LProjectName + '_' + LULog.GetLogFileName()
    # LULog.LoggerTLogger.AddHandlerFILE_JSON(LFileName, logging.DEBUG)
    # print ('========================================')
    # TEST_PrintLogger (LULog.LoggerTLogger)

    # GLogger.handlers
    LULog.LoggerTLogger.log (LULog.TEXT, LULog.LoggerTLogger.handlers)
    for item in LULog.LoggerTLogger.handlers:
        LULog.LoggerTLogger.log (LULog.TEXT, item.name)
        LULog.LoggerTLogger.log (LULog.TEXT, type (item))
        LULog.LoggerTLogger.log (LULog.TEXT, item.level)
        LULog.LoggerTLogger.log (LULog.TEXT, type (item.formatter))
        LULog.LoggerTLogger.log (LULog.TEXT, item.formatter.__str__ ())
    #enfor

    TEST_PrintLogger (LULog.LoggerTLogger)
#endfunction

def TEST_Log_LoggerCONFIG ():
    """TEST_Log_LoggerCONFIG"""
#beginfunction
    PrintInfoObject('---------TEST_Log_LoggerCONFIG----------')
    PrintInfoObject(TEST_Log_LoggerCONFIG)

    # list_dict (LOGGING_CONFIG)
    def TEST_Log_LoggerCONFIG_root ():
        """TEST_Log_LoggerCONFIG_root"""
    #beginfunction
        LLogger = LULog.CreateLoggerCONFIG (LULog.CDefaultFileLogCONFIG, 'root',
                                            'LOG', 'LOGGING_CONFIG.log',
                                            'LOGGING_FILEINI_json.log')

        if not LLogger is None:
            TEST_PrintLogger (LLogger)
    #endfunction

    def TEST_Log_LoggerCONFIG_log02 ():
        """TEST_Log_LoggerCONFIG_log02"""
    #beginfunction
        LLogger = LULog.CreateLoggerCONFIG (LULog.CDefaultFileLogCONFIG, 'log02',
                                            'LOG', 'LOGGING_CONFIG.log',
                                            'LOGGING_FILEINI_json.log'
                                            )
        if not LLogger is None:
            TEST_PrintLogger (LLogger)
    #endfunction

    TEST_Log_LoggerCONFIG_root ()
    TEST_Log_LoggerCONFIG_log02 ()
#endfunction

def TEST_Log_LoggerFILEINI_01 ():
    """TEST_Log_LoggerFILEINI_01"""
#beginfunction
    PrintInfoObject('---------TEST_Log_LoggerFILEINI_01----------')
    PrintInfoObject(TEST_Log_LoggerFILEINI_01)

    def TEST_Log_LoggerFILEINI_root ():
        """TEST_Log_LoggerFILEINI_01_root"""
    #beginfunction
        LLogger = LULog.CreateLoggerFILEINI (LULog.CDefaultFileLogINI, 'root',
                                             'LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')
        if not LLogger is None:
            TEST_PrintLogger (LLogger)
    #endfunction

    def TEST_Log_LoggerFILEINI_log02 ():
        """TEST_Log_LoggerFILEINI_01_log02"""
    #beginfunction
        LLogger = LULog.CreateLoggerFILEINI (LULog.CDefaultFileLogINI, 'log02',
                                             'LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')
        if not LLogger is None:
            TEST_PrintLogger (LLogger)
    #endfunction


    TEST_Log_LoggerFILEINI_root ()
    TEST_Log_LoggerFILEINI_log02 ()

#endfunction

def TEST_Log_LoggerFILEINI_02 ():
    """TEST_Log_LoggerFILEINI_02"""
#beginfunction
    PrintInfoObject('---------TEST_Log_LoggerFILEINI_02----------')
    PrintInfoObject(TEST_Log_LoggerFILEINI_02)

    if not LULog.LoggerTOOLS is None:
       TEST_PrintLogger (LULog.LoggerTOOLS)
    #endif

    if not LULog.LoggerAPPS is None:
       TEST_PrintLogger (LULog.LoggerAPPS)
    #endif
#endfunction

def TEST_Log_LoggerBASIC ():
    """TEST_Log_LoggerBASIC"""
#beginfunction
    PrintInfoObject('---------TEST_Log_LoggerBASIC----------')
    PrintInfoObject(TEST_Log_LoggerBASIC)

    LLogger = LULog.CreateLoggerBASIC (logging.DEBUG, 'LOG\\'+LULog.CDefaultFileLogFILEBASIC, 'root')
    if not LLogger is None:
        TEST_PrintLogger (LLogger)
#endfunction
class C (argparse.Namespace):
    pass
#endclass
def __GetARGS ():
    """__GetARGS"""
#beginfunction
    LArgs = {
        'LD': {'name': '-ld', 'dest': 'ld', 'type': str, 'default': '',
               'help': 'log dir', 'action': 'store'},
        'LF': {'name': '-lf', 'dest': 'lf', 'type': str, 'default': '',
               'help': 'log FILE', 'action': 'store'},
        'LFJ': {'name': '-lfj', 'dest': 'lfj', 'type': str, 'default': '',
                'help': 'log FILE_JSON', 'action': 'store'},
        'INI': {'name': '-ini', 'dest': 'ini', 'type': str, 'default': '',
                'help': 'log INI', 'action': 'store'}
    }
    # print (LArgs['LD']['name'])
    # print (LArgs ['LD'] ['dest'])
    # print (LArgs['LD']['type'])
    # for name, value in LArgs.items():
    #     print (f"{name}={value}")
    #     for name1, value1 in value.items ():
    #         print (f"{name1}={value1}")

    if not GArgParser is None:
        GArgParser.Clear()
        GArgParser.ArgParser.description = GArgParser.ArgParser.description+' '+'TEST_LULog.py'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, GArgParser.ArgParser.description)
        if GArgParser.Args is None:
            GArgParser.ReadARGS (LArgs)
            # print (GArgParser.Args)
            # print (GArgParser.ArgsUnknown)

            # print (f'ld = {GArgParser.Args.ld}')
            # print (f'lf = {GArgParser.Args.lf}')
            # print (f'lfj = {GArgParser.Args.lfj}')
            # print (f'ini = {GArgParser.Args.ini}')

            # print (f'ld = {GArgParser.ArgsDICT["ld"]}')
            # print (f'lf = {GArgParser.ArgsDICT["lf"]}')
            # print (f'lfj = {GArgParser.ArgsDICT["lfj"]}')
            # print (f'ini = {GArgParser.ArgsDICT["ini"]}')
        else:
            LULog.LoggerAPPS_AddLevel (GArgParser.Args)
        #endif
    #endif
#endfunction

def __GetINI ():
    """__GetINI"""
#beginfunction
    if not GArgParser is None:
        # from ArgParser
        if len(GArgParser.Args.lf) == 0:
            LLogFile = 'LOGGING_FILEINI.log'
        else:
            LLogFile = GArgParser.Args.lf
        #endif
        # LLogFile = LUFile.ExpandFileName(LLogFile)

        if len(GArgParser.Args.ini) == 0:
            GINIFile.FileNameINI = 'logging.ini'
        else:
            GINIFile.FileNameINI = GArgParser.Args.ini
        #endif
        # set LogFile
        GINIFile.SetOption ('handler_FILE_01', 'args', "('" + LLogFile + "',)")


    else:
        # from INIFile
        GINIFile.FileNameINI = 'logging.ini'
        LOptionValue = GINIFile.GetOption ('handler_FILE_01', 'args', '')
        LLogFile = LOptionValue.split ("'") [1]
        # LFileLog = LUFile.ExpandFileName(LFileLog)
        GINIFile.SetOption ('handler_FILE_01', 'args', "('" + LLogFile + "',)")
    #endif
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LLogFile)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\LOGS',
                        'TEST_LULog.log',
                        'TEST_LULog_json.log')

    TEST_LULog ()

    TEST_GetLogFileName ()
    TEST_GetLogFileNameSufix ()

    TEST_Log_KIX ()

    TEST_Log_LU ()

    TEST_Log_TLogger ()

    TEST_Log_LoggerCONFIG ()

    if LUos.GOSInfo.system == 'Windows':
        TEST_Log_LoggerFILEINI_01 ()
        TEST_Log_LoggerFILEINI_02 ()
    #endif

    TEST_Log_LoggerBASIC ()
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    # __GetARGS ()
    # __GetINI ()

    main()
#endif

#endmodule
