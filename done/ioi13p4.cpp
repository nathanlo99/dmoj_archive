#include "cave.h"

int locked[5002], switches[5002], door[5002];

void exploreCave(int N) {
	for (int i = 0; i < N; i++) {
	    int res = tryCombination(switches);
        int is_open = !(res > i || res == -1);
        int lo = 0, hi = N - 1;
        while (lo != hi) {
            int mid = (lo + hi) / 2;
            for (int j = lo; j <= mid; j++) if (!locked[j]) switches[j] ^= 1;
            res = tryCombination(switches);
            for (int j = lo; j <= mid; j++) if (!locked[j]) switches[j] ^= 1;
            if ((res > i || res == -1) == is_open) hi = mid;
            else lo = mid + 1;
        }
        door[lo] = i;
        switches[lo] = is_open;
        locked[lo] = 1;
	}
    answer(switches, door);
}