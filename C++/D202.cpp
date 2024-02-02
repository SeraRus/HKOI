#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  n = static_cast<int>(n / 2);
  for (int i = 1; i <= n; i++) {
    if (n % i == 0)
      cout << to_string(i) << endl;
  }
}
