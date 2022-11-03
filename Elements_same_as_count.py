n=int(input())
l=list(map(int,input().split(" ")))
h=[]
for i in l:
    if(i==l.count(i)):
        if str(i) not in h:
            h.append(str(i))
if(len(h)>0):print(" ".join(h))
else:print("-1")
