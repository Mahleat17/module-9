import main_character
import random


def choicesInput(choices, prompt):
    temp = []
    print(prompt)
    for i in range(len(choices)):
        randNum = random.randint(0, 9)
        while randNum in temp:
            randNum = random.randint(0, 9)
        temp.append(randNum)
        print(str(temp[i]), ') ', choices[i])
    return temp


def start(player, tip):
    choicesArr = []  # used as temporary variable to store input
    s_choices = ["Circle", "Square", "Triangle", "Custom"]
    choiceArr = choicesInput(s_choices, "Enter the corresponding number to chose the Shape of the cake \n")
    # calls the function choicesInput to assign random
    # number to the choices
    ans = int(input("➤ "))
    while ans not in choiceArr: # this while loop condition that checks if the input is correct
        print('Invalid input, Enter Again! ')
        ans = int(input("➤ "))
    print(ans, '\n')
    for i in choicesArr:
        print(i, ' \n')

    f_choices = ["Chocolate", "Cheesecake", "Red velvet", "Coconut"]
    choiceArr = choicesInput(f_choices, "Enter the corresponding number to choose the Flavor of the cake\n")
    ans = int(input("➤ "))
    while ans not in choiceArr:
        print('Invalid input, Enter Again ')
        ans = int(input("➤ "))

    fr_choices = ["Perfect Buttercream", "Lemon Cream Cheese Frosting", "Browned Butter Frosting"]

    choiceArr = choicesInput(fr_choices, "Enter the corresponding number to choose the Frosting of the cake\n")
    ans = int(input("➤ "))
    while ans not in choiceArr:
        print('Invalid input, Enter Again ')
        ans = int(input("➤ "))

    t_choices = ["Mini chocolate candies", "Chocolate curls", "Spun-sugar flowers", "Cocoa dust"]

    choiceArr = choicesInput(t_choices, "Enter the corresponding number to choose the Topping of the cake\n")
    ans = int(input("➤ "))
    while ans not in choiceArr:
        print('Invalid input, Enter Again ')
        ans = int(input("➤ "))

    d_choices = ["Butter Cream", "Whipped Cream", "Royal Icing", "Cream Cheese Frosting", "Meringue"]

    choiceArr = choicesInput(d_choices, "Enter the corresponding number to choose the Decoration of the cake\n")
    ans = int(input("➤ "))
    while ans not in choiceArr:
        print('Invalid input, Enter Again ')
        ans = int(input("➤ "))

    acc_tip = input("Accept tip if: yes press Y/y , NO press N/n  ")
    if acc_tip == 'y' or acc_tip == 'Y':
        player.mm_coin += (5 + tip)
        return 0
    else:
        return 5 + tip
