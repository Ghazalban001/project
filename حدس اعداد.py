answer = int(input("enter number player1 : "))
correct = False
count = 0
while count < 6 and correct == False:
    guess = int(input("player 2 : enter guss"))
    if guess == answer:
        print("your guss is True")
        correct == True
    elif guess > answer:
        print("your guss is biger than answer ")
        count += 1
    else:
        print("your gusse is smaller than answer ")
        count += 1

    # if correct == False:
        # print("player : you last")
