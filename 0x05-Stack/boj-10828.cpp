#include <iostream> 
#include <stack>

using namespace std;

int main(void){
    int N;
    cin >> N;
    stack<int> S;
    for (int i = 0; i < N; i++){
        string cmd;
        cin >> cmd;
        if (cmd == "push"){
            int value;
            cin >> value;
            S.push(value);
        } else if (cmd == "top"){
            if (S.empty())
                cout << -1 << "\n";
            else   
                cout << S.top() << "\n";
        } else if (cmd == "pop"){
            if (S.empty())
                cout << -1 << "\n";
            else {
                cout << S.top() << "\n";
                S.pop();
            }
        } else if (cmd == "size") {
            cout << S.size() << "\n";
        } else if (cmd == "empty") {
            if (S.empty())
                cout << 1 << "\n";
            else    
                cout << 0 << "\n";
        } 
        
    }
}