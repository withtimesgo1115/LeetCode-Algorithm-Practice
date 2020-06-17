const nd_array = [[1,2,3],[4,5,6],[7,8,9]];
//console.log(nd_array.toString(nd_array));

// reduce solution
function flatten_reduce(arr){
    return arr.reduce((sum, cur) => {
        return sum.concat(Array.isArray(cur) ? flatten_reduce(cur) : cur);
    }, []);
}

var res = flatten_reduce([1,[2,3,[4,5]]]);
console.log(res);
console.log(flatten_reduce(nd_array));

// toString/split/map solution
function flatten_toString(arr){
    return arr.toString().split(',').map(el => {
        return Number(el);
    });
}

var res2 = flatten_toString([1,[2,3,[4,5]]]);
console.log(res2);
console.log(flatten_toString(nd_array));

// join/split/map solution
function flatten_join(arr){
    return arr.join(',').split(',').map(el => {
        return parseInt(el);
    });
}

var res3 = flatten_join([1,[2,3,[4,5]]]);
console.log(res3);
console.log(flatten_join(nd_array));

// recursion solution
function flatten_recursion(arr){
    var res = [];
    arr.map(el => {
        if(Array.isArray(el)){
            res = res.concat(flatten_recursion(el));
        }else{
            res.push(el);
        }
    });
    return res;
}

var res4 = flatten_recursion([1,[2,3,[4,5]]]);
console.log(res4);
console.log(flatten_recursion(nd_array));