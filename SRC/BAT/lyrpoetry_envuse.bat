@echo off
rem -------------------------------------------------------------------
rem lyrpoetry_envuse.bat
rem -------------------------------------------------------------------
rem ������ poetry �� ����������� ������������ ������������
rem -------------------------------------------------------------------
rem 
rem Description:
rem   Activates or creates a new virtualenv for the current project.
rem   Switching between environments
rem 
rem Usage:
rem   env use [options] [--] <python>
rem 
rem Arguments:
rem   python                     The python executable to use.
rem 
rem Options:
rem   -h, --help                 Display help for the given command. When no command is given display help for the list command.
rem   -q, --quiet                Do not output any message.
rem   -V, --version              Display this application version.
rem       --ansi                 Force ANSI output.
rem       --no-ansi              Disable ANSI output.
rem   -n, --no-interaction       Do not ask any interactive question.
rem       --no-plugins           Disables plugins.
rem       --no-cache             Disables Poetry source caches.
rem   -C, --directory=DIRECTORY  The working directory for the Poetry command (defaults to the current working directory).
rem   -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug.
rem -------------------------------------------------------------------
rem   Usage 
rem   For this specific purpose, you can use the env use command to tell Poetry which Python version to use for the current project.
rem     poetry env use /full/path/to/python
rem   If you have the python executable in your PATH you can use it:
rem     poetry env use python3.7
rem   You can even just use the minor Python version in this case:
rem     poetry env use 3.7
rem   If you want to disable the explicitly activated virtual environment, you can use the special system Python version to retrieve the default behavior:
rem     poetry env use system
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

rem --------------------------------------------------------------------------------
rem 
rem --------------------------------------------------------------------------------
:begin
    set BATNAME=%~nx0
    echo Start !BATNAME! ...

    set DEBUG=

    rem -------------------------------------------------------------------
    rem SCRIPTS_DIR - ������� ��������
    rem LIB_BAT - ������� ���������� ��������
    rem SCRIPTS_DIR_KIX - ������� �������� KIX
    rem -------------------------------------------------------------------
    call :MAIN_INIT %* || exit /b 1

    rem ���������� ����������
    call :Read_N %* || exit /b 1
    rem echo Read_N: !Read_N!

    call :SET_LIB %0 || exit /b 1
    rem echo CURRENT_DIR: !CURRENT_DIR!

    call :StartLogFile || exit /b 1
    set OK=yes
    call :MAIN_SET %* || exit /b 1
    if defined OK if not defined Read_N (
        call :MAIN_CHECK_PARAMETR %* || exit /b 1
    )
    if defined OK (
        call :MAIN %* || exit /b 1
    )
    call :StopLogFile || exit /b 1

    exit /b 0
:end
rem --------------------------------------------------------------------------------

rem -----------------------------------------------
rem procedure MAIN_INIT (FULLFILENAME, DEBUG)
rem -----------------------------------------------
:MAIN_INIT
rem beginfunction
    set FUNCNAME=%0
    set FUNCNAME=MAIN_INIT
    if defined DEBUG (
        echo DEBUG: procedure !FUNCNAME! ...
    )

    rem -------------------------------------------------------------------
    rem SCRIPTS_DIR - ������� ��������
    rem -------------------------------------------------------------------
    if not defined SCRIPTS_DIR (
        set SCRIPTS_DIR=D:\TOOLS\TOOLS_BAT
        set SCRIPTS_DIR=D:\PROJECTS_LYR\CHECK_LIST\03_SCRIPT\04_BAT\PROJECTS_BAT\TOOLS_BAT
    )
    rem echo SCRIPTS_DIR: %SCRIPTS_DIR%
    rem -------------------------------------------------------------------
    rem LIB_BAT - ������� ���������� ��������
    rem -------------------------------------------------------------------
    if not defined LIB_BAT (
        set LIB_BAT=!SCRIPTS_DIR!\LIB
        rem echo LIB_BAT: !LIB_BAT!
    )
    if not exist !LIB_BAT!\ (
        echo ERROR: ������� ���������� LYR !LIB_BAT! �� ����������...
        exit /b 0
    )
    rem -------------------------------------------------------------------
    rem SCRIPTS_DIR_KIX - ������� �������� KIX
    rem -------------------------------------------------------------------
    if not defined SCRIPTS_DIR_KIX (
        set SCRIPTS_DIR_KIX=D:\TOOLS\TOOLS_KIX
        set SCRIPTS_DIR_KIX=D:\PROJECTS_LYR\CHECK_LIST\03_SCRIPT\01_KIX\PROJECTS_KIX\TOOLS_KIX
    )
    rem echo SCRIPTS_DIR_KIX: !SCRIPTS_DIR_KIX!

    exit /b 0
