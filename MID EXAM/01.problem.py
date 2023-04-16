from math import ceil

budget = float(input())
students = int(input())
price_flour_pckg = float(input())
price_single_egg = float(input())
price_apron = float(input())

costs = 0
costs += 10 * price_single_egg * students
costs += price_apron * ceil(students * 1.2)
costs += price_flour_pckg * students
free_flour_pckgs = students // 5
costs -= free_flour_pckgs * price_flour_pckg

if budget >= costs:
    print(f"Items purchased for {costs:.2f}$.")
else:
    print(f"{abs(budget-costs):.2f}$ more needed.")

