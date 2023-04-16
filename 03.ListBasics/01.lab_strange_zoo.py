tail = input()
body = input()
head = input()

meerkat = [tail, body, head]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]  # swapping
# temp = meerkat[0]
# meerkat[0] = meerkat[2]
# meerkat[2] = temp
print(meerkat)
