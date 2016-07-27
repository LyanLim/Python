# -*- coding: utf-8 -*-

from fabric.api import *

def deploy(ip, password, user, src_full_path, dst_path):
    with settings(
        hide('warnings', 'running', 'stdout'),
        #parallel = True,
        host_string=ip,
        user = user,
        password = password,
    ):
        result = put(src_full_path, dst_path).succeeded

    return result


def remote_commander(ip, password, user, dst_full_path, script_name):

    command = 'ls `cat ' + dst_full_path + '/' + script_name + '`'
    with settings(
        hide('warnings', 'running', 'stdout'),
        #parallel = True,
        host_string=ip,
        user = user,
        password = password,
    ):

        with cd(dst_full_path):
            with quiet():
                result = run(command).succeeded

    return result


def main():
    ip_list = {
        '1.255.85.210'  :   'dev123$%^',
        '1.255.85.211'  :   'tbdev12!(',
        '1.255.85.212'  :   'tbdev12!(',
        '1.255.85.213'  :   'tbdev12!(',
        '1.255.85.214'  :   'tbdev12!(',
        '1.255.85.215'  :   'tbdev12!(',
        '1.255.85.219'  :   'tbdev12!('
    }

    for ip in ip_list.keys():
        if deploy(ip, ip_list[ip], user_id, src_full_path, dst_path):
            print ("remote_commander,%s,%s" % (ip, remote_commander(ip, ip_list[ip], user_id, dst_full_path, 'filelist1.txt')))
        else:
            print ("%s, File Transfer Fail" % ip)


if __name__ == '__main__':
    user_id='root'
    src_path = './'
    src_dir_name='transfer'
    dst_path='/home'
    src_full_path = src_path + src_dir_name
    dst_full_path = dst_path + '/' + src_dir_name

    # start!!
    main()

