import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Progressive Number Guessing Game")
        self.root.geometry("400x380") 
        self.root.configure(padx=20, pady=20)

        # Game States Variables for Progressive Difficulty
        self.current_level = 1
        self.min_range = 1
        self.current_max_range = 100 
        
        self.attempts = 0
        self.max_attempts = 7
        self.secret_number = 0 # this intialise rounds

        self.create_widgets()
        self.start_round() # Initialize the first round

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="I'm thinking of a number...", font=("Helvetica", 14, "bold"))
        self.title_label.pack(pady=(0, 5))

        # Range label 
        self.range_label = tk.Label(self.root, text="", font=("Helvetica", 11, "bold"), fg="purple")
        self.range_label.pack()

        self.instruction_label = tk.Label(self.root, text="")
        self.instruction_label.pack()

        self.attempt_label = tk.Label(self.root, text="", font=("Helvetica", 10))
        self.attempt_label.pack(pady=5)

        # Input Field
        self.entry = tk.Entry(self.root, font=("Helvetica", 12), justify='center')
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.check_guess())
        self.entry.focus_set() 

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.check_button = tk.Button(self.button_frame, text="Check Guess", command=self.check_guess,
        bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), padx=10, width=12)
        self.check_button.pack(side=tk.LEFT, padx=5)

        # "Reset Game" button (full reset, starts over from level 1)
        self.reset_button = tk.Button(self.button_frame, text="Full Reset", command=self.full_game_reset, 
        bg="#f44336", fg="white", font=("Helvetica", 10, "bold"), padx=10, width=12)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 10, "italic"))
        self.result_label.pack(pady=10)

    def start_round(self):
        self.secret_number = random.randint(self.min_range, self.current_max_range)
        self.attempts = 0
        
        # Updates UI text to reflect current difficulty
        self.range_label.config(text=f"Level {self.current_level}: {self.min_range} - {self.current_max_range}")
        self.instruction_label.config(text=f"(Max {self.max_attempts} attempts)")
        self.update_attempt_label()
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Good luck!", fg="blue")
        self.entry.focus_set()

    def update_attempt_label(self):
        self.attempt_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

    def check_guess(self):
        try:
            # Input Validation 
            input_value = self.entry.get()
            
            #checks if the string is a whole number
            guess = int(input_value)
            
            if guess < self.min_range or guess > self.current_max_range:
                messagebox.showwarning("Out of Range", f"Please enter a number within the current range: {self.min_range} to {self.current_max_range}.")
                self.entry.delete(0, tk.END) 
                return

        except ValueError:
            # Triggered if 'guess' is text, decimal, or empty
            messagebox.showwarning("Invalid Input", "That is not a number. Please enter a whole number.")
            self.entry.delete(0, tk.END) # Clear input but DON'T add attempt
            return # Exit check_guess immediately.

        # Increment attempt counter
        self.attempts += 1
        self.update_attempt_label()

        # Checks for Win Condition
        if guess == self.secret_number:
            self.result_label.config(text="COGRAGULATIONS YOU GOT IT! ", fg="green")
        
            message = f"Winner! {self.secret_number} was correct.\nIt took {self.attempts} attempts.\n\n"
            
            self.current_level += 1
            self.current_max_range += 100 

            message += f"Want to play the next harder level (Level {self.current_level}: {self.min_range}-{self.current_max_range})?"
            
            if messagebox.askyesno("Round Over!", message):
                self.start_round() 
            else:
                self.full_game_reset() 
            return

        # Check for the Lose Condition
        if self.attempts >= self.max_attempts:
            messagebox.showwarning("Game Over!", f"Out of attempts!\n\nThe number was {self.secret_number}.\nTry starting over?")
            self.full_game_reset() 
            return

        # Handle incorrect guesses (Too high / Too low)
        if guess < self.secret_number:
            self.result_label.config(text=f"Too low! (Last guess: {guess})", fg="red")
        elif guess > self.secret_number:
            self.result_label.config(text=f"Too high! (Last guess: {guess})", fg="red")
        
        self.entry.delete(0, tk.END) # Clears entry for next guess

    # Completely resets difficulty back to Level 1
    def full_game_reset(self):
        self.current_level = 1
        self.current_max_range = 100
        self.result_label.config(text="Game restarted from Level 1.", fg="black")
        self.start_round()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGame(root)
    root.mainloop()