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
import datetime

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

#------------------------------------------
# 01.01 Базовое подключение к Outlook
#------------------------------------------
def OutlookApplication ():
    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")
    # print(f"Почтовый ящик: {namespace.CurrentUser.Name}")
    # print(f"Папки: {[f.Name for f in namespace.Folders]}")

    return outlook, namespace

#------------------------------------------
# 01.02. Отправка письма
#------------------------------------------
#------------------------------------------
# send_email
#------------------------------------------
def send_email (to, subject, body, attachments=None):
    outlook, namespace = OutlookApplication ()

    mail = outlook.CreateItem (0)  # 0 = olMailItem
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    if attachments:
        for path in attachments:
            mail.Attachments.Add (path)
    mail.Send ()  # или mail.Display() для просмотра перед отправкой

#------------------------------------------
# 01.03. Чтение писем из папки Входящие
#------------------------------------------
#------------------------------------------
# read_inbox
#------------------------------------------
def read_inbox ():
    outlook, namespace = OutlookApplication ()

    inbox = namespace.GetDefaultFolder (6)  # 6 = olFolderInbox
    messages = inbox.Items
    messages.Sort ("[ReceivedTime]", True)  # Новые сверху

    return messages
    
#------------------------------------------
# 2.Коллекция namespace.Folders содержит корневые папки всех хранилищ (магазинов), подключенных к вашему профилю Outlook
#------------------------------------------

#------------------------------------------
# 2.1. Вывод списка всех корневых хранилищ
#------------------------------------------
def list_root_folders ():
    outlook, namespace = OutlookApplication ()

    print (f"Всего хранилищ: {namespace.Folders.Count}\n")

    # for i, folder in enumerate (namespace.Folders, 1):
    #     print (f"{i}. {folder.Name}")
    #     # Можно проверить путь к файлу, если это PST
    #     try:
    #         if folder.StoreFilePath:
    #             print (f"   Путь: {folder.StoreFilePath}")
    #     except:
    #         pass

    return enumerate (namespace.Folders, 1), namespace.Folders

#------------------------------------------
# 2.2. Рекурсивный обход всех папок (Дерево папок)
#------------------------------------------
def print_folder_tree (folder, level=0):
    indent = "  " * level
    print (f"{indent}📁 {folder.Name}")

    try:
        for subfolder in folder.Folders:
            print_folder_tree (subfolder, level + 1)
    except Exception as e:
        print (f"{indent}   ⚠ Ошибка доступа: {e}")

def show_all_folders ():
    outlook, namespace = OutlookApplication ()
    for root_folder in namespace.Folders:
        print_folder_tree (root_folder)

#------------------------------------------
# 2.3. Доступ к Входящим конкретного аккаунта
#------------------------------------------
def get_inbox_by_account_name (account_name):
    outlook, namespace = OutlookApplication ()

    # 1. Находим корневую папку аккаунта
    try:
        root_folder = namespace.Folders [account_name]

        # 2. Внутри неё ищем папку "Входящие" (или "Inbox")
        # Имя папки зависит от языка интерфейса Outlook!
        inbox = root_folder.Folders ["Входящие"]

        print (f"Найдено писем в {account_name}: {inbox.Items.Count}")
        return inbox

    except Exception as e:
        print (f"Ошибка: {e}")
        return None

#------------------------------------------
# 2.4. Поиск папки по имени во всех хранилищах
#------------------------------------------
def find_folder_by_name (target_name):
    outlook, namespace = OutlookApplication ()

    for root in namespace.Folders:
        folder = find_folder_recursive (root, target_name)
        if folder:
            return folder
    return None

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

#------------------------------------------
# 3.Чтение сообщений из конкретной папки в хранилище Outlook
#------------------------------------------

