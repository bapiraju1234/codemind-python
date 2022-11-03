n=int(input())
l=list(map(int,input().split(" ")))
h=[]
for i in l:
    if(i==l.count(i)):
        if i not in h:
            h.append(i)
if(len(h)>0):print("{:.2f}".format(sum(h)/len(h)))
else:print("-1")