#include <cstdio>
#include <vector>
#include <queue>

int indeg[100], outdeg[100], value[100]; // linearize the array
std::vector<int> in[100], out[100], stack;
std::queue<int> q;

constexpr int cell(char c, int d) {
    return (c - 'A') * 9 + d - 1;
}

constexpr int to_idx(int i, int j) {
    return i * 9 + j;
}

void get_input(int i, int j) {
    int idx = to_idx(i, j);
    char c;
    value[idx] = -1;
    c = getchar();
    if ('0' <= c && c <= '9') {
        // we're geting a number
        int d = (c - '0');
        for (;;) {
            c = getchar();
            if (c == ' ' || c == '\n' || c == '\r' || c == EOF) {
                break;
            } else {
                d = d * 10 + (c - '0');
            }
        }
        value[idx] = d;
    } else if ('A' <= c && c <= 'J') {
        char d = getchar(); // c||d forms the first cell
        int cell_ = cell(c, (d - '0'));
        in[idx].push_back(cell_);
        indeg[idx]++;
        out[cell_].push_back(idx);
        outdeg[cell_]++;
        // printf("Cell: %c%c\n", c, d);
        for (;;) {
            c = getchar();
            if (c != '+') break;
            c = getchar(); d = getchar();
            // printf("Cell: %c%c\n", c, d);
            cell_ = cell(c, (d - '0'));
            in[idx].push_back(cell_);
            indeg[idx]++;
            out[cell_].push_back(idx);
            outdeg[cell_]++;
        }
    } else {
        printf("Bad char: '%c'\n", c);
    }
}

int main() {
    // get input
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 9; j++) {
            get_input(i, j);
        }
    }

    // find topo sort, define undefines and stuff
    // for (int i = 0; i < 90; i++) {
    //     if (in[i].size() == 0 && value[i] == -1) continue;
    //     printf("Cell %d: val: %d\n", i, value[i]);
    //     for (int next: in[i]) printf("%d\n", next);
    // }

    for (int i = 0; i < 90; i++) {
        if (outdeg[i] == 0) q.push(i);
    }

    while (!q.empty()) {
        int top = q.front(); q.pop();
        stack.push_back(top);
        for (int dep: in[top]) {
            outdeg[dep]--;
            if (outdeg[dep] == 0) q.push(dep);
        }
    }

    while (!q.empty()) {
        int top = q.front(); q.pop();
        value[top] = -1;
    }

    for (int i = stack.size() - 1; i >= 0; i--) {
        // you can evalute i now
        int thing = stack[i];

        // the value is already in the array
        if (in[thing].size() == 0) continue;

        // printf("Evaluating %d\n", thing);
        int ans = 0;
        for (int j : in[thing]) {
            if (value[j] == -1) {
                // printf("%d is undefined, breaking\n", j);
                value[thing] = -2;
                break;
            } else {
                ans += value[j];
            }
        }
        if (value[thing] != -2) value[thing] = ans;
        // printf("Got %d\n", value[thing]);
    }

    // print everything
    for (int i = 0; i < 90; i++) {
        if (value[i] < 0) printf("* ");
        else printf("%d ", value[i]);
        if (i % 9 == 8) printf("\n");
    }
}