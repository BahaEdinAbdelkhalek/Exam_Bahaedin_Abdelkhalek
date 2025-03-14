def somme(L):
    s = 0
    for e in L:
        s += e
    return s


my_list = [1, 5, 7]
if my_list:
    print("la somme est:", sum(my_list))
    print("le max est :", max(my_list))
    print("le min est : ", min(my_list))
else:
    print("la liste est vide")
