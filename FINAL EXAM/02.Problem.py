import re

pattern = r'(?P<employee>[A-Z][a-z]*\ [A-Z][a-z]*)\#+(?P<job>[A-Z][A-Za-z]*(\&[A-Z][A-Za-z]*){,2})\d{2}(?P<company>[' \
          r'A-Z][A-Za-z0-9]* (JSC|Ltd.))'

n = int(input())
for _ in range(n):
    text = input()
    valid_input = re.finditer(pattern, text)
    for val_in in valid_input:
        current_input = val_in.groupdict()
        if '&' in current_input['job']:
            current_input['job'] = current_input['job'].replace('&', ' ')
        print(f"{current_input['employee']} is {current_input['job']} at {current_input['company']}")
