import random

# Alla kombinationer som finns i Yatzy
tillgangliga_kombinationer = ["Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor", "Par", "Två par", "Tretal", "Fyrtal", "Kåk", "Liten stege", "Stor stege", "Chans", "Yatzy"]

# Lista för poäng
poang_lista = {}


# Retunerar ett tal mellan 1 och 6
def kasta_tarning():
    return random.randint(1, 6)


# Skapa en lista med 5 tärningar
def skapa_hand():
    hand = []
    for _ in range(5):
        hand.append(kasta_tarning())
    return hand


# Visar tärningarna för spelaren
def skriv_ut_hand(hand):
    print("Dina tärningar: ", hand)


# Kasta om tärningar
def omkastningar(hand):
    omkastningar_kvar = 2

    while omkastningar_kvar > 0:
        svar = input("\nVill du kasta om några tärningar? (ja/nej): ")

        if svar.lower() == "nej":
            break
        

        elif svar.lower() == "ja":
            val = input("Vilka tärningar vill du kasta om? (ange nummer 1-5, separerade med mellanslag): ")
            valda = val.split()

            if not all(nummer.isdigit() for nummer in valda):
                print("\nDu behöver skriva ett tal mellan 1 och 5. Försök igen!")
                continue
            if not all(1<= int(nummer)<= 5 for nummer in valda):
                 print("\nDu behöver skriva ett tal mellan 1 och 5. Försök igen!")
                 continue
            if len(set(valda)) != len(valda):
                print("\nDu kan inte skriva samma tärning två gånger. Försök igen!")
                continue


            for nummer in valda:
                index = int(nummer) - 1
                hand[index] = kasta_tarning()

            skriv_ut_hand(hand)
            if(omkastningar_kvar > 1):
                visa_mojliga_kombinationer(hand, tillgangliga_kombinationer)
            omkastningar_kvar = omkastningar_kvar - 1

        else:
            print("Du måste skriva 'ja' eller 'nej'!")
    
    return hand

# Räkna hur många av varje nummer som finns

def skapa_antal_lista(hand):
    antal_lista = [0, 0, 0, 0, 0, 0]
    for tarning in hand:
        index = tarning -1
        antal_lista[index] = antal_lista[index] + 1

    return antal_lista


def hitta_kombinationer(antal_lista, hand):
    mojliga = []

# Ettor-Sexor

    if antal_lista[0] > 0:
        mojliga.append("Ettor")
    if antal_lista[1] > 0:
        mojliga.append("Tvåor")
    if antal_lista[2] > 0:
        mojliga.append("Treor")
    if antal_lista[3] > 0:
        mojliga.append("Fyror")
    if antal_lista[4] > 0:
        mojliga.append("Femmor")
    if antal_lista[5] > 0:
        mojliga.append("Sexor")

# Par

    for antal in antal_lista:
        if antal >= 2:
            mojliga.append("Par")
            break

# Två par

    antal_par = 0 
    for antal in antal_lista:
        if antal >=2:
            antal_par = antal_par + 1
    if antal_par >= 2:
        mojliga.append("Två par")

# Tretal

    for antal in antal_lista:
        if antal >= 3:
            mojliga.append("Tretal")
            break

# Fyrtal

    for antal in antal_lista:
        if antal >= 4:
            mojliga.append("Fyrtal")
            break

# Kåk

    finns_tretal = False
    finns_par = False
    for antal in antal_lista:
        if antal == 3:
            finns_tretal = True
        if antal == 2:
            finns_par = True
    if finns_tretal and finns_par:
        mojliga.append("Kåk")

# Liten stege

    if antal_lista == [1, 1, 1, 1, 1, 0]:
        mojliga.append("Liten stege")

# Stor stege

    if antal_lista == [0, 1, 1, 1, 1, 1]:
        mojliga.append("Stor stege")

# Chans
    mojliga.append("Chans")

# Yatzy

    for antal in antal_lista:
        if antal == 5:
            mojliga.append("Yatzy")
            break

    return mojliga


# Kolla om de möjliga kombinationerna finns tillgängliga

def filtrera_mojliga(mojliga, tillgangliga):
    giltiga = []
    for komb in mojliga:
        if komb in tillgangliga:
            giltiga.append(komb)
    return giltiga


# Visa möjliga kombinationer

