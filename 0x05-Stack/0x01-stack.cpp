#include <iostream>
#include <list>

using namespace std;
const int MX = 1000005;
int dat[MX];
int pos = 0;

void push(int x){
    dat[pos++] = x;
}

void pop() {
    pos--;
}

int top() {
    return dat[pos-1];
}

void test() {
    push(1);
    push(2);
    pop();
    push(3);
    for (int i = 0; i < pos; i++){
        cout << dat[i] << ' ';
    }
}


int main(void){
    test();
}