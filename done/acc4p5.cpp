bool f(int N) {
    for (int i = 2; i * i <= N; ++i)
    {
        if (N % i == 0)
            return 0;
    }
    return 1;
}