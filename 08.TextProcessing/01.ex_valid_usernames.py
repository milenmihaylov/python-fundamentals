for username in input().split(', '):
    username_valid = False
    if 3 <= len(username) <= 16:
        for ch in username:
            if ch.isalnum() or ch == '-' or ch == '_':
                username_valid = True
            else:
                username_valid = False
                break
    if username_valid:
        print(username)
