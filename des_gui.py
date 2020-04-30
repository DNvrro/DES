# Description: 
# Authors: Daniel Navarro, Nick Bishop
import tkinter.font as font
from tkinter import *
from des import DesKey


def encrypt():
    pass


def decrypt():
    pass


root = Tk()
root.title("Welcome to the DES...")
root.configure(background="#3e3e3e")
root.geometry('720x480')

# define font
myFont = font.Font(size=20)

# Intro Label - Dialog box
Intro_title = Label(
    root,
    text="Welcome to our DES Project!",
    foreground="white",  # Set the text color to white
    background="#3e3e3e"  # Set the background color to grayish
)
Intro_title['font'] = myFont

# description below introductory title
Intro_desc = Label(
    root,
    text="Description of app and how to use it. Description of app "
         "and how to use it. Description of app and how to use it.",
    foreground="white",
    background="#3e3e3e",
    # background="red",
    width="70",
    wraplength="300"
)

# choose_str_frame = Frame(
#                     root,
#                     background="White",
#                     height=9,
#                     width=15
# )

# Label for prompting user to enter a string
choose_str = Label(
    root,
    text="Choose a string to Encrypt",
    foreground="white",
    background="#3e3e3e",
    bd="3",
    relief="solid"
)

# label for display/prompting user the encrypted string
encrypt_str_lab = Label(
    root,
    text="Encrypted String",
    foreground="white",
    background="#3e3e3e",
    bd="3",
    relief="solid"
)

# label for display/prompting user the decrypted string
decrypt_str_lab = Label(
    root,
    text="Decrypted String: ",
    foreground="white",
    background="#3e3e3e",
    bd="3",
    relief="solid"
)

# Need an entry field box for user string to encrypt
ent_encrypt = Entry(
    root,
    foreground="white",
    background="#3e3e3e",
    bd="6",
    relief="solid"
)

# Need an entry field box for decrypting string
ent_decrypt = Entry(root)

# Need an entry field for DISPLAYING decrypted string ONLY
ent_display_decrypt = Entry(root)

# Need a button for encrypting text [button 1]
encrypt_str_bt = Button(
    root,
    text="Encrypt",
    command=encrypt
)

# Need a button for decrypting text [button 2]
decrypt_str_bt = Button(
    root,
    text="Decrypt",
    command=decrypt
)

""" pushing onto the screen and positioning """

Intro_title.grid(row=0)
Intro_desc.grid(row=1)
# choose_str_frame.grid(row=2, column=0)
choose_str.grid(row=2, column=0, pady=5)
encrypt_str_lab.grid(row=6, column=0, pady=5)
decrypt_str_lab.grid(row=10, column=0, pady=5)
# Entry Fields
ent_encrypt.grid(row=3, column=0, padx=10)
ent_decrypt.grid(row=7, column=0)
ent_display_decrypt.grid(row=11, column=0)
# buttons
encrypt_str_bt.grid(row=4, column=0, pady=10)
decrypt_str_bt.grid(row=8, column=0, pady=10)

root.mainloop()
