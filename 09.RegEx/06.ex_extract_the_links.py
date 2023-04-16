import re

pattern = r"(www).(?P<domain_name>[A-Za-z0-9-]+)(?P<domain_extension>(\.[a-z]+)+)"
links = []
text = input()
while text:
    links.append(text)
    text = input()

valid_links = re.finditer(pattern, ' '.join(links))
for link in valid_links:
    current_link = link.groupdict()
    print(f"www.{current_link['domain_name']}{current_link['domain_extension']}")
