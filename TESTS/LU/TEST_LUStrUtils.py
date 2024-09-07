"""TEST_LUStrUtils.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023 19.07
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_LUStrUtils.py

 =======================================================
"""
#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys
import logging

import string
import locale
import re
# from curses.ascii import isprint
import itertools


#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
from lyrpy.LUDoc import *
import lyrpy.LUStrUtils as LUStrUtils

def TEST_LUStrUtils ():
    """TEST_LUStrUtils"""
#beginfunction
    PrintInfoObject('---------TEST_LUStrUtils----------')
    PrintInfoObject(TEST_LUStrUtils)
    PrintInfoObject(LUStrUtils)
    ...
#endfunction

#--------------------------------------------------------------------
#ExtractWord (i, String, Delimiter):
#--------------------------------------------------------------------
def TEST_ExtractWord ():
    """TEST_ExtractWord"""
#beginfunction
    PrintInfoObject('---------TEST_ExtractWord----------')
    PrintInfoObject(TEST_ExtractWord)

    s = 'один,два,три'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.ExtractWord (2, s, ',')
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#--------------------------------------------------------------------
# WordCount (String, Delimiter):
#--------------------------------------------------------------------
def TEST_WordCount ():
    """TEST_WordCount"""
#beginfunction
    PrintInfoObject('---------TEST_WordCount----------')
    PrintInfoObject(TEST_WordCount)

    s = 'один,два,три'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    Num = LUStrUtils.WordCount (s, ',')
    s = f'Num={Num}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#--------------------------------------------------------------------
#ExistWord (String, Delimiter, Word):
#--------------------------------------------------------------------
def TEST_ExistWord ():
    """TEST_ExistWord"""
#beginfunction
    PrintInfoObject('---------TEST_ExistWord----------')
    PrintInfoObject(TEST_ExistWord)

    s = 'один,два,три'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    Bool = LUStrUtils.ExistWord (s, ',', 'два')
    s = F'Bool={Bool}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#--------------------------------------------------------------------
#AddChar (Pad, Input, Length):
#--------------------------------------------------------------------
def TEST_AddChar ():
    """TEST_AddChar"""
#beginfunction
    PrintInfoObject('---------TEST_AddChar----------')
    PrintInfoObject(TEST_AddChar)

    s = 'Input'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    s = LUStrUtils.AddChar ('.', s, 20)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    s = '11'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    s = LUStrUtils.AddChar ('0', s, 3)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#--------------------------------------------------------------------
# AddCharR (Pad, Input, Length):
#--------------------------------------------------------------------
def TEST_AddCharR ():
    """TEST_AddCharR"""
#beginfunction
    PrintInfoObject('---------TEST_AddCharR----------')
    PrintInfoObject(TEST_AddCharR)

    s = 'Input'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.AddCharR ('.', s, 20)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_Trim ():
    """TEST_Trim"""
#beginfunction
    PrintInfoObject('---------TEST_Trim----------')
    PrintInfoObject(TEST_Trim)

    s = '    Input    '
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.Trim (s)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_TrimL ():
    """TEST_TrimL"""
#beginfunction
    PrintInfoObject('---------TEST_TrimL----------')
    PrintInfoObject(TEST_TrimL)

    s = '    Input    '
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.TrimL (s)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_TrimR ():
    """TEST_TrimR"""
#beginfunction
    PrintInfoObject('---------TEST_TrimR----------')
    PrintInfoObject(TEST_TrimR)

    s = '    Input    '
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.TrimR (s)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_TrimChar ():
    """TEST_TrimChar"""
#beginfunction
    PrintInfoObject('---------TEST_TrimChar----------')
    PrintInfoObject(TEST_TrimChar)

    s = '....Input....'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.TrimChar (s, '.')
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_TrimCharL ():
    """TEST_TrimCharL"""
#beginfunction
    PrintInfoObject('---------TEST_TrimCharL----------')
    PrintInfoObject(TEST_TrimCharL)

    s = '....Input....'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.TrimCharL (s, '.')
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_TrimCharR ():
    """TEST_TrimCharR"""
#beginfunction
    PrintInfoObject('---------TEST_TrimCharR----------')
    PrintInfoObject(TEST_TrimCharR)

    s = '....Input....'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.TrimCharR (s, '.')
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
# MakeStr return a string of length N filled with character C. }
#---------------------------------------------------------------
def TEST_MakeStr ():
    """TEST_MakeStr"""
#beginfunction
    PrintInfoObject('---------TEST_MakeStr----------')
    PrintInfoObject(TEST_MakeStr)

    s = LUStrUtils.MakeStr('.', 20)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_CharFromSet ():
    """TEST_CharFromSet"""
#beginfunction
    PrintInfoObject('---------TEST_CharFromSet----------')
    PrintInfoObject(TEST_CharFromSet)

    s = LUStrUtils.CharFromSet(LUStrUtils.cBrackets)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_GetParamFromString ():
    """TEST_GetParamFromString"""
