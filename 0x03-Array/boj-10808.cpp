#include <iostream>
using namespace std;

int main(void) {
    string input;
    int arr[26] = {};

    std::cin >> input;

    for (int k = 0; k < input.size(); k++){
        int index = input[k] - 'a';
        arr[index]++;

        // arr[input[k] - 'a]++; 
    }

    for (int e: arr)
        cout << e << ' ';

    
}