#!/bin/bash

DATAFILE=/home/gb/public_html/gbmonitor/he10/data/now
TEMPHIST=/home/hikaru/public_html/status/temp_monitor/tempHist.txt
CMD=/home/hikaru/public_html/status/temp_monitor/monitor.py

echo "-----------------------------"
echo "| Monitoring Start!         |"
echo '|' `date '+Date: %Y-%m-%d %H:%M:%S'` '|'
echo "-----------------------------"
nice -n 19 $CMD $DATAFILE | tee -a $TEMPHIST
