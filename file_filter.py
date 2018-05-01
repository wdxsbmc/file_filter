#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win_unicode_console
win_unicode_console.enable()
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

#import win32api
#from win32api import GetFileVersionInfo, LOWORD, HIWORD

import pefile
import requests
import moviepy
from moviepy.editor import VideoFileClip

import subprocess
import re

import os

def get_mts_info(filename):
    result = subprocess.Popen(["ffprobe", filename],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print(FFprobe(filename).Video)
    #return [x for x in result.stdout.readlines()]

    #for x in result.stdout.readlines:
    #    if(x)

    #for i in iter(result.stdout.readline,'b'):
    #    print(i)

    #list1 = ['a','b']
    #return [x for x in list1]
    #print(re.split(r'[;|,\r\n]+',result.stdout.readlines()))
    result_list = result.stdout.readlines()
    for x in result_list:
        #x.decode('UTF-8')
        if(x.find(b'Video: h264'and b'29.97 fps') > 0 ):
            #print(x)
            return 1
    return 0


def del_mts_file(path):
    if os.path.exists(path):
        #删除文件，可使用以下两种方法。
        os.remove(path)

def get_vedio_info(path):
    clip = VideoFileClip(path)
    print(clip.duration)  # second


'''
def LOWORD(dword):
    return dword & 0x0000ffff
def HIWORD(dword): 
    return dword >> 16
def get_product_version(path):
#just for exe|sys|dll  win32 file
    pe = pefile.PE(path)
    print(PE.dump_info())

    ms = pe.VS_FIXEDFILEINFO.ProductVersionMS
    ls = pe.VS_FIXEDFILEINFO.ProductVersionLS
    return (HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls))

def get_version_number (filename):
  nSize = win32api.GetfileVersionSize(filename,0)
  print('nSize=', nSize)
  info = win32api.GetFileVersionInfo(filename,"\\")
  ms = info['FileVersionMS']
  ls = info['FileVersionLS']
  return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
'''

if __name__ == '__main__':
    #  import os
    #  filename = os.environ["COMSPEC"]
    #  print ".".join ([str (i) for i in get_version_number ("./aa.txt")])
    # print(get_product_version ("C:/Users/lmfpe/workspace/tsb/python/file_filter/aa.txt"))
   # print(get_mts_info("D:/workspace_bi/python/file_filter/001955.mts"))
    #print(get_mts_info("D:/workspace_bi/python/file_filter/014512.mts"))
    # print(get_vedio_info("C:/Users/lmfpe/workspace/tsb/python/file_filter/aa.avi"))
    #print(get_version_number ("./aa.txt"))
#    mts_info = get_mts_info("C:/Users/lmfpe/workspace/tsb/python/file_filter/002775.mts")
#    propNames = ('Video', 'InternalName', 'ProductName',
#         'CompanyName', 'LegalCopyright', 'ProductVersion',
#         'FileDescription', 'LegalTrademarks', 'PrivateBuild',
#         'FileVersion', 'OriginalFilename', 'SpecialBuild')

#    props = {'Video': None, 'StringFileInfo': None, 'FileVersion': None}
#    props['Video'] = mts_info[]

     #check_result = get_mts_info("C:/Users/lmfpe/workspace/tsb/python/file_filter/002775.mts")
     #if(check_result != b'1920X1080'):
         #del file



    #myPath="D:/workspace_bi/python/file_filter/test/"
    myPath = "E:/recover2"
    print("start at :",myPath)
    del_count = 0
    for root, dirs, files in os.walk(myPath):
        for file in files:
            file = file.lower() # Convert .EXE to .exe so next line works
            if (file.count('.mts')): # Check only exe or dll files
                fullPathToFile=os.path.join(root,file)
                ret = get_mts_info(fullPathToFile)
                print(fullPathToFile)
                if(ret != 1):
                    #del mts file
                    del_mts_file(fullPathToFile)
                    del_count += 1
                    print(str(del_count))

    print("total del:",str(del_count))


'''
from win32com.client import Dispatch

ver_parser = Dispatch('Scripting.FileSystemObject')
info = ver_parser.GetFileVersion("F:/recover2/aa.txt")

if info == 'No Version Information Available':
    info = None
'''
