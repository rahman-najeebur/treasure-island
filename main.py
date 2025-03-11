from ascii_art import art

# display Ascii art.
print(art)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice1 = input("Type 'left' or 'right'\n").lower()

if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You won!!")
        elif choice3 == "red":
            print("Burned by fire. Game Over")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Wrong choice. Game Over")
    else:
        print("You get attacked by an angry trout. Game Over.")
elif choice1 == "right":
    print("You Fall into a hole. Game Over!!")
else:
    print("Wrong move. Game Over.")
