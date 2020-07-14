#include <iostream>
#include <algorithm>
#include <cmath>
#include "math.h"
#include "limits.h"

using namespace std;

// 定义这个二维数组维度的最大值，由题目给出，我们可能用不到这么多但是需要一个足够大的内存空间
const int maxlayer = 200;
// 使用长长整型防止大数据溢出，同样定义一个二维数组并初始化为0
// 这是一种极为简便的C语言写法，用的是栈中的内存空间，空间换时间
long long int map[maxlayer][maxlayer] = { 0 };

// 定义一个函数来判断是否这个区域可以建中转站
// 思路就是遍历每个位置，查看每个位置的值，如果有一个空地即可建立
// 如果一个空地都没有，则表示不能建立，这里我们不关心最佳值，只考虑可以不可以建立中转站
// 由于需要遍历，所以每个维度的范围极限需要作为形参
bool canBuild(int level) {
	for (int i = 0; i < level; i ++ ) {
		for (int j = 0; j < level; j++) {
			if (map[i][j] == 0) {
				return true;
			}
		}
	}
	return false;
}

// 主函数逻辑
int main() {
	// 定义一个变量存储数组维度
	int level;
	cin >> level;
	// 有了维度范围，可以直接使用for循环来给二维数组赋值，值就是用户输入的
	for (int i = 0; i < level; i++) {
		for (int j = 0; j < level; j++) {
			cin >> map[i][j];
		}
	}
	// 输入好地图信息后，先判断当前维度的地图是否可以建中转站，如果不能直接返回-1
	if (canBuild(level) == false) {
		cout << -1 << endl;
	}
	// 如果可以建，那么我们需要寻找最佳位置，找到一个位置使得它到所有房子距离的总和最小
	else {
		// 先定义一个变量存储最大整数值
		int bestValue = INT_MAX;
		// 还是暴力遍历
		for (int i = 0; i < level; i++) {
			for (int j = 0; j < level; j++) {
				// 只有当遍历的当前位置为0，那么才需要计算其总距离
				if (map[i][j] == 0) {
					// 定义局部变量距离来存储当前位置的总距离
					int distance = 0;
					// 再次循环二维数组找房子，非常暴力的解法，并不理想，但是足够有效解题
					for (int ii = 0; ii < level; ii++) {
						for (int jj = 0; jj < level; jj++) {
							// 如果找到一个位置有房子，需要计算当前空地到该房子的距离并加到总距离遍历里
							if (map[ii][jj] == 1) {
								// 注意我们使用索引计算距离，也就是说这里只需要计算水平和竖直距离而无需考虑二者直线距离
								// 注意使用绝对值
								distance += abs(i - ii) + abs(j - jj);
							}
						}
					}
					// 取最小值
					bestValue = min(bestValue, distance);
				}
			}

		}
		// 最后输出最佳值
		cout << bestValue << endl;
	}
}