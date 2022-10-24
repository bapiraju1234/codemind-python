def add_digits(n):
    a = 0
    while(n>0):
        r = n%10
        a = a + r
        n = n//10
    return a
a = int(input())
while(a>9):
    a= add_digits(a)
print(a)