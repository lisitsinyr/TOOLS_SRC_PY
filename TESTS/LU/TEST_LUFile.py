"""TEST_LUFile.py"""
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
     TEST_LUFile.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import platform

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import datetime

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
import lyrpy.LUFile as LUFile
import lyrpy.LUos as LUos
import lyrpy.LUErrors as LUErrors
from lyrpy.LUDoc import *
if platform.system() == 'Windows':
    import lyrpy.LUParserREG as LUParserREG
#endif

def TEST_LUFile ():
    """TEST_LUFile"""
#beginfunction
    PrintInfoObject('---------TEST_LUFile----------')
    PrintInfoObject(TEST_LUFile)
    PrintInfoObject(LUFile)
#endfunction

def TEST_DirectoryExists ():
    """TEST_DirectoryExists"""
    LPath1 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU'
    LPath2 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_L'
    LPath3 = 'D:\\WORK'
#beginfunction
    PrintInfoObject('---------TEST_DirectoryExists----------')
    PrintInfoObject(TEST_DirectoryExists)

    b = LUFile.DirectoryExists (LPath1)
    s = f'Директория: {LPath1} {b}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    b = LUFile.DirectoryExists (LPath2)
    s = f'Директория: {LPath2} {b}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    b = LUFile.DirectoryExists (LPath3)
    s = f'Директория: {LPath3} {b}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_ForceDirectories ():
    """TEST_ForceDirectories"""
    LPath1 = r"D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\WORK"
#beginfunction
    PrintInfoObject('---------TEST_ForceDirectories----------')
    PrintInfoObject(TEST_ForceDirectories)

    LPath0 = LPath1 + '/1/1'
    LUFile.ForceDirectories (LPath0)
    b = LUFile.DirectoryExists (LPath0)
    s = f'Директория: {LPath0} {b}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetFileDateTime ():
    """TEST_GetFileDateTime"""
    LFileName = r"D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\WORK\LOGGING_FILEINI.log"
#beginfunction
    PrintInfoObject('---------TEST_GetFileDateTime----------')
    PrintInfoObject(TEST_GetFileDateTime)

    b = LUFile.FileExists (LFileName)
    s = f'Файл: {LFileName} {b}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LDateTime = LUFile.GetFileDateTime(LFileName)
    s = f'Файл: {LFileName} {LDateTime}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = f'Время последней записи: {LDateTime[0]} Время создания: {LDateTime[1]}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_WriteStrToFile ():
    """TEST_WriteStrToFile"""
    LStr = 'Тестовая строка'
    LFileName = r"D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\WORK\TEST.txt"
#beginfunction
    PrintInfoObject('---------TEST_WriteStrToFile----------')
    PrintInfoObject(TEST_WriteStrToFile)

    LUFile.WriteStrToFile (LStr, LFileName)
#endfunction

def TEST_Extract_Get ():
    """ TEST_Extract_Get """
    LFileName0 = "1\\1\\1.txt"
#beginfunction
    PrintInfoObject('---------TEST_Extract_Get----------')
    PrintInfoObject(TEST_Extract_Get)

    s = f'Файл: {LFileName0}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    s = LUFile.ExpandFileName (LFileName0)
    s = f'Файл: {s}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileDir = LUFile.ExtractFileDir (s)
    s = f'FileDir: {LFileDir}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileName = LUFile.ExtractFileName (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileName = LUFile.ExtractFileNameWithoutExt (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileExt = LUFile.ExtractFileExt (s)
    s = f'FileExt: {LFileExt}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileDir = LUFile.GetFileDir (s)
    s = f'FileDir: {LFileDir}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileName = LUFile.GetFileName (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)

    LFileExt = LUFile.GetFileExt (s)
    s = f'FileExt: {LFileExt}'

    LFileName = LUFile.GetFileNameWithoutExt (s)
    s = f'FileName: {LFileName}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetFileEncoding ():
    """TEST_GetFileEncoding"""
#beginfunction
    PrintInfoObject('---------TEST_GetFileEncoding----------')
    PrintInfoObject(TEST_GetFileEncoding)


    LFileName = r"D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\WORK\FAKE\FakeFile_1_1.txt"

    LEncoding = LUFile.GetFileEncoding (LFileName)
    if LEncoding == '':
        LEncoding = LUFile.cDefaultEncoding
    LFile = open (LFileName, 'r', encoding = LEncoding)
    for s in LFile:
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s[:-1])
    LFile.close()
#endfunction

def TEST_IncludeTrailingBackslash ():
    """TEST_IncludeTrailingBackslash"""
#beginfunction
    PrintInfoObject('---------TEST_IncludeTrailingBackslash----------')
    PrintInfoObject(TEST_IncludeTrailingBackslash)

    LPath1 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\'
    LPath2 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU'
    LPath11 = LUFile.IncludeTrailingBackslash(LPath1)
    LPath21 = LUFile.IncludeTrailingBackslash(LPath2)
    s = f'LPath11: {LPath11}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = f'LPath21: {LPath21}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetDirNameYYMMDD ():
    """TEST_GetDirNameYYMMDD"""
