#!/bin/bash

DATAFILE=/home/gb/public_html/gbmonitor/he10/data/now
# DATADIR=/home/hikaru/gbmonitor/data
#FILENAME=`date '+%Y%m%d%H%M%S'`
CMD=/home/hikaru/gbmonitor/monitor.py

#ln -sf ${FILENAME}.dat ${DATADIR}/latest

# $CMD $DATAFILE | tee ${DATADIR}/${FILENAME}.dat
echo "Start!"
$CMD $DATAFILE >> tempHist.txt
