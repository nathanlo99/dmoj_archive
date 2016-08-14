#include <stdio.h>
#define scan(x)                                                                \
  do {                                                                         \
    while ((x = getchar_unlocked()) < '0')                                     \
      ;                                                                        \
    for (x -= '0'; '0' <= (_ = getchar_unlocked());                            \
         x = (x << 3) + (x << 1) + _ - '0')                                    \
      ;                                                                        \
  } while (0)
char _;

int N;
int solutions[100] = {
    0,      0,      0,      0,      1,      4,      10,     20,     35,
    56,     84,     120,    165,    220,    286,    364,    455,    560,
    680,    816,    969,    1140,   1330,   1540,   1771,   2024,   2300,
    2600,   2925,   3276,   3654,   4060,   4495,   4960,   5456,   5984,
    6545,   7140,   7770,   8436,   9139,   9880,   10660,  11480,  12341,
    13244,  14190,  15180,  16215,  17296,  18424,  19600,  20825,  22100,
    23426,  24804,  26235,  27720,  29260,  30856,  32509,  34220,  35990,
    37820,  39711,  41664,  43680,  45760,  47905,  50116,  52394,  54740,
    57155,  59640,  62196,  64824,  67525,  70300,  73150,  76076,  79079,
    82160,  85320,  88560,  91881,  95284,  98770,  102340, 105995, 109736,
    113564, 117480, 121485, 125580, 129766, 134044, 138415, 142880, 147440,
    152096};

int main() {
  scan(N);
  printf("%d\n", solutions[N]);
  return 0;
}
