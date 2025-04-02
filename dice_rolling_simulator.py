# import random

# def dice_rolling():
#         dice_drawing = {
#         1: (
#             "-----",
#             "|   |",
#             "| o |",
#             "|   |",
#             "-----",
#         ),
#         2: (
#             "-----",
#             "|o  |",
#             "|   |",
#             "|  o|",
#             "-----",
#         ),
#         3: (
#             "-----",
#             "|o  |",
#             "| o |",
#             "|  o|",
#             "-----",
#         ),
#         4: (
#             "-----",
#             "|o o|",
#             "|   |",
#             "|o o|",
#             "-----",
#         ),
#         5: (
#             "-----",
#             "|o o|",
#             "| o |",
#             "|o o|",
#             "-----",
#         ),
#         6: (
#             "-----",
#             "|o o|",
#             "|o o|",
#             "|o o|",
#             "-----",
#         ),

#     }
        
#         roll_dice = input("Roll the dice(Yes/No): ")
#         while roll_dice.lower()== "Yes".lower():
#             dice1 = random.randint(1,6)
#             dice2 = random.randint(1,6)

#             print("The dice rolled: {} and {}".format(dice1,dice2))
            
#             print("\n".join(dice_drawing[dice1]))
#             print("\n".join(dice_drawing[dice2]))
            
#             roll_dice = input("Roll the dice(Yes/No): ")

# dice_rolling()

import random

def roll_dice():
    dice_desigin ={
                1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
        
    roll= input("Do you want dice roll(yes/no): ")
    while roll.lower() == "yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("Your dice is: {} and {}".format(dice1,dice2))
        
        print("\n".join(dice_desigin[dice1]))
        print("\n".join(dice_desigin[dice2]))
        
        roll = input("Do you want dice roll(yes/no): ")
        
roll_dice()