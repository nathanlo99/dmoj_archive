main(int A, char** C) {
    while(~(*(*C) = getchar()))
        if(*(*C) == ' ') A++;
    printf("%d", A);
}