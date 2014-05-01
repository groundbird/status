#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from numpy import loadtxt
from sys import argv, stdout
import subprocess as sp

def tail(fname):
    d = sp.Popen('tail -n 1 %s' % fname, shell=True, stdout=sp.PIPE)
    data = d.stdout.readline().split()
    dictTemp = {'Time':0, 'Unix Time':1,
                'He3U Head':8, 'He3I Head':9, 'He4 Head':10,
                'He4 Film Burner':12,
                'He4 Pump':13, 'He3I Pump':14, 'He3U Pump':15,
                'He4 SW':16, 'He3I SW':17, 'He3U SW':18}
    t    = data[dictTemp['Time']]
    ts   = float(data[dictTemp['Unix Time']])
    he3u = float(data[dictTemp['He3U Head']])
    he3i = float(data[dictTemp['He3I Head']])
    he4  = float(data[dictTemp['He4 Head']])
    return t, ts, he3u, he3i, he4

if __name__ == '__main__':
    fname    = argv[1]
    T_cooled = 0.25
    if tail(fname)[2] < T_cooled: flag = True
    else: flag = False
    cooledDate = []
    temp = []
    # print '#'
    # print '# Time  Temperature [K]'
    # print '# UTC+9  He3U Head [K]  He3I Head [K]  He4 Head [K]'
    # print '#'
    while True:
        try:
            date, ts, he3u, he3i, he4 = tail(fname)
            if (not flag) & (he3u < T_cooled): # Cooled
                cooledDate.append(ts)
                print '%s  %s  %s  %s  -  -  Cooled' % (date, he3u, he3i, he4)
                flag = True
            elif he3u < T_cooled: temp.append(he3u)
            elif flag & (he3u >= T_cooled):
                cooledDate.append(ts)
                holdtime = (cooledDate[-1] - cooledDate[0])/60/60
                lowest = min(temp)
                print '%s  %s  %s  %s  %.2f  %.3f  He3U Head > %.2f K' % (date, he3u, he3i, he4, holdtime, lowest, T_cooled)
                flag = False
                cooledDate = []
                temp = []
            else: pass
            stdout.flush()
            sleep(1)
        except KeyboardInterrupt: break
        pass
