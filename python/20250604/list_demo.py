# pylint: disable=missing-module-docstring

# pylint : skip-file

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

my_list.append(6)
print(my_list)
# my_list.append(6,7) will raise TypeError: append() takes exactly one argument (2 given)
my_list.append([6, 7, 8])
print(my_list)

element = my_list.pop()
print(element)
print(my_list.pop(-1))
print(my_list)

print(element.clear())

another_list = my_list[6:-1]
print(my_list)
print("another list: ", another_list)

another_list = [i * 2 for i in another_list]
print("another list: ", another_list)
print("my_list: ", my_list)
