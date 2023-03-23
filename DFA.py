f = open("automat.txt","r")
l=[[x for x in linie.split()] for linie in f.readlines()]
f.close()
stare_f=l[len(l)-1]
l.pop()
print(l)
cuvant = input("Cuvantul citit este: ")
transitions = []
drum=[]
for i in cuvant:
    transitions.append(int(i))
print("tranzitiile sunt: ",transitions)
stare_curenta=l[0][0]
print("starea curenta este: ",stare_curenta)
k=0
drum.append(stare_curenta)
while len(transitions)>0:
    ok=0
    if True:
        for i in l:
            if (stare_curenta==i[0] and transitions[0]==int(i[1])):
                stare_curenta=i[2]
                print(stare_curenta)
                transitions.pop(0)
                ok = 1
                drum.append(stare_curenta)
                break
    if ok == 0:
        print("cuvantul nu este acceptat")
        k=1
        break

if stare_curenta in stare_f and k==0:
    print("cuvantul este acceptat")
    for j in range(len(drum)-1):
        print(drum[j],end=" "+ "->" + " ")
    print(drum[len(drum)-1])
