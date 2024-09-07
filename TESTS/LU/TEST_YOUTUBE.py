"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YOUTUBE_PY
     Python (PROJECTS)
 Module:
     TEST_YOUTUBE.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import threading
import time
import datetime

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pyperclip
import schedule
import pytube
import pytube.exceptions

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
from lyrpy.LUDoc import *
import lyrpy.LUos as LUos
import lyrpy.LUObjectsYT as LUObjectsYT
import lyrpy.LUYouTube as LUYouTube
import lyrpy.LUFile as LUFile
import lyrpy.LUStrUtils as LUStrUtils
import lyrpy.LUDict as LUDict
import lyrpy.LUDateTime as LUDateTime

def TEST_YOUTUBE_Proc ():
    """TEST_YOUTUBE_Proc"""
#beginfunction
    PrintInfoObject('-----TEST_YOUTUBE_Proc----')
    PrintInfoObject(TEST_YOUTUBE_Proc)
#endfunction

def TEST_YOUTUBE_01_DownloadURL ():
    """TEST_YOUTUBE_00_DownloadURL"""
#beginfunction
    PrintInfoObject ('-----TEST_YOUTUBE_01_DownloadURL----')
    PrintInfoObject(TEST_YOUTUBE_01_DownloadURL)

    CPATH = os.path.join (LUos.GetCurrentDir(), 'WORK')
    if not LUFile.DirectoryExists (CPATH):
        LUFile.ForceDirectories (CPATH)
    #endif

    LURLs = dict()
    LURL_12 = 'https://www.youtube.com/watch?v=Sx_NM3yX1vs'
    LUObjectsYT.CheckURLs (LURL_12, LURLs)
    LURL_02 = 'https://www.youtube.com/playlist?list=PLtIhFg9DB4TsQuHjmSh3H1YwhMdHF7bCz'
    LUObjectsYT.CheckURLs (LURL_02, LURLs)

    for LURL, value in LURLs.items ():
        # print(LURL, value)
        if len(value['PlayListName']) > 0:
            LPATH = os.path.join (CPATH, value['PlayListName'])
            if not LUFile.DirectoryExists (LPATH):
                LUFile.ForceDirectories (LPATH)
            Lfilename_prefix = LUStrUtils.AddChar('0', str(value['NN']), 3)+'. '
        else:
            LPATH = CPATH
            Lfilename_prefix = 'test'
            Lfilename_prefix = ''
        #endif

        LMaxRes = LUObjectsYT.cMaxRes1080p
        LMaxRes = LUObjectsYT.cMaxRes480p
        LUObjectsYT.DownloadURL (LURL, LPATH, LMaxRes, ADownload=True,
                                 filename_prefix = Lfilename_prefix,
                                 type='video', file_extension='mp4')
    #endfor
#endfunction

def TEST_YOUTUBE_02_YouTubeObjectsItem ():
    """TEST_YOUTUBE_02_YouTubeObjectsItem"""
#beginfunction
    PrintInfoObject ('-----TEST_YOUTUBE_02_YouTubeObjectsItem----')
    PrintInfoObject(TEST_YOUTUBE_02_YouTubeObjectsItem)

    # CPATH = 'd:\\work'
    CPATH = os.path.join (LUos.GetCurrentDir(), 'WORK')
    if not LUFile.DirectoryExists (CPATH):
        LUFile.ForceDirectories (CPATH)
    #endif

    LURLs = dict()
    LURL_12 = 'https://www.youtube.com/watch?v=Sx_NM3yX1vs'
    LUObjectsYT.CheckURLs (LURL_12, LURLs)
    LURL_02 = 'https://www.youtube.com/playlist?list=PLtIhFg9DB4TsQuHjmSh3H1YwhMdHF7bCz'
    LUObjectsYT.CheckURLs (LURL_02, LURLs)

    # LTYouTube
    LTYouTube = LUYouTube.TYouTube (CPATH)
    for LURL, value in LURLs.items ():
        s = 'CreateObject...'
        LULog.LoggerTOOLS.log(LULog.PROCESS, s)
        LObjectID: datetime = LUDateTime.Now()
        s = LUDateTime.GenerateObjectIDStr (LObjectID)
        LULog.LoggerTOOLS.log(LULog.PROCESS, s)

        # LYouTubeObjectItem
        LMaxRes = LUObjectsYT.cMaxRes1080p
        LMaxRes = LUObjectsYT.cMaxRes480p
        LYouTubeObjectsItem = LTYouTube.YouTubeObjectsCollection.AddItem()
        LYouTubeObjectsItem.YouTubeObject.ID = LObjectID
        LYouTubeObjectsItem.YouTubeObject.SetURL(LURL, LMaxRes, value['PlayListName'],
                                                 value['NN'], value['N'])
        # LYouTubeObjectsItem.YouTubeObject.FONcomplete = LYouTubeObjectsItem.ONcomplete
        # LYouTubeObjectsItem.YouTubeObject.FONprogress = LYouTubeObjectsItem.ONprogress
        LYouTubeObjectsItem.YouTubeObject.SetStream(LMaxRes)
    #endfor
    for i in range (len(LTYouTube.YouTubeObjectsCollection)):
        LYouTubeObjectsItem: LUYouTube.TYouTubeObjectsItem = LTYouTube.YouTubeObjectsCollection[i]
        LPATH = CPATH
        Lfilename_prefix = 'test'
        Lfilename_prefix = ''
        LYouTubeObjectsItem.YouTubeObject.DownloadURL (LPATH)
    #endfor
