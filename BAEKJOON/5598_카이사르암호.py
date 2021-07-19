#5598_카이사르암호

import sys

caesar_word = sys.stdin.readline().rstrip()

real_word = ''
# A = 65, Z = 90
for alpha in caesar_word:
    if 91 >= ord(alpha) >= 68:
        real_word += chr(ord(alpha) - 3)
    else:
        real_word += chr(ord(alpha) + 26 -3) 
print(real_word)