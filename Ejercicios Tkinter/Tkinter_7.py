import tkinter as tk

root = tk.Tk()  # Creating instance of Tk class
root.title("Centering windows")
root.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 500#768#500
window_width = 900#1366#900

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2)) #☻- (window_width/2)) - 7
y_cordinate = int((screen_height/2) )#- (window_height/2))
print(x_cordinate)
print(y_cordinate)

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.update()
print(root.geometry())

root.mainloop()