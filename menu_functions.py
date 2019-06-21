import d20pfsrd_classes
import os
import sys
import time

#-------- File handler for dynamic menu -------#
fh1 = d20pfsrd_classes.File_Handler()
menu_items = fh1.Open_File('menu.json')

#-------------- Startup Message ---------------#
def startup():
    os.system('clear')
    print('''

        # # # # # # # # # # #
        #  Pick some loot!  #
        # # # # # # # # # # #
    ''')
    time.sleep(3)
    os.system('clear')

#------------------- Main Menu ---------------#
def main_menu():
    os.system('clear')
    menu_keys = list(menu_items.keys())
    global choice

    print('****************** MAIN MENU ******************\n')
    for i in range(len(menu_items.keys())):
        print(str(i+1) + ') ' + menu_keys[i])

    choice = input('\nEnter your selection here: ')
    print(choice)
    time.sleep(3)
    main_menu()
