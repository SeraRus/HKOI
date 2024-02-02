#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double weight, height;
    cin >> weight >> height;
    double BMI = weight / (height * height);
    cout << fixed << setprecision(3) << BMI << endl;

    if (BMI < 18.5) {
        cout << "Underweight" << endl;
    } else if (BMI < 23.0) {
        cout << "Normal" << endl;
    } else if (BMI < 25.0) {
        cout << "Overweight" << endl;
    } else {
        cout << "Obese" << endl;
    }
    return 0;
}
