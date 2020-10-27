#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

# used to remove warnings from packages
import warnings

import paramiko

import csv


# filter out any warnings with the word Paramiko
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    #credz = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "zoidberg", "ip": "10.10.2.5"},\
    #        {"un": "fry", "ip": "10.10.2.4"}]

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa") 
 
    with open("hosts.csv", "r") as hostfile:
        host_data = csv.reader(hostfile)
        for host in host_data:
            ip = host[0]
            un = host[1]
            ## create a session object
            sshsession = paramiko.SSHClient()

            ## add host key policy
            sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ## display our connections
            print("Connecting to... " + un + "@" + ip)

            ## make a connection
            sshsession.connect(hostname=ip, username=un, pkey=mykey)

            ## touch the file goodnews.everyone in each user's home directory
            sshsession.exec_command("touch /home/" + un + "/goodnews.everyone")

            ## list the contents of each home directory
            sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + un)

            ## display output
            print(sessout.read().decode('utf-8'))

            ## close/cleanup SSH connection
            sshsession.close()

    print("Thanks for looping with Alta3!")

main()

