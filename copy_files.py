__author__ = 'wyb'
# -*- coding: utf-8 -*-
import os
import sys
import shutil
import time


def copy_files():
    input_files_path = r"G:\test\input"
    output_files_path = r"G:\test\output"
    remove_files_path = r"G:\test\remove_files"
    copy_list = []
    remove_list = []
    if not os.path.exists(output_files_path):
        os.mkdir(output_files_path)
    for file_name in os.listdir(input_files_path):
        copy_list.append(file_name)
    for remove_name in os.listdir(remove_files_path):
        remove_list.append(remove_name)
    copy_list = list(set(copy_list).difference(set(remove_list)))

    for copy_file in copy_list:
        cp_files_inputpath = os.path.join(input_files_path, copy_file)
        cp_files_outputpath = os.path.join(output_files_path, copy_file)
        try:
            shutil.copy(cp_files_inputpath, cp_files_outputpath)
            f = open(r"G:\test\Copying_log.txt", "a+")
            f.write(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())) + ":Copying   " + copy_file + "\n")
        except Exception as e:
            ex_type, ex_value, ex_traceback = sys.exc_info()
            print "Copy error:", e.meessage, ex_type, ex_value, ex_traceback
            with open(r"G:\test\Copying_log.txt", "a+") as f:
                f.write(time.strftime("%Y+%m-%d-%H-%M-%S", time.localtime(time.time())) + ":Copying Error   " +
                        copy_file + ":" + e.message + "\n")
        print "Copying %s from %s to %s" % (copy_file.decode("gbk").encode("utf-8"), input_files_path, output_files_path)


if __name__ == "__main__":
    copy_files()
    print "Copying finished!"





