"""TEST_LUParserREG.py"""
# -*- coding: UTF-8 -*-
__annotations__ ="""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_LUParserREG.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys
import platform

if platform.system() == 'Windows':
    from winreg import *
#endif

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
from lyrpy.LUDoc import *
import lyrpy.LUos as LUos

if platform.system() == 'Windows':
    import lyrpy.LUParserREG as LUParserREG
#endif

def TEST_LUParserREG ():
    """TEST_LUParserREG"""
#beginfunction
    PrintInfoObject('---------TEST_LUParserREG----------')
    PrintInfoObject(TEST_LUParserREG)
    PrintInfoObject(LUParserREG)
#endfunction

def TEST_TREGParser ():
    """TEST_TREGParser"""
#beginfunction
    PrintInfoObject('---------TEST_TREGParser----------')
    PrintInfoObject(TEST_TREGParser)
    PrintInfoObject(LUParserREG.TREGParser)

    LTREGParser = LUParserREG.TREGParser()

    #------------------------------
    # GetKeyReg
    #------------------------------
    LKeyName = 'Fonts'
    LValue, LType = LTREGParser.GetKeyReg(LUParserREG.THKEYConst.cHKCU,
                        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',
                        LKeyName)
    s = f'{LValue}, {LType}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LDefault = LTREGParser.GetKeyReg(LUParserREG.THKEYConst.cHKCU,
                        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', '')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LDefault)
    #------------------------------
    # QueryInfoKeyReg
    #------------------------------
    LInfo = LTREGParser.QueryInfoKeyReg(LUParserREG.THKEYConst.cHKCU,
                        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LInfo)
    #------------------------------
    # EnumKeyReg
    #------------------------------
    LListKey = LTREGParser.EnumKeyReg(LUParserREG.THKEYConst.cHKCU,
                        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LListKey)
    #------------------------------
    # GetOptionsReg
    #------------------------------
    LSection = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    LListKey = LTREGParser.GetOptionsReg(LUParserREG.THKEYConst.cHKCU, LSection)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LListKey)
    #------------------------------
    # EnumValueReg
    #------------------------------
    LSection = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    LListKeyValue = LTREGParser.EnumValueReg(LUParserREG.THKEYConst.cHKCU, LSection)
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, LListKeyValue)
    #------------------------------
    # IsSection
    #------------------------------
    LSection = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    LResult = LTREGParser.IsSection(LUParserREG.THKEYConst.cHKCU, LSection)
    s = f'{LResult} - {LSection}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    #------------------------------
    # IsOption
    #------------------------------
    LSection = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders!'
    LOption = 'Fonts'
    LOption = 'My Music'
    LResult = LTREGParser.IsOption(LUParserREG.THKEYConst.cHKCU, LSection, LOption)
    s = f'{LSection}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = f'{LResult} - {LOption}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    #------------------------------
    LSystemAPP = 'TEST_LU'
    cSOFTWARE = 'SOFTWARE'
    #LUParserREG.THKEYConst.cHKCU
    rkSoftware = cSOFTWARE + '\\' + LSystemAPP
    rkSoftware = r'SOFTWARE\TEST_LU'
    LOption_TEST_EXPAND_SZ = 'TEST_EXPAND_SZ'
    LValue_TEST_EXPAND_SZ = 'TEST_EXPAND_SZ'
    LOption_TEST_DWORD = 'TEST_DWORD'
    LValue_TEST_DWORD = 1000
    LFileName = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\TEST_LU\SOFTWARE'
    #------------------------------
    # CreateKeyReg
    #------------------------------
    LTREGParser.CreateKeyReg (LUParserREG.THKEYConst.cHKCU, rkSoftware)
    #------------------------------
    # SetKeyReg
    #------------------------------
    LTREGParser.SetValueReg (LUParserREG.THKEYConst.cHKCU, rkSoftware,
                            LOption_TEST_EXPAND_SZ, LUParserREG.TValueTypes.vtEXPAND_SZ, LValue_TEST_EXPAND_SZ)
    #------------------------------
    # SaveKeyReg
    #------------------------------
    # LTREGParser.SaveKeyReg (LUParserREG.THKEYConst.cHKCU, rkSoftware, LFileName)
    #------------------------------
    # LoadKeyReg
    #------------------------------
    # LTREGParser.LoadKeyReg (LUParserREG.THKEYConst.cHKCU, rkSoftware, LFileName)
    #------------------------------
    # DeleteValueReg
    #------------------------------
    # LTREGParser.DeleteValueReg (LUParserREG.THKEYConst.cHKCU, rkSoftware, LOption_TEST_EXPAND_SZ)
    #------------------------------
    # DeleteValueReg
    #------------------------------
    # LTREGParser.DeleteKeyReg (LUParserREG.THKEYConst.cHKCU, rkSoftware)

    del LTREGParser
#endfunction

def TEST_Regedit ():
    """TEST_Regedit"""
#beginfunction
    PrintInfoObject('---------TEST_Regedit----------')
    PrintInfoObject(TEST_Regedit)

    LFileName = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\TEST_LU\SOFTWARE.reg'
    LFileName = 'SOFTWARE.reg'
    LSection = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    LUParserREG.SaveRegToFile_regedit (LFileName, LUParserREG.THKEYConst.cHKCU, LSection)
#endfunction

#--------------------------------------------------------------------------------
# TEST_GetFolderCU()
#--------------------------------------------------------------------------------
def TEST_GetFolderCU():
    """TEST_GetFolderCU"""
#beginfunction
    PrintInfoObject('---------TEST_GetFolderCU----------')
    PrintInfoObject(TEST_GetFolderCU)
    PrintInfoObject(LUParserREG.TREGParser)
    LKeyName = 'Fonts'
    with OpenKey (HKEY_CURRENT_USER,
                         r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',
                         0, KEY_ALL_ACCESS) as LKey:
        LValue, LType = QueryValueEx (LKey, LKeyName)
        s = f'{LValue}, {LType}'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

        LDefault = QueryValue (LKey, None)
        s = F'Default=,{LDefault}'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

        # l = EnumKey(LKey, 0)
        # LWork = QueryInfoKey (LKey)
        # print (LWork)
        # for i in range (LWork[0],LWork[1]):
        #     LKeyName, LValue, item3 = EnumValue (LKey, i)
        #     print (LKeyName, LValue, item3)
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_LUParserREG ()
    TEST_TREGParser ()
    TEST_GetFolderCU()
    TEST_Regedit ()
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    if platform.system() == 'Windows':
    #if LUos.GOSInfo.system == 'Windows':
        print("win32")
        main ()
    #endif

#endif

#endmodule

