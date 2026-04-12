num_user = int(input("Ingresa un numero y veras su tabla del 1 al 10: "))

for i in range(10):
    print(f"{num_user} x {i+1} = {num_user * (i+1)}")