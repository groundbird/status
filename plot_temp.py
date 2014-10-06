#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv, stdout
from os import system
from time import sleep, strftime
from numpy import loadtxt
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
from matplotlib.pyplot import *
from matplotlib.dates import *
import  matplotlib.artist as ma
from itertools import cycle


def plot_temp(fname, log=False, period='all'):
    d = loadtxt(fname, usecols=range(1, 10))
    dates = [datetime.fromtimestamp(t) for t in d[:,0]]

    if period == 'hour' and len(dates) > 3600:
        d     = d[-3600:]
        dates = dates[-3600:]
    elif period == 'day' and len(dates) > 86400:
        d     = d[-86400:]
        dates = dates[-86400:]
    elif period == 'week' and len(dates) > 604800:
        d     = d[-604800:]
        dates = dates[-604800:]
    elif period == 'month' and len(dates) > 18144000:
        d     = d[-18144000:]
        dates = dates[-18144000:]
    else: pass

    fig, ax = subplots()
    lines = ['-', '--', ':', '.-']
    linecycler = cycle(lines)
    label = ['ch 0', 'ch 1', 'ch 2', 'ch 3', 'ch 4', 'ch 5', 'ch 6', 'ch 7']
    for i in range(1, 9):
        ax.plot(dates, d[:,i], next(linecycler), label=label[i-1])
        pass
    xfmt = DateFormatter('%m/%d\n%H:%M')
    ax.xaxis.set_major_formatter(xfmt)
    ax.grid()
    if log: ax.set_yscale('log')
    leg = ax.legend(loc='best')
    leg.get_frame().set_alpha(0.5)
    ax.set_ylabel('Temperature [K]')
    savefig('/home/hikaru/public_html/pictures/temp_GM_%s.png' % period)


def status_plot(datfileTemp, datfileCurr, lastN):
    tsTemp = loadtxt(datfileTemp, usecols=(1,))
    tsCurr = loadtxt(datfileCurr, usecols=(1,))
    lastN = int(lastN)

    if (len(tsTemp) > len(tsCurr)) and (lastN > len(tsCurr)): lastN = len(tsCurr)
    if (len(tsCurr) > len(tsTemp)) and (lastN > len(tsTemp)): lastN = len(tsTemp)

    datesTemp = [datetime.fromtimestamp(t) for t in tsTemp[-lastN:]]
    datesCurr = [datetime.fromtimestamp(t) for t in tsCurr[-lastN:]]
    fig = figure(figsize=(12, 8))
    ax1 = subplot2grid((4, 1), (0, 0), rowspan=2)
    ax2 = subplot2grid((4, 1), (2, 0))
    ax3 = subplot2grid((4, 1), (3, 0))
    subplots_adjust(hspace=0.001)
    ax1.grid()
    ax1.grid(which='minor')
    ax2.grid()
    ax3.grid()
    xmax = datesCurr[-1]
    xmin = datesCurr[-lastN]
    ax1.set_xlim(xmin, xmax)
    ax2.set_xlim(xmin, xmax)
    ax3.set_xlim(xmin, xmax)
    ax2.set_ylim(ymin=-10, ymax=119)
    ax3.set_ylim(ymin=-0.04, ymax=0.33)
    ax1.set_yscale('log')
    ax1.set_ylabel('Temperature [K]')
    fig.text(0.08, 0.3, 'Current [mA]', ha='center', va='center', rotation='vertical')
    dictTemp = {'Unix Time':1,
                'He3U Head':8, 'He3I Head':9, 'He4 Head':10,
                'He4 Film Burner':12,
                'He4 Pump':13, 'He3I Pump':14, 'He3U Pump':15,
                'He4 SW':16, 'He3I SW':17, 'He3U SW':18}
    dictCurr = {'Unix Time':1,
               'He4 Pump':2, 'He3I Pump':3, 'He3U Pump':4,
               'He4 SW':5, 'He3I SW':6, 'He3U SW':7}
    i = 0
    temp = []
    # lines = ['-', '--', ':']
    # linecycler = cycle(lines)
    for k, v in sorted(dictTemp.items(), key=lambda x: x[1]):
        if k == 'Unix Time': continue
        temp.append(loadtxt(datfileTemp, usecols=(v,)))
        ax1.plot(datesTemp, temp[i][-lastN:], label=k)
        i += 1
        # ax1.plot(dataTemp,
        #          loadtxt(datfileTemp, usecols=(v,)),
        #          next(linecycler),
        #          label=k)
    i = 0
    currPump = []
    for k, v in sorted(dictCurr.items(), key=lambda x: x[1]):
        if k == 'Unix Time': continue
        if v > 4: continue
        currPump.append(loadtxt(datfileCurr, usecols=(v,)))
        ax2.plot(datesCurr, currPump[i][-lastN:], label=k)
        i += 1
    i = 0
    currSW = []
    for k, v in sorted(dictCurr.items(), key=lambda x: x[1]):
        if v < 5: continue
        currSW.append(loadtxt(datfileCurr, usecols=(v,)))
        ax3.plot(datesCurr, currSW[i][-lastN:], label=k)
        i += 1

    xfmt = DateFormatter('%m/%d\n%H:%M')
    gca().xaxis.set_major_formatter(xfmt)
    setp(ax1.get_xticklabels(), visible=False)
    setp(ax2.get_xticklabels(), visible=False)
    legTemp = ax1.legend(loc='upper left')
    legTemp.get_frame().set_alpha(0.5)
    legAdc = ax2.legend(loc='upper left')
    legAdc.get_frame().set_alpha(0.5)
    legAdcSW = ax3.legend(loc='upper left')
    legAdcSW.get_frame().set_alpha(0.5)
    savefig('/home/hikaru/public_html/pictures/temp.png')
    pass

if __name__ == '__main__':
    datfileTemp = argv[1]
    datfileCurr = argv[2]
    lastN = [600, 600*24, 600*24*7, 600*24*30] # [1 hour, 1 day, 1 week, 1 month]
    i = 0
    for n in lastN:
        status_plot(datfileTemp, datfileCurr, n)
        path = '/home/hikaru/public_html/pictures'
        system('mv %s/temp.png %s/temp%d.png' % (path, path, i))
        print '%s: update figure' % strftime('%Y-%m-%d %H:%M:%S')
        i += 1
        pass

    # GM Cooler
    for p in ['hour', 'day', 'week', 'month']:
        plot_temp('/home/gb/public_html/gbmonitor/temp/data/lastest', log=False, period=p)
        print '%s: update figure' % strftime('%Y-%m-%d %H:%M:%S')
