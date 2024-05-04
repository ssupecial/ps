#include <iostream>
using namespace std;

const int MX = 1000005;
int dat[MX*2+1];
int head = MX, tail = MX;

void push_front(int x){
    dat[--head] = x;
}

void push_back(int x){
    dat[tail++] = x;
}

void pop_front(){
    head++;
}

void pop_back(){
    tail--;
}

int front(){
    return dat[head+1];
}

int back(){
    return dat[tail-1];
}

void test(){
    push_front(1);
    push_back(2);
    push_front(3);
    cout << front() << ' ' << back();
}

int main(void){
    test();
}