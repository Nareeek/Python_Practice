import random
from time import sleep

str = ("Guess the number between 1 to 100")
print(str.center(80))
sleep(2)

number = random.randint(0, 100)
user_input = []

while user_input != number:
    while True:
        try:
            user_input = int(input("\nEnter a number: "))
            if user_input > 100:
                print("You exceeded the input parameter, but anyways,")
            elif user_input < 0:
                print("You exceeded the input parameter, but anyways,")
            break
        except ValueError:
            print("Not valid")
    if number > user_input:
        print("The number is greater that that you entered ")
    elif number < user_input:
        print("The number is smaller than that you entered ")

else:
    print("Congratulation. You made it!")
