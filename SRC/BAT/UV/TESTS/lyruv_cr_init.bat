@echo off
rem -------------------------------------------------------------------
rem lyrpy.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

rem --------------------------------------------------------------------------------
rem 
rem --------------------------------------------------------------------------------
:begin
    rem Creating projects

    goto begin_01

:begin_01
    rem Initialise a project in the current directory
    rem �������������� ����� Python-������ � ��������� ���������� � ������� ��������
    rem <DIR>.git
    rem .gitignore
    rem .python-version
    rem main.py
    rem pyproject.toml
    rem README.md
    
    rem --no-workspace  ������� ��������� ������, �� ����������� � �������� ������������
    rem �� ��������� uv ���� ������� ������������ � ������� �������� ��� ����� ������������ ��������
    rem � ������� ����� ����� ������� ��������� ������������� ������

    rem --python - Use Python 3.X[.X] for your project

    rem uv init [--app] [...] [--no-workspace] [--python 3.13.1]

    rem uv init --python 3.13.1

    uv init

    exit /b 0

:begin_02
    rem Initialise a project project_name in the current directory in the directory project_name

    rem uv init [--app] [...] [--no-workspace] project_name

    uv init project_name

    exit /b 0

:begin_03
    rem Initialise a project myproj in the directory project_dir

    rem uv init [--app] [...] [--no-workspace] project_dir

    uv init D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\PROJECTS_PY\UV\project_name

    exit /b 0

:begin_04
    rem Initialise a packageable app (e.g., CLI, web app, ...)

    rem uv init [--app] --package [...] [--no-workspace]

    rem <DIR>.git
    rem .gitignore
    rem .python-version
    rem <DIR>src
    rem pyproject.toml
    rem README.md

    exit /b 0

:begin_05
    rem Initialise a packageable library (code you import)

    rem uv init --lib [--package] [...] [--no-workspace]
    
    rem <DIR>.git
    rem .gitignore
    rem .python-version
    rem <DIR>src
    rem pyproject.toml
    rem README.md

    exit /b 0

:begin_06
    rem ���� ����� ������� ����������� ������, ����� ������������ ����� --bare
    rem UV �� ������� ���� � ��������� ������ Python, README � ����� �������� ��� �����.

    rem uv init --bare [...] [--no-workspace]

    rem pyproject.toml

    exit /b 0

:end
rem =================================================


