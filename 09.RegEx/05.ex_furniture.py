import re

pattern = r"(>>)(?P<furniture>[A-Za-z]+)(<<)(?P<price>[0-9]+[.]{0,1}[0-9]*)(!)(?P<quantity>[0-9]+)"
furniture_list = []
total_cost = 0
text = input()
print(f"Bought furniture:")
while not text == "Purchase":
    furniture_list.append(text)
    text = input()

valid_furniture = re.finditer(pattern, ' '.join(furniture_list))
for furniture in valid_furniture:
    current_furniture = furniture.groupdict()
    total_cost += float(current_furniture['price']) * int(current_furniture['quantity'])
    print(f"{current_furniture['furniture']}")

print(f"Total money spend: {total_cost:.2f}")
