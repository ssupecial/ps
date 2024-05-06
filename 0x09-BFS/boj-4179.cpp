#include <bits/stdc++.h>
using namespace std;

int board[1000][1000];

struct Node {
    int x;
    int y;
    int times;
};

int main(void){
    int n, m;
    cin >> n >> m;
    cin.ignore();
    queue<Node> Q;
    queue<Node> fires;
    int result = -1;
    int fire_alarm = 0;
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};


    for (int i = 0; i < n; i++){
        string value;
        getline(cin, value);
        for (int j = 0; j < m; j++){
            if (value[j] == '#')
                board[i][j] = -1;
            else if (value[j] == 'J'){
                board[i][j] = 1;
                Q.push({i, j, 0});
            }
            else if (value[j] == 'F'){
                board[i][j] = 2;
                fires.push({i, j, 0});
            }
            else if (value[j] == '.'){
                board[i][j] = 0;
            }
        }
    }

    while(!Q.empty()){
        Node cur = Q.front();
        Q.pop();
        

        if (cur.times > fire_alarm){ // 불 전파해야함
            fire_alarm = cur.times;

            while(!fires.empty()){
                Node cur_fire = fires.front();
                if(cur_fire.times >= fire_alarm) break;
                fires.pop();
                for (int i = 0; i < 4; i++){
                    int nx = cur_fire.x + dx[i];
                    int ny = cur_fire.y + dy[i];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                    if (board[nx][ny] == -1 || board[nx][ny] == 2) continue;
                    board[nx][ny] = 2;
                    fires.push({nx, ny, cur_fire.times+1});

                }
            }
            
           
        }

        if (board[cur.x][cur.y] == 2) continue; // 불에게 이미 전파된 경우

        for(int i = 0; i < 4; i++){
            int nx = cur.x + dx[i];
            int ny = cur.y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                cout << cur.times + 1;
                return 0;
            }
            if (board[nx][ny] != 0) continue;

            board[nx][ny] = 1;
            Q.push({nx, ny, cur.times+1});

        }



    }

    
    cout << "IMPOSSIBLE";
}