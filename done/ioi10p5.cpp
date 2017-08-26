#include <map>

char res;
std::map<char, int> cache;

void play() {
   for (int i = 1; i <= 50; i++) {
       res = faceup(i);
       if (cache.count(res) != 0) faceup(cache[res]);
       else cache[res] = i, faceup(i + 1);
   }
}