# Zum Prüfen, ob Daten, die in main.py generiert und in statistics.xlsx gespeichert wurden, korrekt sind

import time


def find_brute(t, p):
    n, m = len(t), len(p)

    for i in range(n - m + 1):
        k = 0
        while k < m and t[i + k] == p[k]:
            k += 1
        if k == m:
            return i
    return -1


fText = open('file.txt')
fPattern = open('pattern.txt')

text = fText.read()
pattern = fPattern.read()
text = text[:int(len(text)/2)] + pattern + text[int(len(text)/2):]

print("Text länge: " + str(len(text)))
print("Pattern länge: " + str(len(pattern)))

start = time.time_ns()

print(find_brute(text, pattern))

end = time.time_ns()
print("Time: " + str(end - start) + " ns")
print("Time: " + str((end - start) / 1000000) + " ms")
