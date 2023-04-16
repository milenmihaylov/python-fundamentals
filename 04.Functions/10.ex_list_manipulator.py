def happy_milen():
    string = input().split()
    num_list = [int(x) for x in string]
    manipulation_command = input().split()
    command = manipulation_command[0]
    added_num = 0
    # temp_list = num_list
    # max_even = 0
    # max_odd = 0
    # min_even = 0
    # min_odd = 0

    while not command == 'end':
        temp_list = [x for x in num_list]
        if command == 'exchange':
            index = int(manipulation_command[1])
            if 0 <= index < len(num_list):
                num_list = num_list[index + 1:] + num_list[:index + 1]
            else:
                print("Invalid index")

        elif command == 'max':
            if manipulation_command[1] == 'even':
                while temp_list:
                    if max(temp_list) % 2 == 0:
                        for i in range(len(num_list) - 1, -1, -1):
                            if num_list[i] == max(temp_list):
                                max_even = i
                                print(max_even)
                                temp_list = []
                                break
                    else:
                        temp_list.remove(max(temp_list))

            elif manipulation_command[1] == 'odd':
                while temp_list:
                    if not max(temp_list) % 2 == 0:
                        for i in range(len(num_list) - 1, -1, -1):
                            if num_list[i] == max(temp_list):
                                max_odd = i
                                print(max_odd)
                                temp_list = []
                                break
                    else:
                        temp_list.remove(max(temp_list))
                        if len(temp_list) == 0:
                            print("No matches")
                            break

        elif command == 'min':
            if manipulation_command[1] == 'even':
                while temp_list:
                    if min(temp_list) % 2 == 0:
                        for i in range(len(num_list) - 1, -1, -1):
                            if num_list[i] == min(temp_list):
                                min_even = i
                                print(min_even)
                                temp_list = []
                                break

                    else:
                        temp_list.remove(min(temp_list))
                        if len(temp_list) == 0:
                            print("No matches")
                            break

            elif manipulation_command[1] == 'odd':
                while temp_list:
                    if not min(temp_list) % 2 == 0:
                        for i in range(len(num_list) - 1, -1, -1):
                            if num_list[i] == min(temp_list):
                                min_odd = i
                                print(min_odd)
                                temp_list = []
                                break
                    else:
                        temp_list.remove(min(temp_list))
                        if len(temp_list) == 0:
                            print("No matches")
                            break

        elif command == 'first':
            temp_list = []
            index = -1
            count = int(manipulation_command[1])
            number = manipulation_command[2]
            if count > len(num_list):
                print("Invalid count")
            else:

                if number == 'even':
                    for i in num_list:
                        index += 1
                        if not i % 2 == 0:
                            temp_list.append(num_list[index])
                            added_num += 1
                            if added_num == count:
                                break
                    print(temp_list)

                elif number == 'odd':
                    for i in num_list:
                        index += 1
                        if not i % 2 == 0:
                            temp_list.append(num_list[index])
                            added_num += 1
                            if added_num == count:
                                break
                    print(temp_list)

        elif command == 'last':
            temp_list = []
            count = int(manipulation_command[1])
            number = manipulation_command[2]
            if count > len(num_list):
                print("Invalid count")
            else:

                if number == 'even':
                    for el in num_list:
                        if el % 2 == 0:
                            temp_list.append(el)
                            temp_list = temp_list[len(temp_list) - count:]
                    print(temp_list)
                elif number == 'odd':
                    for el in num_list:
                        if not el % 2 == 0:
                            temp_list.append(el)
                    temp_list = temp_list[len(temp_list) - count:]
                    print(temp_list)

        manipulation_command = input().split()
        command = manipulation_command[0]

    print(num_list)


happy_milen()