#beginfunction
    PrintInfoObject('---------TEST_GetParamFromString----------')
    PrintInfoObject(TEST_GetParamFromString)

    s0 = "T:\b\files|T:\b\files||$SAVE|move,del|0"
    s = 'String IN='+s0
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    pPATHIN = 'PATHIN'
    pPATHOUT = 'PATHOUT'
    pPATHOUTMAIL = 'PATHOUTMAIL'
    pWILDCARDS = 'WILDCARDS'
    pOPERATIONS = 'OPERATIONS'
    pActive = 'ACTIVE'
    LParamNamePath = (pPATHIN, pPATHOUT, pPATHOUTMAIL, pWILDCARDS, pOPERATIONS, pActive)
    LParamNames = LParamNamePath

    LParamName = pPATHIN
    s = LUStrUtils.GetParamFromString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pPATHOUT
    s = LUStrUtils.GetParamFromString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pPATHOUTMAIL
    s = LUStrUtils.GetParamFromString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pWILDCARDS
    s = LUStrUtils.GetParamFromString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pOPERATIONS
    s = LUStrUtils.GetParamFromString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pActive
    s = LUStrUtils.GetParamFromString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_SetParamToString ():
    """TEST_SetParamToString"""
#beginfunction
    PrintInfoObject('---------TEST_SetParamToString----------')
    PrintInfoObject(TEST_SetParamToString)

    s0 = "T:\\b\\files|T:\\b\\files||$SAVE|move,del|0"
    s = 'String IN='+s0
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    pPATHIN = 'PATHIN'
    pPATHOUT = 'PATHOUT'
    pPATHOUTMAIL = 'PATHOUTMAIL'
    pWILDCARDS = 'WILDCARDS'
    pOPERATIONS = 'OPERATIONS'
    pActive = 'ACTIVE'
    LParamNamePath = (pPATHIN, pPATHOUT, pPATHOUTMAIL, pWILDCARDS, pOPERATIONS, pActive)
    LParamNames = LParamNamePath
    LValue = 'TEST'

    LParamName = pPATHIN
    s = LUStrUtils.SetParamToString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter, LValue)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pPATHOUT
    s = LUStrUtils.SetParamToString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter, LValue)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pPATHOUTMAIL
    s = LUStrUtils.SetParamToString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter, LValue)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pWILDCARDS
    s = LUStrUtils.SetParamToString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter, LValue)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pOPERATIONS
    s = LUStrUtils.SetParamToString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter, LValue)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    LParamName = pActive
    s = LUStrUtils.SetParamToString (LParamName, s0, LParamNames, LUStrUtils.cWordDelimiter, LValue)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
# DelChars return a string with all Chr characters removed
#---------------------------------------------------------------
def TEST_DelChars ():
    """TEST_DelChars"""
#beginfunction
    PrintInfoObject('---------TEST_DelChars----------')
    PrintInfoObject(TEST_DelChars)

    s0 = "T:\\b\\files|T:\\b\\files||$SAVE|move,del|0"
    s = 'String IN='+s0
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.DelChars(s0, '|')
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
# DelSpace return a string with all white spaces removed.
#---------------------------------------------------------------
def TEST_DelSpaces ():
    """TEST_DelSpaces"""
#beginfunction
    PrintInfoObject('---------TEST_DelSpaces----------')
    PrintInfoObject(TEST_DelSpaces)

    s = "T:\\b\\files||$SAVE|move,del|0"
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.DelSpaces(s)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
# DelSpace return a string with all white spaces removed.
#---------------------------------------------------------------
def TEST_ReplaceChars ():
    """TEST_ReplaceChars"""
#beginfunction
    PrintInfoObject('---------TEST_ReplaceChars----------')
    PrintInfoObject(TEST_ReplaceChars)

    s = 'TEST_ReplaceChars'
    s = 'String IN='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.ReplaceChars(s,'TEST','SUPER')
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_CenterStr ():
    """TEST_CenterStr"""
#beginfunction
    PrintInfoObject('---------TEST_CenterStr----------')
    PrintInfoObject(TEST_CenterStr)

    s0 = 'TEST_CenterStr'
    s = 'String IN='+s0
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.CenterStr('TEST_CenterStr',' ',len(s0)+20)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = LUStrUtils.CenterStr('TEST_CenterStr','-',len(s0)+20)
    s = 'String OUT='+s
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

#---------------------------------------------------------------
#
#---------------------------------------------------------------
def TEST_PrintableStr ():
    """TEST_PrintableStr"""
#beginfunction
    PrintInfoObject('---------TEST_PrintableStr----------')
    PrintInfoObject(TEST_CenterStr)

    print (string.printable)
    s = 'КАК СДЕЛАТЬ КРУТОЙ ПУСК НА WINDOWS 11 🌀'
    print (s)
    s = LUStrUtils.PrintableStr(s)
    print (s)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_LUStrUtils ()
    TEST_ExtractWord ()
    TEST_WordCount ()
    TEST_ExistWord ()
    TEST_AddChar ()
    TEST_AddCharR ()
    TEST_Trim ()
    TEST_TrimL ()
    TEST_TrimR ()
    TEST_TrimChar ()
    TEST_TrimCharL ()
    TEST_TrimCharR ()
    TEST_MakeStr ()
    TEST_CharFromSet ()
    TEST_GetParamFromString ()
    TEST_SetParamToString ()
    TEST_DelChars ()
    TEST_DelSpaces ()
    TEST_ReplaceChars ()
    TEST_CenterStr ()

    TEST_PrintableStr ()
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
