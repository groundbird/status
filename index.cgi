#!/usr/bin/env python

from status import status_of_gb

print "Content-type: text/html; charset=UTF-8\n"
print status_of_gb().encode('utf-8')
