#!/usr/bin/env python3

import pickle

class Veicolo():
    def __init__(self, targa, modello):
        self.targa = targa
        self.modello = modello
        self.disponibile = True

    def affitto(self):
        if self.disponibile: # se True
            self.disponibile = False
            print(f"\nHai Affittato con successo il Veicolo: {self.modello} con Targa: {self.targa}")
        else:
            print(f"Veicolo: {self.modello} con Targa: {self.targa} NON è disponibile ")

    def veicolo_disponibile(self):
        self.disponibile = True

    def __str__(self):
        return f"{self.modello} Targato: {self.targa} -> {'Disponibile' if self.disponibile == True else 'NON Disponibile'}"
    
    def __repr__(self):
        return __str__()




class Flotta():

    def __init__(self):
        self.veicoli = [] # lista

    def esistenza_veicolo(self, targa): # questo metodo vede se il veicolo è già esistente tramite la targa
        for veicolo in self.veicoli:
            if veicolo.targa == targa:
                return True # esiste
            else:
                return False # NON esiste

    def aggiungere_veicolo(self, veicolo):
        if not self.esistenza_veicolo(veicolo.targa): # controliamo con il metodo esistenza_veicolo se il veicolo esiste già nella lista
            self.veicoli.append(veicolo)
            print(f"Veicolo con targa: {veicolo.targa} Modello: {veicolo.modello} è stato inserito nella flotta con successo")
        else:
            print(f"Veicolo con targa: {veicolo.targa} già esistente nella flotta")

    def __str__(self):
        return f"\n".join(str(veicolo) for veicolo in self.veicoli)
    
    def affitto_veicolo(self, targa):        
        for veicolo in self.veicoli:
            if veicolo.targa == targa: # controliamo se il veicolo esiste
                veicolo.affitto()
                return # una volta trovato la targa quindi il veicolo può uscire da questo metodo
           
        print(f"Questo veicolo con targa: {targa} NON esiste nella flotta !!!") # questa riga lo esegue solo finisce il ciclo for e non trova la targa del veicolo 
        
    
    def elenco_veicoli_affittati(self):
        return [print(veicolo) for veicolo in self.veicoli if veicolo.disponibile == False]

    def ritorno_veicoli(self, targa):
        for veicolo in self.veicoli:
            if veicolo.targa == targa and veicolo.disponibile == False:
                veicolo.veicolo_disponibile()
                print(f"\nIl veicolo {veicolo.modello} con targa: {veicolo.targa} è nuovamente disponibile")
                return # una volta trovato la targa deve uscire dal ciclo for
            else:                                                                   # questo else se non si verifica una delle 2 condizioni del if sopra
                if veicolo.targa == targa and veicolo.disponibile == True:           # verifichiamo se è la disponibilità è la condizione non valida del if sopra
                    print(f"\nIl veicolo con targa: {targa} è già disponibile !!!")
                    return # una volta trovato la targa deve uscire dal ciclo 
        print(f"\n[!] Rientro NON RIUSCITO -> Veicolo con targa: {targa} non appartiene alla flotta !!!") # questa riga si esegue solo sei il ciclo for finisce senza risultati
                                                                                                          # quindi non passando per i return

    def elimina_veicolo(self, targa):
        for veicolo in self.veicoli:
            if veicolo.targa == targa: # controlliamo se il veicolo esiste
                if veicolo.disponibile == True: # controlliamo se è disponibilè, cioè che non è affittato 
                    self.veicoli.remove(veicolo)
                    return
                else:
                    print(f"\n Il Veicolo con targa: {targa} non può essere eliminato perchè è affittato !!!")
                    return
        print(f"\nVeicolo con la targa: {targa} NON esiste nella flotta") # viene eseguita solo se non trova il veicolo 

                        
    def salva_file(self):
        with open("flotta_dati.pkl", "wb") as file:
            pickle.dump(self.veicoli, file)


    def carica_file(self):
        try:
            with open("flotta_dati.pkl", "rb") as file:
                self.veicoli = pickle.load(file)
        except FileNotFoundError:
            print(f"\nFile Dati non presente!")
        except PermissionError:
            print(f"\nAttenzione non hai i permessi per accedere al file dati...")
        else:
            print(f"\nSistema Aggiornato")
            
                


if __name__ == '__main__':

    myflotta = Flotta()

# prove con uso del salvataggio/caricamento su file
    '''
    myflotta.aggiungere_veicolo(Veicolo("FF002XX", "BMV 330"))
    myflotta.aggiungere_veicolo(Veicolo("SS843CC", "Smart for 2"))
    myflotta.aggiungere_veicolo(Veicolo("GH123EV", "AUDI A$"))
    myflotta.aggiungere_veicolo(Veicolo("RS567VX", "Audi Q5"))
    
    myflotta.salva_file()
    '''
    myflotta.carica_file()
    print(f"\nLista Flotta Auto")
    print(myflotta)
    # myflotta.affitto_veicolo("SS843CC")
    # myflotta.elimina_veicolo("GH123EV")
    # myflotta.salva_file()


### prove programma (prove funzionameto dei metodo/classi)
    '''
    myflotta.aggiungere_veicolo(Veicolo("FF002XX", "BMW 330")) # aggiungiamo un oggetto Veicolo direttamente nella classe myflotta
    myflotta.aggiungere_veicolo(Veicolo("KK434NA", "Fiat Punto"))
    

    print(f"\nProva del Programma--------------")
    print(f"\nFlotta Veicoli Iniziale")
    print(myflotta)
    
    print(f"\nInseriamo un auto esistente nella flotta")
    myflotta.aggiungere_veicolo(Veicolo("FF002XX", "BMW X3"))
    
    print("\nInseriamo una nuova auto che non esiste nella flotta")
    myflotta.aggiungere_veicolo(Veicolo("SS443CC", "Smart"))

    # myflotta.salva_file()  
    # myflotta.carica_file()

    print(f"\nFlotta Aggiornata")
    print(myflotta)

    print(f"\nAffittiamo auto che non esiste nella flotta")
    myflotta.affitto_veicolo("SS843CC")

    print(f"\nAffittiamo auto che è presente nella flotta")
    myflotta.affitto_veicolo("SS443CC")
    print(f"\n")
    print(f"Elenco auto affittati:")
    myflotta.elenco_veicoli_affittati()
    
    print(f"\n-------------")  

    print("\nRientriamo veicolo affittato")
    myflotta.ritorno_veicoli("SS443CC")

    print(f"\nLista flotta aggiornata")
    print(myflotta)

    print(f"\n-----------")

    print(f"\nRientriamo dal affitto  un veicolo che non esiste nella nostra flotta")
    myflotta.ritorno_veicoli("ZZ34XX")

    print(f"\n---------")
    print(f"\nRientriamo un veicolo che è già DISPONIBILE")
    myflotta.ritorno_veicoli("FF002XX")

    print(f"\n-------")
    print(f"\nEliminiamo un veicolo dalla flotta")
    myflotta.elimina_veicolo("SS443CC")
    print(myflotta)
    
    print(f"\n--------")
    print(f"\nTentativo di eliminare un veicolo che è in affitto")
    myflotta.affitto_veicolo("FF002XX")
    myflotta.elimina_veicolo("FF002XX")
    print(myflotta)

    print(f"\n--------")
    print(f"\nTentativo di eliminare un veicolo che non esiste nella flotta")
    myflotta.elimina_veicolo("FF009XX")
    print(myflotta)
    '''
