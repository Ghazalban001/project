import random
game=["sang","kaghaz","ghachi"]
lap=int(input("lets play a few times : "))
dr=0
pl=0
for num in range(1,lap):
    player1=random.choice(game)
    player2=input("sang _ kaghaz _ ghachi : ")
    print(player1)

    if player1=="sang" and player2=="sang":
        print("🤞")
    if player1=="sang" and player2=="kaghaz":
        print("you won")
        pl+=1
    if player1=="sang" and player2=="ghachi":
        print("you won")
        pl+=1
    if player1=="kaghaz" and player2=="sang":
        print("drive won")
        dr+=1
    if player1=="kaghaz" and player2=="kaghaz":
        print("🤞")
    if player1=="kaghaz" and player2=="ghachi":
        print("you won")
        pl+=1
    if player1=="ghachi" and player2=="sang":
        print("you won")
        pl+=1
    if player1=="ghachi" and player2=="ghachi":
        print("🤞")
    if player1=="ghachi" and player2=="kaghaz":
        print("drive won")
        dr+=1
print(f"you : {pl} and drive : {dr}")



