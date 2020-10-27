#!/usr/bin/env python3
import shutil
import os

os.chdir("/home/student/")

shutil.copy("file01.txt", "/home/student/static/file01.txt")
print("File copied!")

answer = input("Would you like to copy more files? ")
print("You said", answer)
