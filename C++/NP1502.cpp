#include <iostream>
#include <fstream>
using namespace std;

bool a[105][105];

int main() {
    ifstream inputFile("mine.in");
    ofstream outputFile("mine.out");

    int n, m;
    inputFile >> n >> m;

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            char ch;
            inputFile >> ch;
            a[i][j] = (ch == '*');
        }
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            if (a[i][j] == true) {
                outputFile << '*';
            } else {
                int count = a[i + 1][j + 1] +
                            a[i + 1][j - 1] +
                            a[i + 1][j] +
                            a[i][j + 1] +
                            a[i][j - 1] +
                            a[i - 1][j + 1] +
                            a[i - 1][j] +
                            a[i - 1][j - 1];
                outputFile << count;
            }
        }
        outputFile << '\n';
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
