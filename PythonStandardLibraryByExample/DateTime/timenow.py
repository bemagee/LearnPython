import datetime,time

print 'datetime now: ', datetime.datetime.now()
print 'time now: ', datetime.datetime.now().time()


from time import gmtime, strftime
print 'diff time ', strftime("%Y-%m-%d %H:%M:%S", gmtime())
