#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import datetime as dt
import pandas as pds
import glob
import os.path
import pytz

class TOD(object):
    """
    filename のデータ形式は 0 列目をタイムスタンプ, 1 列目以降を各値 
    (e.g., [[1412001639, 219.67, ...], [1412001640, 219.67, ...], ...])
    となるように usecols を指定する.
    ファイルの最終行はデータの抜け等による read error を回避するために読んで
    いない (skip_footer=1).
    """
    def __init__(self, filename, usecols=None):
        self._filename = filename
        self._usecols  = usecols
        self._data     = np.genfromtxt(filename, skip_footer=1, usecols=usecols)
        self._ts       = np.array(self._data[:,0])
        self._vals     = np.array(self._data[:,1:])
    def ts(self, skip=1):
        return self._ts[::skip]
    def dates(self, skip=1, tz=pytz.timezone('Asia/Tokyo')):
        return np.array([dt.datetime.fromtimestamp(t, tz) for t in self.ts()])
    def vals(self, skip=1):
        return self._vals[::skip]
    def get_channel_vals(self, channel, skip=1):
        return self._vals[:,channel:skip]
    def gentod(self, skip=1, colslabel=None):
        return pds.DataFrame(self._vals[::skip], index=self.dates(skip), columns=colslabel)
    def gentod_all(self, directory=None, extension='dat', colslabel=None):
        if not directory: directory = os.path.dirname(self._filename)
        todAll = []
        for f in sorted(glob.glob('%s/*.%s' % (directory, extension))):
            tod = TOD(f, usecols=self._usecols)
            todAll.append(tod.gentod(colslabel=colslabel))
        return pds.concat(todAll, axis=0)
