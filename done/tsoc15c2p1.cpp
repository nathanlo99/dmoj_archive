#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(){
    int N;
    cin >> N;
    int nums[N];
    for(int i = 0; i < N; i++){
        cin >> nums[i];
    }
    int pt = nums[0];
    string res = "";
    string alpha = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    while(nums[pt]){
        res += alpha[nums[pt]];
        pt += nums[pt+1] + 1;
    }
    cout << res << endl;
	return 0;
}