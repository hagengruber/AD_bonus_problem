from IPython import get_ipython
import sys
from tqdm import tqdm

#
# ACHTUNG: Script muss mit ipython aufgerufen werden
#

ipython = get_ipython()


class Logger:
    stdout = sys.stdout
    messages = []

    def start(self):
        sys.stdout = self

    def stop(self):
        sys.stdout = self.stdout

    def write(self, text):
        self.messages.append(text)


f = open('file.txt')
bibel_text = f.read()
bibel = ""
p = open('pattern.txt')
pattern = p.read()
# pattern = "Moin"


def find_brute(t, p):
    n, m = len(t), len(p)

    for i in range(n - m + 1):
        k = 0
        while k < m and t[i + k] == p[k]:
            k += 1
        if k == m:
            return i
    return -1


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


def do_brute_force(p):
    if p == 0:
        find_brute(bibel, pattern)
    else:
        print(find_brute(bibel, pattern))


def do_boyer_moore(p):
    if p == 0:
        print(find_boyer_moore(bibel, pattern))
    else:
        print(find_boyer_moore(bibel, pattern))


def do_kmp(p):
    if p == 0:
        find_kmp(bibel, pattern)
    else:
        print(find_kmp(bibel, pattern))


zeichen = ""
al1 = "Brute Force"
al2 = "Boyer Moore"
al3 = "KMP"

log = Logger()

start = 5
end = len(bibel_text)
print((end - start) / 191)
sprung = int((end - start) / 191)
output = tqdm(total=int((end - start) / sprung))

for a in range(start, end, int((end - start) / 191)):

    # os.system("cls")
    # print("Pattern: " + pattern)
    a_first = int(a/2)
    a_last = a - a_first
    bibel = bibel_text[:a_last] + pattern + bibel_text[a_last:a]

    # bibel = bibel_text + "Moin"

    zeichen += ";" + str(len(bibel)) + " Zeichen"

    fz = open("fz.txt", "w")
    fz.write(zeichen)
    fz.close()

    log.start()
    ipython.run_line_magic("timeit", "do_brute_force(0)")
    log.stop()

    m = log.messages
    time = float(log.messages[len(m) - 2].split(' ')[0])
    type = log.messages[len(m) - 2].split(' ')[1]

    # print("Eigentliche Zeit: " + str(time) + " " + type)

    if type == "us":
        time /= 1000
    elif type == "s":
        time *= 1000

    # print("Konvertierte Zeit: " + str(time) + " ms")

    al1 += ";" + str(time).replace('.', ',')

    log.start()
    ipython.run_line_magic("timeit", "do_boyer_moore(0)")
    log.stop()

    m = log.messages
    time = float(log.messages[len(m) - 2].split(' ')[0])
    type = log.messages[len(m) - 2].split(' ')[1]

    # print("Eigentliche Zeit: " + str(time) + " " + type)

    if type == "us":
        time /= 1000
    elif type == "s":
        time *= 1000

    # print("Konvertierte Zeit: " + str(time) + " ms")

    al2 += ";" + str(time).replace('.', ',')

    log.start()
    ipython.run_line_magic("timeit", "do_kmp(0)")
    log.stop()

    m = log.messages
    time = float(log.messages[len(m) - 2].split(' ')[0])
    type = log.messages[len(m) - 2].split(' ')[1]

    # print("Eigentliche Zeit: " + str(time) + " " + type)

    if type == "us":
        time /= 1000
    elif type == "s":
        time *= 1000

    # print("Konvertierte Zeit: " + str(time) + " ms")

    al3 += ";" + str(time).replace('.', ',')

    f1 = open("a1.txt", "w")
    f1.write(al1)
    f1.close()

    f2 = open("a2.txt", "w")
    f2.write(al2)
    f2.close()

    f3 = open("a3.txt", "w")
    f3.write(al3)
    f3.close()

    output.update()

f = open("test.csv", "w")
f.write(zeichen + "\n")
f.write(al1 + "\n")
f.write(al2 + "\n")
f.write(al3 + "\n")

f.close()
