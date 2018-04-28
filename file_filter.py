#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
import win32api
from win32api import GetFileVersionInfo, LOWORD, HIWORD
import sys

def getFileProperties(fname):
    """
    读取给定文件的所有属性, 返回一个字典.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
        'CompanyName', 'LegalCopyright', 'ProductVersion',
        'FileDescription', 'LegalTrademarks', 'PrivateBuild',
        'FileVersion', 'OriginalFilename', 'SpecialBuild')
 
    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}
 
    try:
        #len = win32api.GetfileVersionSize(fname,0)
        fixedInfo = GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                fixedInfo['FileVersionLS'] % 65536)
 
        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]
 
        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above
 
        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            ## print str_info
            strInfo[propName] = GetFileVersionInfo(fname, strInfoPath)
 
        props['StringFileInfo'] = strInfo
    except:
        print('GetLastError:',win32api.GetLastError())
        pass
 
    return props

if __name__ == "__main__":
    print('start>>>')
    #print(getFileProperties('./NFCDndToolM24.exe'))
    #print(getFileProperties('./000260a.mts'))
    print(getFileProperties('./aa.txt'))
    print('stop<<<')
'''

import win32api
from win32api import GetFileVersionInfo, LOWORD, HIWORD


def get_version_number (filename):
  info = win32api.GetFileVersionInfo(filename,"\\")
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)


if __name__ == '__main__':
#  import os
#  filename = os.environ["COMSPEC"]
#  print ".".join ([str (i) for i in get_version_number ("./aa.txt")])    
   print(get_version_number ("./aa.txt"))


'''
import os,filever

myPath="C:\\path\\to\\check"

for root, dirs, files in os.walk(myPath):
    for file in files:
        file = file.lower() # Convert .EXE to .exe so next line works
        if (file.count('.exe') or file.count('.dll')): # Check only exe or dll files
            fullPathToFile=os.path.join(root,file)
            major,minor,subminor,revision=filever.get_version_number(fullPathToFile)
            print "Filename: %s \t Version: %s.%s.%s.%s" % (file,major,minor,subminor,revision)
'''

'''
from win32com.client import Dispatch

ver_parser = Dispatch('Scripting.FileSystemObject')
info = ver_parser.GetFileVersion("F:/recover2/aa.txt")

if info == 'No Version Information Available':
    info = None
'''    