#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> li;
    int n, r;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> r;
        li.push_back(r);
    }
    sort(li.begin(), li.end());
    cout << li[li.size()/2] << endl;
    return 0;
}
