#include "stdio.h"
#include "string.h"

static char C[1000005];

void compute(char* A, char* B, const int flip, const int add) {
    const int lenA = strlen(A);
    const int lenB = strlen(B);
    const int maxL = lenA > lenB ? lenA : lenB;
    if (lenA > lenB) {
        const int diff = lenA - lenB;
        for (int i = lenB; i >= 0; i--) B[i + diff] = B[i];
        for (int i = 0; i < diff; i++) B[i] = '0';
    } else {
        const int diff = lenB - lenA;
        for (int i = lenA; i >= 0; i--) A[i + diff] = A[i];
        for (int i = 0; i < diff; i++) A[i] = '0';
    }

    if (add) {
        int carry = 0;
        char* Cp = C;
        int Cindex = 0;
        for (int i = maxL - 1; i >= 0; i--) {
            const int value = A[i] - '0' + B[i] - '0' + carry;
            carry = value >= 10;
            *Cp++ = value % 10 + '0';
        }
        if (carry) *Cp++ = '1';
        if (flip) printf("-");
        Cp--;
        while (Cp >= C) printf("%c", *Cp--);

    } else {
        int comp = 0;
        char ac, bc;

        if (lenA > lenB) comp = 1;
        else if (lenB > lenA) comp = -1;
        else {
            for (int i = 0; i < lenA; i++) {
                ac = A[i];
                bc = B[i];
                if (ac == bc) continue;
                comp = ac > bc ? 1 : -1;
                break;
            }
        }

        if (comp == 0) {
            printf("0");
            return;
        } else if (comp == -1) {
            compute(B, A, !flip, 0);
            return;
        }

        int borrow = 0;
        int Cindex = 0;
        char* Cp = C;
        for (int i = maxL - 1; i >= 0; i--) {
            const int value = A[i] - B[i] - borrow;
            borrow = value < 0;
            *Cp++ = (value + 10) % 10 + '0';
        }
        if (flip) printf("-");
        Cp--;
        if (*Cp != '0') printf("%c", *Cp);
        Cp--;
        while (Cp >= C) printf("%c", *Cp--);
    }
}

int main() {
    int N;
    char A[100001], B[100001];
    scanf("%d", &N);
    while (N--) {
        scanf("%s %s", A, B);
        if (A[0] == '-' && B[0] == '-') compute(A + 1, B + 1, 1, 1);
        else if (A[0] == '-') compute(B, A + 1, 0, 0);
        else if (B[0] == '-') compute(A, B + 1, 0, 0);
        else compute(A, B, 0, 1);
        printf("\n");
    }
    return 0;
}
