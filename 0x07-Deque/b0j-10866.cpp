#include <iostream>
#include <deque>
using namespace std;

int main(void){
    int N;
    cin >> N;
    deque<int> DQ;

    for (int i = 0; i < N; i++){
        string cmd;
        cin >> cmd;
        if (cmd == "push_front"){
            int value;
            cin >> value;
            DQ.push_front(value);
        } else if (cmd == "push_back") {
            int value;
            cin >> value;
            DQ.push_back(value);
        } else if (cmd == "pop_front") {
            if (DQ.empty())
                cout << -1 << '\n';
            else {
                cout << DQ.front() << '\n';
                DQ.pop_front();
            }
        } else if (cmd == "pop_back") {
            if (DQ.empty())
                cout << -1 << '\n';
            else {
                cout << DQ.back() << '\n';
                DQ.pop_back();
            }
        } else if (cmd == "size") {
            cout << DQ.size() << '\n';
        } else if (cmd == "empty"){
            if (DQ.empty())
                cout << 1 << '\n';
            else    
                cout << 0 << '\n';
        } else if (cmd == "front"){
            if (DQ.empty())
                cout << -1 << '\n';
            else 
                cout << DQ.front() << '\n';
        } else if (cmd == "back"){
            if (DQ.empty())
                cout << -1 << '\n';
            else 
                cout << DQ.back() << '\n';
        }
    }
}