print("WELLCOME TO THE GAME OF STONE, PAPER AND SCISSORS ")
print("RULES---->\n1. Do not use 'CAPSLOCK'\n2. press 'ENTER' to lock your choice\n3. Once you locked your choice you cant change it\n4. spell correctly")
print("press'ENTER'to start the game", end="")
i=input()
p=input("with whom do you  want to play\nPLAY WITH YOUR FREIND\nPLAY WITH BOT\nTO PLAY WITH FREIND ENTER--> freind\nTO PLAY WITH BOT ENTER--> bot \n---> ")
if(p=='bot'):
    import random
    list = ['stone', 'paper', 'scissors']
    print("you are playing with a bot,\n choose one of the following:\n stone\n paper\n scissors")
    you = input("YOUR TURN, CHOOSE ONE ---> ")
    bot= random.choice(list)
    print("BOT'S TURN, BOT CHOOSE ---> ", bot)
    if(you == bot):
        print("IT'S A TIE!!!")
    elif(you == "stone" and bot == "scissors"):
        print("YOU WIN!!!")
    elif(you == "paper" and bot == "stone"):
        print("YOU WIN!!!")
    elif(you == "scissors" and bot == "paper"):
        print("YOU WIN!!!")
    else:
        print("BOT WIN!!!")
else:
    print("choose one of the following:\nstone \npaper\nscissors ")
    player1=input("You are player 1, choose one--->")
    player2=input("You are player 2, choose one--->")
    if(player1==player2):
        print("IT'S A TIE!!!")
    elif(player1=="stone"and player2=="scissors"):
        print("PLAYER-1 WINS!!!")
    elif(player1=="paper"and player2=="stone"):
        print("PLAYER-1 WINS!!!")
    elif(player1=="scissors"and player2=="paper"):
        print("PLAYER-1 WINS!!!")
    else:
        print("PLAYER-2 WINS!!!")
    print("!!!THANKS F PLAYING!!!\n !!!GAME OVER!!!")