#endfunction

def TEST_YOUTUBE_03_YouTubeObjectsItem_Thread ():
    """TEST_YOUTUBE_03_YouTubeObjectsItem_Thread"""
#beginfunction
    PrintInfoObject ('-----TEST_YOUTUBE_03_YouTubeObjectsItem_Thread----')
    PrintInfoObject(TEST_YOUTUBE_03_YouTubeObjectsItem_Thread)

    # CPATH = 'd:\\work'
    CPATH = os.path.join (LUos.GetCurrentDir(), 'WORK')
    if not LUFile.DirectoryExists (CPATH):
        LUFile.ForceDirectories (CPATH)
    #endif

    LURLs = dict()
    LURL_12 = 'https://www.youtube.com/watch?v=Sx_NM3yX1vs'
    LUObjectsYT.CheckURLs (LURL_12, LURLs)
    LURL_02 = 'https://www.youtube.com/playlist?list=PLtIhFg9DB4TsQuHjmSh3H1YwhMdHF7bCz'
    LUObjectsYT.CheckURLs (LURL_02, LURLs)

    # LTYouTube
    LTYouTube = LUYouTube.TYouTube (CPATH)
    for LURL, value in LURLs.items ():
        s = 'CreateObject...'
        LULog.LoggerTOOLS.log(LULog.PROCESS, s)
        LObjectID: datetime = LUDateTime.Now()
        s = LUDateTime.GenerateObjectIDStr (LObjectID)
        LULog.LoggerTOOLS.log(LULog.PROCESS, s)

        # LYouTubeObjectItem
        LMaxRes = LUObjectsYT.cMaxRes1080p
        LMaxRes = LUObjectsYT.cMaxRes480p
        LYouTubeObjectsItem = LTYouTube.YouTubeObjectsCollection.AddItem()
        LYouTubeObjectsItem.YouTubeObject.ID = LObjectID
        LYouTubeObjectsItem.YouTubeObject.SetURL(LURL, LMaxRes, value['PlayListName'],
                                                 value['NN'], value['N'])
        # LYouTubeObjectsItem.YouTubeObject.FONcomplete = LYouTubeObjectsItem.ONcomplete
        # LYouTubeObjectsItem.YouTubeObject.FONprogress = LYouTubeObjectsItem.ONprogress
        LYouTubeObjectsItem.YouTubeObject.SetStream (LMaxRes)
    #endfor
    for i in range (len(LTYouTube.YouTubeObjectsCollection)):
        LYouTubeObjectsItem: LUYouTube.TYouTubeObjectsItem = LTYouTube.YouTubeObjectsCollection[i]
        LPATH = CPATH
        Lfilename_prefix = 'test'
        Lfilename_prefix = ''
        LYouTubeObjectsItem.YouTubeObject.StartYouTubeThread(LPATH,
                                                             ADownload=True, Achunk=True,
                                                             filename_prefix=Lfilename_prefix)
    #endfor

    # Ждем завершения работы всех потоков
    while len (threading.enumerate()) > 1:
        ...

    # Остался главный поток python
    for tread in threading.enumerate():
        s = f'Остался главный поток python={tread}'
        LULog.LoggerAPPS_AddInfo(s)

    # for i in range (len(LTYouTube.YouTubeObjectsCollection)):
    #     LYouTubeObjectsItem: LUYouTube.TYouTubeObjectsItem = LTYouTube.YouTubeObjectsCollection[i]
    #     s = f'LYouTubeObjectsItem.YouTubeObject.URL={LYouTubeObjectsItem.YouTubeObject.URL}'
    #     LULog.LoggerAPPS_AddInfo(s)
    # #endfor
