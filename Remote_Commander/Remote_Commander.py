# -*- coding: utf-8 -*-

from fabric.api import *

def deploy(ip, password, user='root'):
    with settings(
        hide('warnings', 'running', 'stdout', 'stderr'),
        host_string=ip,
        user = user,
        password = password
    ):
        #put('kk.txt', '/root/')
        result=run("hostname")

    return result


def main():
    ip_list = {
        '1.255.85.210'  :   'dev123$%^',
        '1.255.85.211'  :   'tbdev12!(',
        '1.255.85.212'  :   'tbdev12!(',
        '1.255.85.213'  :   'tbdev12!(',
        '1.255.85.214'  :   'tbdev12!(',
        '1.255.85.215'  :   'tbdev12!(',
        '1.255.85.219'  :   'tbdev12!(',
    }

    for ip in ip_list.keys():
        print deploy(ip, ip_list[ip])

if __name__ == '__main__':
    main()