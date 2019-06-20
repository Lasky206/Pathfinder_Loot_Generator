import d20pfsrd_classes
import random

# d21 = d20pfsrd_classes.d20pfsrd(6,'https://www.d20pfsrd.com/magic-items/potions')
# d22 = d20pfsrd_classes.d20pfsrd(4,'https://www.d20pfsrd.com/magic-items/rings')
# d23 = d20pfsrd_classes.d20pfsrd(5,'https://www.d20pfsrd.com/magic-items/staves')
# wr1 = d20pfsrd_classes.scribe()

fh1 = d20pfsrd_classes.File_Handler()
menu_items = fh1.Open_File('menu.json')['Potions']

#----------- Create Example -------------------#
# rings = d22.list_generator(4,0,3)
# wr1.write_json(rings,'rings.json')
#----------- Append Example -------------------#
# wr1.append_json('rings.json',[{'fake':'list'},{'fake2':'list2'}])

print(menu_items)
