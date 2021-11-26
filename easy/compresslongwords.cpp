/**
 * Given an int n and n words. Return the word if its less than 10, else return
 * the first letter + number of letters - 2 + last letter.
 */
#include <iostream>

using namespace std;

int main() {
    int n;
    string s;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;
        int len = s.length();
        if (len > 10) {
            cout << s[0] << len - 2 << s[len - 1] << endl;
        } else {
            cout << s << endl;
        }
    }
    return 0;
}