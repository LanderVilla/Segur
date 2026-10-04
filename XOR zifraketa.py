def xor_eragiketa(datuak_bytes, gakoa_bytes):
    """XOR eragiketa aplikatzen du, gakoa behar adina aldiz errepikatuz."""
    emaitza = bytearray()
    for i in range(len(datuak_bytes)):
        gako_byte = gakoa_bytes[i % len(gakoa_bytes)]
        xor_byte = datuak_bytes[i] ^ gako_byte
        emaitza.append(xor_byte)
    return bytes(emaitza)

def main():
    print("=== XOR FLUXU-ZIFRAKETA ===")
    mezua = input("Sartu zifratu nahi duzun mezua: ")
    gakoa = input("Sartu erabili nahi duzun gakoa: ")

    if not mezua or not gakoa:
        print("Errorea: Mezua eta gakoa ezin dira hutsik egon.")
        return
    mezua_bytes = mezua.encode('utf-8')
    gakoa_bytes = gakoa.encode('utf-8')
    kriptograma = xor_eragiketa(mezua_bytes, gakoa_bytes)
    print("\n--- ZIFRATZEA ---")
    print(f"Kriptograma (Hexadezimalean): {kriptograma.hex()}")
    berreskuratua_bytes = xor_eragiketa(kriptograma, gakoa_bytes)
    berreskuratua = berreskuratua_bytes.decode('utf-8')
    print("\n--- DESZIFRATZEA ---")
    print(f"Berreskuratutako mezua: {berreskuratua}")
    if mezua == berreskuratua:
        print("\n[OK] Deszifratzeak jatorrizko mezua berreskuratu du.")
    else:
        print("\n[ERROREA] Datuak galdu edo aldatu dira prozesuan.")

if __name__ == "__main__":
    main()
