def list_sum(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

print(list_sum([1, 2, 3, 4]))