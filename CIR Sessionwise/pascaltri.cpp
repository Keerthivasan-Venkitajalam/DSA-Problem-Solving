//code to disp pascal triangle like pyramid
#include <iostream>
#include <iomanip>
using namespace std;
void printPascalsTriangle(int n) {
    for (int j=0; j<n; j++) {
        cout << setw(n-j);
        int num = 1;
        for (int i=0; i<=j; i++) {
            cout<<num<<" ";
            num=num*(j-i)/(i+1);
        }
        cout<<endl;
    }
}

int main() {
    int n;
    cout<<"Enter the number of rows for Pascal's Triangle: ";
    cin>>n;
    printPascalsTriangle(n);
    return 0;
}