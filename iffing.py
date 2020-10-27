# if (something is True):
#    do an action

name = "Sam"

if name:
    print(f"Your name is {name}")


x = 15

# x < 10 = False
if x < 10:
    print("X is less than 10")
else:
    print(x)
    print("We hit the else block")
    print("X is not less than 10, silly")

y = 2

if y == 25:
    print("You win!")
else:
    print("You lose :{")



scores = [52, 98, 65, 78, 84, 86, 30, 90]

for score in scores:
    if score >= 90:
        print("A", score)
    elif score >= 80:
        print("B", score)
    elif score >= 70:
        print("C", score)
    elif score >= 60:
        print("D", score)
    else: 
        print("You failed!", score)


cat = "yep"
name = "fluffy"

if cat == "yep" and name == "fluffy":
    print("Yes, you have a cat named fluffy")


if cat == "yep" or name == "poodle":
    print("You might have a cat, or a poodle")




