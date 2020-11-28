#!/usr/bin/env python
#  Copyright (c) 2020.
#  You can freely change the code part, but you must follow the MIT protocol
#  You cannot delete any information about UTS
#  You cannot use this program to disrupt social order.

import argparse
import json
import shelve
import os
import sys
from pytube import YouTube

# 多语言设置
file_lists = os.listdir(os.path.expanduser('~'))
if 'mop.json' in file_lists:
    file = open(os.path.expanduser('~/mop.json'), 'r')
    mop_db_path = json.load(file)
    file.close()
    mop_db = shelve.open(mop_db_path + 'mop')
    if mop_db['language'] == 'en':
        down_help = 'Download the file'
        dir_help = 'Set the default download folder'
        down_text = '开始下载 -->'
        successful = 'Success'
    else:
        down_help = '下载文件'
        dir_help = '设置默认下载文件夹'
        down_text = 'Downloading now -->'
        successful = '成功'
    mop_db.close()
else:
    print('Error|出错')
    sys.exit()

# 命令参数设置
parser = argparse.ArgumentParser(description='YouTubeDown-MacOS-11')

parser.add_argument('-d', type=str, help=down_help, nargs='+')
parser.add_argument('-dir', type=str, help=dir_help, nargs=1)

args = parser.parse_args()

if args.d:
    down_url_list = str(args.d[0]).split('&&')
    mop_db = shelve.open(mop_db_path + 'mop')
    for url in down_url_list:
        print(down_text+' '+url)
        if len(args.d) == 2:
            YouTube(url).streams.first().download(os.path.expanduser(str(args.d[1])))
        else:
            path = mop_db_path['save_path']
            YouTube(url).streams.first().download(os.path.expanduser(path))
    print(successful)
    mop_db.close()

if args.dir:
    mop_db = shelve.open(mop_db_path + 'mop')
    mop_db_path['save_path'] = str(args.dir[0])
    print(successful)
