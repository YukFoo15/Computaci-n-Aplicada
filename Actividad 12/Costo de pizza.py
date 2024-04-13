import os; os.system("clear")

ing = {"T":1.50, "P":3.50, "C":3.74, "A":0.40, "Q":4}
base = 15
st = tot = des = 0

pedido = input("Especifique el tipo de ingredientes de su pizza: ").upper()
for i in pedido:
    if i in "TPCAQ":
        st = st + ing[i]
st = st + base

if st >= 20:
    des = (st * 0.05)
    tot = st - des

print(f"El subtotal es: {st}, con un descuento del {des}% (5%)")
print(f"El total es: {tot}")