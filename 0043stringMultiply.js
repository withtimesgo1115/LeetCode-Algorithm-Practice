/*
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
*/

var multiply = function(num1, num2){
    if(Number(num1) === 0 || Number(num2) === 0) return "0";
    let res = new Array(num1.length + num2.length).fill(0);
    for(let i = num1.length - 1; i >= 0; i--){
        let n1 = num1.charAt(i) - '0';
        for(let j = num2.length - 1; j >= 0; j--){
            let n2 = num2.charAt(j) - '0';
            let sum = (res[i+j+1] + n1*n2);
            res[i+j+1] = sum%10;
            res[i+j] = Math.floor(sum/10); 
        }
    }
    let result = [];
    for(let i = 0; i < res.length; i++){
        if(i === 0 && res[i] === 0) continue;
        result.push(res[i]);
    }
    return result.join('');
}