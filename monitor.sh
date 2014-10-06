#!/bin/bash

DATAFILE=/home/gb/public_html/gbmonitor/he10/data/now
TEMPHIST=/home/hikaru/public_html/status/tempHist.txt
# DATADIR=/home/hikaru/gbmonitor/data
#FILENAME=`date '+%Y%m%d%H%M%S'`
CMD=/home/hikaru/public_html/status/monitor.py

#ln -sf ${FILENAME}.dat ${DATADIR}/latest

# $CMD $DATAFILE | tee ${DATADIR}/${FILENAME}.dat
echo "-----------------------------"
echo "| Monitoring Start!         |"
echo '|' `date '+Date: %Y-%m-%d %H:%M:%S'` '|'
echo "-----------------------------"
nice -n 19 $CMD $DATAFILE | tee -a $TEMPHIST
