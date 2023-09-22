                                                         # Guess Number in 10 Attemots (limited attempts)
import tkinter as tk
import random

winning_no = random.randint(1,50)
attempts = 0


def Guessing_Game():
    global attempts
    attempts += 1
    num = int(entry.get())             # # This will store the value entered in entry(textbox) into 'num' variable

    if attempts == 10:
        result_label.configure(text = "---!GAME OVER!---")
        Guess_button.configure(state = tk.DISABLED)

    elif num > winning_no:
        if num in range(winning_no + 1, winning_no + 4):
            result_label.configure(text = "You are too close!, Enter a little smaller no.")        #print() will print msg in pycharm (not in GUI window)
        else:
            result_label.configure(text = "Too Large!, Enter a smaller no.")

    elif num < winning_no:
        if num in range(winning_no - 3, winning_no):
            result_label.configure(text = "You are too close!, Enter a little Larger no.")
        else:
            result_label.configure(text="Too small!, Enter a Larger no.")

    else:
        result_label.configure(text = f"*_*_*_*YOU WON_*_*_*_*\n You have guessed the number in {attempts} guesses")
        Guess_button.configure(state=tk.DISABLED)

    attempt_label.config(text=f"Attempts left: {10 - attempts}")




root = tk.Tk()                       # Create a window
root.title("Guessing Game")          # Give Title to window
root.geometry("400x200")             # set window size

label = tk.Label(root,text = "*Welcome To The Number Guessing Game*\nGuess the number (between 1 to 50) in 10 attempts")      # Add Text to window
label.pack(pady = 10)                                                                    # To include text in window and adjust position using pady

attempt_label = tk.Label(root, text ="")
attempt_label.pack()

entry = tk.Entry(root, width= 40)
entry.pack(pady = 10)

Guess_button = tk.Button(root,text="Guess", command = Guessing_Game)
Guess_button.pack()

result_label = tk.Label(root,text="")
result_label.pack(pady = 10)

root.mainloop()
