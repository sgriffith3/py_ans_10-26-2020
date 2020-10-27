

import csv


with open("hosts.csv", "r") as hostfile:
    host_data = csv.reader(hostfile)
    for host in host_data:
        print(host)
        ip = host[0]
        un = host[1]
        print(f"Connecting to ip {ip} using the username {un}")
