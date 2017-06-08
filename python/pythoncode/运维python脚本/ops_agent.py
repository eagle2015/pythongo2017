#!/usr/bin/env  python
# -*- coding:utf-8 -*-
# =========================================
# Filename : ops_agent.py
# Filetype : Python
# Author   :
# Create   :
# =========================================

import os, sys, paramiko, re, csv
from optparse import OptionParser
from multiprocessing import Process, cpu_count, Lock
from time import sleep
from threading import Thread


def print_process_result():
    output_fmt = {}
    output_fmt['ERROR'] = '\033[31;5mERROR\033[0m'
    output_fmt['WRONG'] = '\033[33;1mWRONG\033[0m'
    output_fmt['RIGHT'] = '\033[32mRIGHT\033[0m'
    output_fmt['LOCAL'] = '\033[32mLOCAL\033[0m'
    csv_rfp = open('/tmp/agent_result.csv', 'rb')
    for record in csv.reader(csv_rfp):
        record[0] = record[0] + '-' * (15 - len(record[0]))
        record[1] = output_fmt[record[1]]
        print '-> '.join(record)
    csv_rfp.close()
    return


def write_csv(record):
    process_lock.acquire()
    csv_writer.writerow(record)
    process_lock.release()
    return


def time_out(record):
    sleep(options.timeout)
    write_csv(record)
    os.kill(os.getpid(), 9)
    return


def start_timer(record):
    if 0 >= options.timeout:
        return
    thread_timer = Thread(target=time_out, args=(record,))
    thread_timer.setDaemon(1)
    thread_timer.start()
    return


def ssh_command(ip):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=22, username='root', pkey=ssh_key, timeout=10)
    except Exception, e:
        write_csv((ip, 'ERROR', str(e)))
        return
    command = re.sub(r'IIPP', ip, options.remote_cmd)
    start_timer((ip, 'WRONG', 'TASK TIMEOUT'))
    stdin, stdout, stderr = ssh.exec_command(command)
    err = stderr.readlines()
    out = stdout.readlines()
    if err:
        write_csv((ip, 'WRONG', ' '.join([x.strip() for x in err])))
    else:
        write_csv((ip, 'RIGHT', ' '.join([x.strip() for x in out])))
    return


def ssh_transport(ip):
    try:
        t = paramiko.Transport((ip, 22))
        t.connect(username='root', pkey=ssh_key)
    except Exception, e:
        write_csv((ip, 'ERROR', str(e)))
        return
    sftp = paramiko.SFTPClient.from_transport(t)
    remote_file = re.sub(r'IIPP', ip, os.path.join(options.dst_path, os.path.basename(options.src_file)))
    start_timer((ip, 'WRONG', 'TASK TIMEOUT'))
    try:
        sftp.put(options.src_file, remote_file)
        write_csv((ip, 'RIGHT', ''))
    except Exception, e:
        write_csv((ip, 'WRONG', str(e)))
    return


def local_command(ip):
    command = re.sub(r'IIPP', ip, options.local_cmd)
    start_timer((ip, 'WRONG', 'TASK TIMEOUT'))
    result = os.popen(command)
    write_csv((ip, 'LOCAL', ' '.join([x.strip() for x in result.readlines()])))
    return


def check_pool_state(empty=False):
    while True:
        print "\033[2J\033[0;0H"
        for ip, process in process_list.items():
            if process.is_alive():
                print 'Handling', ip, '...'
            else:
                # print ip, '\033[32mfinished\033[0m'
                process_list.pop(ip)
        if not empty and options.process > len(process_list): break
        if empty and 0 == len(process_list): break
        sleep(0.5)
    return


def start_process_pool():
    for ip in ips:
        if options.remote_cmd:
            sub_process = Process(target=ssh_command, args=(ip,))
        elif options.src_file:
            sub_process = Process(target=ssh_transport, args=(ip,))
        elif options.local_cmd:
            sub_process = Process(target=local_command, args=(ip,))
        else:
            print 'Unknown parameter ...'
            sys.exit(1)
        sub_process.start()
        process_list[ip] = sub_process
        check_pool_state()
    check_pool_state(empty=True)
    return


