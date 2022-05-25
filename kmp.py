# Zum Prüfen, ob Daten, die in main.py generiert und in statistics.xlsx gespeichert wurden, korrekt sind

import time


def find_kmp(t, p):
    n, m = len(t), len(p)

    if m == 0:
        return 0
    fail = compute_kmp_fail(p)
    j = 0
    k = 0

    while j < n:
        if t[j] == p[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return -1


def compute_kmp_fail(p):
    m = len(p)
    fail = [0] * m
    j = 1
    k = 0

    while j < m:
        if p[j] == p[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return fail


fText = open('file.txt')
fPattern = open('pattern.txt')

text = fText.read()
pattern = fPattern.read()
# text += pattern

text = text[:int(len(text)/2)] + pattern + text[int(len(text)/2):]

print("Text länge: " + str(len(text)))
print("Pattern länge: " + str(len(pattern)))

start = time.time_ns()

print(find_kmp(text, pattern))

end = time.time_ns()
print("Time: " + str(end - start) + " ns")
print("Time: " + str((end - start) / 1000000) + " ms")
