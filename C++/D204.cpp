#include <iostream>
#include <string>
#include <list>
using namespace std;

int main() {
    int levels;
    cin >> levels;
    levels = static_cast<int>(levels / 2);
    int levels1 = levels;
    int levels2 = levels;
    list<string> reverse;
    for (int i = 0; i < levels + 1; i++) {
        string temp = string(levels1, ' ') + "#";
        temp[levels2] = '#';
        cout << temp << endl;
        levels1++;
        levels2--;
        reverse.push_front(temp);
    }
    reverse.pop_front();
    for (const string& m : reverse) {
        cout << m << endl;
    }
    return 0;
}
