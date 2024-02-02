#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int a, b;
    double c;
    cin >> a;
    cin >> b;
    cin >> c;
    double C = c * M_PI / 180;
    double Area = a*b*0.5*sin(C);
    cout << fixed << setprecision(3) << Area;
    return 0;
}
