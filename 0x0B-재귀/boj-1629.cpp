#include <bits/stdc++.h>
using namespace std;

long long mod(long long x, long long y, long long m){
    
    if (y == 1) {
        return x % m;
    }
    long long val = mod(x, y/2, m);
    if (y % 2 == 0){
        return val * val % m;
    }
    else {
        return val * val * x % m;
    }
}

int main(void) {
    long long a, b, c;
    cin >> a >> b >> c;

    long long result = mod(a, b, c);
    cout << result;

}