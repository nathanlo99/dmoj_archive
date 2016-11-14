#define putz(...) puts(#__VA_ARGS__)
int main() { putz(Hello, World!); }