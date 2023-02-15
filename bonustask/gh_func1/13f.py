import random
name = input("Hello! What is your name?\n")
print(f"Well, {name}, I am thinking of a number between 1 and 20")
num = 0
rnum= random.randint(1, 20)
guess=1
while num!=rnum:
    num = int(input("Take a guess.\n"))
    if num<rnum:
        print("Your guess is too low.")
        guess+=1
    elif num>rnum:
        print("Your guess is too high.")
        guess+=1
    else:
        print(f"Good job, {name}! You guessed my number in {guess} guesses!")
        newrnum=random.randint(1, 20)
        rnum=newrnum
        break
    