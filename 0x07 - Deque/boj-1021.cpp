#include <bits/stdc++.h>

using namespace std;
int N, start;


int main(void){
    
    cin >> N;
    cin >> start;
    deque<int> DQ;
    int num = 0;

    for (int i = 0; i < N; i++)
        DQ.push_back(i+1);

    for (int i = 0; i < start; i++){
        int value;
        cin >> value;
        int idx = find(DQ.begin(), DQ.end(), value) - DQ.begin();
        if (idx < DQ.size() - idx){
            num += idx;
            while (idx--) {
                DQ.push_back(DQ.front());
                DQ.pop_front();
            }
        } else {
            idx = DQ.size() - idx;
            num += idx;
            while (idx--) {
                DQ.push_front(DQ.back());
                DQ.pop_back();
            }
        }
        DQ.pop_front();

    }
    cout << num;
    





}