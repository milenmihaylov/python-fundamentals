def new_funck():
    products = ['123', 'sdas', 'asd21']

    result = "Items in the {self.name} catalogue: "
    for product in products:
        result += product + print()

    return f"{result}"

new_funck()