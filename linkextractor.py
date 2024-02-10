import requests
from colorama import Fore, Style
import time

def stampa_con_effetto(testo, colore=Fore.WHITE, velocita=0.03):
    for carattere in testo:
        print(f"{colore}{carattere}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(velocita)
    print()

def ottieni_link_originale(shortlink):
    try:
        response = requests.head(shortlink, allow_redirects=True)
        return response.url
    except requests.RequestException as e:
        return f"Errore: {e}"

def stampa_messaggio_ringraziamento():
    messaggio = "\nGrazie per aver utilizzato questo tool. Creato da t.me/VikingTerminal"
    stampa_con_effetto(messaggio, colore=Fore.GREEN)

def main():
    benvenuto = "Benvenuto! Questo tool ti aiuterà a ottenere il link originale da uno shortlink."
    stampa_con_effetto(benvenuto, colore=Fore.CYAN)

    while True:
        input_prompt = "Inserisci il link abbreviato (o scrivi 'exit' se vuoi uscire\n): "
        shortlink = input(f"{Fore.YELLOW}{input_prompt}{Style.RESET_ALL}")

        if shortlink.lower() == 'exit':
            stampa_messaggio_ringraziamento()
            break

        link_originale = ottieni_link_originale(shortlink)
        output = f"Link originale:\n{link_originale}\n"
        stampa_con_effetto(output, colore=Fore.GREEN)

if __name__ == "__main__":
    main()
