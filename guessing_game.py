import random

easy_words = ["apple", "train", "school", "money", "india"]
medium_words = ["python", "numpy", "matplotlib", "planet", "laptop"]
hard_words = ["elephant", "diamond", "ai engineer", "dream", "mountains"]

print("Welcome to the Password Guessing Game")
print("Choose the Difficulty Level- Easy/Medium/Hard")

level= input("Enter Diffficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret=random.choice(medium_words)
elif level == "hard":
    secret=random.choice(hard_words)
else:
    print("Invalid Choice. Defaulting to easy level")
    secret= random.choice(easy_words)

attempts = 0
print("\n Guess The Secret Password")

while True:
    guess = input("Enter your Guess: ").lower()
    attempts+=1

    if guess==secret:
        print(f'Congratulations! You Guessed it in {attempts} attempts.')
        break

    hint = "" 
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i].lower():
             hint += secret[i]
        else:
            hint +="_"

    print('Hint : ',hint)
print('You got it Right 🥳👍')
print('Game Over!')

