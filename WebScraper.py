import d20pfsrd_classes

d21 = d20pfsrd_classes.d20pfsrd(6,'https://www.d20pfsrd.com/magic-items/potions')
method_list = d21.dict_convertion(d21.list_generator())

for i in range(len(method_list)):
    print(method_list[i])
