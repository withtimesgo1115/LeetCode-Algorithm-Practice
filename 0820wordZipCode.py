"""
LeetCode 820. 单词的压缩编码 (Short Encoding of Words)

题目描述：
    给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
    例如，假设单词列表为 ["time", "me", "bell"]，我们可以将其编码为字符串
    "time#bell#"，索引列表为 [0, 2, 5]。
    要求找到成功编码给定单词列表所需的最短长度字符串 S。

示例 1：
    输入：words = ["time", "me", "bell"]
    输出：10
    解释：S = "time#bell#"，indexes = [0, 2, 5]
          "time" 从索引 0 开始，"me" 从索引 2 开始（"time" 的后缀），
          "bell" 从索引 5 开始。

示例 2：
    输入：words = ["t"]
    输出：2
    解释：S = "t#"，indexes = [0]

约束条件：
    - 1 <= words.length <= 2000
    - 1 <= words[i].length <= 7
    - words[i] 仅由小写字母组成

解题思路：
    如果一个单词是另一个单词的后缀，那么较短的单词可以被省略（因为它已经
    包含在较长单词的编码中）。使用集合存储所有单词，对于每个单词，将其所有
    后缀从集合中移除。最终集合中剩余的单词就是不能被其他单词包含的单词，
    计算它们的总长度加上 '#' 分隔符的长度即可。
"""


def minimum_length_encoding(words):
    myset = set(words)
    for item in list(myset):
        for i in range(1, len(item)):
            substr = item[i:]
            if substr in myset:
                myset.discard(substr)
    res = 0
    for item in myset:
        res += len(item) + 1
    return res
