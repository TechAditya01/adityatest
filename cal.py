#claculator
first = float(input("enter a number:"))

operator =input("enter operators (+,-,*,/,%) : ")

second =float(input("enter second number:"))

#calculation part

if operator =="+":
    print(first + second)
elif operator =="-":
    print(first - second)
elif operator =="*":
    print(first * second)    
elif operator =="/":
    print(first / second)  
elif operator =="%":
    print(first % second)          
else:
    print("invalid operation")   
