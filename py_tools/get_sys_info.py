# -*- coding:cp936 -*-
# ��ȡ����Ӳ����Ϣ(Windows)

import wmi

w = wmi.WMI()
print "CPU�ͺţ���Ƶ��\n"
for processor in w.Win32_Processor():
	print "Processor ID: %s" % processor.DeviceID
	print "\nProcess Name: %s" % processor.Name.strip()+"\n\n"

print "�ڴ��С��"
totalMemSize = 0
for memModule in w.Win32_PhysicalMemory():
	totalMemSize += int(memModule.Capacity)
print "\nMemory Capacity: %.2fMB" % ((totalMemSize + 1048575) / 1048576)+"\n\n"

print "Ӳ��ʹ�������"
for disk in w.Win32_LogicalDisk(DriveType=3):
	temp = disk.Caption+" %0.2f%% free" % (100.0 * long (disk.FreeSpace) / long (disk.Size))
	print '\n' + temp
print '\n'

print "\n��ʾIP��MAC��\n"
for interface in w.Win32_NetworkAdapterConfiguration(IPEnabled=1):
	print "����������Ϣ��"
	print interface.Description+'\n'
	print "����MAC��ַ��"
	print interface.MACAddress+'\n'
	print "IPv4��ַ��"
	print interface.IPAddress[0]+'\n'
	print "IPv6��ַ��"
	print interface.IPAddress[1]+'\n'
	print '\n'
