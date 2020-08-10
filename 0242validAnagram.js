/* 
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

*/
// method1 O(nlogn) 先按字典序排序 再比较每个值是否一样
var isAnagram = function(s, t) {
    let sarr = s.split('').sort();
    let tarr = t.split('').sort();
    if(s.length !== t.length) return false;
    for(let i = 0; i < sarr.length; i++){
        if(sarr[i] !== tarr[i]){
            return false;
        }
    }
    return true;
};

// method2 O(n) 使用map映射 每次都是O(1) 总共n次
var isAnagram = function(s, t){
    // special case
    if(s.length !== t.length){
        return false;
    }
    // use only one map
    let map = new Map();
    let sarr = s.split('');
    let tarr = t.split('');
    // iterate first array
    sarr.forEach(item => {
        // get item from the map
        const cur = map.get(item);
        // if cur is equal to undefined, then we can set item's value 1
        if(cur === undefined){
            map.set(item, 1);
        }else{
            // else we can set item's value cur+1
            map.set(item, cur+1);
        }
    });
    // then iterate the second array
    tarr.forEach(item => {
        // if there is item in the map 
        if(map.has(item)){
            // we can make this item's value smaller  
            map.set(item, map.get(item)-1);
        }else{
            // if there is no item in the map. just return false
            return false;
        }
    });
    // finally we should judge if all the array's items constructed from map.values are equal to 0
    return [...map.values()].every(item => item === 0);
}