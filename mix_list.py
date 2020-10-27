#!/usr/bin/env python3

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#             0      1    2       3            4        5

# When I ssh into IP addresses 10.0.0.1 or 10.20.30.1 I am unable to ping ports 5060, 80, or 55.

# Concat method
print("When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4] + " I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]) + ".")

# f-string method
print(f"When I {new_list[5]} into IP addresses {new_list[3]} or {new_list[4]} I am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")
