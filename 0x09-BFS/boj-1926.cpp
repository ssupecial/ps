#include <bits/stdc++.h>
using namespace std;


int main(void){
    int n, m;
    cin >> n;
    cin >> m;
    int board[502][502];
    
    priority_queue<int> pictures;
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < m; k ++) {
            int value;
            cin >> value;
            board[i][k] = value;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int k = 0; k < m; k++) {
            if (board[i][k] == 1){
                queue<pair<int, int>> Q;
                board[i][k] = 0;
                Q.push({i, k});
                int area = 0;
                while(!Q.empty()){
                    pair<int, int> cur = Q.front();
                    Q.pop();

                    for (int j = 0; j < 4; j++){
                        int nx = cur.first + dx[j];
                        int ny = cur.second + dy[j];

                        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                        if (board[nx][ny] == 0) continue;
                        board[nx][ny] = 0;
                        Q.push({nx, ny});
                    }
                    area++;
                }
                pictures.push(area);
            }
        }
    }

    cout << pictures.size() << '\n';
    if (pictures.size() == 0)
        cout << 0;
    else
        cout << pictures.top();

}