import random


def get_unique_list_numbers() -> list[int]:
    list_of_numbers = []
    while len(list_of_numbers) != 15:
        count = random.randint(-10, 10)
        if count not in list_of_numbers:
            list_of_numbers.append(count)
    return list_of_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
