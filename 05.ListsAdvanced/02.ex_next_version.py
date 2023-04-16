version = [int(x) for x in input().split('.')]

for index in range(-1, -len(version) - 1, -1):
    if version[index] == 9:
        version[index] = 0
    else:
        version[index] += 1
        break

new_version = [str(x) for x in version]
print('.'.join(new_version))

# не работи:
# newest_version = [+=1 if version[index] != 9 else 0 for index in range(-1, -len(version) - 1, -1)]
