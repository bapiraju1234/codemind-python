def digits(n):
    l=0
    while(n>0):
        n=n//10
        l=l+1
    return l
def Disarium(x,n):
    Sum=0
    while(n>0):
        r=n%10
        Sum=Sum+(r**x)
        x=x-1
        n=n//10
    return Sum
n=int(input())
x=digits(n)
m=Disarium(x,n)
if(m==n):
    print("True")
else:
    print("False")