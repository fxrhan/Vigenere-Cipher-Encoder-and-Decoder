from tkinter import *  #import tkinter module

import random  #imports other necessary modules

import base64  #Vigenere cipher for encryption/decryption

root = Tk()  #creating root object

root.geometry("1200x4500")  #defining size of window

root.title("Encryption/Decryption with Vigenere Cipher")  #window title

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

#------------------------------------code by Farhan Ansari-------------------------------------------

labelInfo = Label(Tops, font=('Rockwell, Garamond', 50, 'bold'),
                    text="Encryption/Decryption with\n Vigenere Cipher",
                    fg="Black", bd=10, anchor='w')

labelInfo.grid(row=0, column=0)

#initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# labels for the messages
labelMessage = Label(f1, font=('Garamond, arial', 16, 'bold'),
                    text="MESSAGE", bd=16, anchor='w')

labelMessage.grid(row=1, column=0)

# Entry box for the message
textMessage = Entry(f1, font=('Garamond, arial', 16, 'bold'),
                    textvariable=Msg, bd=10, insertwidth=4,
                    bg='powder blue', justify=LEFT)  #####

textMessage.grid(row=1, column=1)

#labels for the key
labelKey = Label(f1, font=('Garamond, arial', 16, 'bold'),
                    text="CIPHER KEY (only integer)", bd=16, anchor='w')

labelKey.grid(row=2, column=0)

#Entry box for the key
textKey = Entry(f1, font=('Garamond, arial', 16, 'bold'),
                    textvariable=key, bd=10, insertwidth=4,
                    bg='powder blue', justify=LEFT)

textKey.grid(row=2, column=1)

#label for the mode
labelMode = Label(f1, font=('Garamond, arial', 16, 'bold'),
                    text="MODE (type e for encrypt or d for decrypt)",
                    bd=16, anchor='w')

labelMode.grid(row=3, column=0)

# Entry box for mode
textMode = Entry(f1, font=('Garamond, arial', 16, 'bold'),
                    textvariable=mode, bd=10, insertwidth=4,
                    bg='powder blue', justify=LEFT)

textMode.grid(row=3,column=1)

# Label for result
labelResult = Label(f1, font=('Garamond, arial', 16, 'bold'),
                    text="The Result", bd=16, anchor='w')

labelResult.grid(row=2, column=2)

#Entry box for result
textResult = Entry(f1, font=('Garamond, arial', 16, 'bold'),
                    textvariable=Result, bd=10, insertwidth=4,
                    bg='powder blue', justify=LEFT)

textResult.grid(row=2, column=3)

#-----------------------------------code by FARHAN ANSARI----------------------------------

# Vigenere cipher

# Function to encode
def encode(key,msg):
    enc = []

    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)

        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Function to decode
def decode(key,enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


# Function of result
def Results():
    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))


# Function to exit window
def qExit():
    root.destroy()

# Function to reset window
def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

#message button
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg='black',
                    font=('Garamond, arial', 16, 'bold'),
                    width=10, text="Show Message", bg="powder blue",
                    command=Results).grid(row=7,column=1)    

#reset button                    
btnReset = Button(f1, padx=16, pady=8, bd=16, fg='black',
                    font=('Garamond, arial', 16, 'bold'),
                    width=10, text="Reset", bg="green",
                    command=Reset).grid(row=7,column=2)

#Exit button
btnExit = Button(f1, padx=16, pady=8, bd=16, fg='black',
                    font=('Garamond, arial', 16, 'bold'),
                    width=10, text="Exit", bg="red",
                    command=qExit).grid(row=7,column=3)

#keeps window alive
root.mainloop()