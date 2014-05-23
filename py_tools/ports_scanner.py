#coding=utf-8

import threading
import time
import Queue
import socket

# 常用端口
# 139,445 : NetBIOS/SMB服务，用于Windows"文件和打印机共享"和SAMBA，是IPC$入侵的主要通道
# 80 : HTTP协议
# 135 : 用于远程的打开对方的telnet服务，用于启动与远程计算机的RPC连接，找到这个计算机上运行Exchange Server、版本，还有些DOS攻击直接针对这个端口
# 1433 : SQL Server默认的端口，SQL Server服务使用两个端口：TCP-1433、UDP-1434
# 3389 : Windows 2000(2003) Server远程桌面的服务端口
# 8080 : 用于www代理服务，可能被病毒程序利用
# 137 : 在局域网中提供计算机的名字或IP地址查询服务
# 21 : FTP协议
# 23 : telnet端口
# 25 : 为SMTP服务器所开放，主要用于发送邮件，利用25端口，可以寻找SMTP服务器，用来转发垃圾邮件

port = [139, 445, 80, 135, 1433, 3389, 8080, 137, 21, 23, 25]#扫描常用端口
target = []
ip_range = "192.168.0."

queue = Queue.Queue()
for i in range(254):
    target.append("%s%s" % (ip_range, (i+1)))

for i in target:
    queue.put(i)

class ScanThread(threading.Thread):
    def run(self):
        global queue
        ip = queue.get()
        for p in port:
            s = socket.socket()
            s.settimeout(3)
            fp = open("list.txt", "wb")
            try:
                s.connect((ip, int(p)))
                print "\n----------------------------------------------------------"
                print "IP : %s , Port : %d , Open" % (ip, int(p))
                print "----------------------------------------------------------\n"
                sp = "IP : %s , Port : %d , Open" % (ip, int(p))

            expert:
                print ""

            

