#include <iostream>
#include <string>

using namespace std;

int upper, lower;
string s, n = "";

int main() {
	getline(cin, s);
	for (int i = 0; i < s.size(); i++) {
		char c = s[i];
		if ('A' <= c && c <= 'Z') {
			upper++;
		} else if ('a' <= c && c <= 'z') {
			lower++;
		}
	}
	if (lower == upper) {
		cout << s << endl;
	} else if (lower < upper) {
		// There are less lower than upper, convert to upper
		for (int i = 0; i < s.size(); i++) {
			char c = s[i];
			if ('A' <= c && c <= 'Z') {
				n += c;
			} else if ('a' <= c && c <= 'z') {
				n += (c - 32);
			} else {
				n += c;
			}
		}
		cout << n << endl;
	} else {
		// There are less lower than upper, convert to upper
		for (int i = 0; i < s.size(); i++) {
			char c = s[i];
			if ('A' <= c && c <= 'Z') {
				n += (c + 32);
			} else if ('a' <= c && c <= 'z') {
				n += c;
			} else {
				n += c;
			}
		}
		cout << n << endl;
	}
}