#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from sys import argv
from numpy import loadtxt
from datetime import datetime
from matplotlib.pyplot import *
from matplotlib.dates import *
import  matplotlib.artist as ma

def plot_time_vs_temp(data):
    ts = loadtxt(data, usecols=(1,))
    dates = [datetime.fromtimestamp(t) for t in ts] 
    grid()
    grid(which='minor')
    tmin = datetime(2013, 12, 26, 20)
    tmax = datetime(2014, 1, 4, 12)
    gca().set_xlim(xmin=tmin, xmax=tmax)
    gca().set_ylim(ymax=10)
    gca().set_yscale('log')
    gca().set_ylabel('Temperature [K]')
    gca().set_fontsize(30)
    dictTemp = {'Unix Time':1,
                'He3U Head':8, 'He3I Head':9, 'He4 Head':10}
#                 'He4 Film Burner':12,
#                 'He4 Pump':13, 'He3I Pump':14, 'He3U Pump':15,
#                 'He4 SW':16, 'He3I SW':17, 'He3U SW':18}
    i = 0
    dataTemp = []
    linestyles = ['-', '--', ':']
    for k, v in sorted(dictTemp.items(), key=lambda x: x[1]):
        if k == 'Unix Time': continue
        dataTemp.append(loadtxt(data, usecols=(v,)))
        plot(dates, dataTemp[i], linestyles[i], label=k)
        i += 1
        pass
    # date format
    xfmt = DateFormatter('%Y-%m-%d\n%H:%M:%S')
#     xticks(rotation=25)
    gca().xaxis.set_major_formatter(xfmt)
    # legend
    leg = legend(loc='upper center', ncol=3)
#     leg.get_frame().set_alpha(0.5)
#     savefig("%s.png" % adc[:-4])
#     savefig("temp.png", transparent=True)
#     hoursLoc = HourLocator(interval=6)
    daysLoc = DayLocator(interval=2)
#     gca().xaxis.set_major_locator(hoursLoc)
    gca().xaxis.set_major_locator(daysLoc)
    savefig("temp.png")
    show()
    pass

if __name__ == '__main__':
    data = argv[1]
    plot_time_vs_temp(data)
    pass
