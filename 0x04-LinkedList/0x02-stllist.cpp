#include <iostream>
#include <list>
using namespace std;

int main(void){
    list<int> L = {1,2}; // 1 2
    list<int>::iterator t = L.begin();
    L.push_front(10); // 10 1 2
    cout << *t << '\n'; // 1 출력
    L.push_back(5); // 10 1 2 5
    L.insert(t, 6); // 10 6 1 2 5 t가 가리키는 곳 앞에 6을 삽입
    t++; // t가 가리키는 곳은 2
    t = L.erase(t); // t가 가리키는 곳을 제거 (2 제거), 그 다음 원소인 5의 위치를 반환
    cout << *t << '\n';
    for (list<int>::iterator it = L.begin(); it != L.end(); it++){
        cout << *it << ' ';
    }
}