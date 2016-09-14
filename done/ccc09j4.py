n = int(input())
words = "WELCOME TO CCC GOOD LUCK TODAY".split()
lengths = [len(word) for word in words]
wp = 0
while wp < len(words):
    line_words = []
    line_length = n
    while line_length - lengths[wp] >= 0:
        line_length -= lengths[wp]
        line_words.append(words[wp])
        if line_length > 1:
            line_length -= 1
        wp += 1
        if wp >= len(words):
            break
    spaces = n - sum(len(word) for word in line_words)
    if len(line_words) > 1:
        base_spaces = spaces // (len(line_words) - 1)
        extra_spaces = spaces % (len(line_words) - 1)
        spaces_string = ["." * base_spaces for i in range(len(line_words) - 1)]
        spaces_string.append("")
        for i in range(extra_spaces):
            spaces_string[i] += "."
        lwp = 0
        line = ""
        for word, space in zip(line_words, spaces_string):
            line += word + space
        print(line)
    else:
        print(line_words[0] + "." * (n - len(line_words[0])))