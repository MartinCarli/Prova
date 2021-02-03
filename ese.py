#1 parte1
#rifaccio l eser - studenti

#definisco la classe persona e la inizializzo
class Persona():
    def __init__(self,ruolo,nome,cognome):
        self.nome=nome
        self.ruolo=ruolo
        self.cognome= cognome
#creo il metodo bonjur che permettera di presentarsi
    def bonjur(self):
        print(self.ruolo,': ',self.nome, self.cognome)

#la classe studente e una sottoclasse di 'Persona', creo un nuovo init dove lo studente inserira` i corsi che frequenta, sovrascrivo l' init di persona e metto in ruolo "Studente UniTS" dopodiche starto sovrascrivo bonjur, starto il bonjur della persona e dopodiche` stampo i corsi che frequenta lo studente
class Studente(Persona):
    def __init__(self,nome,cognome,lista_corsi):
        self.lista_corsi=lista_corsi
        super().__init__("Studente UniTS",nome,cognome)
        self.n=len(lista_corsi)
    def bonjur(self):
        Persona.bonjur(self)
        for i in range(0,self.n):
            print('Frequento il corso: {}'.format(self.lista_corsi[i]))

#il concetto e` lo stesso, cambio solo nome di qualche variabile

class Docente(Persona):
    def __init__(self,nome,cognome,lista_corsi):
        self.lista_corsi=lista_corsi
        super().__init__("Docente UniTS",nome,cognome)
        self.n=len(lista_corsi)
    def bonjur(self):
        Persona.bonjur(self)
        for i in range(0,self.n):
            print('Insegno il corso: {}'.format(self.lista_corsi[i]))


# Creo un oggetto e chiamo la funzione bonjour()
obj_Giulio = Studente("Giulio", "Caravagna", ("Programmazione", "Laboratorio di Programmazione", "Analisi", "Geometria"))
obj_Giulio.bonjur()

obj_Mario = Studente("Mario", "Rossi", ("Programmazione", "Laboratorio di Programmazione"))
obj_Mario.bonjur()

obj_ProfRusso = Docente("Stefano Alberto", "Russo", ("Programmazione", "Laboratorio di Programmazione"))

obj_ProfRusso.bonjur()

#ora dovrei iniziare la seconda parte

