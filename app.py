# Project 5 : Hangman Game In Python

import random
import tkinter as tk
from tkinter import messagebox

# Word list for the game
words = ["Pizza", "Fairy", "Bitcoin", "Biryani", "Youtube"]
word = random.choice(words).upper()
guessed_letters = []
attempts = 6

# Create main Tkinter window
root = tk.Tk()
root.title("Futuristic Hangman")
root.geometry("500x600")
root.configure(bg="#00001a")

# Title Label
title_label = tk.Label(root, text="🔮 Hangman Game 🔮", font=("Orbitron", 22, "bold"), fg="#00FFFF", bg="#00001a")
title_label.pack(pady=10)

# Word display
display_word = tk.StringVar()
display_word.set("_ " * len(word))
word_label = tk.Label(root, textvariable=display_word, font=("Orbitron", 18), fg="#FFFFFF", bg="#00001a")
word_label.pack(pady=20)

# Attempts left label
attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Orbitron", 16), fg="#FF6600", bg="#00001a")
attempts_label.pack(pady=10)

def update_display():
    displayed = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    display_word.set(displayed)

def check_letter(letter):
    global attempts
    if letter in guessed_letters:
        messagebox.showinfo("Oops", "You already guessed that letter!")
    else:
        guessed_letters.append(letter)
        if letter not in word:
            attempts -= 1
        update_display()
        attempts_label.config(text=f"Attempts Left: {attempts}")
        check_game_status()

def check_game_status():
    if all(letter in guessed_letters for letter in word):
        messagebox.showinfo("Congratulations!", "You Won! 🎉")
        root.quit()
    elif attempts == 0:
        messagebox.showinfo("Game Over", f"You Lost! The word was {word}.")
        root.quit()

# Letter Buttons
button_frame = tk.Frame(root, bg="#00001a")
button_frame.pack(pady=10)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    btn = tk.Button(
        button_frame, text=letter, font=("Orbitron", 12), bg="#0099FF", fg="black", width=3, relief=tk.FLAT,
        activebackground="#00FFFF", activeforeground="black", command=lambda l=letter: check_letter(l)
    )
    btn.grid(row=(ord(letter) - 65) // 9, column=(ord(letter) - 65) % 9, padx=2, pady=2)

# Exit Button
def exit_game():
    root.quit()

exit_btn = tk.Button(root, text="❌ Exit Game", font=("Orbitron", 14), bg="#FF0000", fg="black", width=12,
                     relief=tk.FLAT, activebackground="#FF3333", activeforeground="black", command=exit_game)
exit_btn.pack(pady=20)

# Start Game
update_display()
root.mainloop()
