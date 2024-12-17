import random

def random_number():
    
    print("Welcome to the game")

    random_num = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter the number"))
            attempts += 1

            if guess < random_num :
                print("number is low")

            elif guess > random_num :
             print("number is high")

            else:
                print("Invalid")

            break

        except ValueError:
            print("Value Error")

random_number()


