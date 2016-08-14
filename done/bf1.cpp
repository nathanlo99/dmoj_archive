#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
  int size;
  scanf("%d", &size);
  int list[size];

  for (int i = 0; i < size; i++) {
    int temp; // Declare a 'bucket' to put the number into
    scanf("%d", &temp);
    list[i] = temp;
  }

  sort(list, list + size);
  // Our list is sorted smallest to greatest

  for (int i = 0; i < size; i++) {
    printf("%d\n", list[i]);
  }

  return 0;
}
