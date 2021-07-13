#1032_명령프롬프트

import sys

num = int(sys.stdin.readline())
f_word = list(sys.stdin.readline())
f_len = len(f_word)

for i in range(num-1):
    o_words = list(sys.stdin.readline())
    for j in range(f_len):
        if f_word[j] != o_words[j]:
            f_word[j] = '?'

print(''.join(f_word))