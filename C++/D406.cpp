#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, num;
    cin >> n;
    vector<int> a, b;
    for (int i = 0; i < n; i++) {
        cin >> num;
        a.push_back(num);
    }
    for (int i : a) {
        bool found = false;
        for (int j : b) {
            if (i == j) {
                found = true;
                break;
            }
        }
        if (!found) {
            b.push_back(i);
        }
    }
    cout << b.size() << endl;
    for (int i : b) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}
