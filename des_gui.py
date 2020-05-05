# Description: 
# Authors: Daniel Navarro, Nick Bishop
import tkinter.font as font
from tkinter import *
from des import DesKey



def encrypt_txt():
    key = ent_choose_key.get().encode()
    key = DesKey(key)
    encrypted_txt = ent_encrypt.get().encode()
    message = key.encrypt(encrypted_txt, padding=True)
    encrypted_txt_lbl["text"] = f"{message}"
    print(message)


def decrypt_txt():
    key = ent_choose_key.get().encode()
    key = DesKey(key)
    decrypted_txt = ent_decrypt.get().encode()
    message = key.decrypt(decrypted_txt, padding=True)
    decrypted_txt_lbl["text"] = f"{message}"
    print(message)



root = Tk()
root.title("Welcome to the DES...")
root.configure(background="#3e3e3e")
#root.geometry('720x580')

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
"""
Key prompt widget
"""
# Label for prompting user for key
choose_key_lbl = Label(
    root,
    text="Choose a key of length 18, 16, or 24:",
    foreground="white",
    background="#3e3e3e",
    # bd="3",
    # relief="solid"
)
# Entry field for key
ent_choose_key = Entry(
    root,
    # foreground="white",
    # background="#3e3e3e",
    # bd="6",
    # relief="solid"
)

"""
Widget for encrypting string
"""
# Label for prompting user to enter a string
choose_str_lbl = Label(
    root,
    text="Enter a string to encrypt:",
    foreground="white",
    background="#3e3e3e",
    # bd="3",
    # relief="solid"
)
# Entry field for user inputted string
ent_encrypt = Entry(
    root,
    # foreground="white",
    # background="#3e3e3e",
    # bd="6",
    # relief="solid"
)
#  button for encrypting text [button 1]
encrypt_str_btn = Button(
    root,
    text="Encrypt",
    command=encrypt_txt
)
encrypted_txt_lbl = Label(
    root,
    text="",
    foreground="white",
    background="#3e3e3e"
)

"""
Widget for decrypting string
"""
# label for display/prompting user the encrypted string
decrypt_str_lbl = Label(
    root,
    text="Enter an encrypted string to decrypt:",
    foreground="white",
    background="#3e3e3e",
    # bd="3",
    # relief="solid"
)
# Entry field  for decrypting string
ent_decrypt = Entry(root, text="enter")
# Need a button for decrypting text [button 2]
decrypt_str_btn = Button(
    root,
    text="Decrypt",
    command=decrypt_txt
)
decrypted_txt_lbl = Label(
    root,
    text="",
    foreground="white",
    background="#3e3e3e"
)



""" 
Positioning on screen 
"""

Intro_title.grid(row=0)
Intro_desc.grid(row=1)
# choose_str_frame.grid(row=2, column=0)

# Prompt for key Label and Entry field
choose_key_lbl.grid(row=2, column=0, pady=5)
ent_choose_key.grid(row=3, column=0)
# Encryption widget: label, entry field, button, and result label
choose_str_lbl.grid(row=4, column=0, pady=10)
ent_encrypt.grid(row=5, column=0, padx=10)
encrypt_str_btn.grid(row=6, column=0, pady=10)
encrypted_txt_lbl.grid(row=7, column=0, pady=10)

# Decrypt label, entry field, and button
decrypt_str_lbl.grid(row=8, column=0, pady=5)
ent_decrypt.grid(row=9, column=0)
decrypt_str_btn.grid(row=10, column=0, pady=10)
decrypted_txt_lbl.grid(row=11, column=0, pady=10)






root.mainloop()
