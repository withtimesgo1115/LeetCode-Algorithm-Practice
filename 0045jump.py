'''
给定一个长度为 n 的 0 索引整数数组 nums。初始位置在下标 0。

每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在索引 i 处，你可以跳转到任意 (i + j) 处：

0 <= j <= nums[i] 且
i + j < n
返回到达 n - 1 的最小跳跃次数。测试用例保证可以到达 n - 1。

 

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        # 贪心算法，border和max_position的区别是
        # border表示当前能跳跃到的位置的最远边界，max_position表示在border范围内能跳跃的最远位置
        border = 0 # 定义边界，表示当前跳跃的最远位置
        max_position = 0 # 定义最大位置，表示当前能跳跃的最远位置
        steps = 0 # 定义步数，表示跳跃的次数
        # 遍历数组，更新最大位置和边界，当到达边界时，增加步数
        for i in range(len(nums) - 1): # 遍历数组，最后一个位置不需要跳跃，因为最后一个位置是目标终点
            max_position = max(max_position, i+nums[i]) # 更新最大位置，表示当前能跳跃的最远位置
            # 当到达边界时，增加步数（表示跳跃一次），并更新边界为最大位置
            if i == border:
                border = max_position
                steps+=1
        # 返回步数，表示跳跃的次数
        return steps




        