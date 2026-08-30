'''
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

你必须编写一个时间复杂度为 O(log(m * n)) 的解决方案。

 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 获取矩阵的行数和列数
        m = len(matrix)
        n = len(matrix[0])
        # 使用二分查找法，将二维矩阵看作一维数组进行查找
        left = 0
        right = m * n - 1
        # 当左指针小于等于右指针时，继续查找
        while left <= right:
            # 计算中间位置的索引
            mid = left + (right - left) // 2
            # 将一维索引转换为二维索引，获取中间位置的元素
            x = matrix[mid // n][mid % n]
            # 如果中间位置的元素等于目标值，返回 True
            if x == target: return True
            # 如果中间位置的元素大于目标值，说明目标值在左半部分，更新右指针为 mid - 1
            if x > target:
                right = mid - 1
            # 否则，说明目标值在右半部分，更新左指针为 mid + 1
            else:
                left = mid + 1
        # 如果循环结束仍未找到目标值，返回 False
        return False



        