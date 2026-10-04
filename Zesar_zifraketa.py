mezua = input("Sartu deszifratu nahi duzun kriptograma: ")
for desplazamendua in range(1, 26):
    deszifratua = ""
    for karaktere in mezua:
        if karaktere.isalpha():
            offset = 65 if karaktere.isupper() else 97
            berria = chr((ord(karaktere) - offset + desplazamendua) % 26 + offset)
            deszifratua += berria
        else:
            deszifratua += karaktere
    print(f"Gakoa {desplazamendua}: {deszifratua}")
