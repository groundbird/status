#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use('Agg')
import todlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import time
import os
import itertools as it

def plot_4periods(tod, savedir, figname):
    files = '%s/%s*.png' % (savedir, figname)
    if os.path.exists(files):
        os.system('rm %s' % files)
    period = {'0_hour' : 60*60,    
              '1_day'  : 60*60*24,  
              '2_week' : 60*60*24*7, 
              '3_month': 60*60*24*30}
    for k, v in sorted(period.items()):
        if v > len(tod): continue
        if k == '0_hour' : rules = 'S'
        if k == '1_day'  : rules = 'T'
        if k == '2_week' : rules = 'H'
        if k == '3_month': rules = 'H'
        tod.tail(v).resample(rules).plot(rot=0)
        xfmt = md.DateFormatter('%m/%d\n%H:%M')
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.gca().legend(loc='upper left')
        plt.savefig('%s/%s_%s.png' % (savedir, figname, k))

    
if __name__ == '__main__':
    tod_GM = todlib.TOD('/home/gb/public_html/gbmonitor/temp/data/lastest',
                        usecols=range(1, 10))
    plot_4periods(tod_GM.gentod(colslabel=['ch. '+str(i) for i in range(8)]),
                  '/home/hikaru/public_html/pictures', 'temp_GM')
