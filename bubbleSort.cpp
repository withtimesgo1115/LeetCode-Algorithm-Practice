#include <iostream>
#include <vector>

using namespace std;
/*
void bubbleSort(){

}
*/

int main(){
    int num = 0;
    vector<int> nums;
    while(cin.get() != '\n'){
        cin >> num;
        nums.push_back(num);
    }
    for(int i=0;i<nums.size();++i){
        cout << num[i];
    }
    //bubbleSort();
}