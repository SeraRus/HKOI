#include <iostream>
#include <list>
using namespace std;

int main() {
    list<int> d1(3);
    list<int> d2(3);
    int num;


    for (int i = 0; i < 3; i++) {
        cin >> num;
        d1.push_back(num);
    }

    for (int i = 0; i < 3; i++) {
        cin >> num;
        d2.push_back(num);
    }

    if (d1>d2)
        cout << "After" << endl;
    else if (d2>d1)
        cout << "Before" << endl;
    else
        cout << "Same" << endl;

    return 0;
}
