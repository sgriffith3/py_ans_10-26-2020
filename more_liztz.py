hosts = ["172.16.2.1", 5555, "docker01"]
# index         0        1        2

print(hosts[0])
print(hosts[1])
print(hosts[2])

print("The ___ host is at IP ___ and is using port ____")

print("The " + hosts[2] + " host is at IP " + hosts[0] + " and is using port " + str(hosts[1]))

print(f"The {hosts[2]} host is at IP {hosts[0]} and is using port {hosts[1]}")


for item in hosts:
    print(item)


mathy = [5, 10, 13, 99, 202, 1, 4, 7, 34]

for num in mathy:
    print(f"{num} + 10 = {num + 10}")


