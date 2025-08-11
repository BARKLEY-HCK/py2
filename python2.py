my_list = []
my_list.extend([10, 20, 30, 40])
my_list.insert(1,15)
my_list.extend([50, 70])
my_list.remove(my_list[6])
my_list = sorted(my_list)
index_30 = my_list.index(30)
print(index_30)
print(my_list)

