@echo off
rem -------------------------------------------------------------------
rem ScanFile.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

:begin
    set SCRIPTS_DIR=D:\PROJECTS_LYR\CHECK_LIST\SCRIPT\04_BAT\PROJECTS_BAT\TOOLS_BAT
    set LIB_BAT=%SCRIPTS_DIR%\LIB

    call :CurrentDir || exit /b 1
    rem  echo CurrentDir: %CurrentDir%

    rem set PDir_CAPTION=Ввод значения
    set PDir=%cd%
    call :Check_P Format %1 || exit /b 1
    rem echo Format: %Format%    

    rem set PMask_CAPTION=Ввод значения
    set PMask=*.*
    call :Check_P PMask %2 || exit /b 1
    rem echo P2: %P2%    

    if "%Format%"=="" (
        echo ERROR: Параметр Format не задан...
        echo Использование: ListDir2.bat [Format] [NLevel]
    ) else (
        call :MAIN_FUNC
    )

:Exit
exit /b 0

rem --------------------------------------------------------------------------------
rem procedure MAIN_FUNC ()
rem --------------------------------------------------------------------------------
:MAIN_FUNC
rem beginfunction
    set FUNCNAME=%0
    if "%DEBUG%"=="1" (
        echo DEBUG: procedure %FUNCNAME% ...
    )

    python.exe ListDir3.py -PDir=%PDir% -PMask=%PMask%

    exit /b 0
rem endfunction

rem =================================================
rem ФУНКЦИИ LIB
rem =================================================
:Check_P
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:ExtractFileDir
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:FullFileName
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:ExtractFileName
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:ExtractFileNameWithoutExt
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:ExtractFileExt
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:FileAttr
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:CurrentDir
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
rem =================================================
