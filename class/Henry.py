def unic(wsaeds):
    fd = []
    for r in wsaeds:
        if fd.count(r)==0:
            fd.append(r)
    return fd
gh = [1, 1, 1, 1, 1, 3, 43, 43, 4, 3, 4, 9, 6, 7, 9, 7, 9, 5, 5, 5, 78, 9, 9, 9, 78, 6, 66, 6]
print(set(gh))