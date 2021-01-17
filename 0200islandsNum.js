/*
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

*/

var numIslands = function(grid) {
    let count = 0;
    // 2D循环遍历地图
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
            // 当遇到陆地时开始dfs深度搜索直到超出边界和遇到海洋
            if(grid[i][j] === '1'){
                dfs(grid, i, j);
                // 此时可以将所有遍历过的陆地连成一个岛屿 因此count+1
                // 紧接着下一个cell，如果是未遍历到的陆地的话继续dfs 否则就下一个
                count++;
            }
        }
    }
    return count;
};

var dfs = function(grid, r, c){
    // 返回条件 剪枝操作（对应于cell超出边界）
    if(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length) return;
    // 返回条件 剪枝操作（对应于cell不是陆地了）
    if(grid[r][c] !== '1') return;
    // 遍历过的修改陆地的值 使得下一次可以忽略这些遍历过的 提升效率
    grid[r][c] = '2';
    
    // 每个cell递归调用 四个分支
    dfs(grid, r-1, c);
    dfs(grid, r+1, c);
    dfs(grid, r, c-1);
    dfs(grid, r, c+1);
};