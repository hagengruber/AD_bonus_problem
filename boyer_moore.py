# Zum Prüfen, ob Daten, die in main.py generiert und in statistics.xlsx gespeichert wurden, korrekt sind

import time


def find_boyer_moore(t, p):
    n, m = len(t), len(p)
    if m == 0:
        return 0
    last = {}

    for k in range(m):
        last[p[k]] = k

    i = m - 1
    k = m - 1

    while i < n:
        if t[i] == p[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(t[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1


fText = open('file.txt')
fPattern = open('pattern.txt')

text = fText.read()
pattern = fPattern.read()
text = text[:int(len(text)/2)] + pattern + text[int(len(text)/2):]

print("Text länge: " + str(len(text)))
print("Pattern länge: " + str(len(pattern)))

start = time.time_ns()

print(find_boyer_moore(text, pattern))

end = time.time_ns()
print("Time: " + str(end - start) + " ns")
print("Time: " + str((end - start) / 1000000) + " ms")
