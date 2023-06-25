import tkinter as tk

def mostrarInfo():   
    if e1.get()=="":
    	TextlbSalida.set("Debe rellenar los campos.")
    else:
    	print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    	TextlbSalida.set("Nombre completo " + e1.get() + " " + e2.get())

root = tk.Tk()
root.title("Formulario nombre")
# The root widget has to be created before any other widgets and there can only be one root widget.
tk.Label(root, 
         text="First Name").grid(row=0)
tk.Label(root, 
         text="Last Name").grid(row=1)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(root, 
          text='Quit', 
          command=root.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.E, 
                                    pady=4)
tk.Button(root, 
          text='Show', command=mostrarInfo).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

TextlbSalida = tk.StringVar()
lbSalida = tk.Label(root, textvariable=TextlbSalida).grid(row=2,columnspan=2)
tk.mainloop()


# mainloop(): There is a method known by the name mainloop() is used when you are ready for the application to run. 
# mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.


# while True:
#   event=wait_for_event()
#   event.process()
#   if main_window_has_been_destroyed():
#     break

# The window won't appear until we enter the Tkinter event loop:
# root.mainloop()
# Our script will remain in the event loop until we close the window.


# https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop/29158947
# Put in the simplest terms possible: always call mainloop as the last logical line of code in your program. 
# That's how Tkinter was designed to be used.




# https://python-para-impacientes.blogspot.com/2016/02/variables-de-control-en-tkinter.html