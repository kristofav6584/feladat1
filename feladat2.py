paros=0
paratlan=0

for i in range(5):
    szam = int(input("Kérem a számot:"))
    if szam %2 == 0:
        paros += 1
    else:
        paratlan += 1

print(f"Páros számokból {paros} volt.")
print(f"Páratlan számokból {paratlan} volt.")