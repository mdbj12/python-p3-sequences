#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = []
    if length > 0:
        my_list.append(0)
        if length > 1:
            my_list.append(1)
            if length > 2:
                for i in range(2, length):
                    my_list.append(my_list[i - 1] + my_list[i - 2])

    print(my_list)