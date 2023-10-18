import random

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        if guess < number:
            print("Pamēģini lielāku skaitli.")
        else:
            print("Pamēģini mazāku skaitli.")

        guess = int(input("Uzmini skaitli: "))
        tries += 1
    else:
        if tries < 3:
            print(f" wow Tu uzminēji pēc {tries} reizēm!")
        elif tries < 7:
            print(f"  Tu uzminēji pēc {tries} reizēm! Normāli!")
        else:
            print (f"  Tu uzminēji pēc {tries} reizēm! Tev vajag patrenēties")
    response = input("Vai vēlies turpināt")
    if response =="y":
        repeat = True
    elif response == "n":
        repeat = False
        print("Paldies par spēli! Bai, baj!")
    else:
        repeat = False
