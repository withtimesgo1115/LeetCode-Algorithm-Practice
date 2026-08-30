'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
 

提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums 中的每个值都 独一无二
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104
'''

class Solution:
    '''
    对于旋转数组 nums = [4,5,6,7,0,1,2]
    首先根据 nums[0] 与 target 的关系判断 target 是在左段还是右段。

    例如 target = 5, 目标值在左半段，因此在 [4, 5, 6, 7, inf, inf, inf] 这个有序数组里找就行了；
    例如 target = 1, 目标值在右半段，因此在 [-inf, -inf, -inf, -inf, 0, 1, 2] 这个有序数组里找就行了。
    如此，我们又双叒叕将「旋转数组中找目标值」 转化成了 「有序数组中找目标值」
    '''
    def search(self, nums: List[int], target: int) -> int:
        low = 0 # 定义左指针，表示当前查找的最左边界
        high = len(nums) - 1 # 定义右指针，表示当前查找的最右边界
        while low <= high: # 当左指针小于等于右指针时，继续查找
            mid = low + (high - low) // 2 # 确定二分查找的索引
            if nums[mid] == target:
                return mid
            # 先根据 nums[0] 与 target 的关系判断目标值是在左半段还是右半段
            if target >= nums[0]:  # 如果在左半段
                if nums[mid] < nums[0]: # 如果 mid 在右半段
                    nums[mid] = float('inf') # 将 mid 位置的值设为正无穷，这样在二分查找时就会被排除掉
            else: # 如果在右半段
                if nums[mid] >= nums[0]: # 如果 mid 在左半段
                    nums[mid] = float('-inf') # 将 mid 位置的值设为负无穷，这样在二分查找时就会被排除掉
            if nums[mid] < target: # 如果 mid 位置的值小于目标值，说明目标值在右半部分，更新左指针为 mid + 1
                low = mid + 1
            else: # 否则，说明目标值在左半部分，更新右指针为 mid - 1
                high = mid - 1
        return -1 # 如果循环结束仍未找到目标值，返回 -1