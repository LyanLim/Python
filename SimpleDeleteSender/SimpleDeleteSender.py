#!/usr/bin/pathon
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from fabric.api import *

def deploy(ip, password, user, src_full_path, dst_path):
    with settings(
        hide('warnings', 'running', 'stdout'),
        # parallel = True,
        host_string=ip,
        user = user,
        password = password,
    ):

        result = put(src_full_path, dst_path).succeeded

    return result


def remote_commander(ip, password, user, dst_full_path, script_name, command):
    with settings(
        hide('warnings', 'running', 'stdout'),
        # parallel = True,
        host_string=ip,
        user = user,
        password = password,
    ):

        with cd(dst_full_path):
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
    for ip in ip_list.keys():

        if config['Excute_Mode']:
            if deploy(ip, ip_list[ip][1], ip_list[ip][0], src_full_path, dst_path):
                print ("deploy,%s,\"%s\" to \"%s\" upload,success" % (ip, src_full_path, dst_path))
                command = 'bash ' + dst_full_path + '/' + start_sctipt
                print ("remote_commander,%s,\"%s\" excute,%s" % (ip, command, remote_commander(ip, ip_list[ip], ip_list[ip][0], dst_full_path, start_sctipt, command)))
            else:
                print ("%s, File Transfer Fail" % ip)
        else:
            pass
if __name__ == '__main__':

    config = {}
    ip_list = {}

    #read config file
    get_cfg()

    src_path = config['Source_Dir_Path']
    src_dir_name= config['Source_Dir_Name']
    dst_path = config['Destination_Path']
    src_full_path = src_path + '/' + src_dir_name
    dst_full_path = dst_path + '/' + src_dir_name
    if int(config['Excute_Mode']):
        if config.get('Start_Sctipt'):
            start_sctipt = config['Start_Sctipt']
        else:
            exit("You must check config file : Start_Sctipt")

    main()

