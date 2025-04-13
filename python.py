print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print ("yout at a cross road .where do you want to go ?")
a=input (     " type \"left\"or\"right\"     ")
if a=="right":
    print("you fell into a hole .game over")
if a=="left":
    print("you/'ve come to a lake.there is an island ")
    b = input(" type \"wait\"to wait for a boat.type\"swim\"to swim across    ")
    if b== "swim":
        print("You get attacked by an angry trout. Game Over.")
    if b=="wait":
        print("You arrive at the island unharmed. There is a house with 3 doors")
        c= input("One red, one yellow and one blue. Which colour do you choose? ")
        if c=="red":
            print('Its a room full of fire. Game Over.')
        elif c=="yellow":
            print ("You found the treasure! You Win!")
        elif c=="blue":
            print("You enter a room of beasts. Game Over.")



