int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int m;
        scanf("%d", &m);
        if (m < 3) printf("-1\n");
        else printf("(2,3)\n");
    }
}