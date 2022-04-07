s = input("Expr: ").split()
e = []
cl={"}","]",")"}
op={"{", "[", "("}
for x in s:
    if x in {"{", "[", "("}:
        e.append(x)
    else:
        if cl.index(x)==e.pop():
            continue
        else:
            flag=False
            break
print("y") if flag else print("n")