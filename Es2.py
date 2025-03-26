import numpy as np
import random 

#Esercizio 1
def primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else: 
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
list = [x for x in range(1,21) if primo(x)]
a = np.array(list)
b = a[a>10]
c = a[a%2==0]


#Esercizio 2 
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b = a[1:3]
c = a[3]
d = a/c


#Esercizio 3
a = np.random.rand(10,3)

distanze = np.abs(a - 0.5)
indici = np.argmin(distanze, axis=1)
b = a[np.arange(10), indici]


#Esercizio 4 
list = [68, 65, 77, 110, 160, 161, 162, 161, 160, 161, 162, 163, 164, 163, 162, 100, 90, 97, 72, 60, 70]
a = np.array(list)
min_a = np.min(a)
max_a = np.max(a)
b = a>120
c = np.sum(b)/len(a)*100


#Esercizio 5 
list = [50000, 105250, 55000, 89000]
a = np.array([50000, 105250, 55000, 89000], dtype=np.float64)
b = np.sum(a)

a[a == np.max(a)] = a[a == np.max(a)]*1.15
a[a == np.min(a)] = a[a == np.min(a)]*1.20

c = np.array(list)
d = sum(a) - sum(c)


#Esercizio 6


#Esercizio 7
survey_matrix = np.array([
    [25, 40000, 10],
    [32, 52000, 12],
    [40, 63000, 14],
    [29, 47000, 11],
    [35, 58000, 13]
])

a = survey_matrix[survey_matrix[:,2]>=12]
b = a[:,1]
c = np.mean(b)


#Esercizio 8
ages = np.array([92, 108, 75, 63, 62, 66, 90, 98, 97, 92, 60, 107, 90, 71, 97, 86, 55, 55,
                 98, 57, 96, 104, 96, 94, 72, 98, 111, 98, 89, 69, 77, 92, 85, 101, 93, 100,
                 90, 101, 96, 98, 999, 87, 106, 86, 108, 55, 67, 65, 68, 59, 67, 72, 57, 79,
                 95, 67, 86, 70, 91, 111, 67, 75, 59, 88, 90, 99, 94, 65, 111, 103, 100, 70,
                 63, 65, 100, 110, 999, 70, 57, 75, 56, 104, 111, 90, 74, 100, 90, 86, 88, 99,
                 58, 103, 88, 103, 64, 96, 105, 89, 83, 65, 100, 62, 73, 105, 83, 105, 58, 96,
                 77, 74, 95, 109, 91, 101, 91, 999, 63, 111, 97, 108, 75, 77, 73, 58, 94, 83,
                 90, 61, 110, 107, 105, 85, 64, 66, 71, 107, 105, 72, 78, 66, 100, 102, 72, 999,
                 74, 68, 73, 72, 90, 93, 99, 55, 92, 83, 58, 71, 89, 75, 98, 87, 999, 78,
                 97, 71, 106, 83, 58, 81, 100, 72, 93, 70, 65, 60, 95, 107, 94, 77, 87, 90,
                 82, 56, 99, 107, 86, 56, 73, 96, 64, 69, 64, 92, 57, 104, 110, 69, 66, 68,
                 84, 89, 72, 80, 55, 75, 87, 57, 106, 69, 66, 62, 102, 76, 111, 999, 96, 83,
                 84, 61, 102, 63, 107, 63, 76, 58, 83, 58, 61, 71, 77, 90, 74, 100, 103, 74,
                 92, 102, 63, 87, 93, 61, 63, 86, 74, 98, 64, 999, 78, 95, 84, 81, 107, 85,
                 79, 82, 89, 65, 107, 57, 74, 77, 97, 92, 58, 96, 105, 60, 55, 74, 57, 80,
                 62, 85, 87, 62, 999, 71, 74, 70, 97, 59, 82, 96, 105, 70, 89, 105, 60, 70,
                 87, 999, 64, 108, 107, 104, 85, 95, 108, 74, 64, 97, 89, 88, 79, 67, 81, 92,
                 63, 80, 76, 94, 104, 67, 73, 61, 99, 96, 68, 90, 86, 79, 85, 111, 75, 98,
                 81, 111, 108, 103, 85, 72, 108, 102, 999, 64, 107, 112, 66, 93, 89, 78, 66, 92,
                 63, 101, 92, 64, 72, 56, 71, 64, 87, 78, 107, 85, 109, 95, 69, 111, 64, 72,
                 55, 66, 99, 57, 78, 55, 58, 90, 88, 71, 90, 103, 92, 98, 67, 97, 77, 68,
                 77, 59, 78, 69, 77, 81, 61, 99, 999, 85, 78, 104, 97, 95, 74, 70, 69, 83,
                 68, 68, 77, 60, 85, 82, 93, 66, 71, 62, 64, 107, 999, 65, 78, 59, 83, 67,
                 108,  58,  95, 106,  83,  79,  67,  59,  96,  90,  55,  55,  96, 109,  82,  55, 101,  58,
                 97, 77, 60, 81, 999, 81, 75, 100, 66, 65, 105, 94, 101, 56, 999, 59, 105, 59,
                 93, 56, 104, 74, 81, 62, 76, 65, 107, 60, 107, 98, 77, 86, 83, 104, 74, 69,
                 97, 80, 91, 56, 108, 87, 65, 91, 93, 60, 91, 110, 107, 88, 96, 70, 60, 99,
                 66, 91, 107, 65, 81, 109, 84, 106, 80, 92, 78, 84, 91, 59])

