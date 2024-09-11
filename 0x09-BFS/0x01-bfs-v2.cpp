#include <bits/stdc++.h>
#define X first;
#define Y second;
using namespace std;

int board[512][512];
int visited[512][512];
int n = 7, m = 8;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, -1, 0, 1};

int main(void){
    queue<pair<int, int>> Q;
    Q.push({0,0});
    visited[0][0] = 1;

    while(!Q.empty()){
        pair<int, int> cur = Q.front();
        Q.pop();

        for (int i=0; i<4; i++){
            int curDx = cur.X + dx[i];
            int curDy = cur.Y + dy[i];

            if (curDx < 0 || curDx >= n || curDy < 0 || curDy >= m) continue;
            if (visited[curDx][curDy]) continue;

            Q.push({curDx, curDy});
            visited[curDx][curDy] = 1;
        }
    }
}