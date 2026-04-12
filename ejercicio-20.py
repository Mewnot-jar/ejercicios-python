palabra_user = input("Ingresa una palabra: ").lower()
for letra in palabra_user:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        continue
    elif letra == 'z':
        break
    else:
        print(letra.upper())