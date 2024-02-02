#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, t;
    cin >> s >> t;

    for (auto& x : s) {
        x = tolower(x);
    }
    for (auto& x : t) {
        x = tolower(x);
    }

    if (s < t) {
        cout << "Smaller" << endl;
    } else if (s > t) {
        cout << "Greater" << endl;
    } else {
        cout << "Equal" << endl;
    }
    return 0;
}
