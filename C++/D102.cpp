#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    string n;
    cin >> n;

    n = n.substr(1);
    double result = (stof(n)+0.05) / 2;

    cout << "$" << fixed << setprecision(1) << result << endl;

    return 0;
}
