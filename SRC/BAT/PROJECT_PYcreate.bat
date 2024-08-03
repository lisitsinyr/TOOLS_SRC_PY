@echo off
rem -------------------------------------------------------------------
rem PROJECT_PYcreate.bat
rem -------------------------------------------------------------------
rem 
rem Description:
rem   �������� ������� PROJECT_PY
rem 
rem Usage:
rem   setupPROJECT_PY.bat <ProjectName> <directory>
rem 
rem Arguments:
rem   name - ��� �������
rem   ProjectName - ������� �������
rem 
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

    if defined OK (
        rem echo ProjectName: !PROJECT_NAME!
        rem echo Directory: !Directory!

        echo �������� ������� !ProjectName! ...
        echo Directory: !Directory!
        if exist "!Directory!"\ (
            echo INFO: ������� ������� "!Directory!" ����������...
            set delete=N
            set PN_CAPTION=�������?
            call :Read_F delete "yN" 5 || exit /b 1
            if defined delete (
                echo �������� �������� ������� "!Directory!"
                rmdir "!Directory!" /s
                mkdir "!Directory!"
            )

            set tomlFile="!Directory!"\pyproject.toml
            call :CheckFile !tomlFile! || exit /b 1
            if defined CheckFile (
                cd /D "!Directory!"
                rem call lyrpoetry_init.bat --name=!ProjectName!
            ) else (
                echo INFO: ���� !tomlFile! �� ���������� ...
                rem call lyrpoetry_new.bat --name=!ProjectName! --src "!Directory!"
                mkdir "!Directory!"
                cd /D "!Directory!"
                rem call lyrpoetry_init.bat --name=!ProjectName!
            )
            set OK=yes
        ) else (
            rem call lyrpoetry_new.bat --name=!ProjectName! --src "!Directory!"
            mkdir "!Directory!"
            cd /D "!Directory!"
            rem call lyrpoetry_init.bat --name=!ProjectName!
            set OK=yes
        )

        rem --------------------------
        rem ��������� ���������
        rem --------------------------
        call PROJECT_PYupdate.bat !ProjectName!

        set tomlFile=pyproject.toml
        call :CheckFile !tomlFile! || exit /b 1
        if not defined CheckFile (
            echo INFO: ���� !tomlFile! �� ���������� ...
            rem call lyrpoetry_init.bat --name=!ProjectName!
        )

        rem --------------------------
        rem GIT
        rem --------------------------
        if exist ".git"\ (
            echo INFO: Repository exist ...
        ) else (
            rem call lyrgit_init.bat .\
        )
    )

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
    if not defined PROJECT_NAME (
        set PN_CAPTION=��� �������
        set ProjectName=PATTERN_PY
        call :Read_P ProjectName %1 || exit /b 1
        rem echo ProjectName: !ProjectName!

        if not defined ProjectName (
            echo ERROR: ProjectName not defined ...
            set OK=
        ) else (
            set OK=yes
        )

        set PN_CAPTION=������� �������
        set Directory=!ProjectName!
        call :Read_P Directory %2 || exit /b 1
        echo Directory: !Directory!
        if not defined Directory (
            echo ERROR: Directory not defined ...
            set OK=
        ) else (
            set OK=yes
        )
    ) else (
        set ProjectName=!PROJECT_NAME!
        set Directory=!CurrentDir!
        set OK=yes
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
:PressAnyKey
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
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
:GetINI
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
:SetINI
%LIB_BAT%\LYRSupport.bat %*
exit /b 0
rem =================================================
