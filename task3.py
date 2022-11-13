def get_unique_list_numbers() -> list[int]:
    ...  # TODO написать функцию для получения списка уникальных целых чисел
    import random
    checklist = list()
    while len(set(checklist)) < 15:
        checklist.append(random.randint(-10, 10))
    return list(set(checklist))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
