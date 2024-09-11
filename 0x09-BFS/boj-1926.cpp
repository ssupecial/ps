#include <bits/stdc++.h>
#define X first;
#define Y second;
using namespace std;



int main(void) {
    int board[500][500];
    int visited[500][500];
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, -1, 0, 1};
    int n, m;
    int num = 0;
    int max = 0;
    cin >> n >> m;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            int s;
            cin >> s;
            board[i][j] = s;
            visited[i][j] = 0;
        }
    }

    for(int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            int curWidth = 0;

            if(board[i][j] == 1 && visited[i][j] == 0){
                queue<pair<int, int>> Q;
                Q.push({i, j});
                visited[i][j] = 1;
                

                while(!Q.empty()){
                    pair<int, int> cur = Q.front();
                    Q.pop();
                    curWidth++;

                    for (int k = 0; k < 4; k++){
                        int curDx = cur.first + dx[k];
                        int curDy = cur.second + dy[k];
                        
                        if (curDx < 0 || curDx >= n || curDy < 0 || curDy >= m) continue;
                        if (board[curDx][curDy] == 0 || visited[curDx][curDy] == 1) continue;

                        Q.push({curDx, curDy});
                        visited[curDx][curDy] = 1;
                    }
                }

                num++;
                if (max < curWidth) max = curWidth;
            }

        }
    }

    cout << num << '\n' << max;


}