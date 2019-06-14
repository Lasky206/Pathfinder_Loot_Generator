import d20pfsrd_classes

d21 = d20pfsrd_classes.d20pfsrd(6,'https://www.d20pfsrd.com/magic-items/potions')
d22 = d20pfsrd_classes.d20pfsrd(4,'https://www.d20pfsrd.com/magic-items/rings')
d23 = d20pfsrd_classes.d20pfsrd(5,'https://www.d20pfsrd.com/magic-items/staves')
wr1 = d20pfsrd_classes.scribe()

# print(d22.list_generator(4,0,4))
# list1 = d22.list_generator(4,0,4)[0]
# print(list1['Ring'])

rings = d22.list_generator(4,0,3)
# print(list)

wr1.write_json(rings,'rings.json')

print(wr1.printer('rings.json'))