#endfunction

def TEST_YOUTUBE_04_YouTubeObject ():
    """TEST_YOUTUBE_04_YouTubeObject"""
#beginfunction
    PrintInfoObject ('-----TEST_YOUTUBE_04_YouTubeObject----')
    PrintInfoObject (TEST_YOUTUBE_04_YouTubeObject)

    # CPATH = 'd:\\work'
    CPATH = os.path.join (LUos.GetCurrentDir(), 'WORK')
    if not LUFile.DirectoryExists (CPATH):
        LUFile.ForceDirectories (CPATH)
    #endif

    LURLs = dict()
    LURL_12 = 'https://www.youtube.com/watch?v=Sx_NM3yX1vs'
    LUObjectsYT.CheckURLs (LURL_12, LURLs)
    LURL_02 = 'https://www.youtube.com/playlist?list=PLtIhFg9DB4TsQuHjmSh3H1YwhMdHF7bCz'
    LUObjectsYT.CheckURLs (LURL_02, LURLs)

    for LURL, value in LURLs.items ():
        s = 'CreateObject...'
        LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        s = LURL
        LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        LObjectID: datetime = LUDateTime.Now ()
        s = LUDateTime.GenerateObjectIDStr (LObjectID)
        LULog.LoggerTOOLS.log (LULog.PROCESS, s)

        # LYouTubeObject
        LYouTubeObject = LUObjectsYT.TYouTubeObject (CPATH)
        LYouTubeObject.ID = LObjectID
        LMaxRes = LUObjectsYT.cMaxRes1080p
        LMaxRes = LUObjectsYT.cMaxRes480p
        LYouTubeObject.SetURL(LURL, LMaxRes, value['PlayListName'],
                                                 value['NN'], value['N'])
        # LYouTubeObject.FONcomplete = ONcomplete
        # LYouTubeObject.FONprogress = ONprogress
        # LYouTubeObject.FONcomplete = complete_func
        # LYouTubeObject.FONprogress = progress_func
        LYouTubeObject.SetStream(LMaxRes)
        Lfilename_prefix = 'test'
        Lfilename_prefix = ''
        LYouTubeObject.DownloadURL (CPATH)

    #endfor
#endfunction

def TEST_YOUTUBE_05_YouTubeObject_Thread ():
    """TEST_YOUTUBE_05_YouTubeObject_Thread"""
#beginfunction
    PrintInfoObject ('-----TEST_YOUTUBE_05_YouTubeObject_Thread----')
    PrintInfoObject (TEST_YOUTUBE_05_YouTubeObject_Thread)

    # CPATH = 'd:\\work'
    CPATH = os.path.join (LUos.GetCurrentDir(), 'WORK')
    if not LUFile.DirectoryExists (CPATH):
        LUFile.ForceDirectories (CPATH)
    #endif

    LURLs = dict()
    LURL_12 = 'https://www.youtube.com/watch?v=Sx_NM3yX1vs'
    LUObjectsYT.CheckURLs (LURL_12, LURLs)
    LURL_02 = 'https://www.youtube.com/playlist?list=PLtIhFg9DB4TsQuHjmSh3H1YwhMdHF7bCz'
    LUObjectsYT.CheckURLs (LURL_02, LURLs)

    for LURL, value in LURLs.items ():
        s = 'CreateObject...'
        LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        s = LURL
        LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        LObjectID: datetime = LUDateTime.Now ()
        s = LUDateTime.GenerateObjectIDStr (LObjectID)
        LULog.LoggerTOOLS.log (LULog.PROCESS, s)

        # LYouTubeObject
        LYouTubeObject = LUObjectsYT.TYouTubeObject (CPATH)
        LYouTubeObject.ID = LObjectID
        LMaxRes = LUObjectsYT.cMaxRes1080p
        LMaxRes = LUObjectsYT.cMaxRes480p
        LYouTubeObject.SetURL(LURL, LMaxRes, value['PlayListName'],
                                                 value['NN'], value['N'])
        LYouTubeObject.SetStream(LMaxRes)
        # LYouTubeObject.FONcomplete = ONcomplete
        # LYouTubeObject.FONprogress = ONprogress
        # LYouTubeObject.FONcomplete = complete_func
        # LYouTubeObject.FONprogress = progress_func
        Lfilename_prefix = 'test'
        Lfilename_prefix = ''
        LYouTubeObject.StartYouTubeThread (CPATH, ADownload=True, Achunk=True,
                                           filename_prefix=Lfilename_prefix)

    #endfor

    # Ждем завершения работы всех потоков
    while len (threading.enumerate ()) > 1:
        ...

    # Остался главный поток python
    for tread in threading.enumerate ():
        s = f'Остался главный поток python={tread}'
        LULog.LoggerAPPS_AddInfo(s)
    #endfor
