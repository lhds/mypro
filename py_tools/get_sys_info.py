# -*- coding:cp936 -*-
# 获取本机硬件信息(Windows)

import wmi

w = wmi.WMI()
print "CPU型号，主频：\n"
for processor in w.Win32_Processor():
	print "Processor ID: %s" % processor.DeviceID
	print "\nProcess Name: %s" % processor.Name.strip()+"\n\n"

print "内存大小："
totalMemSize = 0
for memModule in w.Win32_PhysicalMemory():
	totalMemSize += int(memModule.Capacity)
print "\nMemory Capacity: %.2fMB" % ((totalMemSize + 1048575) / 1048576)+"\n\n"

print "硬盘使用情况："
for disk in w.Win32_LogicalDisk(DriveType=3):
	temp = disk.Caption+" %0.2f%% free" % (100.0 * long (disk.FreeSpace) / long (disk.Size))
	print '\n' + temp
print '\n'

print "\n显示IP和MAC：\n"
for interface in w.Win32_NetworkAdapterConfiguration(IPEnabled=1):
	print "网卡驱动信息："
	print interface.Description+'\n'
	print "网卡MAC地址："
	print interface.MACAddress+'\n'
	print "IPv4地址："
	print interface.IPAddress[0]+'\n'
	print "IPv6地址："
	print interface.IPAddress[1]+'\n'
	print '\n'
