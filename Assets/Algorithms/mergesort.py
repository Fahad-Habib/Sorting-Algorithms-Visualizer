from random import shuffle


def merge(a, b):
    c = []
    n = len(a) + len(b)
    while len(c) != n:
        if len(a) == 0 and len(b) != 0:
            c += b
        elif len(b) == 0 and len(a) != 0:
            c += a
        else:
            if b[0] < a[0]:
                c.append(b[0])
                b.remove(b[0])
            else:
                c.append(a[0])
                a.remove(a[0])
    return c


def mergeSort(A):
    if len(A) == 1:
        return A
    else:
        a = A[:len(A) // 2]
        b = A[len(A) // 2:]
        return merge(mergeSort(a), mergeSort(b))


link = [x for x in range(20)]
shuffle(link)
print(link)
print(mergeSort(link))
