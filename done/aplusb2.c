#include "stdio.h"
#include "string.h"

int N;
char A[100001], B[100001], C[100005];

static void compute(char *A, char *B, const int lenA, const int lenB,
                    int flip, const int add) {
  int carry = 0, comp = 0, borrow = 0, maxL;
  char *Cp = C;

  if (lenA > lenB) {
    const int diff = lenA - lenB;
    for (int i = lenB; i >= 0; i--)
      B[i + diff] = B[i];
    for (int i = 0; i < diff; i++)
      B[i] = '0';
    maxL = lenA;
  } else {
    const int diff = lenB - lenA;
    for (int i = lenA; i >= 0; i--)
      A[i + diff] = A[i];
    for (int i = 0; i < diff; i++)
      A[i] = '0';
    maxL = lenB;
  }

  if (add) {
    for (int i = maxL - 1; i >= 0; i--) {
      const int value = A[i] - '0' + B[i] - '0' + carry;
      carry = value >= 10;
      *Cp++ = value % 10 + '0';
    }
    if (carry)
      *Cp++ = '1';
    if (flip)
      printf("-");
    Cp--;
    while (Cp >= C)
      printf("%c", *Cp--);

  } else {
    if (lenA > lenB)
      comp = 1;
    else if (lenB > lenA)
      comp = -1;
    else {
      for (int i = 0; i < lenA; i++) {
        if (A[i] == B[i])
          continue;
        comp = A[i] > B[i] ? 1 : -1;
        break;
      }
    }

    if (comp == 0) {
      printf("0");
      return;
    } else if (comp == -1) {
      char *temp = A;
      A = B;
      B = temp;
      flip = !flip;
    }

    for (int i = maxL - 1; i >= 0; i--) {
      const int value = A[i] - B[i] - borrow;
      borrow = value < 0;
      *Cp++ = (value + 10) % 10 + '0';
    }
    if (flip)
      printf("-");
    Cp--;
    if (*Cp != '0')
      printf("%c", *Cp);
    Cp--;
    while (Cp >= C)
      printf("%c", *Cp--);
  }
}

int main() {
  scanf("%d", &N);
  while (N--) {
    scanf("%s %s", A, B);
    int lenA = strlen(A);
    int lenB = strlen(B);
    if (A[0] == '-' && B[0] == '-')
      compute(A + 1, B + 1, lenA - 1, lenB - 1, 1, 1);
    else if (A[0] == '-')
      compute(B, A + 1, lenB, lenA - 1, 0, 0);
    else if (B[0] == '-')
      compute(A, B + 1, lenA, lenB - 1, 0, 0);
    else
      compute(A, B, lenA, lenB, 0, 1);
    printf("\n");
  }
  return 0;
}