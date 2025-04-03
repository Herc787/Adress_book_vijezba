import json

DATOTEKA_ADRESARA = "adresar.json"

def ucitaj_podatke() -> dict:
    """
    Učitava podatke iz JSON datoteke. Ako datoteka ne postoji ili je oštećena,
    vraća prazan adresar.

    Returns:
        dict: Podaci o kontaktima iz JSON datoteke ili prazan adresar.
    """
    try:
        with open(DATOTEKA_ADRESARA, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        data = {}
        return data


    

def spremi_podatke(podaci: dict) -> None:
    """
    Spremi podatke u JSON datoteku.

    Args:
        podaci (dict): Podaci koji će biti pohranjeni u datoteku.
    """
    with open(DATOTEKA_ADRESARA, "w", encoding="utf-8")as file:
        json.dump(podaci, file)

def provjeri_telefon(telefon: str) -> bool:
    """
    Provjerava je li telefon sastavljen samo od brojki.

    Args:
        telefon (str): Broj telefona.

    Returns:
        bool: True ako telefon sadrži samo brojke, inače False.
    """
    if telefon.replace(" ", "").replace("+", "").replace("-", "").isdigit():
        return True
    else: return False

def provjeri_email(email: str) -> bool:
    """
    Provjerava sadrži li email znak '@'.

    Args:
        email (str): Email adresa.

    Returns:
        bool: True ako email sadrži '@', inače False.
    """
    if "@" in email: return True
    else: return False

def dodaj_kontakt(ime: str, telefon: str, email: str, adresa: str) -> None:
    """
    Dodaje kontakt u adresar ako su svi podaci ispravni.

    Args:
        ime (str): Ime kontakta.
        telefon (str): Telefon kontakta.
        email (str): Email kontakta.
        adresa (str): Adresa kontakta.
    """
    if provjeri_telefon(telefon) and provjeri_email(email) == True:
        adresar = ucitaj_podatke()
        if "Kontakti" not in adresar:
            adresar["Kontakti"] = {}
        
        if ime in adresar["Kontakti"]:
            print("Kontakt pod tim imenom vec postoji")
            
            while True:
                yn = input(f"Zelite li overwritati podatke za kontakt {ime}(y/n)").strip().lower()
                if yn == "y": break
                elif yn == "n":
                    print(f"Kontakt {ime} se nije promijenio")
                    return
                else:
                    print("Morate unjeti y/n")

        adresar["Kontakti"][ime] = {
            "Telefon": telefon,
            "Email": email,
            "Adresa": adresa
        }

        spremi_podatke(adresar)
    else: print("Nesto je krivo uneseno")

def prikazi_kontakte() -> None:
    """
    Prikazuje sve kontakte u adresaru.
    """
    adresar = ucitaj_podatke()

    if "Kontakti" not in adresar:
        print("Adresar je prazan")
        return
    
    for ime, data in adresar["Kontakti"].items():
        print("-" * 30, end="")
        print(f"\nIme: {ime}")
        print(f"Telefon: {data['Telefon']}")
        print(f"Email: {data['Email']}")
        print(f"Adresa: {data['Adresa']}")
    print("-" * 30, end="")
    print()


def pretrazi_kontakt(ime: str) -> None:
    """
    Pretražuje adresar prema imenu kontakta.

    Args:
        ime (str): Ime kontakta za pretragu.
    """
    adresar = ucitaj_podatke()
    
    if "Kontakti" not in adresar or not adresar["Kontakti"]:
        print("Adresar je prazan :()")
        return
    
    if ime in adresar["Kontakti"]:
        kontakt = adresar["Kontakti"][ime]
        kontakt.strip().lower()
        print("-" * 30, end="")
        print(f"\nIme: {ime}")
        print(f"Telefon: {kontakt['Telefon']}")
        print(f"Email: {kontakt['Email']}")
        print(f"Adresa: {kontakt['Adresa']}")
        print("-" * 30, end="")
    else: print(f"Kontakt {ime} nije pronadjen")


def obrisi_kontakt(ime: str) -> None:
    """
    Briše kontakt iz adresara prema imenu.

    Args:
        ime (str): Ime kontakta koji će biti obrisan.
    """

    adresar = ucitaj_podatke()

    #Ovo sam vec odavno trebal pretvoriti u funkciju ali sad je pre kasno za to
    if "Kontakti" not in adresar or not adresar["Kontakti"]:
        print("Adresar je prazan")
        return

    if ime in adresar["Kontakti"]:
        potvrda = input(f"Jeste li sigurni da želite obrisati kontakt '{ime}'? (y/n): ").strip().lower()
        if potvrda == "y":
            del adresar["Kontakti"][ime]
            spremi_podatke(adresar)
            print(f"Kontakt '{ime}' je obrisan.")
        else:
            print("Brisanje otkazano.")
    else:
        print(f"Kontakt '{ime}' nije pronađen.")

    

def main() -> None:
    """
    Glavna funkcija koja omogućava korisniku da bira opcije u adresaru.
    """
    while True:
        print("\nAdresar - Odaberite opciju:")
        print("1. Dodaj kontakt")
        print("2. Prikaži sve kontakte")
        print("3. Pretraži kontakt")
        print("4. Obriši kontakt")
        print("5. Izlaz")
        
        izbor = input("Unesite broj opcije: ")
        if izbor == "1":
            ime = input("Unesite ime: ")
            telefon = input("Unesite broj telefona: ")
            email = input("Unesite email: ")
            adresa = input("Unesite adresu: ")
            dodaj_kontakt(ime, telefon, email, adresa)
        elif izbor == "2":
            prikazi_kontakte()
        elif izbor == "3":
            ime = input("Unesite ime za pretragu: ").strip().lower()
            pretrazi_kontakt(ime)
        elif izbor == "4":
            ime = input("Unesite ime za brisanje: ").strip().lower()
            obrisi_kontakt(ime)
        elif izbor == "5":
            print("Izlaz iz aplikacije.")
            break
        else:
            print("Pogrešan unos, pokušajte ponovo.")

if __name__ == "__main__":
    main()
