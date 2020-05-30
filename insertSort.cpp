#include <iostream>
#include <vector>

using namespace std;

/**************
--------------------------
Insert Sort: O(n*n) stable
--------------------------
Thoght: 
1. iterate an unsorted array but start from the second element since we suppose the 
   first element is ordered.
2. store current element into key and assign the second iterator j which is i-1.
3. use while loop to judge if j is larger or equal to 0 to avoid out of index and arr[j] 
   should be larger than key which means we should do something.
4. After checking the former element and update the current element, we update the former
   element in the end.
5. Note: we assume the former sub-array is ordered already because we handle from the first data
         so that we actually just jump out from the while loop when we checked only once
**************/

void insertSort(vector<int>& arr) {
	for (int i = 1; i < arr.size(); ++i) {
		int key = arr[i];
		int j = i - 1;
		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			--j;
		}
		arr[j + 1] = key;
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
	insertSort(nums);
	for (int i = 0; i < nums.size(); i++) {
		cout << nums[i] << ' ';
	}
	return 0;
}