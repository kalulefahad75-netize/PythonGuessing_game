**Progressive Number Guessing Game**

This is a GUI-based number guessing game built using Python and the Tkinter library.
The game challenges players to guess a randomly generated number within a given range, with progressively increasing difficulty after each successful round.

========Features========

Graphical User Interface (GUI) using Tkinter
 
Random number generation using random module

Progressive difficulty (range increases every level)

Limited number of attempts per round

Input validation (handles invalid or out-of-range input)

======Option to:======

Continue to next level

Fully reset the game

========How the Game Works========

The game starts at Level 1 with a number range from 1 to 100.

The player has 7 attempts to guess the correct number.

After each guess:

The game tells you if your guess is too high or too low.

If the player guesses correctly:

They move to the next level.

The number range increases by +100 (e.g., 1–200, 1–300…).

If the player runs out of attempts:

The game ends and resets to Level 1

=========Input Handling========

Only whole numbers are accepted.

If the user enters:

Text → warning message

Decimal → warning message

Number outside range → warning message

Invalid inputs do not count as attempts.

========Code Structure========

Class: GuessingGame

The entire game is managed inside this class.

Key Methods:

__init__(): Initializes the game window and variables.

create_widgets(): Creates all GUI components (labels, buttons, entry fields).

start_round(): Starts a new round and generates a new random number.

check_guess():Handles:

Input validation

Guess checking

Win/Lose logic

update_attempt_label()

Updates the attempt counter display.

full_game_reset()

Resets the game back to Level 1.

🖥️ Requirements

Python 3.x

Tkinter (comes pre-installed with most Python distributions)

▶️ How to Run

Save the code in a file, e.g.:

guessing_game.py

Open terminal/command prompt.

Run the program:

python guessing_game.py

========Game Interface========

The interface includes:

Title and instructions

Current level and range

Attempt counter

Input box for guesses

Buttons:

Check Guess

Full Reset


By KALULE FAHAD
