#include <fstream>
using namespace std;

long long a, b, c;
string ans;

int main() {
    ifstream inputFile("area.in");
    ofstream outputFile("area.out");
    inputFile >> a >> b >> c;
    if (a*a > b*c) {
        ans = "Alice";
    } else {
        ans = "Bob";
    }
    outputFile << ans << endl;

    inputFile.close();
    outputFile.close();

    return 0;
}
