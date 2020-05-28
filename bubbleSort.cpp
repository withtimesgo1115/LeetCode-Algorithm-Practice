#include <iostream>
#include <vector>
#include<time.h>

using namespace std;

// 2 3 1 5 4
// 2 3 1 4 5
// 2 1 3 4 5
// 1 2 3 4 5
// O(n^2) stable suit for small dataset
void bubbleSort(vector<int>& arr){
    if (arr.size() == 0) {
        return;
    }
    for (int i = 0; i < arr.size(); ++i) {
        for (int j = arr.size() - 1; j > i; j--) {
            if (arr[j - 1] > arr[j]) {
                swap(arr[j - 1], arr[j]);
            }
       }
    }
}

// optimize bubbleSort 
// stop doing the first iteration if there is no need to swap elements
// use a flag to mark the state
void bubbleSortOpt(vector<int>& arr) {
    if (arr.size() == 0) {
        return;
    }
    bool flag = false;
    for (int i = 0; i < arr.size() && flag == false; i++) {
        flag = true;
        for (int j = arr.size() - 1; j > i; j--) {
            if (arr[j - 1] > arr[j]) {
                swap(arr[j - 1], arr[j]);
                flag = true;
            }
        }
    }
}

int main() {
    clock_t startTime, endTime;
    int num = 0;
    vector<int> nums;
    while (cin >> num)
    {
        nums.push_back(num);
        if (cin.get() == '\n')
            break;
    }
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << ' ';
    }
    cout << endl;
    startTime = clock();
    //bubbleSort(nums);
    bubbleSortOpt(nums);
    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << ' ';
    }
    endTime = clock();
    cout << endl;
    cout << "Totle Time : " << (double)(endTime - startTime) / CLOCKS_PER_SEC << "s" << endl;
    return 0;
}
