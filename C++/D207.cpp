#include <iostream>
#include <numeric>
using namespace std;

int main() {
    int num1, num2;
    cin >> num1 >> num2;
    cout << gcd(num1, num2) << endl;
    cout << static_cast<int>(num1 * num2 / gcd(num1, num2)) << endl;
    return 0;
}
