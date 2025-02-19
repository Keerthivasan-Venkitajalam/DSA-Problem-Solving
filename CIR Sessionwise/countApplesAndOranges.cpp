#include <iostream>
#include <vector>

using namespace std;

void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
    int appleCount=0, orangeCount=0; //initialize to 0

    //counting apples that fall within the house range
    for (int apple:apples) {
        int applePosition=a+apple;
        if (applePosition>=s && applePosition<=t) {
            appleCount++;
        }
    }
    
    //counting oranges that fall within the house range
    for (int orange:oranges) {
        int orangePosition=b+orange;
        if (orangePosition>=s && orangePosition<=t) {
            orangeCount++;
        }
    }
    
    cout << appleCount << endl;
    cout << orangeCount << endl;
}

int main() {
    int s, t, a, b, m, n;
    
    cin >> s >> t;
    cin >> a >> b;
    cin >> m >> n;
    
    vector<int> apples(m);
    vector<int> oranges(n);
    
    for (int i = 0; i < m; i++) {
        cin >> apples[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> oranges[i];
    }
    //function call
    countApplesAndOranges(s, t, a, b, apples, oranges);
    return 0;
}
