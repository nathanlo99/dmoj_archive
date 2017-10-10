#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> ranks, suits;
int res[10], a, b, a1, b1, a2, b2;

int eval(int a1, int b1, int a2, int b2, int a3, int b3, int a4, int b4, int a5, int b5) {
    ranks.clear(); suits.clear();
    ranks.push_back(a1); suits.push_back(b1);
    ranks.push_back(a2); suits.push_back(b2);
    ranks.push_back(a3); suits.push_back(b3);
    ranks.push_back(a4); suits.push_back(b4);
    ranks.push_back(a5); suits.push_back(b5);
    sort(ranks.begin(), ranks.end());
    sort(suits.begin(), suits.end());

    bool straight = 1, flush;
    flush = suits[0] == suits[4];
    for (int i = 0; i < 4; i++) {
        if (ranks[i + 1] - ranks[i] != 1) straight = 0;
    }

    if (straight && flush) return 1;
    if (ranks[0] == ranks[1] && ranks[1] == ranks[2] && ranks[2] == ranks[3])
        return 2;
    if (ranks[1] == ranks[2] && ranks[2] == ranks[3] && ranks[3] == ranks[4])
        return 2;
    if (ranks[0] == ranks[1] && ranks[1] == ranks[2] && ranks[3] == ranks[4])
        return 3;
    if (ranks[0] == ranks[1] && ranks[2] == ranks[3] && ranks[3] == ranks[4])
        return 3;
    if (flush) return 4;
    if (straight) return 5;
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            for (int k = j + 1; k < 5; k++) {
                if (ranks[i] == ranks[j] && ranks[j] == ranks[k]) return 6;
            }
        }
    }
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            for (int k = 0; k < 5; k++) {
                for (int l = k + 1; l < 5; l++) {
                    if (i != k && j != l && ranks[i] == ranks[k] && ranks[j] == ranks[l]) return 7;
                }
            }
        }
    }
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (ranks[i] == ranks[j]) return 8;
        }
    }
    return 9;
}

int main() {
    scanf("%d %d %d %d %d %d", &a, &b, &a1, &b1, &a2, &b2);
    for (int a3 = 0; a3 < a; a3++) {
        for (int b3 = 0; b3 < b; b3++) {
            if (a1 == a3 && b1 == b3) continue;
            if (a2 == a3 && b2 == b3) continue;
            for (int a4 = 0; a4 < a; a4++) {
                for (int b4 = 0; b4 < b; b4++) {
                    if (a1 == a4 && b1 == b4) continue;
                    if (a2 == a4 && b2 == b4) continue;
                    if (a3 == a4 && b3 == b4) continue;
                    for (int a5 = 0; a5 < a; a5++) {
                        for (int b5 = 0; b5 < b; b5++) {
                            if (a1 == a5 && b1 == b5) continue;
                            if (a2 == a5 && b2 == b5) continue;
                            if (a3 == a5 && b3 == b5) continue;
                            if (a4 == a5 && b4 == b5) continue;

                            res[eval(a1, b1, a2, b2, a3, b3, a4, b4, a5, b5)]++;
                        }
                    }
                }
            }
        }
    }

    for (int i = 1; i <= 9; i++) {
        printf("%d", res[i] / 6);
        if (i != 9) printf(" ");
    }
    printf("\n");
}