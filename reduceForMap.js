// this is a simple example to use reduce function to build a map function
// arr.reduce is used to operate each element in an array and sum the result
// arr.map is used to operate each element in an array 
// they are all based on the callback function

// Array.prototype.map should be overwritten
Array.prototype.map = function(callback){
    // define a variable using this which points to current array
    var arr = this;
    // use a clousre
    // a callback function in the reduce
    return arr.reduce((acc, cur, i) => {
        // use acc as an array to return
        acc.push(callback(cur, i, arr));
        return acc;
    }, []);
}


var m = [1,2,3,4,54].map(function(v, i, arr){
    return v * v;
});
console.log(m);