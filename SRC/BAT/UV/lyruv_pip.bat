@echo off
rem -------------------------------------------------------------------
rem lyrpy.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

    rem -------------------------------------------------------------------
    rem PROJECTS_LYR_ROOT - ������� ROOT
    rem -------------------------------------------------------------------
    rem set PROJECTS_LYR_ROOT=D:\WORK\WIN
    set PROJECTS_LYR_ROOT=D:
    rem echo PROJECTS_LYR_ROOT:!PROJECTS_LYR_ROOT!

    rem -------------------------------------------------------------------
    rem PROJECTS_LYR_DIR - ������� �������� LYR
    rem -------------------------------------------------------------------
    set PROJECTS_LYR_DIR=!PROJECTS_LYR_ROOT!\PROJECTS_LYR
    rem echo PROJECTS_LYR_DIR:!PROJECTS_LYR_DIR!
    if not exist "!PROJECTS_LYR_DIR!"\ (
        rem echo INFO: Dir "!PROJECTS_LYR_DIR!" not exist ...
        rem echo INFO: Create "!PROJECTS_LYR_DIR!" ...
        rem mkdir "!PROJECTS_LYR_DIR!"
        exit /b 1
    )

    rem -------------------------------------------------------------------
    rem SCRIPTS_DIR_SRC - ������� �������� BAT
    rem -------------------------------------------------------------------
    if not defined SCRIPTS_DIR_SRC (
        rem set SCRIPTS_DIR=D:\TOOLS\TOOLS_BAT
        set SCRIPTS_DIR_SRC=!PROJECTS_LYR_DIR!\CHECK_LIST\SCRIPT\BAT\PROJECTS_BAT\TOOLS_SRC_BAT\SRC
    )
    rem echo SCRIPTS_DIR_SRC:!SCRIPTS_DIR_SRC!

    rem -------------------------------------------------------------------
    rem LIB_BAT - ������� ���������� �������� BAT
    rem -------------------------------------------------------------------
    if not defined LIB_BAT (
        set LIB_BAT=!SCRIPTS_DIR_SRC!\LIB
    )
    rem echo LIB_BAT:!LIB_BAT!
    if not exist !LIB_BAT!\ (
        echo ERROR: ������� ���������� LYR !LIB_BAT! �� ����������...
        exit /b 1
    )

    rem -------------------------------------------------------------------
    rem ���������� ����������
    rem -------------------------------------------------------------------
    call :Read_N %* || exit /b 1

    rem -------------------------------------------------------------------
    rem ��������� �����
    rem -------------------------------------------------------------------
    call :SET_LIB %~f0 || exit /b 1

