import ntplib
import datetime
import os
c = ntplib.NTPClient()
response = c.request('time.windows.com', version=3)#Server time
center=datetime.datetime.fromtimestamp(response.tx_time)
print center
print type(center)
os.system("pause")