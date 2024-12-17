def rock_paper(play1, play2, play3):

    if (play1 == "rock" and play2 == "scissors") or \
       (play1 == "scissor" and play2 == "paper") or \
       (play1 == "paper" and play2 == "rock"):
        print("player 1 wins ")
       
    elif(play2 == "rock" and play3 == "scissors") or \
        (play2 == "scissor" and play3 == "paper") or \
        (play2 == "paper" and play3 == "rock"):
        print("player 2 wins")

    elif(play3 == "rock" and play1 == "scissors") or \
        (play3 == "scissor" and play1 == "paper") or \
        (play3 == "paper" and play1 == "rock"):
        print("player 2 wins")

    else:
        print("its a tie")

    

play1 = input("Enter the input:").lower()
play2 = input("Enter the input:").lower()
play3 = input("Enter the input:").lower()

rock_paper(play1, play2, play3)

