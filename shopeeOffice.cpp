﻿#include <iostream>
#include <vector>

using namespace std;

int main() {
	int x, y, n;
	// 直接输入即可，牛客网的题目不需要考虑数据之间的空格
	cin >> x >> y >> n;
	// 首先根据范围定义一个足够装得下的二维数组并赋初值，很可能有一部分空间是用不到的，但是这样却是最快捷的
	// 使用long long int防止大数溢出
	long long int dp[30 + 1][30 + 1] = { 0 };
	// 接下来有n行，非常确定，所以使用for循环来给二维数组中的BOSS位置赋值
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		dp[x][y] = -1;
	}
	// 对于最下面一行的所有位置，都只有一种方案，就是一直左移
	for (int i = 0; i <= x; i++) {
		dp[i][0] = 1;
	}
	// 对于最左面一列的所有位置，都只有一种方案，就是一直下移
	for (int j = 0; j <= y; j++) {
		dp[0][j] = 1;
	}
	// 遍历二维数组，求解每个剩余位置所具有的方案数目
	// 注意这里要从索引1开始，因为0处的情况已经考虑，范围的上限由x，y决定也就是小虾同学的位置(右上角的坐标)
	for (int i = 1; i <= x; i++) {
		for (int j = 1; j <= y; j++) {
			// 碰到数据为-1的位置，直接跳过，进行下次循环
			if (dp[i][j] == -1) {
				continue;
			}
			// 如果当前位置左侧的那个位置没有BOSS，那么当前位置的方案数就等于当前位置数目+左侧位置的数目
			if (dp[i - 1][j] != -1) {
				dp[i][j] += dp[i - 1][j];
			}
			// 如果当前位置下侧的那个位置没有BOSS，那么当前位置的方案数就等于当前位置数目+下侧位置的数目
			if (dp[i][j - 1] != -1) {
				dp[i][j] += dp[i][j - 1];
			}
		}
	}
	cout << dp[x][y] << endl;
	return 0;
}