#beginfunction
    PrintInfoObject('---------TEST_GetDirNameYYMMDD----------')
    PrintInfoObject(TEST_GetDirNameYYMMDD)

    LPath1 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU\\'
    LPath2 = 'D:\\PROJECTS_LYR\\CHECK_LIST\\05_DESKTOP\\02_Python\\PROJECTS_PY\\TESTS_PY\\TEST_LU'
    LNow: datetime = datetime.datetime.now()
    LDirNameYYMMDD1: str = LUFile.GetDirNameYYMMDD(LPath1, LNow)
    LDirNameYYMMDD2: str = LUFile.GetDirNameYYMMDD(LPath2, LNow)
    s = f'LDirNameYYMMDD1: {LDirNameYYMMDD1}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s = f'LDirNameYYMMDD2: {LDirNameYYMMDD2}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetDirNameYYMM ():
    """TEST_GetDirNameYYMM"""
#beginfunction
    PrintInfoObject('---------TEST_GetDirNameYYMM----------')
    PrintInfoObject(TEST_GetDirNameYYMM)

    LPath1 = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\TEST_LU'
    LPath2 = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\TEST_LU'
    LNow: datetime = datetime.datetime.now()
    LDirNameYYMM1: str = LUFile.GetDirNameYYMM(LPath1, LNow)
    LDirNameYYMM2: str = LUFile.GetDirNameYYMM(LPath2, LNow)
    s = f'LDirNameYYMMDD1: {LDirNameYYMM1}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    s  = f'LDirNameYYMMDD2: {LDirNameYYMM2}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_GetTempDir ():
    """TEST_GetTempDir"""
#beginfunction
    PrintInfoObject('---------TEST_GetTempDir----------')
    PrintInfoObject(TEST_GetTempDir)

    LTempDir: str = LUFile.GetTempDir()
    s = f'LTempDir: {LTempDir}'
    LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
#endfunction

def TEST_SearchFile ():
    """TTEST_SearchFileExt"""
#beginfunction
    PrintInfoObject('---------TEST_SearchFile----------')
    PrintInfoObject(TEST_SearchFile)

    LDir = r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\WORK\FAKE'
    LFileName = 'FakeFile_1_2.txt'
    LMask = r'.*.txt'
    LMask = ''
    LExt = '.txt'
    LExt = ''

    LList = LUFile.__SearchFile(LDir, LFileName, LMask, LExt, False)
    for Litem in LList:
        s = f'FullFileName: {Litem}'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    #endif

#endfunction

def TEST_SearchFileDirs ():
    """TEST_SearchFileDirs"""
#beginfunction
    PrintInfoObject('---------TEST_SearchFileDirs----------')
    PrintInfoObject(TEST_SearchFileDirs)

    LpathVar = LUos.GetEnvVar('Path').split(';')
    # print (LpathVar)

    # #------------------------------
    # # GetKeyReg
    # #------------------------------
    # LSectionName = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    # LKeyName = 'Path'
    # # LValue, LType = LUParserREG.GREGParser.GetKeyReg (LUParserREG.THKEYConst.cHKLM, LSectionName, LKeyName)
    # # s = f'{LValue}, {LType}'
    # s = LUParserREG.GREGParser.GetKeyReg (LUParserREG.THKEYConst.cHKLM, LSectionName, LKeyName)
    # print(s)

    LpathVar = [r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\WORK\FAKE']

    LFileName = 'jdeprscan.exe'
    LFileName = ''

    LMask = r'.*.txt'
    LMask = ''

    LExt = '.txt'
    # LExt = '.exe'
    # LExt = ''

    LListDirs = LUFile.SearchFileDirs(LpathVar, LFileName, LMask, LExt, False)
    for Litem in LListDirs:
        s = f'FullFileName: {Litem}'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    #endif
#endfunction

def TEST_SearchINIFile ():
    """TEST_SearchINIFile"""
#beginfunction
    PrintInfoObject('---------TEST_SearchINIFile----------')
    PrintInfoObject(TEST_SearchINIFile)

    LpathVar = [r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY']
    LFileName = 'TEST_LU.ini'
    LMask = ''
    LExt = '.ini'

    LListDirs = LUFile.SearchFileDirs(LpathVar, LFileName, LMask, LExt, True)
    for Litem in LListDirs:
        s = f'FullFileName: {Litem}'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    #endif
#endfunction

def TEST_SearchEXEFile ():
    """TEST_SearchINIFile"""
#beginfunction
    PrintInfoObject('---------TEST_SearchEXEFile----------')
    PrintInfoObject(TEST_SearchEXEFile)

    LpathVar = [r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY']
    LFileName = 'python.exe'
    LMask = ''
    LExt = '.exe'

    LListDirs = LUFile.SearchFileDirs (LpathVar, LFileName, LMask, LExt, True)
    for Litem in LListDirs:
        s = f'FullFileName: {Litem}'
        LULog.LoggerAdd (LULog.LoggerAPPS, LULog.TEXT, s)
    #endif
#endfunction

#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,
                        r'D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TESTS_PY\LOG',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    # TEST_DirectoryExists ()
    # TEST_ForceDirectories ()
    # TEST_GetFileDateTime ()

    # try:
    #     TEST_WriteStrToFile ()
    # except LUErrors.LUFileError_FileERROR as ERROR:
    #     ERROR.Message = 'Тестовое сообщение'
    #     s = f'!!!! {ERROR}'
    #     LULog.LoggerAPPS_AddError(s)
    # else:
    #     ...
    # #endtry

    # TEST_Extract_Get ()
    # TEST_GetFileEncoding ()
    # TEST_IncludeTrailingBackslash ()

    TEST_GetDirNameYYMMDD ()
    TEST_GetDirNameYYMM ()

    # TEST_GetTempDir ()

    # TEST_SearchFile ()
    # TEST_SearchFileDirs ()

    # TEST_SearchINIFile ()
    # TEST_SearchEXEFile ()

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
