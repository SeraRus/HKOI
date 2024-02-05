#include <string>
#include <iostream>
using namespace std;


int main(){
    int N, time;
    string name;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> time >> name;
        if (time >= 1800 | time < 0600) {
            cout << "Good evening, " << name << "!" << endl;
        } else if (time >= 0600 & time < 1200) {
            cout << "Good morning, " << name << "!" << endl;
        } else if (time >= 1200) {
            cout << "Good afternoon, " << name << "!" << endl;
        }
    }
    return 0;
}
