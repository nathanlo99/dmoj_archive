main(int _, char** __) {
    while (getchar_unlocked()!='\n');
    while ((**__=getchar_unlocked())!=-1) putchar_unlocked(**__);
}