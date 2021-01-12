/*
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
*/
var longestPalindrome = function(s) {
    let len = s.length;
    if(len < 2){
        return s;
    }
    let maxLen = 1;
    let begin = 0;
    //dp[i][j]表示s[i][j]是否为回文串
    let dp = new Array(len);
    for(let i = 0; i < len; i++){
        dp[i] = new Array(len).fill(0);
    }
    let charArray = s.split('');
    for(let i = 0; i < len; i++){
        dp[i][i] = true;
    }
    for(let j = 1; j < len; j++){
        for(let i = 0; i < j; i++){
            if(charArray[i] !== charArray[j]){
                dp[i][j] = false;
            }else{
                if(j - i < 3){
                    dp[i][j] = true;
                }else{
                    dp[i][j] = dp[i+1][j-1];
                }
            }
            // 只要dp[i][j]==true成立,就表示子串s[i,j]是回文的
            // 此时记录回文长度和起始位置
            if(dp[i][j] && j - i + 1 > maxLen){
                maxLen = j - i + 1;
                begin = i;
            }
        }
    }
    return s.substring(begin, begin + maxLen);
};
