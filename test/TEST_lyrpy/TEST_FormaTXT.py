"""TEST_LULog.py"""
# -*- coding: UTF-8 -*-
__annotations__ = """
 =======================================================
 Copyright (c) 2024
 Author:
     Lisitsin Y.R.
 Project:
     LU_PY
     Python (LU)
 Module:
     TEST_FormaTXT.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import textwrap
import sys
import os
import chardet

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКА LU 
#------------------------------------------
#import LULog

#--------------------------------------------------------------------------------
# GetFileEncoding (AFileName: str) -> str:
#--------------------------------------------------------------------------------
def GetFileEncoding (AFileName: str) -> str:
    """GetFileEncoding"""
#beginfunction
    LFile = open (AFileName, 'rb')
    LRawData = LFile.read ()
    LResult = chardet.detect (LRawData)
    LEncoding = LResult ['encoding']
    LFile.close ()
    return LEncoding
#endfunction

#------------------------------------------
def main ():
#beginfunction
    # Set default width
    default_width = 80

    def print_usage():
        print("Usage:", sys.argv[0], "<input file> [width (default:", default_width, ")]")
        sys.exit(1)

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print_usage()

    filename = sys.argv[1]

    # Check if the file exists
    if not os.path.isfile(filename):
        print("Error: The file", filename, "does not exist.")
        print_usage()

    # Use the provided width if available, otherwise use the default
    width = int(sys.argv[2]) if len(sys.argv) == 3 else default_width

    #!!!! check File encoding
    cDefaultEncoding = 'utf8'
    encodingFILE = GetFileEncoding (filename)
    if encodingFILE == '':
        encodingFILE = cDefaultEncoding
    #endif

    with open(filename, 'r') as file:
    # with open(filename, 'r', encoding='utf8') as file:
        content = file.read()

    #!!!! paragraphs = content.split('\r\n')
    paragraphs = content.split('\n')

    formatted_paragraphs = []

    for paragraph in paragraphs:
        # Remove newline characters within paragraphs
        #!!!! paragraph = paragraph.replace('\n', ' ')
        formatted_paragraphs.append(textwrap.fill(paragraph, width=width))

    #!!!! with open(filename, 'w') as file:
    with open(filename, 'w', encoding='utf8') as file:
        #!!!! file.write('\n\n'.join(formatted_paragraphs))
        file.write('\n'.join(formatted_paragraphs))
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
