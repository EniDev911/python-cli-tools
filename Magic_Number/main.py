import random

attempts = 5

#random_number = random.randint(0, 100)
random_number = int(random.random()*100)
running = True
print(random_number)

while attempts!=0 and running:
    print("")
    number = int(input("What number between 1 and 100 do you imagine I'm thinking?:\n"))
    if number<random_number:
        attempts-=1
        print(f"The number I'm thinking is higher (attempts:{attempts})")
    elif number>random_number:
        attempts-=1
        print(f"The number I'm thinking is less (attempts:{attempts})")
    elif number==random_number:
        print("Congrats you guessed the magic number in {attempts} attempts".format(attempts=attempts))
        break
    if attempts==0:
        print("Good luck for the next goodbye")
        running = False

    