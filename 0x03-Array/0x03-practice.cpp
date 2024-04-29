#include <iostream>
using namespace std;

int check(int arr[], int N){
    int count[101] = {};

    for(int i = 0; i < N; i++){
        if (count[100-arr[i]] > 0) {
            return 1;
        }
        count[arr[i]]++;
    }
    return 0;
}

int main(void){
    int arr[] = {1, 23, 53, 77, 60};
    int check_value = check(arr, 5);
    cout << check_value;

    
}