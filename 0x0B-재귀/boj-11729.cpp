#include <bits/stdc++.h>
using namespace std;

void hanoi(int a, int b, int n){
    if (n == 1){
        cout << a << " " << b << "\n";
        return;
    }


    hanoi(a, 6-b-a, n-1);
    cout << a << " " << b << "\n";
    hanoi(6-b-a, b, n-1);
}

int main(void) {
    int n;
    cin >> n;

    cout << (1<<n) -1 << "\n";
    hanoi(1, 3, n);

    
}