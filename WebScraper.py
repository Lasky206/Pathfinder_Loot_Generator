import d20pfsrd_classes

d21 = d20pfsrd_classes.d20pfsrd(6,'https://www.d20pfsrd.com/magic-items/potions')
d22 = d20pfsrd_classes.d20pfsrd(4,'https://www.d20pfsrd.com/magic-items/rings')
d23 = d20pfsrd_classes.d20pfsrd(5,'https://www.d20pfsrd.com/magic-items/staves')

# print(d22.list_generator(4,0,4))
list1 = d22.list_generator(4,0,4)[0]
print(list1['Ring'])

print(d23.list_generator(3,0,3))
