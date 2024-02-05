#include <iostream>
using namespace std;


int main(){
    int N, num;
    cin >> N;
    cout << "1" << endl;
    for (int i = 1; i < N; i++) {
        num = 1+(i*i);
        for (int u = 0; u <= i; u++) {
            while (num > 0) {
                cout << num << " ";
                num -= i;
            }
        }
        cout << endl;
    }
    return 0;
}
