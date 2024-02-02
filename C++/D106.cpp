#include <iostream>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n;
    n = "0" + n;

    if (n[n.length() - 2] == '1') {
        cout << stoi(n) << "th" << endl;
    } else if (n[n.length() - 1] == '1') {
        cout << stoi(n) << "st" << endl;
    } else if (n[n.length() - 1] == '2') {
        cout << stoi(n) << "nd" << endl;
    } else if (n[n.length() - 1] == '3') {
        cout << stoi(n) << "rd" << endl;
    } else {
        cout << stoi(n) << "th" << endl;
    }

    return 0;
}
