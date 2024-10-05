ara = "fsd efedsdfsed fsefsefsdfsefsfse fsefsefsefse fesefaefase fefwewfefeawfs"
def Fred(werqw):
    wa = werqw.split(" ")
    revers_wa = []
    l = len(wa) - 1
    while l >= 0:
        revers_wa.append(wa[l])
        l = l - 1
    return revers_wa
print(Fred(ara))