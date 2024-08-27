#PASSWORD GENERATOR

import random
import string
print("============WELCOME TO PASSWORD GENERATOR============")
while(True):
    print("PRESS 1 TO CONTINUE.")
    print("PRESS 0 TO QUIT.")
    choice = int(input("ENTER YOUR CHOICE:"))
    if choice == 1:
        length = int(input("ENTER THE LENGTH OF PASSWORD:"))
        complexity = input("ENTER THE COMPLEXITY OF PASSWORD YOU WANT(easy,medium,hard):")
        char_sets={1:string.ascii_lowercase,
                    2:string.ascii_letters + string.digits, 
                    3: string.ascii_letters+string.punctuation+string.digits}
        if complexity.lower() == 'easy':
            password = ''.join(random.choice(char_sets[1]) for _ in range(length))
            print("YOUR GENERATED PASSWORD IS:",password)
                
                
        elif complexity.lower() == 'medium':
            password = ''.join(random.choice(char_sets[2]) for _ in range(length)) 
            print("YOUR GENERATED PASSWORD IS:",password)
            
        elif complexity.lower() == 'hard':
            password = ''.join(random.choice(char_sets[3]) for _ in range(length))
            print("YOUR GENERATED PASSWORD IS:",password)
        
        else:
            print("INVALID COMPLEXITY ENTERED.")

    else:
        print("===========THANKS FOR USING OUR PASSWORD GENERATOR==========")
        break 