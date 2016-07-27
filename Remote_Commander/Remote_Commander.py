# -*- coding: utf-8 -*-

from fabric.api import *

def deploy(ip, password, user='root'):
    with settings(
            hide('warnings', 'running', 'stdout'),
            #parallel = True,
            host_string=ip,
            user = user,
            password = password,
            cwd = '/home/'
            #warn_only = True
        ):
            result = put('filelist.txt', '/home/').succeeded

    return result


def remote_commander(ip, password, user='root'):
    with settings(
            hide('warnings', 'running', 'stdout'),
            #parallel = True,
            host_string=ip,
            user = user,
            password = password,
            cwd = '/home/'
            #warn_only = True
        ):
            # with prefix("hostname"), prefix('echo "test : "'):

            with cd('/home'):
                 with quiet():
                     result = run('ls `cat filelist.txt`').succeeded
                    # result = run('bash test.sh')
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
        if deploy(ip, ip_list[ip]):
            print ("%s :: %s" % (ip, remote_commander(ip, ip_list[ip])))
        else:
            print ("%s, File Transfer Fail" % ip)


if __name__ == '__main__':
    main()


