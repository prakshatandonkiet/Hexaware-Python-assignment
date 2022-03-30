num1 = int(input("Enter the Number: "))
num2 = int(input("Enter the Number: "))
num3 = int(input("Enter the Number: "))
if(num1>num2 and num1>num3):
    largest = num1
elif(num2>num3 and num2>num1):
    largest = num2
else:
    largest = num3

print("Largest is ", largest)