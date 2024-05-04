#include <bits/stdc++.h>
using namespace std;

int main(void){
    string value;
    getline(cin, value);
    stack<char> symbols;
    int num = 0;
    int flag = 0;
    for(char c: value){
        if (c == '('){
            symbols.push(c);
            flag = 1;
        } else if (c == ')'){
            symbols.pop();
            if (flag == 1){ // 레이저
                num += symbols.size();
            } else { // 쇠막대기 끝
                num += 1;
            }
            flag = 0;
        }
    }
    cout << num;
}