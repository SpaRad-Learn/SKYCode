#pip install gtts
import tkinter as tk
#import gTTS as gtts
from IPython.display import Audio

root = tk.Tk() # Create the main application window a.k.a. widget
root.title("SKY Tkinter App") # Set the window title
root.iconbitmap('Cross.ico') # Set the window icon , must be in same directory as this file 
root.geometry("800x500") # Set the window size

#mylabel = tk.Label(root, text="Welcome to SKY Tkinter App!", font=("Helvetica", 16)) # Create a label
#mylabel.pack(pady=20) # Pack the label with some vertical padding   
#mylabel2 = tk.Label(root, text="This is a sample Tkinter application.", font=("Helvetica", 12)) # Create another label
#mylabel2.pack(pady=10) # Pack the second label with some vertical padding
#mylabel.grid(row=0, column=0) # Position the first label using grid
#mylabel2.grid(row=1, column=1) # Position the second label using grid
e = tk.Entry(root, width=40, borderwidth=5) # Create an entry widget
e.pack() # Pack the entry widget
lang= tk.picklist = ["English", "Spanish", "French", "Italian", "Telugu"]    # List of programming languages
lang_var = tk.StringVar(root) # Create a StringVar to hold the selected language
#lang_var.set(lang[0]) # Set the default value to the first language
lang_menu = tk.OptionMenu(root, lang_var, *lang) # Create an OptionMenu widget
lang_menu.pack() # Pack the OptionMenu widget


VoiceAs = tk.StringVar(root) # Create a StringVar to hold the selected voice
VoiceAs.get() 

Radiobutton1 = tk.Radiobutton(root, text="Male",variable=VoiceAs, value='Male') # Create a Radiobutton
Radiobutton1.pack() # Pack the Radiobutton  
Radiobutton2 = tk.Radiobutton(root, text="Female", variable=VoiceAs, value='Female') # Create a Radiobutton
Radiobutton2.pack() # Pack the Radiobutton  

def say_hello():
    my_label = tk.Label(root, text="Hello There! You selected "+lang_var.get()+ " and voice " + VoiceAs.get(),fg="blue", font=("Helvetica", 16)) # Create a label
    my_label.pack()
button = tk.Button(root, text="Say Hello",command=say_hello,fg="red",bg="yellow",font=("Helvetica", 12)) # Create and pack a button##
button.pack(padx=60, pady=30) # Add some padding around the button



root.mainloop() # Start the Tkinter event loop