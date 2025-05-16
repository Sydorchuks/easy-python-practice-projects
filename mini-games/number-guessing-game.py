import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Enter a larger number")
        quit()
else:
    print("Please type a number next time")
    quit()


random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if(user_guess > random_number):
        print("Too high! Try again")
        guesses +=1
        continue
    
    if user_guess < random_number:
        print("Too low! Try again")
        guesses +=1
        continue

    if(user_guess == random_number):
        print(f"Congratulations! You got it right in {guesses} tries!")
        if(guesses == 0):
            print("Congratulations! You got it right in a first try! ")
        guesses = 0
        break

