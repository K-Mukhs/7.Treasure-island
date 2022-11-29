# Welcome to Treasure Island.
# Your mission is to find the treasure.
# You're at a cross road. Where do you want to go? Type "left" or "right" 
# Right or anything else - You fell into a hole. Game over!
# Left - You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.
# Swim or anything else - You get attacked by an angry trout. Game over!
# Wait - You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?  
# Yellow - You found the treasure! You Win!
# Red  - It's a room full of fire. Game over!
# Blue - You enter a room of beasts. Game over!
# Anything else  - You chose a door that doesn't exist. Game over!



# from art import logo
# print(logo)
## Here it imports and prints the same logo as it is printing below with the print statement:

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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


#If we use you’re in the string which of course starts with ‘ and ends same way and we use also “ ” symbols in the string too then we can get it to ignore a symbol ’ in you’re as a string ending symbol by using the backslash like this you\’re. So this way it basically escapes the string and it will see it as text and now we have a complete string, and this is just going to be interpreted as text because we told it to with the backslash. See the following example:

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

# The .lower() is to change all the letters to the lower case for the program no matter how we’ve typed them, e.g Left, LEFT, left and so on.

if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")