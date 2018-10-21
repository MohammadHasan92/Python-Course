Num=float(input("Enter your Fahrenheit Or Celsius Number: "))
Way=input("F OR C ??")

#convert Fahrenheit to Celsius
if Way == "F":
     print((Num - 32) / 1.8," °C")
#convert Fahrenheit to Celsius
else:
    print((Num * 1.8) + 32," °F")
  