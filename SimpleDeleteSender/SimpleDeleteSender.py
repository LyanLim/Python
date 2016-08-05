#!/usr/bin/pathon
# -*- coding: utf-8 -*-

import re
import os
import glob
from fabric.api import *

def remote_delete(ip, password, user, filename):
    with settings(
        hide('warnings', 'running', 'stdout'),
        # parallel = True,
        host_string=ip,
        user = user,
        password = password,
    ):

        with cd(dst_path):
            with quiet():
                result = run(command).succeeded

    return result

def get_cfg():
    f = open("Remote_Commander.cfg", "r")
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

    if mode:
        pass
    else:
        for t_file in glob.glob(import_dir):
            if t_file == delete_file:
                #os.rename(import_dir + "/" + delete_file, work_dir + "/" + delete_file)
                print t_file

        # for ip in ip_list.keys():



if __name__ == '__main__':

    config = {}
    ip_list = {}

    get_cfg()


    import_dir = config['Import_Dir']
    work_dir = config['Temp_Dir']
    result_dir = config['Result_Dir']
    delete_file = config['Delete_File_Name']
    root_dir = config['RootDir']
    mode = config['Mode']
    main()



Import_Dir=/Users/hellolcs/GitHub/SimpleDeleteSender/Transaction/import
Delete_File_Name=deletefile.txt
Temp_Dir=/Users/hellolcs/GitHub/SimpleDeleteSender/Transaction/work
Result_Dir=/Users/hellolcs/GitHub/SimpleDeleteSender/Transaction/result
RootDir=/data/pub/hanaro