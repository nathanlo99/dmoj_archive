bool init = false;
std::vector<int> facts(1000000);

std::vector<int> f(int N) {
    if (!init) {
        facts[0] = 1;
        for (int i = 1; i < 1000000; ++i)
            facts[i] = ((long long)facts[i - 1] * (i + 1)) % 998244353LL;
        init = 1;
    }
    std::vector<int> res(facts.begin(), facts.begin() + N);
    return res;
}