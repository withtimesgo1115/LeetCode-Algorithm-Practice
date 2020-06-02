#include<iostream>
using namespace std;

/******************
Shopee written exam Q1

shopee的办公室非常大，小虾同学的位置坐落在右上角，而大门却在左下角，可以把所有位置抽象为一个网格（门口的坐标为0，0）,
小虾同学很聪明，每次只向下，或者向左走，因为这样最容易接近目的地，但是小虾同学不想让自己的boss们看到自己经常在他们面前
出没，或者迟到被发现。他决定研究一下如果他不通过boss们的位置，他可以有多少种走法？

动态规划： DP法
******************/

int main() {
    int x, y, n;
    // no need to consider the space, console will neglect them
    cin >> x >> y >> n;
    // defien a 2D matrix and initialize with 0
    // in this matrix, we store how many solutions at each position
    // due to the size limitation of the matrix, we can just build a big enough matrix to use. 
    long long int dp[30 + 1][30 + 1] = { 0 };
    for (int i = 0; i < n; i++) {
        // assign the position of each boss and dp[x][y] means the boss sits here so that value is -1
        // because worker cannot move in that position
        int x, y;
        cin >> x >> y;
        dp[x][y] = -1;
    }
    // for the first row and first column, the worker can only move in one direction (left and downward)
    for (int i = 0; i <= x; i++) dp[i][0] = 1;
    for (int j = 0; j <= y; j++) dp[0][j] = 1;
    // we should start from 1 since we will use i-1 and j-1
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            // the worker met the boss
            if (dp[i][j] == -1) continue; 
            // current steps should add following steps if the worker won't meet the boss
            if (dp[i - 1][j] != -1) dp[i][j] += dp[i - 1][j];
            if (dp[i][j - 1] != -1) dp[i][j] += dp[i][j - 1];
        }
    }
    cout << dp[x][y] << endl;
    return 0;
}