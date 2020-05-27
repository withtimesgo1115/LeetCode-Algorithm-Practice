#include <iostream>
#include <vector>

using namespace std;

void quickSort(int left, int right, vector<int>& arr){
    if(left > right){
        return;
    }
    int i, j, base, temp;
    i = left, j = right;
    base = arr[left];
    while(i < j){
        while(arr[j] >= base && i < j){
            j--;
        }
        while(arr[i] <= base && i < j){
            i++;
        }
        if(i < j){
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    arr[left] = arr[i];
    arr[i] = base;
    quickSort(left,i-1,arr);
    quickSort(j+1,right,arr);
}