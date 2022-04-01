def calculate_sum(limit): 
  
    sum = 0
    for i in range(0,limit):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
        i = i + 1
    return sum
userInput = int(input("Enter limiting number: "))
plusOne = userInput + 1
print(calculate_sum(plusOne))