import re

pattern_names = r'\b(?<=\%)(?P<name>[A-Z][a-z]+)(?=\%)'
pattern_products = r'(?<=\<)(?P<product>\w+)(?=\>)'
pattern_count = r'(?<=\|)(?P<count>\d+)(?=\|)'
pattern_price = r'(\d+[.\d+]*)(?=\$)\b'
total_income = 0
text = input()
while not text == "end of shift":
    valid_name = re.finditer(pattern_names, text)
    valid_product = re.finditer(pattern_products, text)
    valid_count = re.finditer(pattern_count, text)
    valid_price = re.finditer(pattern_price, text)
    for name in valid_name:
        for product in valid_product:
            for count in valid_count:
                for price in valid_price:
                    total_price = int(count.group()) * float(price.group())
                    print(f"{name.group()}: {product.group()} - {total_price:.2f}")
                    total_income += total_price

    text = input()

print(f"Total income: {total_income:.2f}")
