# 🔐 Password Guessing Game

A simple and fun Python command-line game where players try to guess a secret password.  
The game offers **Easy**, **Medium**, and **Hard** difficulty levels, with hints after every wrong guess.

---

## 📌 Table of Contents
- [About the Game](#-about-the-game)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Game Rules](#-game-rules)
- [Example Gameplay](#-example-gameplay)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔍 About the Game
This game randomly selects a password from a list of words based on the difficulty level chosen by the player.  
Players must guess the password in as few attempts as possible, with hints provided to reveal correctly guessed letters in their exact positions.

---

## ✨ Features
- Three difficulty levels:
  - **Easy** (simple, short words)
  - **Medium** (moderate-length words)
  - **Hard** (long or tricky words)
- Random password selection
- Hints after every wrong guess
- Tracks the number of attempts
- Simple, beginner-friendly Python code

---

## 🛠 Technologies Used
- **Python 3**
- **Random module** – For random word selection

---

## 📥 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/password-guessing-game.git
   cd password-guessing-game
Run the game

bash
Copy
Edit
python guessing_game.py
🚀 Usage
Choose the difficulty level: Easy, Medium, or Hard.

Guess the password by typing words.

After each wrong guess, you’ll get a hint showing correctly placed letters.

Keep guessing until you find the correct password.

🎮 Game Rules
You can guess unlimited times until you get the correct password.

A hint will replace correctly guessed letters in their right positions.

Wrong guesses will not be penalized but will increase your attempt count.

📝 Example Gameplay
mathematica
Copy
Edit
Welcome to the Password Guessing Game
Choose the Difficulty Level- Easy/Medium/Hard
Enter Difficulty: easy

Guess The Secret Password
Enter your Guess: apple
Congratulations! You Guessed it in 1 attempts.
You got it Right 🥳👍
Game Over!
🤝 Contributing
Fork the repository

Create a new branch (feature/YourFeatureName)

Commit your changes

Push to your branch and open a Pull Request

