import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Word list
word_list = [
    "apple", "banana", "cherry", "dog", "elephant", "forest", "guitar",
    "honey", "island", "jungle", "kangaroo", "lemon", "mountain", "notebook",
    "ocean", "pencil", "quartz", "river", "sunflower", "tiger", "umbrella",
    "violet", "whale", "xylophone", "yellow", "zebra"
]

# Initialize game variables
chosen_word = random.choice(word_list)
placeholder = "_" * len(chosen_word)
added_letters = []
wrong_guesses = []
lives = 6

# GUI setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("600x700")
root.configure(bg="#f0f8ff")  # Light blue background

# Function to load hangman images
def load_hangman_image(stage):
    img = Image.open(f"hangman{stage}.png")  # Replace with your image paths
    img = img.resize((300, 300), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

# GUI components
hangman_image = load_hangman_image(0)
image_label = tk.Label(root, image=hangman_image, bg="#f0f8ff")
image_label.pack(pady=20)

placeholder_label = tk.Label(
    root, text=placeholder, font=("Helvetica", 24), bg="#f0f8ff", fg="black"
)
placeholder_label.pack(pady=10)

wrong_label = tk.Label(
    root, text="Wrong guesses: None", font=("Helvetica", 14), bg="#f0f8ff", fg="red"
)
wrong_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

guess_label = tk.Label(input_frame, text="Enter a letter:", font=("Helvetica", 14), bg="#f0f8ff")
guess_label.grid(row=0, column=0, padx=5)

guess_entry = tk.Entry(input_frame, font=("Helvetica", 14))
guess_entry.grid(row=0, column=1, padx=5)

submit_button = tk.Button(
    input_frame, text="Submit", font=("Helvetica", 14), bg="#4CAF50", fg="white",
    command=lambda: process_guess()
)
submit_button.grid(row=0, column=2, padx=5)

status_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f0f8ff", fg="black")
status_label.pack(pady=20)

# Function to process the user's guess
def process_guess():
    global placeholder, lives, added_letters, wrong_guesses

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)  # Clear the entry box

    if not guess.isalpha() or len(guess) != 1:
        status_label.config(text="Please enter a single valid letter.")
        return

    if guess in added_letters or guess in wrong_guesses:
        status_label.config(text=f"You've already guessed '{guess}'. Try again.")
        return

    # Check if guess is correct
    if guess in chosen_word:
        added_letters.append(guess)
        new_placeholder = ""
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess or placeholder[i] != "_":
                new_placeholder += chosen_word[i]
            else:
                new_placeholder += "_"
        placeholder = new_placeholder
        placeholder_label.config(text=placeholder)
        status_label.config(text="Correct guess!")
    else:
        wrong_guesses.append(guess)
        lives -= 1
        wrong_label.config(text=f"Wrong guesses: {', '.join(wrong_guesses)}")
        status_label.config(text=f"Wrong guess! Lives left: {lives}")

        # Update hangman image
        new_image = load_hangman_image(6 - lives)
        image_label.config(image=new_image)
        image_label.image = new_image

    # Check for game over
    if "_" not in placeholder:
        messagebox.showinfo("Hangman", "Congratulations, you win! 🎉")
        root.destroy()
    elif lives == 0:
        messagebox.showinfo("Hangman", f"You lose! The word was '{chosen_word}'.")
        root.destroy()

# Run the GUI loop
root.mainloop()
