from IPython import get_ipython

#
# ACHTUNG: Script muss mit ipython aufgerufen werden
#

ipython = get_ipython()

f = open('file.txt')
bibel_text = f.read()
bibel = ""


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
            k = fail[k-1]
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
            k = fail[k-1]
        else:
            j += 1

    return fail


def do_brute_force(p):
    if p == 0:
        find_brute(bibel, 'Moin')
    else:
        print(find_brute(bibel, 'Moin'))


def do_boyer_moore(p):
    if p == 0:
        find_boyer_moore(bibel, 'Moin')
    else:
        print(find_boyer_moore(bibel, 'Moin'))


def do_kmp(p):
    if p == 0:
        find_kmp(bibel, 'Moin')
    else:
        print(find_kmp(bibel, 'Moin'))


for a in range(5, 100):

    bibel = bibel_text[:a] + "Moin"
    print(str(len(bibel)))

    # print("Länge " + str(i))
    # print(bibel)
    print("Brute Force: ", end='')
    ipython.run_line_magic("timeit",  "do_brute_force(0)")

    print("Boyer Moore: ", end='')
    ipython.run_line_magic("timeit",  "do_boyer_moore(0)")

    print("KMP: ", end='')
    ipython.run_line_magic("timeit",  "do_kmp(0)")
