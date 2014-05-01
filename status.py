#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template, debug
from os import listdir, stat, path
from sys import argv
from glob import glob
from datetime import datetime
from numpy import loadtxt
# from paste import httpserver
import subprocess as sp
import pytz

@route('/<name>')
def status_of_gb(name='status'):
    fnameHe10 = '/home/gb/public_html/gbmonitor/he10/data/now'
    dictTemp = {'Time':0, 'He3U Head':8, 'He3I Head':9, 'He4 Head':10}
    t = sp.Popen('tail -n 1 %s' % fnameHe10, shell=True, stdout=sp.PIPE)
    tail = t.stdout.readline().split()
    now = []
    for v in sorted(dictTemp.values()): now.append(tail[v])
    img = [path.basename(x) for x in glob('/home/hikaru/public_html/pictures/temp*.png')]
    imgLinks = []
    for i in sorted(img):
        imgLink = 'http://ahiru.kek.jp/~hikaru/pictures/%s' % i
        imgLinks.append(imgLink)
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
    for line in open('/home/hikaru/public_html/status/dev/status_update_dev.txt', 'r'): update.append(line)
    return template('status', now=now, img=imgLinks, rows=data, mod=mod, lists=update)

if __name__ == '__main__':
    # run(host='ahiru.kek.jp', port=8080, debug=True, reloader=True)
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
    # debug(True)
    # run(reloader=True)
    # run(server='cgi')
