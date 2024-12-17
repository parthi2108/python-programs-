# def add(x,y):
#     return x+y
# def subract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y

# print("Select Operation")
# print("1.add")
# print("2.subract")
# print("3.multiply")
# print("4.divide")

# while True:
#     choice=input("enter your choice : 1,2,3,4: ")

#     if choice in ('1','2','3','4'):

#         try :
#             num1 = float(input("Enter your number: "))
#             num2 = float(input("Enter ypur number: "))

#         except ValueError:
#             print("Invalid input")

#         if choice == '1'1':
#             print(add(num1+num2))

#         elif choice == '2':
#             print(subract(num1-num2))
    
#         elif choice == '3':
#             print(multiply(num1*num2))

#         elif choice == '4':
#             print(divide(num1/num2))

#         else:
#             print("Invalid input")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter your choice (1, 2, 3, 4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue  # Restart the loop

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")

        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")

    else:
        print("Invalid choice! Please select a valid option.")


