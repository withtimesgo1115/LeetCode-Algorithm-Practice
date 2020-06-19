const validPalidrome = function(s){
    // store the length of the array
    const len = s.length;
    // define two pointers
    let i = 0;
    let j = len - 1;
    // use while to loop
    while(i < j && s[i] === s[j]){
        i++;
        j--;
    }
    // when there are two distinct elements, jump out of the array
    if(isParadrome(i+1,j)){
        return true;
    }
    if(isParadrome(i,j-1)){
        return true;
    }


    // support function which requires two pointers: start and end
    function isParadrome(start,end){
        // use while to loop and since we have two pointers, the start must be smaller than end pointer
        while(start < end){
            // compare the data pointed by start and end, if the symmetric data is not the same, return false, else move the pointers  
            if(s[start] !== s[end]){
                return false;
            }
            start++;
            end--;
        }
        // all the data has been checked so that we can return true
        return true;
    }

    // default output
    return false;
}