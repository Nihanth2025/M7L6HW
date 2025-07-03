import tkinter as tk
from tkinter import messagebox
import random
def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    result = decide_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Rock", width=15, command=lambda: play('Rock')).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play('Paper')).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play('Scissors')).pack(pady=5)

root.mainloop()