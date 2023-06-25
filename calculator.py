import tkinter as tk
import math

def blink_cursor():
    pass


def calculate():
    global display_content
    global display_label
    global operation_ended
    result = eval(display_content) # Calculate the operation
    display_content = result # Show the result on the display
    print(result)
    operation_ended = True


def clear_display():
    global display_content
    display_content = ""


def clear_symbol():
    global display_content

    print("Antes: ", end='')
    print(display_content)
    display_content = display_content[:-1]
    print("Después: ", end='')
    print(display_content)

def update_display():
    
    global display_label
    print("Update display: ", end ='')
    print(display_content)
    display_label.configure(text=display_content)
    

def button_pressed(text):
    global display_content
    global operation_ended

    if (operation_ended):
        display_content=""
        update_display()
        operation_ended = False

    if (text == "="):
        calculate()
    elif (text == "C"):
        clear_display()
    elif (text == "<-"):
        print("Pulsado <- : " + display_content)
        clear_symbol()
    else:
        display_content += text
    
    update_display()


# Main window, size, background and title
root = tk.Tk()
root.geometry('300x200')
root.configure(background = "Light blue")
root.title("Numbers")

base_frame = tk.Frame(master=root, bg="Light blue")
base_frame.pack(expand=True)


# Buttons and labels
display_content = ""
operation_ended = False

display_label = tk.Label(base_frame, text = display_content, background = "White")
display_label.grid(row = 0, column = 0, columnspan = 4, sticky = "EW")


key_labels = ['C', '<', '%', '/', 
            '7', '8', '9', '*', 
            '4', '5', '6', '-', 
            '1', '2', '3', '+', 
            '^', '0', '.', '=']

buttons = []

for i in range(0, len(key_labels)):
    buttons.append( tk.Button(base_frame, text = key_labels[i]) )

    #print( ord(key_labels[i]) )
    #if ( ord(key_labels[i]) >= ord('0') and ord(key_labels[i]) <= ord('9') ):
    #    img_name = 'numbers/images/' + key_labels[i] + '.png'
    #    print(img_name)
    #    buttons[i].configure(image = img_name)
    #    buttons[i].configure(compound = tk.LEFT)
    
    curr_row = math.floor(i/4+1)
    curr_col = i%4

    buttons[i].grid(row = curr_row, column = curr_col, sticky = "NSEW", padx = 2, pady = 2)
    buttons[i].configure(command = lambda arg=buttons[i].cget("text"): button_pressed(arg) )


root.mainloop()