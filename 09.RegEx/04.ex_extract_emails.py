import re

text = input()
pattern = r"(^|(?<=\s))(?P<user>[A-Za-z0-9]{1}[A-Za-z0-9._-]*[A-Za-z0-9]{1})(@)(?P<host>[A-Za-z]{1}[A-Za-z-]*[A-Za-z]{1}[.]{1}[A-Za-z]{1}[A-Za-z-]*[A-Za-z]{1}(\.[A-Za-z]{1}[A-Za-z-]*[A-Za-z]{1})*)($|(?=\s|,|.))"

emails = re.finditer(pattern, text)
for email in emails:
    current_email = email.groupdict()
    print(f"{current_email['user']}@{current_email['host']}")
