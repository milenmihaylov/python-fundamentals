# def repeat_string(string, counter):
#     return string * counter
#
#
# print(repeat_string(input(), int(input())))


x = lambda string, counter: string * counter
print(x(string=input(), counter=int(input())))
