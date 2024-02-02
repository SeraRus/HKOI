#include <iostream>
using namespace std;

int main() {
    int x;
    cin >> x;
    int bn[6] = {1000,500,100,50,20,10};
    for (auto i : bn) {
        while (x >= i) {
            cout << i << endl;
            x -= i;
        }
    }
    return 0;
}
