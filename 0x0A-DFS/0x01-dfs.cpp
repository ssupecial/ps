#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[512][512];
int visited[512][512];
int n = 7, m = 10;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main(void){
    stack<pair<int, int>> S;
    S.push({0, 0});
    while(!S.empty()){
        pair<int, int> cur = S.top();
        S.pop();
        for (int i = 0; i < 4; i++){
            int nx = cur.X + dx[i];
            int ny = cur.Y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (board[nx][ny] != 1 || visited[nx][ny] == 1) continue;
            visited[nx][ny] = 1;
            S.push({nx, ny});
        }
    }
}