import random

rand_list = [random.randint(0,20) for _ in range(10)]

list_comprehension_below_10 = [num for num in rand_list if num < 10]

filtered_list_below_10 = list(filter(lambda x: x < 10, rand_list))

print(list_comprehension_below_10)
print(filtered_list_below_10)