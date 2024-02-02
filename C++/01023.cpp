#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int findClosestNumber(const vector<int>& numbers, int key) {
    int left = 0;
    int right = numbers.size() - 1;

    int closestNumber = numbers[right];
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (numbers[mid] == key) {
            return numbers[mid];
        } else if (numbers[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
        
        if (abs(numbers[mid] - key) < abs(closestNumber - key)) {
            closestNumber = numbers[mid];
        } else if (abs(numbers[mid] - key) == abs(closestNumber - key)) {
            closestNumber = max(closestNumber, numbers[mid]);
        }
    }

    return closestNumber;
}

int main() {
    int N, K;
    cin >> N >> K;

    vector<int> numbers(N);
    for (int i = 0; i < N; i++) {
        cin >> numbers[i];
    }

    int closestNumber = findClosestNumber(numbers, K);
    cout << closestNumber << endl;

    return 0;
}
