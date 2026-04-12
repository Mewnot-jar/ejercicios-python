frase = input("Ingresa una frase: ").lower()
contador = 0

for letra in frase:
    if letra == "a":
        contador +=1

print(f"La letra 'a' aparece {contador} veces en la frase")