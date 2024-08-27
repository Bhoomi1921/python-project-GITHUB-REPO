#rock , paper and scissor

import random
user_score =0
computer_score = 0
tie_match=0
def win(user,computer):
    if (user =='r' and computer == 's') or (user == 's' and computer == 'p') or (user=='p' and computer=='r'):
        global user_score 
        user_score += 1
        
        return True
    else:
        global computer_score 
        computer_score += 1

        return False
print("===================WELCOME TO ROCK-PAPER-SCISSORS GAME!====================")
while(True):
    print("PRESS 1 TO CONTINUE PLAYING GAME.")
    print("PRESS 0 TO QUIT THE GAME.")
    print("PRESS 2 TO KNOW YOUR SCORES.")
    choice = int(input("ENTER YOUR CHOICE:"))
    if choice == 0:
        print("============THANKS FOR PLAYING!=============")
        break
    elif choice==1:
        print("PRESS 'r' FOR ROCK.")
        print("PRESS 'p' FOR PAPER.")
        print("PRESS 's' FOR SCISSORS")
        list =['r','p','s']
        user = input(" WHAT WOULD YOU LIKE TO CHOOSE:")
        if user not in list:
            print("YOU HAVE ENTERED AN UNVALID CHARACTER.")
        computer = random.choice(list)
        print("computer chooses:",computer)
        if(user == computer):
            tie_match+=1 
            print("====IT'S A TIE.====")
        elif win(user , computer):
            print("====HURRAY! YOU WON THE GAME.====")
        else:
            print("====ALAS! YOU LOSE THE GAME.BETTER LUCK NEXT TIME.====")  
    elif choice == 2:
        print("YOUR SCORE IS:",user_score)
        print("COMPUTER SCORE IS:",computer_score)
        print("TOTAL TIE MATCHES ARE:",tie_match)
      