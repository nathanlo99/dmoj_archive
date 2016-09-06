#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    if(n!= 1 && n!= 4)
        cout << " * * * " << endl;

    bool t1 = (n == 0 || n == 4 || n == 5 || n == 6 || n == 8 || n == 9);
    bool t2 = (n != 5 && n != 6);
    for (int i = 0; i < 3; i++)
        cout << (t1?"*":" ") << "     " << (t2?"*":" ") << endl;
    
    if(n == 2 || n == 3 || n == 4 || n == 5 || n == 6 || n == 8 || n == 9)
        cout << " * * * " << endl;
    else
        cout << endl;
    
    bool b1 = (n == 0 || n == 2 || n == 6 || n == 8);
    bool b2 = (n != 2);
    
    for (int i = 0; i < 3; i++)
        cout << (b1?"*":" ") << "     " << (b2?"*":" ") << endl;
    
    if(n != 1 && n != 4 && n != 7)
        cout << " * * * " << endl;
    else
        cout << endl;
    
    return 0;
}