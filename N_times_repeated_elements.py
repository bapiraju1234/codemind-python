n=int(input())
l=list(map(int,input().split(" ")))
h=[]
k=int(input())
for i in l:
    if(k==l.count(i)):
        if str(i) not in h:
            h.append(str(i))
if(len(h)>0):print(" ".join(h))
else:print("-1")