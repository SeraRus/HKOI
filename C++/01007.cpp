#include <string>
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
    int v;
    cin >> v;
    string arr[v];
    int rec = 0;
    while (rec != v){
        string dest, ser, code, asc;
        cin >> setw(3) >> dest >> setw(2) >> ser >> setw(4) >> code;
        getline(cin, asc);
        int cd = stoi(code);
        int check = 0;
        for (int i = 0; i < asc.length(); i++){
            check += asc[i];
        }
        if (cd == check){
            arr[stoi(ser) - 1] = asc;
            rec++;
        }
    }
    for (int i = 0; i < v; i++){
        cout << arr[i];
    }
}
