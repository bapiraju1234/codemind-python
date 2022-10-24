t = int(input())
while(t>0):
    num = int(input())
    reversed_num = 0
    temp = num
    
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if(temp==reversed_num):
        print("True")
    else:
        print("False")
    t = t-1
