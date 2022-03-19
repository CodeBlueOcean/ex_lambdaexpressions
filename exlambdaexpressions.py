#Square
my_list = [5,4,3]

new_list = list(map(lambda num: num**2, my_list))
print(new_list)

#List Sorting (sort by the second item)
a = [(0,2), (4,3), (10, -1), (9,9)]
a.sort(key=lambda x: x[1])
print(a)


