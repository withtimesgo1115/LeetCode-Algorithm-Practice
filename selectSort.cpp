#include <iostream>
#include <vector>

using namespace std;

void selectSort(vector<int>& arr) {
	int temp;
	for (int i = 0; i < arr.size(); ++i) {
		int index = i;
		for (int j = i + 1; j < arr.size(); ++j) {
			if (arr[index] > arr[j]) {
				index = j;
			}
		}
		if (index != i) {
			temp = arr[index];
			arr[index] = arr[i];
			arr[i] = temp;
		}
	}
}

int main() {
	int num;
	vector<int> nums;
	while (cin >> num) {
		nums.push_back(num);
		if (cin.get() == '\n') {
			break;
		}
	}
	for (int i = 0; i < nums.size(); ++i) {
		cout << nums[i] << ' ';
	}
	cout << endl;
	selectSort(nums);
	for (int i = 0; i < nums.size(); ++i) {
		cout << nums[i] << ' ';
	}
	return 0;
}