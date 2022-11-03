n=int(input())
l=list(map(int,input().split(" ")))
k=[]*-1
for i in l:
    if(l.count(i)==i):
        k.append(i)
if(len(k)==0):print("-1")
else:print(min(k),max(k))
    