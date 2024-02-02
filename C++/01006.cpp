#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int OriVal, Times, Pri, AddValue;
    cin >> OriVal;
    cin >> Times;
    AddValue = 0;

    for (int i = 0; i < Times; ++i) {
        cin >> Pri;
        if (OriVal > Pri) {
            OriVal -= Pri;
        } else {
            while (OriVal <= Pri) {
                OriVal += 250;
                AddValue += 1;
            }
            OriVal -= Pri;
        }
    }
    if (OriVal == 0) {
        AddValue +=1;
    }
    cout << "$" << AddValue*250 << endl;
    return 0;
}
