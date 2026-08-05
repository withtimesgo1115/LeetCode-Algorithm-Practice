"""
查找字符串中出现次数最多的字符 (Find Most Frequent Character)

题目描述：
    给定一个字符串，找出其中出现次数最多的字符，
    并返回该字符及其出现次数。

示例：
    输入："hello world"
    输出：('l', 3)
    解释：字符 'l' 出现了 3 次，是出现次数最多的字符。

    输入："aabbbcc"
    输出：('b', 3)
    解释：字符 'b' 出现了 3 次，是出现次数最多的字符。

    输入："abcabc"
    输出：('a', 2)（或 'b' 或 'c'，出现次数相同取其一）
    解释：三个字符各出现 2 次，返回其中一个。

实现方式：
    使用双重循环统计每个字符的出现次数，将结果存入字典，
    然后遍历字典找出出现次数最多的字符。

    时间复杂度：O(n^2)，其中 n 为字符串长度，
    因为对每个字符都需要遍历整个字符串进行计数。
    空间复杂度：O(k)，其中 k 为不同字符的数量（字典的大小）。

    更优解法：使用 collections.Counter 可以在 O(n) 时间内完成统计。
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
