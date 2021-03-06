/*
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。


示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

*/

/*
我们使用一个二维数组 dp， dp[i][j] 表示 s1 前 i 个字符和 s2 前 j 个字符中最长公共子序列。我们逐行填充 dp 数组。

对于每一个 dp[i][j]，我们有 2 种选择：

字符 s1[i-1] 和 s2[j−1] 匹配，那么 dp[i][j] 会比两个字符串分别考虑到前 i−1 个字符 和 j−1 个字符的公共子序列长度多 1 。
所以 dp[i][j] 被更新为 dp[i][j] = dp[i-1][j-1] + 1。
注意到 dp[i−1][j−1] 已经被求解过了，所以可以直接使用。

字符 s1[i−1] 和 s2[j−1] 不匹配，这种情况下我们不能直接增加已匹配子序列的长度，
但我们可以将之前已经求解过的最长公共子序列的长度作为当前最长公共子序列的长度。
但是我们应该选择哪一个呢？事实上此时我们有 2 种选择。
我们可以删除 s1 或者 s2 的最后一个字符然后将对应的 dp 数组的值作比较，
也就是取 dp[i-1][j] 和 dp[i][j−1] 的较大值。

最后，与前面方法类似的，我们获得删除次数 m + n - 2*dp[m][n]，其中 m 和 n 分别是 s1 和 s2 的字符串长度，
dp[m][n]是两个字符串的最长公共子序列。

*/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const len1 = word1.length;
    const len2 = word2.length;
    var dp = new Array(); //先声明一维
    // 注意这里二维数组DP的范围为0-len，因为后面要访问索引len，所以要大一点保证足够的存储空间
    for(var i=0; i < len1 + 1; i++){ //一维长度为len1,len1为变量，可以根据实际情况改变
        dp[i] = new Array(); //声明二维，每一个一维数组里面的一个元素都是一个数组；
        for(var j = 0; j < len2 + 1; j++){ //一维数组里面每个元素数组可以包含的数量len2，len2也是一个变量；
            dp[i][j] = 0; //这里将变量初始化，我这边统一初始化为0，后面在用所需的值覆盖里面的值
        }
    }
    // 同样，我们这里从索引1开始求解， 因此要访问到索引len！
    for(let i = 1; i < len1+1; i++){
        for(let j = 1; j < len2+1; j++){
            dp[i][j] = word1[i-1] === word2[j-1] ? dp[i-1][j-1] + 1 : Math.max(dp[i][j-1], dp[i-1][j]);
        }
    }
    // 这个根据题意返回相应的值
    // dp[m][n]存储的就是两个数组最长公共子数据的长度
    return len1+len2-2*dp[len1][len2];
};
