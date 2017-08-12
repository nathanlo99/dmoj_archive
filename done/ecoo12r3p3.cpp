#include <cstdio>
#include <cassert>

char c;

int expr() {
	char c = getchar();
	if (c == '(') {
		char op = getchar();
		getchar();
		int a = expr();
		getchar();
		int b = expr();
		getchar();
		switch(op) {
			case '+':
				return a + b;
			case '-':
				return a - b;
			case '*':
				return a * b;
			case 'q':
				return a / b;
			case 'r':
				return a % b;
			default:
				printf("Bad op: '%c'\n", op);
				return -1;
		}
	} else if (c >= '0' && c <= '9'){
		return c - '0';
	} else {
		printf("Bad number: '%c'\n", c);
		return -1;
	}
}

int main() {
	for (int i = 0; i < 10; i++) {
		int res = expr();
		while ((c = getchar()) != '\n' && (c != EOF));
		printf("%d\n", res);
	}
}