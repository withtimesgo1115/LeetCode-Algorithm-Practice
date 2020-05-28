#include <iostream>
#include <vector>
#include <set>

using namespace std;

void quickSort(int left, int right, vector<int>& arr) {
	if (left > right) {
		return;
	}
	int i, j, base, temp;
	i = left, j = right;
	base = arr[left];
	while (i < j) {
		while (arr[j] >= base && i < j) {
			j--;
		}
		while (arr[i] <= base && i < j) {
			i++;
		}
		if (i < j) {
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
	arr[left] = arr[i];
	arr[i] = base;
	quickSort(left, i - 1, arr);
	quickSort(i + 1, right, arr);
}


int main() {
	vector<int> A = {6,1,2,7,9,3,4,5,10,8};
	for (int i = 0; i < A.size(); ++i) {
		cout << A[i] << " ";
	}
	cout << endl;
	quickSort(0,A.size()-1,A);
	for (int i = 0; i < A.size(); ++i) {
		cout << A[i] << " ";
	}
}