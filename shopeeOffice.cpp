#include<iostream>
using namespace std;

int main() {
    int x, y, n;
    cin >> x >> y >> n;
    long long int dp[30 + 1][30 + 1] = { 0 };
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        dp[x][y] = -1;
    }
    for (int i = 0; i <= x; i++) dp[i][0] = 1;
    for (int j = 0; j <= y; j++) dp[0][j] = 1;
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            if (dp[i][j] == -1) continue;
            if (dp[i - 1][j] != -1) dp[i][j] += dp[i - 1][j];
            if (dp[i][j - 1] != -1) dp[i][j] += dp[i][j - 1];
        }
    }
    cout << dp[x][y] << endl;
    return 0;
}