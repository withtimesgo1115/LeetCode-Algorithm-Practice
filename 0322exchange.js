const coinChange = function(coins,amount){
    // this array is used to store minimum coin number of each target
    const f = [];
    // define conditions known
    f[0] = 0;
    // iterate [1, amount]'s full number of coins 
    for(let i = 1; i <= amount; i++){
        // we can initialzie each position with Infinity sicne we are finding the minimum
        f[i] = Infinity;
        // iterate all the coins that we can use
        for(let j = 0; j < coins.length; j++){
            // coin's value is smaller than current amount, then do next
            if(i - coins[j] >= 0){
                // state transformation equation
                f[i] = Math.min(f[i], f[i-coins[j]] + 1);
            }
        }
    }
    // if target amount's value is Infinity
    // It means there is no coin to update it, return -1
    if(f[amount] === Infinity){
        return -1;
    }
    // else return its result
    return f[amount];
}