#------------------------------------------
# 3.1. Базовый пример чтение из конкретного ящика
#------------------------------------------
def read_messages_from_folder (account_name, folder_name, limit=5):
    outlook, namespace = OutlookApplication ()

    try:
        # 1. Получаем корневую папку хранилища
        store = namespace.Folders [account_name]
        print (store)

        # 2. Получаем нужную папку внутри хранилища
        target_folder = store.Folders [folder_name]

        # 3. Получаем коллекцию сообщений
        messages = target_folder.Items

        # 4. Сортируем по дате (новые сверху)
        messages.Sort ("[ReceivedTime]", True)

        print (f"📬 Папка: {folder_name} в хранилище {account_name}")
        print (f"Всего сообщений: {messages.Count}\n")

        # 5. Читаем последние сообщения
        # for i, message in enumerate (messages [:limit], 1):
        # for i, message in enumerate (messages, 1):
            # print(i)
            # if message.Class == 43:  # 43 = olMail
            #     print (f"--- Сообщение {i} ---")
            #     print (f"От: {message.SenderName}")
            #     print (f"Тема: {message.Subject}")
            #     print (f"Дата: {message.ReceivedTime}")
            #     print (f"Текст: {message.Body [:300]}...")
            #     print (f"Прочитано: {message.UnRead}")
            #     print ()

    except Exception as e:
        print (f"❌ Ошибка: {e}")

#------------------------------------------
# 3.2. Чтение из вложенной папки (рекурсивный поиск)
#------------------------------------------
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
    outlook, namespace = OutlookApplication ()

    try:
        store = namespace.Folders [account_name]
        target_folder = find_folder_path (store, folder_path)
        messages = target_folder.Items
        messages.Sort ("[ReceivedTime]", True)

        print (f"📁 Путь: {' > '.join (folder_path)}")
        print (f"Сообщений: {messages.Count}\n")

        # for i, msg in enumerate (messages [:limit], 1):
        for i, msg in enumerate (messages, 1):
            if msg.Class == 43:
                print (
                    f"{i}. [{msg.ReceivedTime}] {msg.Subject} ({msg.SenderName})")

    except Exception as e:
        print (f"❌ Ошибка: {e}")

#------------------------------------------
# 3.3. Чтение с фильтрацией (по теме, отправителю, дате)
#------------------------------------------
def read_filtered_messages (account_name, folder_name,
                                filter_params=None, limit=10):
    outlook, namespace = OutlookApplication ()

    store = namespace.Folders [account_name]
    folder = store.Folders [folder_name]
    messages = folder.Items
    messages.Sort ("[ReceivedTime]", True)

    if filter_params:
        # Фильтр по теме
        if 'subject' in filter_params:
            messages = messages.Restrict (
                f"[Subject] LIKE '%{filter_params ['subject']}%'")

        # Фильтр по отправителю
        if 'sender' in filter_params:
            messages = messages.Restrict (
                f"[SenderName] LIKE '%{filter_params ['sender']}%'")

        # Фильтр по дате (только за последнюю неделю)
        if 'days' in filter_params:
            date_from = datetime.now () - datetime.timedelta (
                days=filter_params ['days'])
            date_str = date_from.strftime ("%d.%m.%Y")
            messages = messages.Restrict (
                f"[ReceivedTime] >= '{date_str}'")

        # Только непрочитанные
        if filter_params.get ('unread_only'):
            messages = messages.Restrict ("[UnRead] = True")

    print (f"Найдено сообщений: {messages.Count}\n")

    return messages

    # for i, msg in enumerate (messages [:limit], 1):
    #     if msg.Class == 43:
    #         print (f"{i}. 📧 {msg.Subject}")
    #         print (f"   От: {msg.SenderName}")
    #         print (f"   Дата: {msg.ReceivedTime}")
    #         print (f"   Прочитано: {'Нет' if msg.UnRead else 'Да'}")
    #         print ()

# Примеры использования:
# read_filtered_messages("work@company.com", "Входящие", {'subject': 'Отчет', 'unread_only': True})
# read_filtered_messages("work@company.com", "Входящие", {'days': 7, 'sender': 'Иванов'})

