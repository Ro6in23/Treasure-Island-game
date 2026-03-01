print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure.")
direction = input("Where do you want to go? Left or Right: ").upper()
if direction == "RIGHT":
    print("You fell into a hole. Game Over!")
elif direction == "LEFT":
    swim = input("You've come to a lake, there is an island in the middle of the lake.Type 'swim' to swim across the lake or 'wait' to wait for a boat. Swim or Wait: ").upper()
    if swim == "SWIM":
        print("You were attacked by trout. Game Over!")
    elif swim == "WAIT":
        door = input("You have a 3 colored doors in front of you, which one will you choose? Red, Blue or Yellow: ").upper()
        if door == "BLUE":
            print("You were eaten by the beasts. Game Over!")
        elif door == "RED":
            print("You were burned by fire. Game Over!")
        elif door == "YELLOW":
            print("You WIN")
        else:
            print("Game Over!")

print("Thank you for playing the game")