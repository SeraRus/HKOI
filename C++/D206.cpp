#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    cout << n << endl;
    while (n != 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = n * 3 + 1;
        }
        cout << static_cast<int>(n) << endl;
    }
    return 0;
}
