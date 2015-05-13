# __author__ = 'wyb'
# -*- coding:utf-8 -*-
import os
import sys


def search(path, key):
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path, f)):
            search(os.path.join(path, f))
        else:
            if key in os.listdir(path):
                if f.find(key) is not -1:
                    print os.path.join(path, f)


if __name__ == '__main__':
    if len(sys.argv) is not 3:
        print u'输入参数不对！'
        print 'Usage:'
        print 'python input_path key'
    path = sys.argv[1]
    key = sys.argv[2]
    search(path, key)
    print u'搜索完成！'