#endfunction

clipboard = []

def job ():
#beginfunction
    # CPATH = 'd:\\work'
    CPATH = os.path.join (LUos.GetCurrentDir (), 'WORK')
    if not LUFile.DirectoryExists (CPATH):
        LUFile.ForceDirectories (CPATH)
    #endif

    LULog.LoggerAPPS_AddInfo ('job ()')
    last_copied = pyperclip.paste ()
    if last_copied not in clipboard and ("www.youtube.com" in last_copied or "youtu.be" in last_copied):
        LULog.LoggerAPPS_AddInfo (last_copied)
        clipboard.append (last_copied)

        LURLs = dict ()
        LUObjectsYT.CheckURLs (last_copied, LURLs)
        for LURL, value in LURLs.items ():
            s = 'CreateObject...'
            LULog.LoggerTOOLS.log (LULog.PROCESS, s)
            s = LURL
            LULog.LoggerTOOLS.log (LULog.PROCESS, s)
            LObjectID: datetime = LUDateTime.Now ()
            s = LUDateTime.GenerateObjectIDStr (LObjectID)
            LULog.LoggerTOOLS.log (LULog.PROCESS, s)
            # LYouTubeObject
            LYouTubeObject = LUObjectsYT.TYouTubeObject (CPATH)
            LYouTubeObject.ID = LObjectID
            LMaxRes = LUObjectsYT.cMaxRes1080p
            LMaxRes = LUObjectsYT.cMaxRes480p
            LYouTubeObject.SetURL (LURL, LMaxRes, value ['PlayListName'],
                                   value ['NN'], value ['N'])
            LYouTubeObject.SetStream (LMaxRes)
            Lfilename_prefix = 'test'
            Lfilename_prefix = ''
            LYouTubeObject.StartYouTubeThread (CPATH, ADownload = True, Achunk = True,
                                               filename_prefix = Lfilename_prefix)
        #endfor

        # Llist = LUObjectsYT.CheckURLs(last_copied, LUObjectsYT.cMaxRes480p)
        # for item in Llist:
        #     LYouTubeObject: LUObjectsYT.TYouTubeObject = item
        #     s = LYouTubeObject.URL
        #     LULog.LoggerAPPS_AddInfo (s)
        #     Lfilename_prefix = 'test'
        #     Lfilename_prefix = ''
        #     try:
        #         LYouTubeObject.StartYouTubeThread (CPATH, ADownload=True, Achunk=True,
        #                                            filename_prefix=Lfilename_prefix)
        #     except str(pytube.exceptions.VideoUnavailable) as ERROR:
        #         s = 'Ошибка загрузки! '+ERROR
        #         LULog.LoggerAPPS.exception (s, exc_info=True, stack_info=True)
        #         LULog.LoggerAPPS_AddLevel_exception (s, exc_info=True, stack_info=True)
        #     #endtry
        # #endfor
    #endif
#endfunction

def TEST_YOUTUBE_06_YouTubeObject_Thread_Cliboard ():
    """TEST_YOUTUBE_06_YouTubeObject_Thread_Cliboard"""
#beginfunction
    PrintInfoObject ('-----TEST_YOUTUBE_06_YouTubeObject_Thread_Cliboard----')
    PrintInfoObject (TEST_YOUTUBE_06_YouTubeObject_Thread_Cliboard)

    # schedule.every (1).seconds.do (job)
    while True:
        job()
        time.sleep(1)
        # continue

    # Ждем завершения работы всех потоков
    while len (threading.enumerate ()) > 1:
        ...

    # Остался главный поток python
    for tread in threading.enumerate ():
        s = f'Остался главный поток python={tread}'
        LULog.LoggerAPPS_AddInfo(s)
#endfunction

#------------------------------------------
#
#------------------------------------------
def Main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_YOUTUBE_Proc ()

    #--------- TYouTube -----------------
    TEST_YOUTUBE_01_DownloadURL ()

    TEST_YOUTUBE_02_YouTubeObjectsItem ()
    # TEST_YOUTUBE_03_YouTubeObjectsItem_Thread ()
    TEST_YOUTUBE_04_YouTubeObject ()
    # TEST_YOUTUBE_05_YouTubeObject_Thread ()
    # TEST_YOUTUBE_06_YouTubeObject_Thread_Cliboard ()

#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Main ()
else:
    ...
#endif

#endmodule
