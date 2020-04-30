# Description: 
# Authors: Daniel Navarro, Nick Bishop

from tkinter import *
import tkinter.font as font


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
            text="Description of app and how to use it. Description of app and how to use it. Description of app and how to use it.",
            foreground="white",
            background="#3e3e3e",
            # background="red",
            width="70",
            wraplength="300"
)

# choose_str_frame = Frame(
#                     root,
#                     background="White",
#                     # height=9,
#                     # width=15
# )

# Label for prompting user to enter a string
choose_str = Label(
                    root,
                    text="Choose a string to Encrypt",
                    foreground="white",
                    background="#3e3e3e",
                    bd="6",
                    relief="solid"
)

# label for display/prompting user the encrypted string
encrypt_str_lab = Label(
                    root,
                    text="Encrypted String",
                    foreground="white",
                    background="#3e3e3e",
                    bd="6",
                    relief="solid"
)

# label for display/prompting user the dencrypted string
decrypt_str_lab = Label(
                    root,
                    text="Decrypted String ",
                    foreground="white",
                    background="#3e3e3e",
                    bd="8",
                    relief="solid"
)

# Need an entry field box for user string to encrypt
e1 = Entry(
            root,
            foreground="white",
            background="#3e3e3e",
            bd="6",
            relief="solid"
           )

# Need an entry field box for decrypting string
e2 = Entry(root)

# Need an entry field for DISPLAYING decrypted string ONLY
e3 = Entry(root)

# Need a button for encrypting text [button 1]
encrypt_str_bt = Button(
                    root,
                    text="Encrypt"
)

# Need a button for decrypting text [button 2]
decrypt_str_bt = Button(
                    root,
                    text="Decrypt"
)


# pushing onto the screen and 'positioning'
Intro_title.grid(row=0)
Intro_desc.grid(row=1)
# choose_str_frame.grid(row=2, column=0)
choose_str.grid(row=2, column=0)
encrypt_str_lab.grid(row=2, column=1)
decrypt_str_lab.grid(row=2, column=2)
# Entry Fields
e1.grid(row=3, column=0)
e2.grid(row=3, column=1)
e3.grid(row=3, column=3)
# buttons
encrypt_str_bt.grid(row=4, column=0)
decrypt_str_bt.grid(row=4, column=1)

root.mainloop()