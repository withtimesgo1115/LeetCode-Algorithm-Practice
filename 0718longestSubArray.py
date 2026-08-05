"""
718. 最长重复子数组 (Maximum Length of Repeated Subarray)

给两个整数数组 nums1 和 nums2 ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1：
    输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
    输出：3
    解释：长度最长的公共子数组是 [3,2,1] 。

示例 2：
    输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
    输出：5

提示：
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 100
"""


def findLength(A, B):
    n = len(A)
    m = len(B)
    ans = 0
    # dp[i][j] 表示以 A[i] 和 B[j] 开头的最长公共子数组长度
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
            ans = max(ans, dp[i][j])
    return ans
