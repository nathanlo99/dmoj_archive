#include <stdio.h>

int main(int argc, char const *argv[])
{
    int t, s, h;
    scanf("%d\n%d\n%d", &t, &s, &h);
    for (int i = 0; i < t; ++i)
    {
        putchar('*');
        for (int j = 0; j < s; ++j)
        {
            putchar(' ');
        }
        putchar('*');
        for (int j = 0; j < s; ++j)
        {
            putchar(' ');
        }
        putchar('*');
        for (int j = 0; j < s; ++j)
        {
            putchar(' ');
        }
        printf("\n");
    }
    for (int i = 0; i < s*2+3; ++i)
    {
        putchar('*');
    }
    printf("\n");
    for (int i = 0; i < h; ++i)
    {
        for (int j = 0; j < s+1; j++)
        {
            printf(" ");
        }
        printf("*\n");
    }
    return 0;
}