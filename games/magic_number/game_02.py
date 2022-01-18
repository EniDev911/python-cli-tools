import random

attempts = 5
min_number = 1
max_number = 10

print("Hello! What is your name?: ")
username = input()


if username:
    print("Well, "+ username + ". I am thinking in a number between " +\
          str(min_number) + ' and ' + str(max_number))
else:
    print("Well, Player. I am thinking in a number between " +\
          str(min_number) + ' and ' + str(max_number))

magic_number = random.randint(min_number, max_number)
print(magic_number)

while attempts > 0:

    print(f"Type a number: (remaining {attempts} attempts.)")
    try:
        choice_number = input()

        if (int(choice_number) >= 0 and int(choice_number) <= 10):

            if int(choice_number) == magic_number:
                print(f"Great {username}! has wom!")
                break
            elif int(choice_number) < magic_number:
                print("\a")
                print("Your number is less than the number I'm thinking")
                attempts -= 1
            elif int(choice_number) >= magic_number:
                print("\a")
                print("Your number is higher than the number I'm thinking")
                attempts -= 1
        else:
            print("number should be between 1 - 10")
            attempts -= 1

    except ValueError as e:
        attempts -= 1