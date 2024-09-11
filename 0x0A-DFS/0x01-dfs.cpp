#include <bits/stdc++.h>
using namespace std;

int board[512][512];
int visited[512][512];
int n = 7, m = 8;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

int main(void){
    stack<pair<int, int>> S;
    visited[0][0] = 1;
    S.push({0,0});

    while(!S.empty()) {
        pair<int, int> cur = S.top();
        S.pop();

        for(int i = 0; i < 4; i++) {
            int curDx = cur.first + dx[i];
            int curDy = cur.second + dy[i];

            if (curDx < 0 || curDx >= n || curDy < 0 || curDy >= m) continue;
            if (board[curDx][curDy] != -1 || visited[curDx][curDy] == 1) continue;

            visited[curDx][curDy] = 1;
            S.push({curDx, curDy});
        }
    }
}