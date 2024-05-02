#include <iostream>
#include <queue>
using namespace std;

int main(void){
    queue<int> Q;
    Q.push(10);
    Q.push(20);
    cout << Q.size() << ' ' << Q.front() << ' ' << Q.back();
    Q.pop();
}