bool f(int N) {
    for (int i = 0; i <= 1000; ++i) 
        if (i * i == N)
            return 1;
    return 0;
}