#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int numCount;
    cin >> numCount;

    vector<int> nums(numCount);

    for (int i = 0; i < numCount; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());
    cout << nums[numCount - 1] << endl << nums[numCount - 2] << endl;
    return 0;
}