rem --------------------------------------------------------------------------------
rem 
rem --------------------------------------------------------------------------------
:begin
    set BATNAME=%~nx0
    echo Start !BATNAME! ...

    set DEBUG=

    set /a LOG_FILE_ADD=0

    call :CurrentDir || exit /b 1
    rem echo CurrentDir:!CurrentDir!

    rem -------------------------------------
    rem OPTION
    rem -------------------------------------
    set OPTION=

    if not defined O1 (
        set O1_Name=O1
        set O1_Caption=project_dir
        set O1_Default=!CurrentDir!
        set O1=!O1_Default!
        set PN_CAPTION=!O1_Caption!
        call :Read_P O1 || exit /b 1
    )
    echo O1:!O1!
    if defined O1 (
        rem set OPTION=!OPTION! "!O1!"
    ) else (
        echo INFO: O1 [O1_Name:!O1_Name! O1_Caption:!O1_Caption!] not defined ...
    )

    if not defined O2 (
        set O2_Name=O2
        set O2_Caption=VENV
        set O2_Default=P313
        set O2=!O1_Default!
        set PN_CAPTION=!O2_Caption!
        call :Read_P O2 !O2! || exit /b 1
    )
    echo O2:!O2!
    if defined O2 (
        rem set OPTION=!OPTION! -!O2_Name! "!O2!"
    ) else (
        echo INFO: O2 [O2_Name:!O2_Name! O2_Caption:!O2_Caption!] not defined ...
    )

    rem echo OPTION:!OPTION!

    rem -------------------------------------
    rem ARGS
    rem -------------------------------------
    set ARGS=

    rem if not defined A1 (
    rem     set A1_Name=script
    rem     set A1_Caption=script
    rem     set A1_Default=%1
    rem     set A1=!A1_Default!
    rem     set PN_CAPTION=!A1_Caption!
    rem     call :Read_P A1 !A1! || exit /b 1
    rem )
    rem echo A1:!A1!
    rem if defined A1 (
    rem     set ARGS=!ARGS! "!A1!"
    rem ) else (
    rem     echo ERROR: A1 [A1_Name:!A1_Name! A1_Caption:!A1_Caption!] not defined ... 
    rem     set OK=
    rem     exit /b 1
    rem )

    rem echo ARGS:!ARGS!

    rem -------------------------------------------------------------------
    rem project_dir - 
    rem -------------------------------------------------------------------
    set project_dir=!O1!
    echo project_dir:!project_dir!
    if defined project_dir (
        if not exist !project_dir!\ (
            echo ERROR: Dir !project_dir! not exist ...
            exit /b 1
        ) else (
            cd /D !project_dir!
        )
    )
    if not exist .venv\ (
        echo ERROR: Dir .venv not exist ...
        exit /b 1
    )

    rem -------------------------------------------------------------------
    rem ENV - 
    rem -------------------------------------------------------------------
    set PY_ENVDIR=D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\VENV\P313
    echo !O2!
    if exist !O2! (
       set PY_ENVDIR=!O2!
    ) else (
        if !02!==P313 (
            set PY_ENVDIR=D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\VENV\P313
        ) else (
            if !01!==P314 (
                set PY_ENVDIR=D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\VENV\P314
            )
        )
    )
    echo PY_ENVDIR:!PY_ENVDIR!
    if not exist !PY_ENVDIR! (
        echo INFO: Dir !PY_ENVDIR! not exist ...
        exit /b 1
    )
    
    set ChoiceOperation=
    rem ------------------------------------------
    :WHILE
    rem ------------------------------------------
    if not !ChoiceOperation!==10 (
        call :ChoiceOperation || exit /b 1
        goto :WHILE
    )

    rem call :PressAnyKey || exit /b 1
    
    exit /b 0
:end
rem =================================================

rem --------------------------------------------------------------------------------
rem function ChoiceOperation () -> Read_N
rem --------------------------------------------------------------------------------
:ChoiceOperation
rem beginfunction
    set FUNCNAME=%0
    set FUNCNAME=ChoiceOperation
    if defined DEBUG (
        echo DEBUG: procedure !FUNCNAME! ...
    )
    set !FUNCNAME!=

    rem ------------------------------------------
    rem ����
    rem ------------------------------------------
    echo 1.UV_pip list
    echo 2.UV_pip tree
    echo 3.UV_pip check
    echo 4.UV_pip show
    echo 5.UV_pip compile
    echo 6.UV_pip sync
    echo 7.UV_pip freeze
    echo 8.UV_pip install
    echo 9.UV_pip uninstall
    echo Q.Quit

    set C1_Name=C1
    set C1_List=123456789Q
    set C1_Caption=operation
    set C1_Default=Q
    rem set C1=!O1_Default!
    set PN_CAPTION=!C1_Caption!
    rem procedure Read_F (P_Name, P_List, ADefault, ACaption, Atimeout)
    call :Read_F C1 !C1_List! !C1_Default! !C1_Caption! 10 || exit /b 1
    echo C1:!C1!
    set ChoiceOperation=!C1!

    rem Usage: uv pip [OPTIONS] <COMMAND>

    rem ------------------------------------------
    rem CASE
    rem ------------------------------------------
    if !C1!==1 (
        echo list - List, in tabular format, packages installed in an environment
        set APP=uv pip list
        echo APP:!APP!

        uv pip list
        
        exit /b 0
    )
    if !C1!==2 (
        echo tree - Display the dependency tree for an environment
        set APP=uv pip tree
        echo APP:!APP!
        
        uv pip tree
        
        exit /b 0
    )
    if !C1!==3 (
        echo check - Verify installed packages have compatible dependencies
        set APP=uv pip check
        echo APP:!APP!

        uv pip check
        
        exit /b 0
    )
    if !C1!==4 (
        echo show - Show information about one or more installed packages
        set APP=uv pip show
        echo APP:!APP!

        uv pip show
        
        exit /b 0
    )
    if !C1!==5 (
        echo compile - Compile a requirements.in file to a requirements.txt or pylock.toml file
        set APP=uv pip compile pyproject.toml --quiet --output-file requirements.txt
        echo APP:!APP!
        
        uv pip compile pyproject.toml --quiet --output-file requirements.txt
        
        exit /b 0
    )
    if !C1!==6 (
        echo sync - Sync an environment with a `requirements.txt` or `pylock.toml` file
        set APP=uv pip sync
        echo APP:!APP!
        
        uv pip sync
        
        exit /b 0
    )
    if !C1!==7 (
        echo freeze - List, in requirements format, packages installed in an environment
        rem uv pip freeze > requirements.txt
        set APP=uv pip freeze
        echo APP:!APP!
        
        uv pip freeze > requirements.txt
        
        exit /b 0
    )
    if !C1!==8 (
        echo install - Install packages into an environment
        set APP=uv pip install A B C
        echo APP:!APP!

        rem call :PY_ENV_START || exit /b 1

        uv pip install A B C

        rem call :PY_ENV_STOP || exit /b 1

        exit /b 0
    )
    if !C1!==9 (
        echo uninstall - Uninstall packages from an environment
        set APP=uv pip uninstall A B C
        echo APP:!APP!

        rem call :PY_ENV_START || exit /b 1

        uv pip uninstall A B C

        rem call :PY_ENV_STOP || exit /b 1
        
        exit /b 0
    )
    if !C1!==10 (
        exit /b 0
    )

    exit /b 0

