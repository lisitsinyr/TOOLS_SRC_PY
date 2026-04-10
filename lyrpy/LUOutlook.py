"""LUOutlook.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2023-2026
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     LUOutlook.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import win32com.client

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------


#------------------------------------------
# 1. Подключение к локальному Outlook из Python
#------------------------------------------
# 1. Базовое подключение к Outlook.py
#------------------------------------------
def OUTLOOK_1_1 ():
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")

    print(f"Почтовый ящик: {namespace.CurrentUser.Name}")
    print(f"Папки: {[f.Name for f in namespace.Folders]}")









#-------------------------------------------------
# 
#-------------------------------------------------
def read_inbox (limit=5):
    outlook = win32com.client.Dispatch ("Outlook.Application")
    namespace = outlook.GetNamespace ("MAPI")
    inbox = namespace.GetDefaultFolder (6)  # 6 = olFolderInbox

    messages = inbox.Items
    messages.Sort ("[ReceivedTime]", True)  # Новые сверху

    # for i, message in enumerate (messages [:limit]):
    for i, message in enumerate (messages):
        print (f"\n--- Письмо {i + 1} ---")
        print (f"От: {message.SenderName}")
        print (f"Тема: {message.Subject}")
        print (f"Дата: {message.ReceivedTime}")
        print (f"Текст: {message.Body [:200]}...")

#-------------------------------------------------
# 
#-------------------------------------------------
def list_root_folders ():
    outlook = win32com.client.Dispatch ("Outlook.Application")
    namespace = outlook.GetNamespace ("MAPI")

    print (f"Всего хранилищ: {namespace.Folders.Count}\n")

    for i, folder in enumerate (namespace.Folders, 1):
        print (f"{i}. {folder.Name}")
        # Можно проверить путь к файлу, если это PST
        try:
            if folder.StoreFilePath:
                print (f"   Путь: {folder.StoreFilePath}")
        except:
            pass

#-------------------------------------------------
# 
#-------------------------------------------------
def find_folder_by_name (target_name):
    outlook = win32com.client.Dispatch ("Outlook.Application")
    namespace = outlook.GetNamespace ("MAPI")

    for root in namespace.Folders:
        folder = find_folder_recursive (root, target_name)
        if folder:
            return folder
    return None

#-------------------------------------------------
# 
#-------------------------------------------------
def find_folder_recursive (folder, target_name):
    if folder.Name.lower () == target_name.lower ():
        return folder

    try:
        for subfolder in folder.Folders:
            result = find_folder_recursive (subfolder, target_name)
            if result:
                return result
    except:
        pass
    return None

#-------------------------------------------------
# 1. Базовый пример: чтение из конкретного ящика
#-------------------------------------------------
def read_messages_from_folder (account_name, folder_name, limit=5):
    outlook = win32com.client.Dispatch ("Outlook.Application")
    namespace = outlook.GetNamespace ("MAPI")

    try:
        # 1. Получаем корневую папку хранилища
        store = namespace.Folders [account_name]

        # 2. Получаем нужную папку внутри хранилища
        target_folder = store.Folders [folder_name]

        # 3. Получаем коллекцию сообщений
        messages = target_folder.Items

        # 4. Сортируем по дате (новые сверху)
        messages.Sort ("[ReceivedTime]", True)

        print (f"📬 Папка: {folder_name} в хранилище {account_name}")
        print (f"Всего сообщений: {messages.Count}\n")

        # 5. Читаем последние сообщения
        for i, message in enumerate (messages [:limit], 1):
            if message.Class == 43:  # 43 = olMail
                print (f"--- Сообщение {i} ---")
                print (f"От: {message.SenderName}")
                print (f"Тема: {message.Subject}")
                print (f"Дата: {message.ReceivedTime}")
                print (f"Текст: {message.Body [:300]}...")
                print (f"Прочитано: {message.UnRead}")
                print ()

    except Exception as e:
        print (f"❌ Ошибка: {e}")

#-------------------------------------------------
# 2. Чтение из вложенной папки (рекурсивный поиск)
#-------------------------------------------------
def find_folder_path (store, folder_path):
    """
    folder_path: список имен папок, например ["Проекты", "Клиент А"]
    """
    current = store
    for folder_name in folder_path:
        found = False
        for folder in current.Folders:
            if folder.Name.lower () == folder_name.lower ():
                current = folder
                found = True
                break
        if not found:
            raise Exception (f"Папка '{folder_name}' не найдена")
    return current


def read_from_nested_folder (account_name, folder_path, limit=5):
    outlook = win32com.client.Dispatch ("Outlook.Application")
    namespace = outlook.GetNamespace ("MAPI")

    try:
        store = namespace.Folders [account_name]
        target_folder = find_folder_path (store, folder_path)
        messages = target_folder.Items
        messages.Sort ("[ReceivedTime]", True)

        print (f"📁 Путь: {' > '.join (folder_path)}")
        print (f"Сообщений: {messages.Count}\n")

        for i, msg in enumerate (messages [:limit], 1):
            if msg.Class == 43:
                print (
                    f"{i}. [{msg.ReceivedTime}] {msg.Subject} ({msg.SenderName})")

    except Exception as e:
        print (f"❌ Ошибка: {e}")

