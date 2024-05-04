#include <iostream>
#include <deque>
using namespace std;

int main(void){
    deque<int> DQ;
    DQ.push_front(10); // 10
    DQ.push_back(50); // 10 50
    DQ.push_front(24); // 24 10 50
    for(auto x: DQ) cout << x << ' ';
    cout << DQ.size() << '\n';
    DQ.pop_front(); // 10 50
    DQ.pop_back(); // 10
    cout << DQ.front() << ' ' << DQ.back() << '\n'; // 10 10
}