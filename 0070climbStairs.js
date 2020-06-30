// critical condition
// f(n) = f(n-1) + f(n-2)  f(1)=1 f(2)=2

// avoid repeat -> memory search
//define an array to store states
const f = [];
const climbStaris = function(n){
    // border conditions
    if(n === 1){
        return 1;
    }
    if(n === 2){
        return 2;
    }
    // recursion 
    if(f[n] === undefined){
        f[n] = climbStaris(n-1) + climbStaris(n-2);
    }
    // f[n] exists, just return
    return f[n];
}

//DP dynamic planning
const climbStaris = function(n){
    const f = [];
    f[1] = 1;
    f[2] = 2;
    for(let i = 3; i <= n; i++){
        f[i] = f[i-1] + f[i-2];
    }
    return f[n];
}

