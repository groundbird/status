#-*- coding: utf-8 -*-

import sys, os

os.chdir('/home/hikaru/public_html/status')

import bottle
import status

application = bottle.default_app()
