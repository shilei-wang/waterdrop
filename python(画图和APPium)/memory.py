#!/usr/bin/python
# coding=utf-8

import psutil
from time import sleep,clock
from draw import *


min = 120
interval = 15  #(15半小时 30是1小时  60是2小时)

def get_pid(processName):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == processName:
            return pid
    return 0

PID = get_pid("iris.exe")

MemoryList = []
key = 0

for pos in range(1, min+1):
    rss = round(psutil.Process(PID).memory_info().rss/(1024*1024),2)

    if pos == 1:
        t_start = clock()
        m_start = rss
        key = rss

    MemoryList.append(rss)
    print('当前内存占用：', rss, 'MB pos=', pos, key)
    drawMemoryReport(MemoryList, pos, key)

    sleep(interval)
else:
    rss = round(psutil.Process(PID).memory_info().rss/(1024*1024),2)
    MemoryList.append(rss)
    t_end = clock()
    m_end = rss

    drawMemoryReport(MemoryList, pos+1, key)

    # mem_leak = m_end - m_start
    # period_sec = round((t_end-m_start)/60,2)
    # print(period_sec)
    # print(min,'分钟 内存泄漏：', mem_leak, 'MB')
























'''


info = psutil.virtual_memory()
print(u'',info.total)


print('总内存：', info.total)
print('内存占比：', info.percent)
print('cpu个数：', psutil.cpu_count())


# 1G = 1,048,576,k
# 4G = 4,190,392,320
'''