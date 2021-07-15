'''
Write a Python function named select_odds to select the odd items of a list.
Note: function should result a list with result.
'''


def select_odds(a):
    # print(a)
    odd_list = []
    for value in a:
        # print(value)
        if (value % 2):
            print(value)
            odd_list.append(value)
        else:
            print("nothing to add")
    return odd_list


result = select_odds([1, 2, 3, 4, 5, 6])
print(result)
