@echo off
rem -------------------------------------------------------------------
rem lyrpy.bat
rem -------------------------------------------------------------------
chcp 1251>NUL

setlocal enabledelayedexpansion

rem ��������� uv

rem ������������� ������ ��������� uv � ������� ����������� �����������
rem ��� Windows:

rem powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
"C:\Program Files\PowerShell\7\pwsh.exe" -c "irm https://astral.sh/uv/install.ps1 | iex"