a = ages[ages<999]
b = np.max(a)


#Esercio 9
lista_parole = [
    'INSEDIAMENTO', 'SEPARAZIONE', 'DIFFERENZA', 'APPLICAZIONE', 'ATTEGGIAMENTO', 
    'VERDURA', 'IMPERO', 'RICEVIMENTO', 'IGNORANZA', 'BIOGRAFIA', 'VISIONE', 
    'AGENTE DI POLIZIA', 'PROVA', 'PRESTAZIONE', 'PRESENTAZIONE', 'PARENTE',
    'GIUSTIFICAZIONE', 'FILOSOFIA', 'DIREZIONE', 'BENEFICIARIO', 'BATTERIA', 
    'CERIMONIA', 'AGONIA', 'RECUPERO', 'ALFABETIZZAZIONE', 'CONSEGNA', 
    'SERBATOIO', 'VOLONTARIO', 'DEPOSITO', 'BIRILLO DA BOWLING', 'NEMICO', 
    'ANNUNCIO', 'CARAMELLA ZUCCHERATA', 'FULMINE', 'PALLONCINO', 'COPERTA', 
    'SCOPERTA', 'PENALITÀ', 'GENERALE', 'ALPACA', 'VANTAGGIO', 'HOT DOG', 
    'ABITO', 'MATEMATICA', 'VARIANTE'
]

template_storia = (
    "In epoche passate, viveva una donna saggia che era molto orgogliosa dell'antico __ che proteggeva. "
    "Quando un anziano del villaggio venne a chiederle consiglio su come garantire al meglio un raccolto abbondante e le offrì il __ come dono, "
    "i suoi occhi si spalancarono e lei esclamò una sola parola, \"__\".\n"
    "Radunò il villaggio e, per i successivi 100 giorni, su sua richiesta, gli abitanti cercarono nella foresta un __.\n"
    "Nel 101° giorno, il bambino più giovane del villaggio trovò ciò che stavano cercando e tutti corsero dalla donna saggia per donarglielo.\n"
    "Con un sorriso da un orecchio all’altro, e cantando canti di festa, la donna saggia guardò i suoi compaesani e disse: "
    "\"Ora è giunto il tempo del banchetto - nessuno rimarrà mai più senza __!\" Ci fu grande gioia e celebrazione."
)

parole_scelte = np.random.choice(lista_parole, size=5, replace=True)
storia_completata = template_storia
for parola in parole_scelte:
    storia_completata = storia_completata.replace("__", parola, 1)