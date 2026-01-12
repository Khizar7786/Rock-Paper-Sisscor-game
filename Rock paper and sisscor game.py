
import random
choices = ["rock", "paper", "sisscor"]
player = None
playing = True
playAgainchoice = ["yes" , "no", "n","y"]
playAgain= None
while playing:
    player = None       # RESET inside loop
    playAgain = None    # RESET inside loop

    computer = random.choice(choices)
    while player not in choices:
        player = input("Choose one ROCK | PAPER | SISCOR ").lower()
    print(f"Computer's chooice is {computer}")    
    if computer == player:
        print("It is a tie")
    elif (computer =="rock" and player == "sisscor") or (computer =="sisscor" and player == "paper") or (computer =="paper" and player == "rock"):
        print("YOU LOOSE")
    else:
        print("You won")
    while playAgain not in playAgainchoice:
        playAgain = input("DO YOU WISH TO PLAY AGAIN y/n").lower()
        if playAgain in ["no","n"]:  
         playing= False
print("THE ENDDDD")         

