import sys        #this sys file is very important for this type programmes

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalied input")
    sys.exit(1)      # 1 is the default value

try:
    result = x / y
except ZeroDivisionError:                 #if some number divide by zero then display "ZeroDivisionError" this error massege
    print("Error: Cannot divide by 0.")
    sys.exit(1)        #1 is the  default value

print(f"{x} / {y} = {result}")