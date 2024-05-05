#include <bits/stdc++.h>
using namespace std;

int board[512][512];
bool visited[512][512];
int n = 7, m = 10;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main(void){
    queue<pair<int, int>> Q;
    visited[0][0] = true;
    Q.push({0,0});

    while (!Q.empty()){
        pair<int, int> cur = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++){
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (visited[nx][ny]) continue;

            visited[nx][ny] = true;
            Q.push({nx, ny});
        }
    }
    
}