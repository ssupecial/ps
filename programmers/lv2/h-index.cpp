#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool compare(int a, int b){
    return a > b;
}

int solution(vector<int> citations) {
    int answer = citations.size();
    
    sort(citations.begin(), citations.end(), compare);
    for(int i = 0; i < citations.size(); i++){
        if (citations[i] < (i+1)) {
            answer = i;
            break;
        }
            
    }
        
    
    
    return answer;
}