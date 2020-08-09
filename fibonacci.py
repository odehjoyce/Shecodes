number = int(input("Enter the number: "))
num1 = 0
num2 = 1
count = 0

if number <= 0:
    print("Please, do enter a positive number")
elif number == 1:
    print("The Fibonacci sequence is upto", number)
    print(num1)
else:
    print("Fibonacci sequence is: ")
    while count < number:
        print(num1)
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1