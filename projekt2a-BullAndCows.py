"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Bernas
email: jiri.bernas@nacr.cz
discord: jirka B.#0164
 """
 
import random

def generujCislo(delkaCisla):
    cislo = str(random.randrange(1,10))

    while (len(cislo)<delkaCisla):
        pom = str(random.randrange(0,9))
        if cislo.rfind(pom)==(-1):
            cislo = cislo + pom

    return cislo

def kontrolaCisla(tajneCislo,hadaneCislo,delkaCisla):
    cows=0
    bulls=0
    zprava=''

    if (not hadaneCislo.isnumeric()):
        zprava='Zadaný řetězec není číslo!'
    elif (len(hadaneCislo)!=delkaCisla): 
        zprava='Zadané číslo nemá správnou délku ('+str(delkaCisla)+')!'
    elif (hadaneCislo==tajneCislo):
        zprava='Uhodl jsi!'
        bulls=delkaCisla
    else:
        for x in range(0,delkaCisla):
           for y in range(0,delkaCisla):
               if (tajneCislo[x]==hadaneCislo[y]):
                   if (x==y):
                       bulls+=1
                   else:
                       cows+=1
        zprava=str(bulls)+' bulls, '+str(cows)+' cows'

    return bulls,cows,zprava

def bullAndCow(delkaCisla=4):
    print ('Ahoj')
    print ('Nyní vygeneruji číslo o',delkaCisla,'číslicích a tvým úkolem je toto číslo uhodnout.')
    print ("""Pokud uhodneš číslici na správné pozici, získáváš bulls.
    Uhodneš-li číslici, která je v hádaném čísle, ale na nesprávné pozici, získáváš cow.""")

    tajneCislo=generujCislo(delkaCisla)

    konec=False
    pocetHadani=1

    while not konec:
        info='Zadej svůj '+str(pocetHadani)+'. tip: '
        hadaneCislo=str(input(info))
        bulls,cows,zprava=kontrolaCisla(tajneCislo,hadaneCislo,delkaCisla)
        print (zprava)
        if (bulls==delkaCisla):
            konec=True
            print ('Vyhrál jsi po',pocetHadani,'pokusech.')
        else:
            pocetHadani+=1

if (__name__=="__main__"):
    bullAndCow()
