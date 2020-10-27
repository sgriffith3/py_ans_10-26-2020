#Python Challenge Lab # 1


#Take these 3 existing lists:

dogs = []
fish = []

pets = [{"type": "dog", "name": "mudge", "age": 4}, 
        {"type": "fish", "name": "dorothy", "age": "3 days"},
        {"type": "dog", "name": "bingo", "age": 12},
        {"type": "fish", "name": "nemo", "age": 2},
        {"type": "cat", "name": "fluffy", "age": 1}
        ]
		
#Use a for loop to sort each pet dictionary from the 
#list of pets into the dogs or fish list.

for item in pets:
    print(item)
    print(item["type"])
    if item["type"] == "dog":
        dogs.append(item['name'])
        print(f"{item['name']} is my pet dog")
    elif item["type"] == "fish":
        fish.append(item['name'])
        print(f"{item['name']} is my pet fish")
    else:
        print(f"{item['name']} is not my pet")


print(dogs)
print(fish)
#*Hint: if your iterator is "item" you will need to use item["type"] to
#       determine what type of animal it is.

#If it is not a dog or a fish, print "Not my pet"
