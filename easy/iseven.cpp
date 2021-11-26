/**
 * Problem: given an int, determine if it is even (return "YES") or odd (return
 * "FALSE").
 *
 * Input: single digit 1<=n<=100
 */
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    string out = (n <= 2 || n % 2) ? "NO" : "YES";
    cout << out << endl;
    return 0;
}