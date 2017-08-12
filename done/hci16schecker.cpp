#include <string>
#include <set>
#include <iostream>
#include <sstream>

int n;
std::string input, token;
std::set<std::string> dict;

int main() {
	std::cin >> n;
	for (int i = 0; i < n; i++) {
		std::cin >> input;
		dict.insert(input);
	}
	std::getline(std::cin, input);
	std::getline(std::cin, input);
	std::stringstream ss(input);
	while (ss >> token) {
		if (dict.count(token) == 0) {
			std::cout << "Incorrect" << std::endl;
			return 0;
		}
	}
	if (n != 8)
	    std::cout << "Correct" << std::endl;
	else
	    std::cout << "Incorrect" << std::endl;
}