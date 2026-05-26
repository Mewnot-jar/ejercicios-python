texto_bruto = "bErSeRk, oNe pIeCe, VaGaBoNd, nArUtO, bLeAcH"
mangas_limpios = []

for manga in texto_bruto.split(","):
    mangas_limpios.append(manga.strip().title())
mangas_limpios.sort()
print(mangas_limpios)