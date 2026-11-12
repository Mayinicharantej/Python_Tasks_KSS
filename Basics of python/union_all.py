list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
set1 = set(list1)
set2 = set(list2)

common = set1 & set2
only_first = set1 - set2
all_unique = set1 | set2

print(list(common))
print(list(only_first))
print(list(all_unique))