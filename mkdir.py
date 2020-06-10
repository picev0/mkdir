import datetime
import os
now = datetime.datetime.now()
print('{0:%Y%m%d%H%M}'.format(now))
path = './{0:%Y%m%d%H%M}'.format(now)
os.mkdir(path)
