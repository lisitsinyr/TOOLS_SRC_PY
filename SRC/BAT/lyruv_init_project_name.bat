@echo off
rem -------------------------------------------------------------------
rem lyrpy.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

rem �������������� ����� Python-������ � ��������� ����������

rem ���������� ���������� ����� �������� �������:
rem .gitignore
rem .python-version
rem hello.py
rem pyproject.toml
rem README.md

rem uv init project_name

uv init %1
