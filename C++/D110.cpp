#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string pt1, pt2;
    int y1, y2;
    vector<string> ab {"", "a", "b", "c", "d", "e", "f", "g", "h"};
    
    cin >> pt1;
    auto it1 = find(ab.begin(), ab.end(), pt1.substr(0, 1));
    y1 = stoi(pt1.substr(1));
    
    cin >> pt2;
    auto it2 = find(ab.begin(), ab.end(), pt2.substr(0, 1));
    y2 = stoi(pt2.substr(1));
    
    if (it1 != ab.end() && it2 != ab.end()) {
        auto x1 = distance(ab.begin(), it1);
        auto x2 = distance(ab.begin(), it2);
        auto l1 = abs(x1 - x2);
        auto l2 = abs(y1 - y2);
        
        if (l1 > l2) {
            cout << l1 << endl;
        } else {
            cout << l2 << endl;
        }
    }
    
    return 0;
}
