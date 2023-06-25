# Push the button to reveal a regular or shiny Magikarp

import tkinter as tk
import random


# Functions
def reset_count():

	count = 0
	count_label.config(text = str(count))


def check_shiny():
	
	probability = random.randint(0,9)
	if probability == 0: # Shiny!
		img_label.config(image=shiny)
		count = int(count_label.cget("text"))
		count_label.config(text = str(count+1))
	else: # Regular
		img_label.config(image=regular)
	
	str_prob = str(probability)
	prob_label.config(text = str_prob)


# Main window, size, background and title
root = tk.Tk()
root.geometry('300x120')							
root.configure(background = "Light blue")
root.title("Magikarp.exe")

# container.columnconfigure(index, weight)
root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)


# Image objects
regular = tk.PhotoImage(file="shuny/regular_magikarp.png")
shiny = tk.PhotoImage(file="shuny/shiny_magikarp.png")
question = tk.PhotoImage(file="shuny/question.png")

# Labels
intro_label = tk.Label(root, text = "Check if your Magikarp is shiny")
intro_label.grid(row=0, column=0, columnspan = 3) #, sticky=tk.W, padx=5, pady=5)

# Label showing initial question image and the future Magikarp image
img_label = tk.Label(root, image = question)				
img_label.grid(row=1, column=0, rowspan = 2)

# Button revealing the Magikarp when pushing it
action_button = tk.Button(root, text="Gimme", command = check_shiny)
action_button.grid(row=1, column=1)

# Reset button
reset_button = tk.Button(root, text="Reset", command = reset_count)
reset_button.grid(row=1, column=2)

# Probability label
str_prob = str(0)
prob_label = tk.Label(root, text = str_prob )
prob_label.grid(row=2, column=1)

# Count label
count = 0
count_label = tk.Label(root)
reset_count()
count_label.grid(row=2, column=2)


root.mainloop()