#include <stdio.h>
#include <string>
#include <iostream>

std::string ss[22] = {
    "1", "1", "2", "6", "24", "120", "720", "5040", "40320", "362880",
    "3628800", "39916800", "479001600", "6227020800", "87178291200", 
    "1307674368000", "20922789888000", "355687428096000", "6402373705728000",
    "121645100408832000", "2432902008176640000"
};

int main() {
    std::string s;
    std::getline(std::cin, s);
    for (int i = 0, n; i < s.length(); i++) {
        if (!s[i]) break;
        if (s[i] == '!' && i > 0 && s[i - 1] >= '0' && s[i - 1] <= '9') {
            n = 0;
            for (int j = i - 2; j < i; j++) {
                if (s[j] >= '0' && s[j] <= '9') {
                    n = 10 * n + s[j] - '0';
                }
            }
            printf("%s\n", ss[n].c_str());
            return 0;
        }
    }
    printf("-1\n");
}