'''
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

返回一个表示每个字符串片段的长度的列表。

 

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
示例 2：

输入：s = "eccbbbbdec"
输出：[10]
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last字典存储每个字符最后一次出现的索引位置
        last = {c: i for i, c in enumerate(s)}
        # res列表存储每个片段的长度
        res = []
        # start和end分别表示当前片段的起始和结束位置
        start = end = 0
        # 遍历字符串s，更新end为当前字符最后一次出现的位置
        # 如果i等于end，说明当前片段结束，将片段长度加入res，并更新start为下一个片段的起始位置
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

        