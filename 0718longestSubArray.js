/*
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
*/

/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number}
 */
var findLength = function(A, B) {
    let n = A.length;
    let m = B.length;
    let ans = 0;
    let dp = new Array();
    for(let i = 0; i < n + 1; i++){
        dp[i] = new Array();
        for(let j = 0; j < m + 1; j++){
            dp[i][j] = 0;
        }
    }
    for(let i = n - 1; i > -1; i--){
        for(let j = m - 1; j > -1; j--){
            dp[i][j] = A[i] == B[j] ? dp[i+1][j+1] + 1 : 0;
            ans = Math.max(ans, dp[i][j]);
        }
    }
    return ans;
};
