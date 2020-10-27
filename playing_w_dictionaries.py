# the_dictionary = {"first name": "Sam"}

pets = {"dog": "mudge"}

print(pets)
print(type(pets))

pets.update({"age": 5})

print(pets)

pets.update({"age": 6})
print(pets)

fish = {"fish": "dorothy", "age": "3 days"}

print(fish["fish"])
print(fish["age"])

my_pets = [pets, fish]
print(my_pets)
print(my_pets[0])
print(my_pets[0]["dog"])
print(my_pets[0]["age"])
print(my_pets[0].get("platypus"))

fish["type"] = "goldfish"
print(fish)

fish["food"] = None
print(fish)

fish.update({"living": "" })
print(fish)

print(fish.keys())
print(fish.values())

