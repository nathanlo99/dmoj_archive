int n; unsigned long long s, a;
main(){scanf("%d",&n);while(n-->0)scanf("%llu",&a),s+=-a;s?putchar('-'):0;printf("%llu\n",s);}