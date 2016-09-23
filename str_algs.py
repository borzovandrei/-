s = str(raw_input())

def rev(a):
    ra = ""
    for i in range(len(a) - 1, -1, -1):
         ra += a[i]
    return ra

print(rev(s))