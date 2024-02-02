#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int sidesOfPolygon;
    cin >> sidesOfPolygon;
    vector<vector<int>> point;
    vector<int> temp(2);
    for (int i = 0; i < sidesOfPolygon; i++) {
        cin >> temp[0] >> temp[1];
        point.push_back(temp);
    }
    point.push_back(point[0]);
    int area = 0;
    for (int i = 0; i < sidesOfPolygon; i++) {
        area += point[i][0] * point[i+1][1];
        area -= point[i+1][0] * point[i][1];
    }
    auto areaOut = static_cast<float>(area);
    areaOut /= 2;
    cout << fixed << setprecision(1) << areaOut << endl;
    return 0;
}
