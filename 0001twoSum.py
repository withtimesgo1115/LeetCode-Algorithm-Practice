'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        if len(nums) == 0: return []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mymap:
                # 如果diff在mymap中，说明之前已经有一个数可以和当前的nums[i]相加等于target，直接返回当前的索引和之前存储的索引
                return [i, mymap[diff]]
            # 将当前的数和它的索引存入mymap中，方便后续查找
            mymap[nums[i]] = i
        return []
            