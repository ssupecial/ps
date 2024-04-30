#include <iostream>
using namespace std;

const int MX = 1000005;
char dat[MX];
int nxt[MX];
int pre[MX];
int unused = 1;
int cursor;

void insert(int addr, char value){
    dat[unused] = value;
    pre[unused] = addr;
    nxt[unused] = nxt[addr];
    if (nxt[addr] != -1)
        pre[nxt[addr]] = unused;
    nxt[addr] = unused;
    
    unused++;
}

void erase(int addr){
    nxt[pre[addr]] = nxt[addr];
    if (nxt[addr] != -1)
        pre[nxt[addr]] = pre[addr];
}

void traverse(){
  int cur = nxt[0];
  while(cur != -1){
    cout << dat[cur];
    cur = nxt[cur];
  }
}

void init(string input){
    for (int i = 0; i < input.size(); i++){
        insert(i, input[i]);
    }
    cursor = input.size();
}


int main(void){
    string input;
    cin >> input;

    fill(pre, pre+MX, -1);
    fill(nxt, nxt+MX, -1);


    init(input);
    // traverse();

    int num;
    cin >> num;

    for (int i = 0; i < num; i++){
        char op;
        cin >> op;
        if (op == 'L') {
            if(pre[cursor] != -1)
                cursor = pre[cursor];
        }
        else if (op == 'P'){
            char val;
            cin >> val;
            insert(cursor, val);
            cursor = nxt[cursor];
        }
        else if (op == 'D') {
            if (nxt[cursor] != -1)
                cursor = nxt[cursor];
        }
        else {
            if (pre[cursor] != -1){
                erase(cursor);
                cursor = pre[cursor];
            }
        }
    }

    traverse();


}