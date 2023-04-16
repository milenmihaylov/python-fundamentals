def loading_bar(percent):
    bar = '[' + '%' * int(percent * 0.1) + '.' * int(10 - percent * 0.1) + ']'
    if percent < 100:
        print(f"{percent}% {bar}")
        print("Still loading...")
    elif percent == 100:
        print(f"{percent}% Complete!")
        print(f"{bar}")


loading_bar(int(input()))
