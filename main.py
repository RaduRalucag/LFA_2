def inchide(S, A):
    inchideri = []
    for a in S:
        c = []
        for b in A:
            if a == b[0] and 'None' == b[1]:
                c.append(b[2])
        inchideri.append(c)
    for i in range(len(inchideri)):
        s = set(inchideri[i])
        for j in range(len(inchideri)):
            if i != j and S[j] in s:
                s.update(inchideri[j])
        inchideri[i] = list(s - {S[i]})
    return inchideri


def simbol(a, A, S):
    T = []
    for sim in a:
        for st in S:
            p = []
            for t in A:
                if st == t[0] and sim == t[1]:
                    p.append(t[2])
            T.append([st, sim, p])
    for i in range(int(n)):
        if M[i]:
            for j in T:
                if j[0] in M[i] and j[1] == T[i][1]:
                    T[i][2] = [*frozenset(T[i][2] + j[2])]
    return T


A = []
a = []
s = []
S = []
with open("date.in", 'r') as f:
    n = f.readline().strip()
    fin = f.readline().strip().split()
    for i in range(int(n)):
        A.append(f.readline().strip().split())
        if A[i][1] not in a and A[i][1] != 'None':
            a.append(A[i][1])
        S.append('q' + str(i))
ini = A[0][0]
alf = sorted(a)
M = inchide(S, A)
G = simbol(a, A, S)

for b in range(len(S)):
    if M[b] and len(G[b][0]) < 4:
        for i in range(len(G)):
            for j in range(len(M[b])):
                if G[i][2] == [M[b][j]]:
                    G[i][2] = sorted([G[b][0]] + M[b])
        G[b][0] = sorted([G[b][0]] + M[b])
    for i in range(len(G)):
        for j in range(len(G)):
            if str(G[i][0]) in G[j][0]:
                G[i][0] = G[j][0]
for i in range(len(G)):
    for j in range(len(G)):
        if str(G[i][0]) in G[j][2]:
            for a in range(len(G)):
                if G[a][0] == G[i][0]:
                    G[a][0] = G[j][2]
                if G[a][2] == [G[i][0]]:
                    G[a][2] = G[j][2]
            G[i][0] = G[j][2]
        elif str(G[j][2]) in G[i][2]:
            G[j][2] = G[i][2]
F = []
for e in G:
    if e not in F:
        if e[2]:
            F.append(e)
fin2 = []
for st in fin:
    for e in F:
        if st in e[0] and e[0] not in fin2:
            fin2.append(e[0])
        if st in e[2] and e[2] not in fin2:
            fin2.append(e[2])
        if ini in e[0]:
            ini = e[0]
print("Alfabet: ", *alf)
print("Stare initiala: ",*ini)
print("Tranzitiile sunt: ")
for e in F:
    print(*e[0],"-->",e[1],"-->",*e[2])
print("Stari finale: ")
for st in fin2:
    print(*st)