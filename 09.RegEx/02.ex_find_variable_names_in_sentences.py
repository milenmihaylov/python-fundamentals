import re

pattern = r'\b\_(?P<variable_name>[A-Za-z0-9]+)\b'
print(','.join([var_name.group('variable_name') for var_name in re.finditer(pattern, input())]))
