import os
from task3 import with_logfile

with open("recipes.txt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        name = line.strip()
        cook_book[name] = []
        ingredients = int(file.readline().strip())
        for ing in range(ingredients):
            new_dict = {}
            split_line = str(file.readline().strip()).split(" | ")
            new_dict.update({"ingredient_name": split_line[0]})
            new_dict.update({"quantity": split_line[1]})
            new_dict.update({"measure": split_line[2]})
            cook_book[name].append(new_dict)
        file.readline()

file_name = 'log.txt'

@with_logfile(os.path.abspath(file_name))
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                new_dict = {}
                key_word = ingredient["ingredient_name"]
                new_dict["measure"] = ingredient["measure"]
                new_dict["quantity"] = int(ingredient["quantity"]) * person_count
                if key_word in shop_list.keys():
                    shop_list[key_word]["quantity"] += int(ingredient["quantity"]) * person_count
                else:
                    shop_list[key_word] = new_dict
    return shop_list

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