def get_hosts(hosts_file):
    if '/dev/stdin' == hosts_file:
        print 'Specify no host file, enter ip manually here ...'
    try:
        fp = open(hosts_file, 'r')
    except Exception, e:
        print 'Failed to read hosts_file,', e
        sys.exit(1)
    ips = []
    for line in fp:
        matchs = re.match(r'^(10\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
        if matchs: ips.append(matchs.group(1))
    if 0 == len(ips):
        print 'No ips found, quit ...'
    return ips


def initial():
    global csv_writer, process_lock, ssh_key, ips, csv_fp, process_list
    try:
        ssh_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
        csv_fp = open('/tmp/agent_result.csv', 'wb', 0)
        csv_writer = csv.writer(csv_fp)
    except Exception, e:
        print e
        sys.exit(1)
    ips = get_hosts(options.host)
    process_lock = Lock()
    process_list = {}
    return


def get_options():
    global options
    usage = '%s\n\t-R remote-cmd -H ip-file -P process-num -T timeout' % sys.argv[0]
    usage += '\n\t-S local-file -D remote-dir -H ip-file -P process-num -T timeout'
    usage += '\n\t-L local-cmd -H ip-file -P process-num -T timeout'
    usage += '\nThe pattern "IIPP" in options "RSDL" will be replaced by the ip contained in each process.'
    usage += '\nThe result file is /tmp/agent_result.csv'
    parser = OptionParser(usage)
    parser.add_option('-R', '--remote_cmd', action='store', help='Run a shell command in remote servers.')
    parser.add_option('-S', '--src_file', action='store', help='specify the file to remote servers.')
    parser.add_option('-D', '--dst_path', action='store', help='specify the path in remote servers.')
    parser.add_option('-L', '--local_cmd', action='store', help='Run a shell command in localhost.')
    parser.add_option('-H', '--host', action='store', default='/dev/stdin', help='Specify the file contains ip.')
    parser.add_option('-P', '--process', action='store', default=cpu_count(), type='int',
                      help='Specify the num of processes.')
    parser.add_option('-T', '--timeout', action='store', default=0, type='int', help='Specify the seconds of timeout.')
    options, args = parser.parse_args()
    for opt in [options.src_file, options.dst_path, options.local_cmd]:
        if options.remote_cmd and opt:
            parser.print_help()
            sys.exit(1)
    for opt in [options.src_file, options.dst_path]:
        if options.local_cmd and opt:
            parser.print_help()
            sys.exit(1)
    if options.src_file and not options.dst_path or options.dst_path and not options.src_file:
        parser.print_help()
        sys.exit(1)
    if not options.remote_cmd and not options.src_file and not options.local_cmd:
        parser.print_help()
        sys.exit(1)
    return


def main():
    get_options()
    initial()
    start_process_pool()
    print_process_result()
    return 0


if '__main__' == __name__:
    main()



'''
使用：
Usage: ./agent.py
  -R remote-cmd -H ip-file -P process-num -T timeout
  -S local-file -D remote-dir -H ip-file -P process-num -T timeout
  -L local-cmd -H ip-file -P process-num -T timeout
The pattern "IIPP" in options "RSDL" will be replaced by the ip contained in each process.
The result file is /nmsmw/scripts/agent_result.csv

Options:
  -h, --help            show this help message and exit
  -R REMOTE_CMD, --remote_cmd=REMOTE_CMD
                        Run a shell command in remote servers.
  -S SRC_FILE, --src_file=SRC_FILE
                        specify the file to remote servers.
  -D DST_PATH, --dst_path=DST_PATH
                        specify the path in remote servers.
  -L LOCAL_CMD, --local_cmd=LOCAL_CMD
                        Run a shell command in localhost.
  -H HOST, --host=HOST  Specify the file contains ip.
  -P PROCESS, --process=PROCESS
                        Specify the num of processes.
  -T TIMEOUT, --timeout=TIMEOUT
                        Specify the seconds of timeout.
根据Usage显示目前支持三种用法：
1 批量连接远程服务器执行远程命令
2 批量连接远程服务器上传文件
3 批量运行本地命令
参数中的“IIPP”会被匹配换成 -H指定的列表文件中的每一个ip

'''

