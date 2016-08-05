#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import glob
import time
from fabric.api import *

def remote_delete(ip, user, password, filename):
    with settings(
        hide('warnings', 'running', 'stdout'),
        # parallel = True,
        host_string=ip,
        user = user,
        password = password,
    ):
        with quiet():
            command = "ls " + root_dir + "/" + filename
            if run(command).succeeded:

                command = "rm -f " + root_dir + "/" + filename + " " + root_dir + "/" + filename + ".ifr"
                return [run(command).succeeded, filename]
            else:
                return [False, filename, "\"file not found\""]

def get_cfg():
    f = open("SimpleDeleteSender.cfg", "r")
    lines = f.readlines()
    for line in lines:
        if re.match('^#', line[0]):
            pass
        else:
            line = line.strip('\n')
            key = line.split('=')
            if re.match('Target_Information', key[0]):
                value = key[1].split(';')
                ip_list[value[0]] = [value[1], value[2]]
            else:
                config[key[0]] = key[1]
    f.close()

def main():

    if int(mode):
        pass
    else:
        if glob.glob(work_dir + "/" + delete_file):
            print ("exist delete_file(%s) in work directory!" % delete_file)
            exit()

        if glob.glob(import_dir + "/" + delete_file):

            os.rename(import_dir + "/" + delete_file, work_dir + "/" + delete_file)

            n_time = time.strftime("%Y-%m-%d-%H", time.localtime(time.time()))

            result_file = n_time + "_Result.txt"
            done_file = n_time + "_" + delete_file

            f_deletefile = open(work_dir + "/" + delete_file, "r")
            f_resultfile = open(result_dir + "/" + result_file, "w")

            lines = f_deletefile.readlines()
            for filename in lines:
                filename = filename.strip('\n')
                for ip in ip_list.keys():
                    result = remote_delete(ip, ip_list[ip][0], ip_list[ip][1], filename)
                    if result[0]:
                        f_resultfile.write(result[1] + ",success\n")
                    else:
                        f_resultfile.write(result[1] + ",fail," + result[2] + "\n")

            f_deletefile.close()
            f_resultfile.close()

            os.rename(work_dir + "/" + delete_file, result_dir + "/" + done_file)

if __name__ == '__main__':

    config = {}
    ip_list = {}

    get_cfg()

    transaction = config['Transaction_Path']
    import_dir = transaction + "/" + config['Import_Dir']
    work_dir = transaction + "/" + config['Temp_Dir']
    result_dir = transaction + "/" + config['Result_Dir']
    delete_file = config['Delete_File_Name']
    root_dir = config['RootDir']
    mode = config['Mode']

    #create default directory
    if not glob.glob(transaction): os.mkdir(transaction)
    if not glob.glob(import_dir): os.mkdir(import_dir)
    if not glob.glob(work_dir): os.mkdir(work_dir)
    if not glob.glob(result_dir): os.mkdir(result_dir)

    main()
