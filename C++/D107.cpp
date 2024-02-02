#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    bool sql = ((int(sqrt(n)) * int(sqrt(n))) == n);
    bool tri = (fmod(((sqrt(8*n+1)-1)/2), 1.0) == 0.0);

    if (sql && tri) {
        cout << "Both" << endl;
    } else if (sql) {
        cout << "Square" << endl;
    } else if (tri) {
        cout << "Triangular" << endl;
    } else {
        cout << "Neither" << endl;
    }

    return 0;
}
