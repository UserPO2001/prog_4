import tkinter as tk
from tkinter import messagebox
from word_library import get_random_word

class LingoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lingo Grid")
        self.geometry("400x600")  

        # The correct word to guess
        self.correct_word = get_random_word()
        self.current_row = 0  

        # Create the top padding frame
        self.top_frame = tk.Frame(self, height=100, bg="lightgray")
        self.top_frame.grid(row=0, column=0, sticky="ew")  # Position the top padding frame

        # Add welcome text to the top frame
        self.welcome_label = tk.Label(self.top_frame, text="Welkom, raad het woord van vijf letters in vijf beurten",
                                      font=("Helvetica", 12), bg="lightgray")
        self.welcome_label.pack(expand=True, pady=10)  # Center the label with some padding

        # Create the grid frame
        self.grid_frame = tk.Frame(self)
        self.grid_frame.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")  # Place the grid frame

       
        for i in range(5):  
            self.grid_frame.grid_rowconfigure(i, weight=1)
            self.grid_frame.grid_columnconfigure(i, weight=1)

        # Create the 5x5 grid of Entry widgets
        self.entries = []
        for row in range(5):  # 5 rows to handle guesses
            row_entries = []
            for col in range(5):
                entry = tk.Entry(self.grid_frame, font=("Helvetica", 24),  # Larger font size for bigger squares
                                 justify="center", bg="blue", fg="white", width=2)
                entry.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")  # 2-pixel gap
                row_entries.append(entry)
            self.entries.append(row_entries)

        # Create the bottom frame
        self.bottom_frame = tk.Frame(self, height=50, bg="lightgray")
        self.bottom_frame.grid(row=2, column=0, sticky="ew")  # Position the bottom frame

        # Add a submit button to the bottom frame
        self.submit_button = tk.Button(self.bottom_frame, text="Submit", font=("Helvetica", 12),
                                       bg="blue", fg="white", width=10, command=self.check_guess)
        self.submit_button.pack(pady=10)  # Center the button with padding

        # Adjust the weight of the rows and columns to fill the window
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def check_guess(self):
        """
        Checks the current guess against the correct word and updates the grid colors.
        """
        if self.current_row >= 5:
            messagebox.showinfo("Result", "No more guesses allowed.")
            return

        # Collect the guess from the current row
        guess = ''.join(entry.get().lower() for entry in self.entries[self.current_row])
        if len(guess) != 5:
            messagebox.showinfo("Error", "Please enter an other 5-letter word.")
            return

        # Lists to track correct letters and their positions
        correct_positions = [False] * 5
        correct_letter_count = {char: self.correct_word.count(char) for char in set(self.correct_word)}

        # Determine which letters are correct and in the correct position
        for i in range(5):
            if guess[i] == self.correct_word[i]:
                correct_positions[i] = True
                correct_letter_count[guess[i]] -= 1
                self.entries[self.current_row][i].config(bg="red")  # Turn correct positions red

        # Determine which letters are correct but in the wrong position
        for i in range(5):
            if not correct_positions[i] and guess[i] in self.correct_word:
                if guess[i] in correct_letter_count and correct_letter_count[guess[i]] > 0:
                    correct_letter_count[guess[i]] -= 1
                    self.entries[self.current_row][i].config(bg="yellow")  # Turn misplaced letters yellow
                else:
                    self.entries[self.current_row][i].config(bg="gray")  # Optional: turn incorrect letters gray

        # Move correct letters to the next row, leave yellow letters in place
        if guess == self.correct_word:
            messagebox.showinfo("Result", "Correct!")
            self.current_row = 5  # Stop further guesses
        else:
            # Move correct letters to the next row only if guess was not correct
            for i in range(5):
                if correct_positions[i] and self.current_row < 4:
                    self.entries[self.current_row + 1][i].delete(0, tk.END)
                    self.entries[self.current_row + 1][i].insert(0, guess[i])
                    self.entries[self.current_row + 1][i].config(bg="red")

            # Move to the next row only if the guess was not correct
            self.current_row += 1

        # Check if the game is over
        if self.current_row >= 5:
            if guess != self.correct_word:
                messagebox.showinfo("Result", "Game Over! The correct word was " + self.correct_word)

if __name__ == "__main__":
    app = LingoApp()
    app.mainloop()
