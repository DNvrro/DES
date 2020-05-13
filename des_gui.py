# Description: 
# Authors: Daniel Navarro, Nick Bishop
import tkinter as tk
import tkinter.font as font
from tkinter import *
from des import DesKey


def encrypt_txt():

    key = ent_choose_key.get()
    print(len(key))
    if len(key) == 8 or len(key) == 16 or len(key) == 24:
        error_lbl['text'] = ''
        key2 = key.encode()
        print(f'key 2 is : {key2}')
        key2 = DesKey(key2)
        encrypted_txt = ent_encrypt.get().encode()
        print(encrypted_txt)
        message = key2.encrypt(encrypted_txt, padding=True)
        message = str(message)
        message = message[2:]
        message = message[:len(message) - 1]
        encrypted_txt_lbl["text"] = f"Encrypted String: {message}"
        decrypt_str_btn = Button(
            root,
            text="Decrypt",
            command=decrypt_txt
        )
        decrypt_str_btn.grid(row=10, column=0, pady=10)
        print(message)


    else:
        error_lbl['text'] = 'PLEASE MAKE SURE YOUR KEY IS OF LENGTH 8, ' \
                            '16, OR 24!'


def decrypt_txt():
    key = ent_choose_key.get().encode()
    if len(key) == 8 or len(key) == 16 or len(key) == 24:
        error_lbl['text'] = ''
        key2 = DesKey(key)
        decrypted_txt = ent_encrypt.get().encode()
        decrypted_txt = key2.encrypt(decrypted_txt, padding=True)
        message = key2.decrypt(decrypted_txt, padding=True)
        message = str(message)
        message = message[2:]
        message = message[:len(message) - 1]
        decrypted_txt_lbl["text"] = f"Decrypted String: {message}"
        print(message)
    else:
        error_lbl['text'] = 'PLEASE MAKE SURE YOUR KEY IS OF LENGTH 8, ' \
                            '16, OR 24!'

def reset_all():
    ent_choose_key.delete(0, 'end')
    ent_encrypt.delete(0, 'end')
    error_lbl['text'] = ''
    encrypted_txt_lbl['text'] = ''
    decrypted_txt_lbl['text'] = ''



root = Tk()
root.title("Welcome to the DES...")
root.configure(background="#3e3e3e")


# root.geometry('720x580')


# define font
myFont = font.Font(size=20)

# Intro Label - Dialog box
Intro_title = Label(

    root,
    text="Welcome to our DES Project!\n",
    foreground="white",  # Set the text color to white
    background="#3e3e3e"  # Set the background color to grayish
)
Intro_title['font'] = myFont

# description below introductory title
Intro_desc = Label(

    root,
    text="This project encrypts and decrypts a user defined message using the"
         "Data Encryption Standard technique as discussed in CSEN 4340.\n\n"
         "Simply enter a key string and type a message you would like to "
         "encrypt. "
         "When you are ready, click the encrypt button to see your "
         "encrypted message.\n",
    foreground="white",
    background="#3e3e3e",
    # background="red",
    width="70",
    wraplength="350"
)

"""
Key prompt widget
"""
# Label for prompting user for key
choose_key_lbl = Label(

    root,
    text="Choose a key of length 8, 16, or 24:",
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

decrypted_txt_lbl = Label(

    root,
    text="",
    foreground="white",
    background="#3e3e3e"
)
"""
Reset Button
"""
reset_btn = Button(
    root,
    text='Reset',
    width=30,
    command=reset_all
)
"""
Error Label
"""
error_lbl = Label(
    root,
    text='',
    foreground='red',
    background='#3e3e3e'
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

# Positioning of the Decrypt button
decrypted_txt_lbl.grid(row=11, column=0, pady=10)
# Positioning of Error label
error_lbl.grid(row=12, column=0, pady=10)
# Positioning of Reset Button
reset_btn.grid(row=13, column=0, pady=5)
root.mainloop()
