int N, D, C, T;

main() {
  scanf("%d", &N);
  scanf("%d.%d", &D, &C);
  T = D * 100 + C;
  while (N--) {
    scanf("%d.%d", &D, &C);
    T -= 100 * D + C;
  }
  if (T < 0)
    printf("Fardin's broke");
  else
    printf("%d.%02d", T / 100, T % 100);
}
