def mystery_function(lst):
    result = lst.copy()
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            result[i] = lst[i] ** 2
    return result

result_1 = mystery_function([1, 2, 3, 4, 5])
print(result_1)

result_2 = mystery_function([4, 1, 6, 2, 10])
print(result_2)
