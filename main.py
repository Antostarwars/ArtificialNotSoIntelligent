import sys
import percettrone

def main():
    successo, weights, bias = percettrone.carica_pesi("pesi_concerto.txt")
    
    if not successo:
        print("Terminazione del programma a causa di un errore nel caricamento.")
        sys.exit(1)
        
    print("Inserisci i dati:")
    input_data = []
    
    domande = [
        "Artista famoso? (1=Si, 0=No): ",
        "Bel meteo? (1=Si, 0=No): ",
        "Amici presenti? (1=Si, 0=No): ",
        "Cibo buono? (1=Si, 0=No): ",
        "Alcool disponibile? (1=Si, 0=No): "
    ]
    
    for domanda in domande:
        while True:
            try:
                risposta = int(input(domanda))
                input_data.append(risposta)
                break
            except ValueError:
                print("Errore: Inserisci solo numeri interi (1 o 0).")

    decisione = percettrone.prevedi(weights, bias, input_data)
    
    if decisione == 1:
        print("\nVai al concerto!")
    else:
        print("\nResta a casa!")

if __name__ == "__main__":
    main()