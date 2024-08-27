#CALCULATOR

print("=============WELCOME TO OUR CALCULATor=============")
while(True):
    print("PRESS 1 TO CONTINUE.")
    print("PRESS 0 TO QUIT.")
    CHOICE = int(input("ENTER YOUR CHOICE:"))
    if CHOICE == 1:
        num1= float(input("ENTER FIRST NUMBER:"))
        OP = input("ENTER THE OPERATION YOU WANT TO PERFORM:")
        num2 = float(input("ENTER SECOND NUMBER:"))
        match OP:
            case '+': 
                print("YOUR ANSWER IS:",num1+num2)
            case '-':
                print("YOUR ANSWER IS:",num1-num2)
            case '*':
                print("YOUR ANSWER IS:",num1*num2)
            case '/':
                print("YOUR ANSWER IS:",num1/num2)  
            case '%':
                print("YOUR ANSWER IS:",num1%num2)      
            case _ :
                print("please enter a valid operation.")    
    else:
        print("=========THANKS FOR USING OUR CALCULATOR!=========")
        break