function findMostChar(str){
    // define an array to store the characters
    var arr = [];
    // split the string to characters in an array
    arr = str.split('');
    // prepare an object to store info
    var obj = {};
    // prepare two variables to store the max element
    var char = " ";
    var maxtimes = 0;
    for(var i=0; i<arr.length; i++){
        // local variable to store current number for current element
        var num = 0;
        // calculate the appearance of current element
        for(var j=0; j<arr.length;j++){
            if(arr[i] === arr[j]){
                num++;
            }
        }
        // update the max time
        if(num>maxtimes){
            maxtimes = num;
        }
        // write the current character info to the object
        obj[arr[i]] = num;
    }

    // search the char with the most appearance time
    for(var key in obj){
        if(obj[key] === maxtimes){
            char = key;
            maxtimes = obj[key];
            console.log(char + " appears " + maxtimes + " times!"); 
        }
    }
    // there is a problem that it cannot return char!!!!1
    return char, maxtimes;  
}