def visa_mojliga_kombinationer(hand, tillgangliga):
    antal_lista = skapa_antal_lista(hand)
    mojliga = hitta_kombinationer(antal_lista, hand)
    giltiga = filtrera_mojliga(mojliga, tillgangliga)
    
    print("\nMöjliga kombinationer med denna hand: ")
    if len(giltiga) == 0:
        print("Inga möjliga kombinationer just nu.")
    else:
        for komb in giltiga:
            print(" -", komb)


# Om ingen finns

def stryk_kombination(tillgangliga):
    print("\nIngen möjlig kombination finns. ")
    print("Du måste stryka en av de återstående: ")

    for i, komb in enumerate(tillgangliga, start=1):
        print(f"{i}. {komb}")

    while True:
        val = input("Vilken vill du stryka? (skriv numret): ")

        if val.isdigit():
            val = int(val)
            if 1 <= val <= len(tillgangliga):
                vald = tillgangliga[val - 1]
                print(f"Du strök: {vald} (0 poäng)")
                return vald

    
        print("Ogiltigt val, försök igen!")


# Välj vilken kombination

def valj_kombination(mojliga):
    print("\nDu kan välja mellan följande kombinationer: ")
    for i, komb in enumerate(mojliga, start=1):
        print(f"{i}. {komb}")

    while True:
        val = input("Vilken kombination vill du använda? (skriv numret): ")

        if val.isdigit():
            val = int(val)
            if 1 <= val <= len(mojliga):
                return mojliga[val - 1]
            
        print("Ogiltigt val, försök igen!")


# Räkna poäng

def rakna_poang(kombination, hand, antal_lista):
    if kombination == "Ettor": return antal_lista[0] * 1
    if kombination == "Tvåor": return antal_lista[1] * 2
    if kombination == "Treor": return antal_lista[2] * 3
    if kombination == "Fyror": return antal_lista[3] * 4
    if kombination == "Femmor": return antal_lista[4] * 5
    if kombination == "Sexor": return antal_lista[5] * 6

    if kombination == "Par":
        for i in range(5, -1, -1):
            if antal_lista[i] >= 2:
                return (i + 1) * 2
            
    if kombination == "Två par":
        par = []
        for i in range(6):
            if antal_lista[i] >= 2:
                par.append(i + 1)
        return par[0] * 2 + par[1] * 2
    
    if kombination == "Tretal":
        for i in range(6):
            if antal_lista[i] >= 3:
                return (i + 1) * 3
            
    if kombination == "Fyrtal":
        for i in range(6):
            if antal_lista[i] >= 4:
                return (i + 1) * 4
            
    if kombination == "Kåk":
        tretal = 0
        par = 0
        for i in range(6):
            if antal_lista[i] == 3:
                tretal = i + 1
            if antal_lista[i] == 2:
                par = i + 1
        return tretal * 3 + par * 2
    
    if kombination == "Liten stege": return 15
    if kombination == "Stor stege": return 20
    if kombination == "Chans": return sum(hand)
    if kombination == "Yatzy": return 50


# En runda

def spela_runda():
    global tillgangliga_kombinationer

    hand = skapa_hand()
    skriv_ut_hand(hand)

    visa_mojliga_kombinationer(hand, tillgangliga_kombinationer)

    hand = omkastningar(hand)

    antal_lista =skapa_antal_lista(hand)
    mojliga = hitta_kombinationer(antal_lista, hand)

    giltiga = filtrera_mojliga(mojliga, tillgangliga_kombinationer)

    if len(giltiga) == 0:
        vald = stryk_kombination(tillgangliga_kombinationer)
        poang_lista[vald] = 0
        tillgangliga_kombinationer.remove(vald)
        return
    
    vald = valj_kombination(giltiga)
    poang = rakna_poang(vald, hand, antal_lista)

    print(f"\nDu valde {vald} och fick {poang} poäng!")

    poang_lista[vald] = poang
    tillgangliga_kombinationer.remove(vald)



for _ in range(15):
    spela_runda()

# Bonus

over_kombination = ["Ettor", "Tvåor", "Treor", "Fyror", "Femmor", "Sexor"]
over_summa = 0

for komb in over_kombination:
    if komb in poang_lista:
      over_summa += poang_lista[komb]

if over_summa >= 63:
    print("\nDu fick 50 poäng bonus!")
    poang_lista["Bonus"] = 50
else:
    poang_lista["Bonus"] = 0

print("\nSpelet är slut! Här är dina poäng: ")
for komb, poang in poang_lista.items():
    print(f"{komb}: {poang}")
   
total = sum(poang_lista.values())
print(f"\nTOTALPOÄNG: {total}")
