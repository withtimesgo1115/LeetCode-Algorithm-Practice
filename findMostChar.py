"""
Find Most Frequent Character

Given a string, find the character that appears the most times
and return both the character and its count.
"""


def find_most_char(s):
    arr = list(s)
    obj = {}
    char = " "
    maxtimes = 0
    for i in range(len(arr)):
        num = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                num += 1
        if num > maxtimes:
            maxtimes = num
        obj[arr[i]] = num
    for key in obj:
        if obj[key] == maxtimes:
            char = key
            maxtimes = obj[key]
            print(f"{char} appears {maxtimes} times!")
    return char, maxtimes
