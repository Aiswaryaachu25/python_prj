import random

n = int(input ("enter the number limit (0 - ?)"))
secret = random.randint(0,n)
attempt = 0
found=0
for i in range(10):
    attempt = attempt+1
    guess = int(input(f"Guess the number(0-{n}).."))

    if(guess==secret):
        print("\ncongratulations!!!you have found it in your ",attempt,"th attempt 🎊🎉\n\n\n")
        found=1
        break
    elif(guess>secret):
        print("ahmmm lower..")
    else:
        print("ahmmm higher")
if(found==0):
    print("\nOOOPS!!!sorry you are out of limits 😔try again🥹\n")
    