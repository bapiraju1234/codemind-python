def reverse (n) :
    rev = 0
    while n>0:
        r = n%10
        rev = rev*10+r
        n = n//10
    return(rev)
a = int(input())
b = a**2
c = reverse(a)
d = c**2
e = reverse(d)
if (b==e):
    print("True")
else:
    print("False")