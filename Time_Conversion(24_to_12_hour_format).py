
from datetime import datetime
t=input()
s = datetime.strptime(t, "%H:%M")
ts=s.strftime("%r")
a=list(ts)
for i in range(0,5):
    print(a[i],end='')
if a[-2]=='A':
    print(" AM")
else:
    print(" PM")
