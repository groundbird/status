#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib as mpl
mpl.use('Agg')
import todlib
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import time
import os
import itertools as it
import glob
import pytz
import pandas as pd

mpl.rcParams['figure.autolayout'] = True

def plot_4periods(tod, savedir, figname, yscale='log', mode='GM'):
    files = '%s/%s*.png' % (savedir, figname)
    if len(glob.glob(files)): os.system('rm %s' % files)

    if mode == 'He10':
        # He-10's sample rate is 1/11 (1 sample per 11 sec)
        period = {'0_hour' : 60*60/11,
                  '1_day'  : 60*60/11*24,  
                  '2_week' : 60*60/11*24*7, 
                  '3_month': 60*60/11*24*30}
    else:
        # other sample rate is 1
        period = {'0_hour' : 60*60,    
                  '1_day'  : 60*60*24,  
                  '2_week' : 60*60*24*7, 
                  '3_month': 60*60*24*30}
    v_tmp = None
    for k, v in sorted(period.items()):
        if v_tmp:
            if v_tmp > len(tod): continue
        if k == '0_hour' : rules = 'T'
        if k == '1_day'  : rules = 'T'
        if k == '2_week' : rules = 'H'
        if k == '3_month': rules = 'H'

        # if mode == 'He10':
        #     lines = ['-', '-', '-', '--', '-.', '-.', '-.', ':', ':', ':']
        # else:
        #     lines = ['-', '--', '-.', ':']*2

        ax = tod.tail(v).resample(rules).plot(rot=0)
        xfmt = md.DateFormatter('%m/%d\n%H:%M', tz=pytz.timezone('Asia/Tokyo'))
        ax.xaxis.set_major_formatter(xfmt)
        leg = ax.legend(loc='upper left', fancybox=True)
        leg.get_frame().set_alpha(0.5)
        plt.yscale(yscale)
        plt.ylabel('Temperature [K]')
        plt.savefig('%s/%s_%s.png' % (savedir, figname, k))
        v_tmp = v

    
if __name__ == '__main__':
    # GMC
    todGM = todlib.gentod('/home/gb/public_html/gbmonitor/temp/data/lastest',
                          usecols=range(1, 10),
                          colslabel=['ch. '+str(i) for i in range(8)])
    plot_4periods(todGM, '/home/hikaru/public_html/pictures',
                  'temp_GM', 'log')
    plot_4periods(todGM, '/home/hikaru/public_html/pictures',
                  'temp_GM_linear', 'linear')
    # He-10
    todHe10 = todlib.gentod('/home/gb/public_html/gbmonitor/he10/data/now',
                            usecols=[1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13],
                            colslabel=['He3U head', 'He3I head', 'He4 head',
                                       'He4 FB',
                                       'He4 pump', 'He3I pump', 'He3U pump',
                                       'He4 SW', 'He3I SW', 'He3U SW'])
    plot_4periods(todHe10, '/home/hikaru/public_html/pictures',
                  'temp_He10', 'log', 'He10')
    plot_4periods(todHe10, '/home/hikaru/public_html/pictures',
                  'temp_He10_linear', 'linear', 'He10')
