import sys
input = sys.stdin.readline

lengths = [int(input()) for i in range(int(input()))]
line_ptr = 0

words = input().split()

length = 0
ans = ""
for word in words:
    done = False
    while not done:
        line_length = lengths[line_ptr % len(lengths)]
        left = line_length - length
        if len(word) > left:
            if length != 0:
                # Move to next line and try again
                line_ptr += 1
                length = 0
                ans += "\n"
            else:
                # Now that we're on a new line: split until done
                char_ptr = 0
                while len(word) - char_ptr >= line_length:
                    ans += word[char_ptr: char_ptr + line_length]
                    char_ptr += line_length
                    ans += "\n"
                    line_ptr += 1
                    line_length = lengths[line_ptr % len(lengths)]
                ans += word[char_ptr:]
                length += len(word) - char_ptr
                done = True
        else:
            if len(word) + 1 + length <= line_length:
                if length != 0:
                    ans += " "
                    length += 1
                ans += word
                length += len(word)
                if length == line_length:
                    line_ptr += 1
                    ans += "\n"
                    length = 0
                done = True
            elif len(word) == line_length:
                if length == 0:
                    ans += word + "\n"
                    line_ptr += 1
                    done = True
                else:
                    line_ptr += 1
                    length = 0
            else:
                ans += "\n"
                line_ptr += 1
                length = 0
print(ans, end="")