#include <iostream>
#include <stack>

using namespace std;

int main(void){
    stack<int> s;
    s.push(1);
    s.push(2);
    s.pop();
    s.push(3);
    cout << s.top();
}