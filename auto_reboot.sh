#!/bin/sh
! (screen -ls | grep -q gb_status ) && \
screen -dmS gb_status sh -c "cd $HOME/public_html/status && /usr/bin/python2.7 status.py"

! (screen -ls | grep -q gb_temp_monitor ) && \
screen -dmS gb_temp_monitor sh -c "cd $HOME/public_html/status/temp_monitor && ./restart.sh ./monitor.sh"
