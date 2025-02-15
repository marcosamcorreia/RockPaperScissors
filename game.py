def game():
    from random import randint
    import os

    m=["rock","paper", "scissor"]
    result=["Draw", "You won", "You lose"]

    text=input("Rock, Paper or Scissor?\n")
    player=text.lower()
    computer= m[randint(0,2)]

    print(f"You choosed {player} and the computer choosed {computer}")

    if player == computer:
        print(f"It's a {result[0]}!")
    elif player == m[0]:
        if computer == m[2]:
            print(result[1])
        else:
            print(result[2])
    elif player == m[1]:
        if computer == m[0]:
            print(result[1])
        else:
            print(result[2])
    elif player == m[2]:
        if computer == m[1]:
            print(result[1])
        else:
            print(result[2])
    else:
        print("That's not a valid play. Check your spelling!")
        return game()


    again= input("Do you want play again?  Y/N ")

    if again.lower() == "y" or again.lower() == "yes":
        print("If you want to play let's play!")
        game()
    elif again.lower() == "n" or again.lower() == "no":
        print("See you later. Bye!")

    os.system("pause")
