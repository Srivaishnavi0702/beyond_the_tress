# Importing logo
from art import logo, forest, grassland, boat
from art import alligator, quicksand, hole, bear

print(logo)
print("Welcome to Beyond the Trees.")
print("Your mission is to find the wayout from Forest.")
print(forest)

# Choose a way
choice_1 = input("You are at crossing the Bushes.Where do you want to go?.\nType \"Left\" or \"Right\":").lower()
if choice_1 == "left":
    print("There is a three path way for goes to next path.")
    choice_2 = input("Type \'G\' for Grassland or Type \'M\' for Mudland or Type \'R\' for Rockland:").upper()
    if choice_2 == "G":
        print(grassland)
        print("You\'ve come to the lake.There is an island in the middle of the lake.")
        choice_3 = input("Type \"wait\" to wait for the boat or Type \"swim\" to swim across:").lower()
        if choice_3 == "wait":
            print(boat)
            print("You arrive at the island unharmed.")
            print("Hurrraayy!!! You have reach the Crop Field to finish the game and escape from the forest")
        else:
            print(alligator)
            print("You get attacked by the Angry Alligators in lake")
            print("GAME OVER!!!")
    elif choice_2 == "M":
        print(quicksand)
        print("You got stuck and fall into the Quicksand")
        print("GAME OVER!!!")
    else:
        print()
        print("You fell into the Hole")
        print("GAME OVER!!!")
else:
    print()
    print("You got wrong way.Lions and Bears eaten you")
    print("GAME OVER!!!")
