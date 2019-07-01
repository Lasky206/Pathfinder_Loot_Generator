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

    print('****************** MAIN MENU ******************\n')
    for i in range(len(menu_items.keys())):
        print(str(i+1) + ') ' + menu_keys[i])
    print('\nQ: Quit')

    choice = input('\nEnter your selection here: ')

    if choice == 'Q' or choice == 'q':
        sys.exit(0)
    elif '0' <= choice <= '9':
        if int(choice)-1 in list(range(len(menu_items.keys()))):
            # print(menu_items[str(menu_keys[int(choice) - 1])]) #<--------------------------------------------- REMOVE LINE
            sub_dict = menu_items[str(menu_keys[int(choice) - 1])]
            name = menu_keys[int(choice)-1]
            time.sleep(2)
            sub_menu(sub_dict, name)
    else:
        print("Error4!")
        time.sleep(1)

    main_menu()

#------------------- Sub Menu ----------------#
def sub_menu(sub_dict, name):
    os.system('clear')
    menu_keys = list(sub_dict.keys())

    print('****************** ' + name + ' ******************\n')
    for i in range(len(sub_dict.keys())):
        print(str(i+1) + ') ' + menu_keys[i])
    print('\nQ: Back / Quit')

    choice = input('\nEnter your selection here: ')

    if choice == 'Q' or choice == 'q':
        main_menu()
    elif '0' <= choice <= '9':
        if int(choice)-1 in list(range(len(sub_dict.keys()))):
            rz1 = d20pfsrd_classes.randomizer()
            loot_list_path = os.path.join(sys.path[0], 'datacards', sub_dict[str(menu_keys[int(choice) - 1])])
            loot_list = fh1.Open_File(loot_list_path)
            rz1.gen_random_loot_d(3, loot_list)
            # print(sub_dict[str(menu_keys[int(choice) - 1])])
            time.sleep(3)
    else:
        print("Error1!")
        time.sleep(1)

    sub_menu(sub_dict, name)
