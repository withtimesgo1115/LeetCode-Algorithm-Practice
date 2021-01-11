/*
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"
*/

const decodeString = (s) => {
    // 存放倍数的栈
    let numStack = [];
    // 存待拼接的str的栈
    let strStack = [];
    // 倍数的搬运工
    let num = 0;                                                                                            
    // 输出结果字符串                               
    let result = '';
    // 逐个扫描字符
    for(const char of s){
        if(!isNaN(char)){
            // 如果遇到数字，算出倍数
            num = num * 10 + Number(char);
        }
        // 遇到 [ 时
        else if(char === '['){
            // result串入栈
            strStack.push(result);
            // 清空
            result = '';
            // 倍数栈出栈
            numStack.push(num);
            // 清空
            num = 0;
        }
        else if(char === ']'){
            // 输出子串
            let repeatTimes = numStack.pop();
            result = strStack.pop() + result.repeat(repeatTimes);
        }else{
            // 遇到字母 加到result字符串上
            result += char;
        }
    }
    return result;
}