#------------------------------------------
# 3.4. Чтение с вложениями
#------------------------------------------
def read_messages_with_attachments (account_name, folder_name):
    outlook, namespace = OutlookApplication ()

    store = namespace.Folders [account_name]
    folder = store.Folders [folder_name]
    messages = folder.Items
    messages.Sort ("[ReceivedTime]", True)

    return messages

#------------------------------------------
# 3.5. Чтение HTML-писем с сохранением форматирования
#------------------------------------------
def read_html_message (account_name, folder_name, limit=3):
    outlook, namespace = OutlookApplication ()

    store = namespace.Folders [account_name]
    folder = store.Folders [folder_name]
    messages = folder.Items
    messages.Sort ("[ReceivedTime]", True)

    # for i, msg in enumerate (messages [:limit], 1):
    #     if msg.Class == 43:
    #         print (f"\n=== Письмо {i} ===")
    #         print (f"Тема: {msg.Subject}")
    #         print (f"От: {msg.SenderName}")
    #
    #         # Предпочитаем HTML-тело, если есть
    #         if msg.HTMLBody:
    #             print ("Тело (HTML):")
    #             # Первые 500 символов без тегов
    #             import re
    #             clean_text = re.sub ('<.*?>', '', msg.HTMLBody [:500])
    #             print (clean_text + "...")
    #         else:
    #             print ("Тело (текст):")
    #             print (msg.Body [:500] + "...")
    #
    #         print (f"Формат: {'HTML' if msg.HTMLBody else 'Текст'}")

    # read_html_message("work@company.com", "Входящие", 2)
    return messages

#------------------------------------------
# 3.6. Полная информация о сообщении (все свойства)
#------------------------------------------
def get_message_details (account_name, folder_name, message_index=1):
    outlook, namespace = OutlookApplication ()

    store = namespace.Folders [account_name]
    folder = store.Folders [folder_name]
    messages = folder.Items
    messages.Sort ("[ReceivedTime]", True)

    message = messages [message_index - 1]

    details = {
        'Subject': message.Subject,
        'SenderName': message.SenderName,
        'SenderEmail': message.SenderEmailAddress,
        'To': message.To,
        'CC': message.CC,
        'BCC': message.BCC,
        'ReceivedTime': message.ReceivedTime,
        # 'SentTime': message.SentTime,
        'Size': message.Size,
        'UnRead': message.UnRead,
        'Importance': message.Importance,  # 0=Low, 1=Normal, 2=High
        'HasAttachments': message.Attachments.Count > 0,
        'AttachmentCount': message.Attachments.Count,
        'Categories': message.Categories,
        'Body': message.Body,
        'HTMLBody': message.HTMLBody [:500] if message.HTMLBody else None,
    }

    # get_message_details("work@company.com", "Входящие", 1)
    return message, details

#------------------------------------------
# 3.7. Обработка ошибок и таймауты
#------------------------------------------
def safe_read_messages (account_name, folder_name, limit=5, retry=3):
    outlook = None

    for attempt in range (retry):
        try:
            outlook, namespace = OutlookApplication ()

            # Принудительная загрузка хранилищ
            namespace.Logon ()
            # datetime.time.sleep (1)

            store = namespace.Folders [account_name]
            folder = store.Folders [folder_name]
            messages = folder.Items
            messages.Sort ("[ReceivedTime]", True)

            count = min (limit, messages.Count)
            print (f"✅ Успешно. Сообщений: {count}")

            # for message in messages [:count]:
            # for message in enumerate (messages):
                # if message.Class == 43:
                #     print (f"  • {message.Subject}")

            return True

        except Exception as e:
            print (f"⚠ Попытка {attempt + 1}: {e}")
            # datetime.time.sleep (2)

    print ("❌ Не удалось подключиться после нескольких попыток")
    return False

    # safe_read_messages("work@company.com", "Входящие", 5)

#---------------------------------------------------------
# main
#---------------------------------------------------------
def main ():
#beginfunction
    ...
#endfunction

#---------------------------------------------------------
#
#---------------------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
