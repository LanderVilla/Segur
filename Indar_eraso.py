import sys
from collections import Counter
import os
#(EZ DU ONDO FUNTSIONATZEN)
LETRAS_FRECUENTES_MAYUS = 'AIRETOUNKLZSDGBMPHXFJCYVWQ'
LETRAS_FRECUENTES_MINUS = 'airetounklzsdgbmphxfjcyvwq'
EUSKARAZKO_MAIZTASUNA_CASESENSITIVE = LETRAS_FRECUENTES_MAYUS + LETRAS_FRECUENTES_MINUS

def garbitu_pantaila():
    """Terminaleko pantaila garbitzen du."""
    os.system('cls' if os.name == 'nt' else 'clear')

def hasierako_gakoa_sortu(maiztasun_zifratua):
    """Hasierako ordezkapen-gakoa sortzen du, kasua bereiziz."""
    gakoa = {}
    luzera_motzena = min(len(maiztasun_zifratua), len(EUSKARAZKO_MAIZTASUNA_CASESENSITIVE))
    for i in range(luzera_motzena):
        letra_zifratua = maiztasun_zifratua[i]
        letra_ordekoa = EUSKARAZKO_MAIZTASUNA_CASESENSITIVE[i]
        gakoa[letra_zifratua] = letra_ordekoa
    return gakoa

def gakoarekin_deszifratu(testu_zifratua, gakoa):
    """Testua deszifratzen du, karaktere bakoitza zuzenean bilatuz gakoan."""
    testu_deszifratua = ""
    for karakterea in testu_zifratua:
        if karakterea in gakoa:
            testu_deszifratua += gakoa[karakterea]
        else:
            testu_deszifratua += karakterea
    return testu_deszifratua

def nagusia():
    """Aplikazioaren funtzio nagusia."""
    garbitu_pantaila()
    print("=== TESTU ZIFRATUAREN MAIZTASUN ANALISIA (Kasua Bereiziz) ===")
    print("Itsatsi hemen deszifratu nahi duzun kriptograma.")
    print("Amaitzeko, idatzi 'AMAIERA' lerro berri batean eta sakatu Enter:\n")
    
    lerroak = []
    while True:
        try:
            lerroa = input()
            if lerroa.strip().upper() == 'AMAIERA':
                break
            lerroak.append(lerroa)
        except EOFError:
            break
            
    testu_zifratua = "\n".join(lerroak)
    
    if not testu_zifratua.strip():
        print("Ez da testurik sartu. Programa amaitzen...")
        sys.exit(1)

    garbitu_pantaila()
    print("--- Testu Zifratuaren Maiztasun Analisia ---")
    
    # Testu zifratuko letrak bakarrik hartzen ditugu kontuan
    zenbaketa = Counter(c for c in testu_zifratua if c.isalpha())
    
    if not zenbaketa:
        print("Ez da letra zifraturik aurkitu testuan.")
        sys.exit(1)
        
    for letra, kopurua in zenbaketa.most_common():
        print(f"  Karakterea '{letra}': {kopurua} aldiz")
    
    print("\nSakatu ENTER jarraitzeko...")
    input()
    
    maiztasun_zifratua = "".join(letra for letra, _ in zenbaketa.most_common())
    gakoa = hasierako_gakoa_sortu(maiztasun_zifratua)

    while True:
        garbitu_pantaila()
        testu_deszifratua = gakoarekin_deszifratu(testu_zifratua, gakoa)

        print("--- Uneko Ordezkapen Gakoa ---")
        gako_ordenatua = sorted(gakoa.items())
        for zifratua, ordekoa in gako_ordenatua:
            print(f"  '{zifratua}' -> '{ordekoa}'")
        
        print("\n--- Deszifratutako Testua ---")
        print(testu_deszifratua)
        print("\n" + "="*40)

        print("\nKomandoak:")
        print("  - 'aldatu [zif] [ord]' (KASUA BEREIZTEN DU, adib: aldatu v e)")
        print("  - 'gorde [fitxategia.txt]'")
        print("  - 'irten'")
        
        komandoa_sartu = input("> ").split()

        if not komandoa_sartu:
            continue
        
        komando = komandoa_sartu[0].lower()

        if komando == 'irten':
            break
        elif komando == 'aldatu' and len(komandoa_sartu) == 3:
            zifratua, ordekoa = komandoa_sartu[1], komandoa_sartu[2]
            if zifratua in gakoa:
                gakoa[zifratua] = ordekoa
            else:
                print(f"'{zifratua}' karakterea ez dago testu zifratuan.")
                input("Sakatu Enter jarraitzeko...")
        
        elif komando == 'gorde' and len(komandoa_sartu) == 2:
            gorde_izena = komandoa_sartu[1]
            try:
                with open(gorde_izena, 'w', encoding='utf-8') as f:
                    f.write("--- Erabilitako Ordezkapen Gakoa ---\n")
                    gako_ordenatua = sorted(gakoa.items())
                    for zif, ord in gako_ordenatua:
                        f.write(f"  '{zif}' -> '{ord}'\n")
                    
                    f.write("\n" + "="*40 + "\n\n")
                    f.write("--- Deszifratutako Testua ---\n")
                    f.write(testu_deszifratua)
                    
                print(f"\n[INFO] Gakoa eta testua '{gorde_izena}' fitxategian gorde dira.")
            except Exception as e:
                print(f"\n[ERROREA] Ezin izan da fitxategia gorde: {e}")
            input("Sakatu Enter jarraitzeko...")
            
        else:
            print("Komando ezezaguna edo formatu okerra.")
            input("Sakatu Enter jarraitzeko...")

    print("\nDeskodetzea amaituta!")

if __name__ == "__main__":
    nagusia()
