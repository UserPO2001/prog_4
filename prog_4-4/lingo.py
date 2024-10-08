import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import random

from highscores import Highscores

class LingoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lingo Grid")
        self.geometry("400x600")  # Adjusted height to accommodate bottom frame

        # The correct word to guess
        self.correct_word = self.selecteer_woord()
        print(f"Correct word for testing: {self.correct_word}")  # Display word in terminal for testing
        self.current_row = 0  # To track the current row for guesses
        self.beurt = 0  # Track the number of turns (beurten)

        # Initialize the highscores object
        self.highscores = Highscores()

        # Player name variable
        self.player_name = ""

        # Create the top padding frame
        self.top_frame = tk.Frame(self, height=100, bg="lightgray")
        self.top_frame.grid(row=0, column=0, sticky="ew")  # Position the top padding frame

        # Add welcome text to the top frame
        self.welcome_label = tk.Label(self.top_frame, text="Welkom, voer je naam in om te spelen",
                                      font=("Helvetica", 12), bg="lightgray")
        self.welcome_label.pack(expand=True, pady=10)  # Center the label with some padding

        # Create an entry widget for the player to input their name
        self.name_entry = tk.Entry(self.top_frame, font=("Helvetica", 12), justify="center")
        self.name_entry.pack(pady=5)

        # Add a start button to submit the name
        self.start_button = tk.Button(self.top_frame, text="Start", font=("Helvetica", 12),
                                       fg="blue", command=self.start_game)
        self.start_button.pack(pady=5)

        # Add a button to view highscores with a blue background
        self.highscores_button = tk.Button(self.top_frame, text="Highscores", font=("Helvetica", 12),
                                  fg="blue", command=self.show_highscores)
        self.highscores_button.pack(pady=5)


        # Create the grid frame (hidden until the player starts the game)
        self.grid_frame = tk.Frame(self)
        self.grid_frame.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
        self.grid_frame.grid_remove()  # Hide grid frame initially

        # Configure the rows and columns to expand
        for i in range(5):  # 5 rows for guesses
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

        # Create the bottom frame (hidden until the player starts the game)
        self.bottom_frame = tk.Frame(self, height=50, bg="lightgray")
        self.bottom_frame.grid(row=2, column=0, sticky="ew")
        self.bottom_frame.grid_remove()  # Hide bottom frame initially

        # Add a submit button to the bottom frame
        self.submit_button = tk.Button(self.bottom_frame, text="Submit", font=("Helvetica", 12),
                                        fg="blue", width=10, command=self.check_guess)
        self.submit_button.pack(pady=10)  # Center the button with padding

        # Adjust the weight of the rows and columns to fill the window
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def selecteer_woord(self):
        """
        Connects to the SQLite database and selects a random word.
        """
        connection = sqlite3.connect('lingo.sqlite3')
        cursor = connection.cursor()

        # Query to get all words from the database
        cursor.execute("SELECT woord FROM vijfletters")
        words = [row[0] for row in cursor.fetchall() if row[0] is not None]

        # Close the connection
        connection.close()

        if not words:
            raise ValueError("No words found in the database.")
        
        # Return a random word
        return random.choice(words)

    def start_game(self):
        """
        Starts the game by validating the player name and showing the game grid.
        """
        self.player_name = self.name_entry.get().strip()
        if not self.player_name:
            messagebox.showinfo("Error", "Voer je naam in om te beginnen.")
            return

        # Hide the name entry and start button
        self.name_entry.pack_forget()
        self.start_button.pack_forget()

        # Change the welcome text
        self.welcome_label.config(text=f"Welkom {self.player_name}, raad het woord van vijf letters!")

        # Show the game grid and submit button
        self.grid_frame.grid()
        self.bottom_frame.grid()

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
            messagebox.showinfo("Error", "Please enter a 5-letter word.")
            return

        # Increment the number of turns
        self.beurt += 1

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
                    self.entries[self.current_row][i].config(bg="orange")  # Turn misplaced letters orange
              

        # Move correct letters to the next row, leave orange letters in place
        if guess == self.correct_word:
            messagebox.showinfo("Result", "Correct!")
            self.save_score()  # Save the score when the correct word is guessed
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

    def save_score(self):
        """
        Saves the score (number of turns) to the highscores table.
        """
        # Save the score in the highscores table with the player's name
        self.highscores.add_score(self.player_name, self.beurt)

        messagebox.showinfo("Result", f"Correct! You guessed it in {self.beurt} turns.")

    def show_highscores(self):
        """
        Opens a new window to display the highscores from the database.
        """
        # Create a new top-level window for highscores
        highscores_window = tk.Toplevel(self)
        highscores_window.title("Highscores")
        highscores_window.geometry("300x400")

        # Create a Treeview widget to display the highscores in a table
        columns = ("Name", "Turns")
        tree = ttk.Treeview(highscores_window, columns=columns, show="headings")
        tree.heading("Name", text="Name")
        tree.heading("Turns", text="Turns")
        tree.pack(expand=True, fill="both")

        # Fetch the highscores from the database and insert into the table
        highscores = self.highscores.get_highscores()
        for score in highscores:
            tree.insert("", "end", values=score)

        # Add a close button
        close_button = tk.Button(highscores_window, text="Close", command=highscores_window.destroy)
        close_button.pack(pady=10)

if __name__ == "__main__":
    app = LingoApp()
    app.mainloop()
