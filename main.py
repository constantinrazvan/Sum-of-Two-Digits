#This program take an input. 
#For example: 82 
#It slice the number in 2: 8 and 2 
#And make it a sum: 8 + 2 = 10

twoDigits = input("Insert a two digits number: ")

if len(twoDigits) == 2: 
    firstNumber = int(twoDigits[0])
    secondNumber = int(twoDigits[1])
    sum = firstNumber + secondNumber
    print(f"The sum of the first digit and second is: {sum}")
else: 
  print("Your input is invalid!")
