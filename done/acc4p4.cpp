#include <sstream>

std::string f(int N) { 
    long long m{N};
    std::stringstream ss;
    ss << m * m;
    return ss.str();
}