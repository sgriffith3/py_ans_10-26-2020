#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
ip = input("What IP / Machine do you wish to connect to?\n")
t = paramiko.Transport(ip, 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
user = input("What Username should I use?\n")
passwd = input("What's the super secret password?\n")
t.connect(username=user, password=passwd)

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

