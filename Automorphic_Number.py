num = int(input(""))

#find number of digits in num 
n = len(str(num))

#compute square
sqr = num**2

#Extract last n digits from the square
last = sqr%pow(10,n)

#compare last n digits with the input number
if last == num:
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")