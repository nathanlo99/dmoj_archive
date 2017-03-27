#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

std::vector<long long> indices[26];
long long n, start, end, start_down, end_down, num, ans, k, a, length;
char input[1000005], c;

long long get(long long index, long long num) {
    return (std::lower_bound(indices[num].begin(), indices[num].end(), index) - indices[num].begin()) - 1;
}

int main() {
    scanf("%lld %s\n", &n, input);
    length = strlen(input);
    for (int i = 0; i < 26; i++) indices[i].push_back(-1);
    for (int i = 0; i < length; i++) indices[input[i] - 'A'].push_back(i);
    scanf("%lld", &k);
    while (k--) {
        scanf("%lld %c", &a, &c);
        start = (((a >> 1) % length) * ((a - 1 + a % 2) % length)) % length;
        end = start + a;
        const long long start_down = start - start % length;
        const long long end_down = end - end % length;
        ans = get(end % length, c - 'A') - get(start % length, c - 'A');
        ans += ((end_down - start_down) / length) * (indices[c - 'A'].size() - 1);
        printf("%lld\n", ans);
    }
}