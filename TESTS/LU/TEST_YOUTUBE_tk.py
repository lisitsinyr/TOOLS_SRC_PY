"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YOUTUBE_PY
     Python (PROJECTS)
 Module:
     TEST_YOUTUBE_tk.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys
import threading
import logging
import time

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
import pyperclip
import schedule
import pytube
import pytube.exceptions
from pytube import YouTube, request

import tkinter as tk

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import lyrpy.LULog as LULog
import lyrpy.LUConst as LUConst
from lyrpy.LUDoc import *
import lyrpy.LUObjectsYT as LUObjects
import lyrpy.LUYouTube as LUYouTube

is_paused = is_cancelled = False

root = tk.Tk ()
root.title ("YouTube Downloader")

def start_download():
    threading.Thread(target=download_video, args=(url_entry.get(),), daemon=True).start()

def toggle_download():
    global is_paused
    is_paused = not is_paused
    pause_button['text'] = 'Resume' if is_paused else 'Pause'

def cancel_download():
    global is_cancelled
    is_cancelled = True

download_button = tk.Button (root, text = 'Download', width = 20, command = start_download)
download_button.grid (row = 1, column = 2, sticky = 'e', padx = 10, pady = (0, 10))

pause_button = tk.Button (root, text = 'Pause', width = 10, command = toggle_download, state = 'disabled')
pause_button.grid (row = 2, column = 0)

progress = tk.Label (root)
progress.grid (row = 2, column = 1, sticky = 'w')

cancel_button = tk.Button (root, text = 'Cancel', width = 10, command = cancel_download, state = 'disabled')
cancel_button.grid (row = 2, column = 2, sticky = 'e')

tk.Label (root, text = 'URL:').grid (row = 0, column = 0, sticky = 'e')
url_entry = tk.Entry (root, width = 60)
url_entry.grid (row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)

def download_video(url):

    url = 'https://www.youtube.com/watch?v=Sx_NM3yX1vs'

    global is_paused, is_cancelled
    download_button['state'] ='disabled'
    pause_button['state'] ='normal'
    cancel_button['state'] ='normal'
    try:
        progress['text'] = 'Connecting ...'
        yt = YouTube(url)
        # yt = YouTube (url, use_oauth = True, allow_oauth_cache = True)
        stream = yt.streams.first()
        filesize = stream.filesize  # get the video size
        with open('sample.mp4', 'wb') as f:
            is_paused = is_cancelled = False
            stream = request.stream(stream.url) # get an iterable stream
            downloaded = 0
            while True:
                if is_cancelled:
                    progress['text'] = 'Download cancelled'
                    break
                if is_paused:
                    continue
                chunk = next(stream, None) # get next chunk of video
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress['text'] = f'Downloaded {downloaded} / {filesize}'
                else:
                    # no more data
                    progress['text'] = 'Download completed'
                    break
        print('done')
    except Exception as e:
        print(e)
    download_button['state'] ='normal'
    pause_button['state'] ='disabled'
    cancel_button['state'] ='disabled'

def TEST_YOUTUBE_tk ():
    """TEST_YOUTUBE_tk"""
#beginfunction
    PrintInfoObject('-----TEST_YOUTUBE_tk----')
    PrintInfoObject(TEST_YOUTUBE_tk)

    root.mainloop()
#endfunction

#------------------------------------------
#
#------------------------------------------
def Main ():
#beginfunction
    LULog.STARTLogging (LULog.TTypeSETUPLOG.tslINI,'LOG_INIT',
                        'LOGGING_FILEINI.log','LOGGING_FILEINI_json.log')

    TEST_YOUTUBE_tk ()
    ...
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
