#include <bits/stdc++.h>
using namespace std;

int main(void){
    while(true){
        string value;
        int flag = 0;
        getline(cin, value);
        if (value == ".")
            break;
        stack<char> symbols;
        for (char c: value){
            if (c == '(')
                symbols.push('(');
            else if (c == '[')
                symbols.push('[');
            else if (c == ')'){
                if (symbols.size() == 0 || symbols.top() != '('){
                    flag = 1;
                    continue;
                } else {
                    symbols.pop();
                }
            }
            else if (c == ']'){
                if (symbols.size() == 0 || symbols.top() != '['){
                    flag = 1;
                    continue;
                } else {
                    symbols.pop();
                }
            }
        }
        if (flag == 1 || symbols.size() != 0)
            cout << "no" << "\n";
        else 
            cout << "yes" << "\n";
    }
}