#include <iostream>
#include <string>
using namespace std;


int main() {
    string str, target;
    getline(cin, str);
    getline(cin, target);
    string::size_type targetLength = target.length();
    int count = 0;

    if (targetLength > str.length()) {
        cout << 0 << endl;
        return 0;
    }
    
    for (int i = 0; i <= str.length() - targetLength; i++) {
        string substring = str.substr(i, targetLength);
        if (substring == target) {
            count++;
        }
    }

    cout << count << endl;

    return 0;
}
