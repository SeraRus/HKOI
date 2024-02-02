#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    int a, b, c;
    double delta, x, y;
    cin >> a >> b >> c;

    delta = b * b - 4 * a * c;

    if (delta < 0) {
        cout << "None" << endl;
    } else if (delta == 0) {
        x = (-b + sqrt(delta)) / (2*a);
        cout << setprecision(3) << fixed << x << endl;
    } else {
        x = (-b + sqrt(delta)) / (2*a);
        y = (-b - sqrt(delta)) / (2*a);
        if (x < y) {
            cout << setprecision(3) << fixed << x << " " << y << endl;
        } else {
            cout << setprecision(3) << fixed << y << " " << x << endl;
        }
    }
    return 0;
}
