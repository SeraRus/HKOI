#include <iostream>
using namespace std;

int main() {
    string Pnum;
    cin >> Pnum;
    char FirstDigit = Pnum[0];
    if (FirstDigit == '2' || FirstDigit == '3')
        cout << "Fixed" << endl;
    else
        cout << "Mobile" << endl;
    return 0;
}
