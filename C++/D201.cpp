#include <iostream>
using namespace std;

int main() {
    int Times;
    cin >> Times;
    if (Times == 0) {
        cout << 0 << endl;
    }
    else if (Times == 1) {
        cout << 1 << endl;
    }
    else {
        Times -= 1;
        int OldNumber;
        int NewNumber;
        int PrintNumber;
        OldNumber = 0;
        NewNumber = 1;
        for (int i = 0;i < Times;++i) {
            PrintNumber = OldNumber + NewNumber;
            OldNumber = NewNumber;
            NewNumber = PrintNumber;
        }
        cout << PrintNumber << endl;
    }
    return 0;
}
