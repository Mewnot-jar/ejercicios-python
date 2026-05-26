receta_base = {"fideos_gr": 100, "carne_gr": 50, "salsa_ml": 80}
lista_de_compras = {}

for ingrediente, gr in receta_base.items():
    lista_de_compras[ingrediente] = gr * 3
print(lista_de_compras)