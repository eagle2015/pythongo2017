#!/usr/bin/env python
# --*-- coding: utf-8 --*--
#批量上传下载文件

import os
import sys
import time
import argparse
import paramiko
from multiprocessing import Pool, Manager

User = 'root'
Process_number = 8
Pkey_file = os.path.expanduser('~/.ssh/id_rsa')
Key = paramiko.RSAKey.from_private_key_file(Pkey_file)


def multiFTP(l, s, d, choice):
    try:
        host_ip = l.pop()
    except IndexError:
        sys.exit(1)

    try:
        t = paramiko.Transport((host_ip, 22))
        t.connect(username=User, pkey=Key)
        sftp = paramiko.SFTPClient.from_transport(t)
        if choice == 'get':
            local_file = os.path.join(s, host_ip + '_' + os.path.split(d)[-1])
            sftp.get(d, local_file)
            get_size = os.path.getsize(local_file)
            return (host_ip, 'Get size %d' % (get_size))
        elif choice == 'put':
            sftp.put(s, d)
            des_size = int(sftp.stat(d).st_size)
            return (host_ip, 'Put size %d' % (des_size))
        sftp.close()
    except Exception, e:
        return (host_ip, '%s exception' % (choice))


def run():
    p = argparse.ArgumentParser(description='这个工具主要用来并发下发文件到设备上，或者从设备上面获取文件')
    p.add_argument('-l', '--list', dest='list', type=argparse.FileType('rt'), help='从文件里面读取主机IP')
    p.add_argument('--stdout', dest='stdout', default=sys.stdout, type=argparse.FileType('wt'),
                   help='默认正确输出结果到屏蔽，指定参数可以将结果输出到文件')
    p.add_argument('--stderr', dest='stderr', default=sys.stderr, type=argparse.FileType('wt'),
                   help='默认错误输出结果到屏幕，指定参数可以将结果输出到文件')
    p.add_argument('-s', '--source', dest='src_file', type=str, help='指定源文件地址(当cmd为put时，指定上传文件，当cmd为get时，指定下载目录)')
    p.add_argument('-d', '--destination', dest='des_file', type=str, help='指定目的文件地址')
    p.add_argument('-c', '--command', dest='cmd', type=str, help='get从服务器下载文件，put上传文件到服务器')

    options = p.parse_args()
    if options.list:
        stdin = options.list
    else:
        p.print_help()
        sys.exit(1)

    if options.cmd == 'put':
        if options.des_file:
            des_file = options.des_file
        else:
            sys.exit('上传目的文件名没指定')

        cmd = options.cmd
        if os.path.exists(options.src_file):
            src_file = options.src_file
        else:
            sys.exit('上传源文件不存在')
    elif options.cmd == 'get':
        if options.des_file:
            des_file = options.des_file
        else:
            sys.exit('下载的目的文件没有指定')

        cmd = options.cmd
        if os.path.isdir(options.src_file):
            src_file = options.src_file
        else:
            sys.exit('必须指定一个下载目录')
    else:
        p.print_help()
        sys.exit(1)

    hosts_ip = [line.strip() for line in stdin.xreadlines()]
    stdin.close()

    pool = Pool(processes=Process_number)
    manager = Manager()
    l = manager.list(hosts_ip)
    res_alist = []
    for i in range(len(hosts_ip)):
        res_alist.append(pool.apply_async(multiFTP, (l, src_file, des_file, cmd)))

    for res in res_alist:
        print >> options.stdout, '%s\t\t%s' % (res.get())


def main():
    global hosts_ip
    hosts_ip = []

    run()


if __name__ == '__main__':
    main()