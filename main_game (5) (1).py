import colorama
import main_character as mc
import layer_1
from time import *
import threading


def start_timer():
    global my_timer
    global pause

    pause = True
    my_timer = 25
    while my_timer > 0:
        if not pause:
            my_timer = my_timer - 1
        sleep(1)
    print("Done")

colorama.init()

print(colorama.Fore.MAGENTA
      , "\t \t \t Get Ready To Play Sweetest Game Of Your Life")

quit = False

while not quit:
    player = mc.main_character()  # assigning a function obj to a variable

    input('Press enter to continue...')
    player.name = input("First, what is your name?")
    cakes = 2  # setting initial value for cakes
    tip = 0  # setting initial value for tip
    level = 1  # setting initial value for level
    timer_thread = threading.Thread(target=start_timer)  # initializing thread and assigning thread variable timer _thread and
    # target being our function start_timer
    timer_thread.start() # starting the timer
    while my_timer > 0:
        cnt = cakes
        while cnt > 0:
            print(colorama.Fore.MAGENTA, "\n\n\nMake " + str(cnt) + " cakes before time runs out, you have "
                  + str(my_timer) + " seconds\n")
            input("Press Any Key To Continue")
            pause = False # telling the time to continue
            tip = layer_1.start(player, tip) * (level % 3 + 1)  # calling the function from layer.py to ask for user input
            cnt -= 1
            if my_timer <= 0:  # break out of the function
                break
        if my_timer <= 0:
            break
        pause = True  # telling the time to stop or(telling thread top stop counting or to pause it )
        level += 1
        print(level)
        print(colorama.Fore.RED, "\n\n Level up!!\nLevel" + str(level))
        input("Press Any Key To Continue")
        print("Strating...")
        cakes += 1
        my_timer = (25 * int(cakes / 2))  # timer is set to ten so as the cake amount increases the time is multiplied by the cake
        print("\n\n" + str(my_timer))
    player.mm_coin += tip
    print("\n\n\n\nTime out/n/n")
    print("Your total coins is " + str(player.mm_coin) + player.name + "\n")
    ans = input("Play Again?(y/n)")
    if ans == 'y' or ans == 'Y':
        quit = False
    else:
        quit = True

print("\n\nThanks for playing", player.name, "!!!")






