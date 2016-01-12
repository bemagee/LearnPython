#!/tools/bin/python -tt

from datetime import datetime

time = 1
day_diff = 30

now = datetime.now()
last_month = datetime.datetime(mydate.year, mydate.month-1, 1)

if type(time) is int:
    diff = now - datetime.fromtimestamp(time)
elif isinstance(time,datetime):
    diff = now - time 
elif not time:
    diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

print "now= %s \n" % now
print "last_month= %s \n" % last_month
print "diff = %s \n" % diff 


if day_diff < 0:
    print ''

if day_diff == 0:
    if second_diff < 10:
        print "just now"
    if second_diff < 60:
        print str(second_diff) + " seconds ago"
    if second_diff < 120:
        print  "a minute ago"
    if second_diff < 3600:
        print str( second_diff / 60 ) + " minutes ago"
    if second_diff < 7200:
        print "an hour ago"
    if second_diff < 86400:
        print str( second_diff / 3600 ) + " hours ago"

if day_diff == 1:
    print "Yesterday"
if day_diff < 7:
    print str(day_diff) + " days ago"
if day_diff < 31:
    print str(day_diff/7) + " weeks ago"
if day_diff < 365:
    print str(day_diff/30) + " months ago"

print str(day_diff/365) + " years ago"
