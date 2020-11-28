#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int L, C;
    cin >> L >> C;

    cout << 2*(L * C) - L - C + 1 << endl;
    cout << 2*((L - 1) + (C - 1)) << endl;

    return 0;
}