rem endfunction

rem --------------------------------------------------------------------------------
rem procedure MAIN_SET ()
rem --------------------------------------------------------------------------------
:MAIN_SET
rem beginfunction
    set FUNCNAME=%0
    set FUNCNAME=MAIN_SET
    if defined DEBUG (
        echo DEBUG: procedure !FUNCNAME! ...
    )

    set tomlFile=pyproject.toml
    call :CheckFile !tomlFile! || exit /b 1
    if not defined CheckFile (
        echo ERROR: ���� !tomlFile! �� ���������� ...
        set OK=
    )

    exit /b 0
rem endfunction

rem --------------------------------------------------------------------------------
rem procedure MAIN ()
rem --------------------------------------------------------------------------------
:MAIN
rem beginfunction
    set FUNCNAME=%0
    if defined DEBUG (
        echo DEBUG: procedure !FUNCNAME! ...
    )

    call :SET_POETRY || exit /b 1

    echo Activates or creates a new virtualenv for the current project ...
    set COMMAND=env use
    
    if not defined Read_N (
        set APPRUN=!APP! !COMMAND!!OPTION!!ARGS!
    ) else (
        set APPRUN=!APP! !COMMAND!!OPTION! %*
    )
    echo APPRUN: !APPRUN!
    !APPRUN!

    exit /b 0
rem endfunction

rem --------------------------------------------------------------------------------
rem procedure MAIN_CHECK_PARAMETR ()
rem --------------------------------------------------------------------------------
:MAIN_CHECK_PARAMETR
rem beginfunction
    set FUNCNAME=%0
    if defined DEBUG (
        echo DEBUG: procedure !FUNCNAME! ...
    )

    rem -------------------------------------
    rem OPTION
    rem -------------------------------------

    rem -------------------------------------
    rem ARGS
    rem -------------------------------------
    rem �������� �� ������������ ���������
    set python=
    set PN_CAPTION=The python executable to use
    call :Read_P python "D:\PROJECTS_LYR\CHECK_LIST\05_DESKTOP\02_Python\VENV\P312\Scripts\python.exe" || exit /b 1
    rem echo python: !python!
    if defined python (
        set ARGS=!ARGS! !python!
    ) else (
        echo ERROR: python defined ...
        set OK=
    )

    exit /b 0
rem endfunction

rem =================================================
rem ������� LIB
rem =================================================
rem =================================================
rem LYRConst.bat
rem =================================================
:SET_LIB
%LIB_BAT%\LYRConst.bat %*
exit /b 0
:SET_POETRY
%LIB_BAT%\LYRConst.bat %*
exit /b 0
:SET_KIX
%LIB_BAT%\LYRConst.bat %*
exit /b 0
rem =================================================
rem LYRDateTime.bat
rem =================================================
:YYYYMMDDHHMMSS
%LIB_BAT%\LYRDateTime.bat %*
exit /b 0
:DateTime
%LIB_BAT%\LYRDateTime.bat %*
exit /b 0
rem =================================================
rem LYRFileUtils.bat
rem =================================================
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
:FileSize
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:CreateDir
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:CreateFile
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:CheckFile
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:CurrentDir
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
rem =================================================
rem LYRLog.bat
rem =================================================
:FormatStr
%LIB_BAT%\LYRLog.bat %*
exit /b 0
:AddLog
%LIB_BAT%\LYRLog.bat %*
exit /b 0
:AddLogFile
%LIB_BAT%\LYRLog.bat %*
exit /b 0
:StartLogFile
%LIB_BAT%\LYRLog.bat %*
exit /b 0
:StopLogFile
%LIB_BAT%\LYRLog.bat %*
exit /b 0
rem =================================================
rem LYRStrUtils.bat
rem =================================================
rem =================================================
rem LYRSupport.bat
rem =================================================
:Pause
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Check_P
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Read_P
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Read_N
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Read_F
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:PressAnyKey
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
rem =================================================
