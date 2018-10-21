x=int(input("Enter your Number: "))
if x < -100:
    print(x * -1)
elif -100 <= x <= -25:
    print(x ** 4)
elif -25 < x <= 0:
    print((3 * (x ** 2)) - 1)
elif 0 < x <= 100:
    print((3.14/2) * x + (3 ** x))
else:
    print(x)



# D) Assume if  we need the numeber to be Integer we use Function int() to get
integer value.