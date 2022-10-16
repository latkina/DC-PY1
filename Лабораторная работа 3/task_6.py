list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

count = 0
index_max_number = 0

for index, number in enumerate(list_numbers):
    if number > count:
        count = number
        index_max_number = index
list_numbers[index_max_number], list_numbers[-1] = list_numbers[-1], list_numbers[index_max_number]
print(list_numbers)
