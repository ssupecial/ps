#include <bits/stdc++.h>

using namespace std;
int N, start;


int main(void){
    
    cin >> N;
    cin >> start;
    deque<int> DQ;

    DQ.push_front(1);
    DQ.push_back(3);
    int idx = find(DQ.begin(), DQ.end(), 3) - DQ.begin();



}