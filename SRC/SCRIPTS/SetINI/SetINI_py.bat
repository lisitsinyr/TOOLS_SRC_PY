@echo off
rem -------------------------------------------------------------------
rem SetINI_py.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

rem -------------------------------------------------------------------
rem SCRIPTS_DIR - Каталог скриптов
rem -------------------------------------------------------------------
if not defined SCRIPTS_DIR (
    set SCRIPTS_DIR=D:\PROJECTS_LYR\CHECK_LIST\03_SCRIPT\04_BAT\PROJECTS_BAT\TOOLS_SRC_BAT
)
rem -------------------------------------------------------------------
rem LIB_BAT - каталог библиотеки скриптов
rem -------------------------------------------------------------------
set LIB_BAT=!SCRIPTS_DIR!\SRC\LIB
rem -------------------------------------------------------------------
rem SCRIPTS_DIR_PY - Каталог скриптов PY
rem -------------------------------------------------------------------
if not defined SCRIPTS_DIR_PY (
    set SCRIPTS_DIR_PY=D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\PROJECTS_PY\TOOLS_SRC_PY
)
echo SCRIPTS_DIR_PY:!SCRIPTS_DIR_PY!

rem --------------------------------------------------------------------------------
rem 
rem --------------------------------------------------------------------------------
:begin
    set BATNAME=%~nx0
    echo Start !BATNAME! ...

    set DEBUG=
    set /a LOG_FILE_ADD=0

    rem Количество аргументов
    call :Read_N %* || exit /b 1

    call :SET_LIB %0 || exit /b 1

    rem -------------------------------------
    rem OPTION
    rem -------------------------------------
    rem set O1=O1
    rem set PN_CAPTION=O1
    rem call :Read_P O1 O1 || exit /b 1
    rem rem echo O1:!O1!
    rem if defined O1 (
    rem     set OPTION=!OPTION! --O1 !O1!
    rem ) else (
    rem     echo INFO: O1 not defined ...
    rem )

    rem -------------------------------------
    rem ARGS
    rem -------------------------------------
    rem Проверка на обязательные аргументы
    set A1=
    set PN_CAPTION=FileName
    call :Read_P A1 A1 || exit /b 1
    echo A1:!A1!
    if defined A1 (
        set ARGS=!ARGS! !A1!
    ) else (
        echo ERROR: A1 not defined ...
        set OK=
    )
    set A2=
    set PN_CAPTION=Directory
    call :Read_P A2 A2 || exit /b 1
    echo A2:!A2!
    if defined A2 (
        set ARGS=!ARGS! !A2!
    ) else (
        echo ERROR: A2 not defined ...
        set OK=
    )
    echo ARGS:!ARGS!

    rem echo %~dp0
    rem echo !SCRIPTS_DIR_PY!
    rem python !%~dp0!COPYFILE.py %1 "%2"

    rem set RUN=!SCRIPTS_DIR_PY!\COPYFILE\COPYFILE.py
    rem echo RUN:!RUN! 
    rem !RUN!

    python "!SCRIPTS_DIR_PY!"\SRC\SCRIPTS\SetINI\SetINI.py !ARGS!

    call :PressAnyKey || exit /b 1

    exit /b 0
:end
rem --------------------------------------------------------------------------------

rem =================================================
rem ФУНКЦИИ LIB
rem =================================================
rem =================================================
rem LYRConst.bat
rem =================================================
:SET_LIB
%LIB_BAT%\LYRConst.bat %*
exit /b 0
:SET_KIX
%LIB_BAT%\LYRConst.bat %*
exit /b 0
rem =================================================
rem LYRDateTime.bat
rem =================================================
rem =================================================
rem LYRFileUtils.bat
rem =================================================
rem =================================================
rem LYRLog.bat
rem =================================================
rem =================================================
rem LYRStrUtils.bat
rem =================================================
rem =================================================
rem LYRSupport.bat
rem =================================================
:PressAnyKey
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Read_N
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Read_P
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
rem =================================================