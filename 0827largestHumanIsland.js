/*
在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。

进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿）

示例 1:

输入: [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
示例 2:

输入: [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
示例 3:

输入: [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
*/

var largestIsland = function(grid) {
    // 如果grid是空的，则只能创造一个面积为1的陆地
    if(!grid || grid.length === 0) return 1;
    // 输出结果
    let res = 0;
    // 0是海洋 1是陆地 为了避免混淆 从2开始
    let index = 2;
    // 使用map结构存储陆地的索引和面积
    let indexAndAreas = new Map();
    // 2D循环遍历整个地图
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
            // 当遍历到陆地时
            if(grid[i][j] === 1){
                // DFS方法求出当前陆地所在的整个岛屿的面积
                let cur_area = area(grid, i, j, index);
                // 设置当前陆地的索引和其所处岛屿的面积
                indexAndAreas.set(index, cur_area);
                // 索引号递增
                index++;
                // 保留最大面积
                res = Math.max(res, cur_area);
            }
        }
    }
    // 如果没有找到陆地，那么就自己造一块
    if(res === 0) return 1;
    // 否则的话，我们需要遍历海洋来找到一块合适的海洋填海造陆使得两个最大的岛屿连接起来
    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
            // 当发现海洋时
            if(grid[i][j] === 0){
                // 调用函数找其邻居并返回一个Set结构，里面保存了邻居的索引（即岛屿编号)， set结构使得不管几个邻居都不会重复
                let hashSet = findNeighbour(grid, i, j);
                // 如果set是空的，则没有发现邻居，跳过这个cell继续搜
                if(hashSet.size < 1) continue;
                // 这时定义一个变量保存两个岛屿连在一起的面积，初始化为1指的是填海造陆的那块土地
                let twoIsland = 1;
                // 遍历set，根据set的值查找邻居所在岛屿的对应面积并添加给变量
                for(let x of hashSet){
                    twoIsland += indexAndAreas.get(x);
                }
                // 最后更新res的值
                res = Math.max(res, twoIsland);
            }
        }
    }
    return res;
};

// 辅助函数寻找当前节点的邻居
var findNeighbour = function(grid, r, c){
    // 定义set来储存邻居的并用作输出
    let hashSet = new Set();
    // 只要相邻节点在区域内，且不是海洋那么就把该节点的索引信息添加到set中去
    if(inArea(grid, r-1, c) && grid[r-1][c] !== 0){
        hashSet.add(grid[r-1][c]);
    }
    if(inArea(grid, r+1, c) && grid[r+1][c] !== 0){
        hashSet.add(grid[r+1][c]);
    }
    if(inArea(grid, r, c-1) && grid[r][c-1] !== 0){
        hashSet.add(grid[r][c-1]);
    }
    if(inArea(grid, r, c+1) && grid[r][c+1] !== 0){
        hashSet.add(grid[r][c+1]);
    }
    return hashSet;
}

// 计算所在岛屿的面积
var area = function(grid, r, c, index){
    if(!inArea(grid, r, c)) return 0;
    if(grid[r][c] !== 1) return 0;
    grid[r][c] = index;
    return 1 + area(grid, r-1, c, index) + area(grid, r+1, c, index)
        + area(grid, r, c-1, index) + area(grid, r, c+1, index);
}

// 判断节点是否越界
var inArea = function(grid, r, c){
    return r >= 0 && c >= 0 && r < grid.length && c < grid[0].length;
}