#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main() {
    //declare variables
    int a, b, c, d;
    //set d to 0 (used for comparing sum of divsors to value)
    d = 0;
    //take the first input which should give me the total number of input
    cin >> a;
    //this loop is used so i run through each number that is given
    for (int e = 0; e < a; e++) {
        //intial value that we are gonna use to compare with original number
        d = 0;
        //grab the next input which is our first number we will use to check
        cin >> b; 
        //loop c starts at 1 and if its less than our input then we loop through then add 1 to c
        for (c = 1; c < b; c++) {
            if (b%c == 0) {
            d = d + c;
            }
        }
        if (d == b) {
            cout << b << " is a perfect number." << endl;
        }
        else if (d > b) {
            cout << b << " is an abundant number." << endl;
        }
        else {
            cout << b << " is a deficient number." << endl;
        }
    }

    return 0;
    }