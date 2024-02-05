#include <iostream>
using namespace std;


int main(){
    int N, num;
    cin >> N;
    num = 0;
    for (int i = 0; i <= N; i++) {
        num += i*N;
    }
    for (int i = N; i > 0; i--) {
        for (int u = 0; u < N; u++) {
            cout << num << " ";
            num -= i;
        }
        cout << endl;
    }
    return 0;
}
