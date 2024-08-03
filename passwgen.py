import random
LENGTH = int(input("ENTER THE LENGTH OF PASSWORD YOU WANT:"))
name = input("ENTER YOUR NAME:")
surname = input("ENTER YOUR SURNAME:")
birth_date = input("ENTER YOUR BIRTH DATE:")
birth_month = input("ENTER YOUR BIRTH MONTH:")
birth_year = input("ENTER YOUR BIRTYH YEAR:")
CONC_PASS = name+birth_date+birth_month+birth_year
password = ''.join(random.choice(CONC_PASS) for _ in range(LENGTH))
print("YOUR GENERATED PASSWORD IS:",password)