rem endfunction

rem =================================================
rem ������� LIB
rem =================================================

rem =================================================
rem LYRPY.bat
rem =================================================
:LYRPY
%LIB_BAT%\LYRPY.bat %*
exit /b 0
:PY_ENV_START
%LIB_BAT%\LYRPY.bat %*
exit /b 0
:PY_ENV_STOP
%LIB_BAT%\LYRPY.bat %*
exit /b 0

rem =================================================
rem LYRDEPLOY.bat
rem =================================================
:REPO_WORK
%LIB_BAT%\LYRDEPLOY.bat %*
exit /b 0
:git_pull
%LIB_BAT%\LYRDEPLOY.bat %*
exit /b 0
:DEPLOY_PROJECT
%LIB_BAT%\LYRDEPLOY.bat %*
exit /b 0

rem =================================================
rem LYRConst.bat
rem =================================================
:SET_LIB
%LIB_BAT%\LYRLIB.bat %*
exit /b 0
:SET_POETRY
%LIB_BAT%\LYRLIB.bat %*
exit /b 0
:SET_KIX
%LIB_BAT%\LYRLIB.bat %*
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
:COPY_FILES
%LIB_BAT%\LYRFileUtils.bat %*
exit /b 0
:XCOPY_FILES
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
:TrimLeft
%LIB_BAT%\LYRStrUtils.bat %*
exit /b 0
:TrimRight
%LIB_BAT%\LYRStrUtils.bat %*
exit /b 0
:Trim
%LIB_BAT%\LYRStrUtils.bat %*
exit /b 0
:Left
%LIB_BAT%\LYRStrUtils.bat %*
exit /b 0
:Mid
%LIB_BAT%\LYRStrUtils.bat %*
exit /b 0
:TrimQuotes
%LIB_BAT%\LYRStrUtils.bat %*
exit /b 0

rem =================================================
rem LYRSupport.bat
rem =================================================
:PressAnyKey
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:Pause
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
:GetDir
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:GetFile
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:FORCicle
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:GetSET
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:GetCMD
%LIB_BAT%\LYRSupport.bat %*
exit /b 0

rem =================================================
rem LYRParserINI.bat
rem =================================================
:GetINI
%LIB_BAT%\LYRParserINI.bat %*
exit /b 0
:SetINI
%LIB_BAT%\LYRParserINI.bat %*
exit /b 0
:GetINIParametr
%LIB_BAT%\LYRParserINI.bat %*
exit /b 0
:GetFileParser
%LIB_BAT%\LYRParserINI.bat %*
exit /b 0
rem =================================================
