//series (1)+(1+2)+(1+2+3).....(1+2+3..n)
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;

    int sum = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            sum += j;
        }
    }

    cout << "The sum of the series is: " << sum << endl;
    return 0;
}
