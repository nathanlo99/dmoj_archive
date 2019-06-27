#include <string>
#include <sstream>

std::string f(int N) {
    std::stringstream ss;
    ss << N;
    return ss.str();
}