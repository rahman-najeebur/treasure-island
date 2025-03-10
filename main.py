from ascii_art import art

# display Ascii art.
print(art)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
move = input("Type 'left' or 'right'\n").lower()

if move == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    move = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if move == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        move = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if move == "yellow":
            print("You won!!")
        elif move == "red":
            print("Burned by fire. Game Over")
        elif move == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Wrong choice. Game Over")
    else:
        print("You get attacked by an angry trout. Game Over.")
elif move == "right":
    print("You Fall into a hole. Game Over!!")
else:
    print("Wrong move. Game Over.")
