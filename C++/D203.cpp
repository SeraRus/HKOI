#include <iostream>
#include <string>
using namespace std;

int main() {
    int s, n, t, t2;
    string n1, s1;
    cin >> s;
    n = 1;
    t = 0;
    t2 = 0;
    while (t != 100) {
        if (t2 == 10) {
            cout << endl;
            t2 = 0;
        }
        t2 ++;
        if (n % s == 0) {
            cout << "Clap ";
        } else {
            n1 = to_string(n);
            s1 = to_string(s);
            string::size_type idx = n1.find(s1);
            if (idx == string::npos) {
                cout << n << " ";
            } else {
                cout << "Clap ";
            }
        }
        t++;
        n++;
    }
    return 0;
}
