def urgent(shipping_list: list, product: str):
    if product not in shipping_list:
        shipping_list.insert(0, product)


def unnecessary(shopping_list: list, product: str):
    if product in shopping_list:
        shopping_list.remove(product)


def correct(shopping_list: list, old_product: str, new_product: str):
    if old_product in shopping_list:
        index = shopping_list.index(old_product)
        shopping_list.remove(old_product)
        shopping_list.insert(index, new_product)


def rearrange(shopping_list: list, product: str):
    if product in shopping_list:
        shopping_list.remove(product)
        shopping_list.append(product)


groceries = [x for x in input().split('!')]

commands = input()
while not commands == "Go Shopping!":
    commands_list = commands.split()
    command = commands_list[0]
    if command == 'Urgent':
        item = commands_list[1]
        urgent(groceries, item)
    elif command == 'Unnecessary':
        item = commands_list[1]
        unnecessary(groceries, item)
    elif command == 'Correct':
        old_item = commands_list[1]
        new_item = commands_list[2]
        correct(groceries, old_item, new_item)
    elif command == 'Rearrange':
        item = commands_list[1]
        rearrange(groceries, item)

    commands = input()


print(', '.join(groceries))
