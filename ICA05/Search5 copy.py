from timeit import Timer


def fillList(l, n):
    l.append(range(1, n + 1))
l = []
fillList(l, 100)

def search_fast(l):
    for item in l:
        if item == 10:
            return True
    return False

def search_slow(l):
    return_value = False
    for item in l:
        if item == 10: 
            return_value = True
    return return_value

t = Timer(lambda: 10 in l)
print(t.timeit())
t = Timer(lambda: search_fast(l))
print t.timeit()
t = Timer(lambda: search_slow(l))
print t.timeit()