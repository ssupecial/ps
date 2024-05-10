#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int main(void){
    int testcase;
    cin >> testcase;

    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};

    while(testcase--){
        int n, m, k;
        cin >> n >> m >> k;
        int board[n][m];
        int visited[n][m];
        fill(&board[0][0], &board[n-1][m], 0);
        fill(&visited[0][0], &visited[n-1][m], 0);
        queue<pair<int, int>> Q;

        for (int i = 0; i < k; i++){
            int a, b;
            cin >> a >> b;
            board[a][b] = 1;
        }
        int num = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if (board[i][j] == 1 && visited[i][j] != 1){
                    num++;
                    visited[i][j] = 1;
                    Q.push({i, j});
                    while(!Q.empty()){
                        pair<int, int> cur = Q.front();
                        Q.pop();
                        for (int t = 0; t < 4; t++){
                            int nx = cur.X + dx[t];
                            int ny = cur.Y + dy[t];

                            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                            if (visited[nx][ny] == 1 || board[nx][ny] != 1) continue;
                            visited[nx][ny] = 1;
                            Q.push({nx, ny});
                        }
                        
                    }

                    
                }
            }
        }
        cout << num << '\n';


    }
    

}