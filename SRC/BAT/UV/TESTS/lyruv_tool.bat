@echo off
rem -------------------------------------------------------------------
rem lyrpy.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

rem ������������� Python CLI-���������� ��� ���������� ���
rem     uv tool install tool_name
rem     ������: uv tool install ruff

rem ��������� CLI-���������� �� ��������� ��������� ��� ���������.
rem     uvx tool args
rem     ������: uvx black script.py

uv tool
