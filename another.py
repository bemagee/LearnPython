#!/tools/bin/python -tt
from datetime import datetime
from dateutil.relativedelta import relativedelta

date_after_month = datetime.today()+ relativedelta(months=-1)
print 'Today: ',datetime.today().strftime('%m/%d/%Y')
print 'A Month Ago:', date_after_month.strftime('%m/%d/%Y')
print 'last months log: gitolite-',date_after_month.strftime('%Y-%d')
This_month=datetime.today().strftime('%m')
Last_month=date_after_month.strftime('%m')

print "This Month = %s and last month = %s" % (This_month, Last_month)
Log_file="logs/gitolite-2014-%s.log" % (Last_month)
print "Logfile = %s" % (Log_file)
