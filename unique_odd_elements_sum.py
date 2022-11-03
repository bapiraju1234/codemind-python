n=int(input())
l=list(map(int,input().split(" ")))
m=[]
sum=0
for i in l:
    if i not in m:
        m.append(i)
for i in m:
    if(i%2!=0):
        sum+=i
print(sum)        