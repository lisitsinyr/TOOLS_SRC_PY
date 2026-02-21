UV заменяет: 
    pip
    pipx 
    venv
    pyenv
    pip-tools
    virtualenv
    poetry

Он позволяет:

— устанавливать пакеты,
— создавать и управлять виртуальными окружениями,
— управлять версиями Python — всё в одном инструменте.

Установка

D:\PROJECTS_LYR\CHECK_LIST\DESKTOP\Python\PROJECTS_PY\TOOLS_SRC_PY\SRC\BAT\lyruv_install_uv.bat

pip install uv

rem source .venv/bin/activate

uv python install 3.14

Вот шпаргалка по uv для Python-разработчиков
Команды ниже позволяют создавать и активировать виртуальное окружение, скачивать пакеты и использовать pip

Инициализирует новый Python-проект с дефолтной структурой
    uv init project_name

Создаёт новое виртуальное окружение в текущем проекте
    uv venv                   

Добавляет пакет в зависимости проекта
    uv add package_name

Удаляет указанный пакет из зависимостей проекта
    uv remove package_name

Устанавливает все зависимости из файла requirements.txt
    uv pip install -r requirements.txt
    uv pip install flask 

Сгенерировать файл requirements.txt с помощью команды 
    uv pip compile pyproject.toml -o requirements.txt
    Это читает файл pyproject.toml и создаёт список фиксированных зависимостей. 

Запускает Python-скрипт или команду внутри окружения проекта
    uv run script.py

Синхронизирует зависимости проекта в соответствии с uv.lock
    uv sync

Устанавливает Python CLI-инструмент как глобальный тул
    uv tool install tool_name
    Пример: uv tool install ruff

Запускает CLI-инструмент во временном окружении без установки.
    uvx tool args
    Пример: uvx black script.py
