cars = ["toyota", "kia", "honda"]

print(cars)

cars.append("ford")
print(cars)

more_cars = ["chevy", "jeep", "ram"]

#combined = cars + more_cars

#print(combined)

cars.append(more_cars)

print(cars)

# ['toyota', 'kia', 'honda', 'ford', ['chevy', 'jeep', 'ram']]
#       0       1       2        3                4
#                                        0        1       2
print(cars[3])
print(cars[4][1])


pets = ["cat", "dog", "lizard"]

more_pets = ["hamster", "goat", "llama"]

pets.extend(more_pets)

print(pets)

pets[2] = "elephant"

print(pets)

pets.remove("goat")

print(pets)


