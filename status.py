#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
from bottle import route, run, template, debug, request
from os import listdir, stat, path
from sys import argv
from glob import glob
from datetime import datetime
from numpy import loadtxt
# from paste import httpserver
import subprocess as sp
import pytz
import todlib


@route('/<name>')
def status_of_gb(name='status', method='GET'):
    fnameHe10 = '/home/gb/public_html/gbmonitor/he10/data/now'
    fnameGM   = '/home/gb/public_html/gbmonitor/temp/data/lastest'

    dictTemp = {'Time':0, 'He3U Head':8, 'He3I Head':9, 'He4 Head':10}

    t    = sp.Popen('tail -n 1 %s' % fnameHe10, shell=True, stdout=sp.PIPE)
    tail = t.stdout.readline().split()
    t_GM    = sp.Popen('tail -n 1 %s' % fnameGM, shell=True, stdout=sp.PIPE)
    tail_GM = t_GM.stdout.readline().split()
    del tail_GM[1] # delete unixtime
    
    now = []
    for v in sorted(dictTemp.values()): now.append(tail[v])
    img = [path.basename(x) for x in glob('/home/hikaru/public_html/pictures/temp[0-3].png')]
    imgLinks = []
    for i in sorted(img):
        imgLink = 'http://ahiru.kek.jp/~hikaru/pictures/%s' % i
        imgLinks.append(imgLink)
    imgGM = [path.basename(x) for x in glob('/home/hikaru/public_html/pictures/temp_GM*.png')]
    imgLinksGM = []
    for i in sorted(imgGM):
        imgLinkGM = 'http://ahiru.kek.jp/~hikaru/pictures/%s' % i
        imgLinksGM.append(imgLinkGM)
    # fnameMonitor = '/home/hikaru/gbmonitor/data/latest'
    fnameMonitor = '/home/hikaru/public_html/status/tempHist.txt'
    data = loadtxt(fnameMonitor, dtype={'names':('Time',
                                              'He3U Head',
                                              'He3I Head',
                                              'He4 Head',
                                              'Hold Time',
                                              'Lowest Temperature',
                                              'State'),
                                     'formats':('S19',
                                                '<f4',
                                                '<f4',
                                                '<f4',
                                                '<S4',
                                                '<S5',
                                                '<S30')},
                   delimiter='  ')
    data = data[::-1]
    ts = int(stat(argv[0]).st_mtime)
    mod = datetime.fromtimestamp(ts, tz=pytz.timezone('Asia/Tokyo'))
    update = []
    fnameUpdate = '/home/hikaru/public_html/status/status_update.txt'
    for line in open(fnameUpdate, 'r'): update.append(line)

    # test-2014-10-20
    # 期間取得
    start = str(request.query.start)
    end   = str(request.query.end)
    if start and end:
        savedir = '/home/hikaru/public_html/pictures'
        t = todlib.TOD(fnameGM, range(1, 10))
        cols = ['ch. '+str(i) for i in range(8)]
        todall = t.gentod_all(colslabel=cols)
        todall[start:end].plot(rot=0, title='%s -- %s' % (start, end))
        xfmt = md.DateFormatter('%m/%d\n%H:%M')
        plt.gca().xaxis.set_major_formatter(xfmt)
        plt.gca().legend(loc='upper left')
        plt.savefig('%s/request.png' % savedir)
        requestPlot = 'http://ahiru.kek.jp/~hikaru/pictures/request.png'
    else: requestPlot = None
    return template('status', now=now, temp_GM=tail_GM, img=imgLinks, imgGM=imgLinksGM, rows=data, mod=mod, lists=update, requestPlot=requestPlot)

if __name__ == '__main__':
    # run(host='0.0.0.0', port=8080, debug=True, reloader=True)
    run(server='paste', host='0.0.0.0', port=8080, debug=True, reloader=True)
    # run(server='paste', host='130.87.195.83', port=80, debug=True, reloader=True)
