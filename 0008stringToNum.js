const myAtoi = function(str){
    // write reg expression
    const reg = /\s*([-\+]?[0-9]*).*/
    // get the caught group
    const groups = str.match(reg);
    // calculate maximum
    const max = Math.pow(2,31) - 1;
    // calculate minimum
    const min = - max - 1;
    // targetNum is used to store the result
    let targetNum = 0;
    // successful matching
    if(groups){
        // full match is the first element in the groups
        // only caught group in () is the second and so on element in the array
        // so here we use groups[1]
        targetNum = groups[1];
        if(isNaN(targetNum)){
            targetNum = 0;
        }
    } 
    // border condition
    if(targetNum > max){
        return max;
    }
    else if(targetNum < min){
        return min;
    }
    return targetNum;
}