"""
projekt2b.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Bernas
email: jiri.bernas@nacr.cz
discord: jirka B.#0164
 """

def KrajniRadek(rozmer):
    vystup="+"
    for i in range(0,rozmer):
        vystup+="---+"
    
    vystup+='\n'
    
    return vystup

def VypisHraciPole(hraciPole,rozmer):
    vystup=KrajniRadek(rozmer)
    
    for i in range(0,rozmer):
        vystup+='|'
        for j in range(0,rozmer):
            index=rozmer*i+j
            vystup+=" "+hraciPole[index]+' |'
        vystup+='\n'+KrajniRadek(rozmer)
    
    print(vystup)
    
def VyhodnotSituaci(hraciPole,rozmer,delka=3):
    vystup="pokracuje"
    vitez=""
    
    '''Vyhodnocení sloupců'''
    for sloupec in range(0,rozmer):
        for radka in range(0,(rozmer-delka+1)):
            pozice=radka*rozmer+sloupec
            if not (hraciPole[pozice]==' '):
                stejne=True
                prvniKamen=hraciPole[pozice]
                for i in range(1,delka):
                    if hraciPole[pozice+(delka*i)]!=prvniKamen:
                        stejne=False
                if stejne:
                    vitez=prvniKamen
                    vystup="vitezstvi"
    
    '''Vyhodnocení řádků'''
    for radka in range(0,rozmer):
        for sloupec in range(0,(rozmer-delka+1)):
            pozice=radka*rozmer+sloupec
            if not (hraciPole[pozice]==' '):
                stejne=True
                prvniKamen=hraciPole[pozice]
                for i in range(1,delka):
                    if hraciPole[pozice+i]!=prvniKamen:
                        stejne=False
                if stejne:
                    vitez=prvniKamen
                    vystup="vitezstvi"
                    
    '''Vyhodnocení křížem zleva doprava'''
    for radka in range(0,(rozmer-delka+1)):
        for sloupec in range(0,(rozmer-delka+1)):
            pozice=radka*rozmer+sloupec
            if not (hraciPole[pozice]==' '):
                stejne=True
                prvniKamen=hraciPole[pozice]
                for i in range(1,delka):
                    if hraciPole[pozice+(i)*delka+i]!=prvniKamen:
                        stejne=False
                if stejne:
                    vitez=prvniKamen
                    vystup="vitezstvi"
                    
    '''Vyhodnocení křížem zprava doleva'''
    for radka in range(rozmer,delka-1,-1):
        for sloupec in range(0,(rozmer-delka+1)):
            pozice=((radka-1)*rozmer)+sloupec
            if not (hraciPole[pozice]==' '):
                stejne=True
                prvniKamen=hraciPole[pozice]
                for i in range(1,delka):
                    poziceK=pozice-(i)*delka+i
                    if hraciPole[poziceK]!=prvniKamen:
                        stejne=False
                if stejne:
                    vitez=prvniKamen
                    vystup="vitezstvi"

    '''Vyhodnocení remízy'''
    jeRemiza=True
    for kamen in hraciPole:

        if kamen==" ":
            jeRemiza=False

    if jeRemiza:
        vystup="remiza"

    return vystup,vitez

def pravidla(delka=""):
    print("""
PRAVIDLA HRY
============
Dva hráči kladou střídace na pole hrací plochy kameny O a X. Cílem je vytvořit souvislou řadu""",delka,"""kamenů.
    
Pole jsou očíslována zleva doprava a shora dolů.
""")

def cara(delkaCary=50):
    print(delkaCary*"=")

rozmer=3
delka=3
hraciPole=[]

for i in range(0,rozmer*rozmer):
    hraciPole+=" "

hrac=0
konecHry=False
kamen={1:"O",2:"X"}

pravidla(delka)

while not konecHry:
    if hrac==1:
        hrac=2
    else:
        hrac=1
        
    cara()
    VypisHraciPole(hraciPole,rozmer)
    spravnyTah=False
    while not spravnyTah:
        tah=input('Na tahu je hráč číslo '+str(hrac)+'. Zadej prosím svůj tah: ')
        if not tah.isnumeric():
            print('Zadej prosím číslo')
            continue
        tah=int(tah)
        if tah<1:
            print('Zadej prosím číslo v rozsahu od 1 do',len(hraciPole))
            continue
        if tah>len(hraciPole):
            print('Zadej prosím číslo v rozsahu od 1 do',len(hraciPole))
            continue
        if hraciPole[tah-1]!=" ":
            print('Pozice',tah,'je již obsazena.')
            continue
        spravnyTah=True
    
    hraciPole[tah-1]=kamen[hrac]
    
    vysledek,viteznyKamen=VyhodnotSituaci(hraciPole,rozmer,delka)
    
    if vysledek!="pokracuje":
        konecHry=True

cara()
VypisHraciPole(hraciPole,rozmer)

if vysledek=="remiza":
    print('Všechny pole jsou obsazena. Hra končí remízou.')
elif vysledek=="vitezstvi":
    for x in kamen:
        if kamen[x]==viteznyKamen:
            print('Zvítězil hráč číslo',x)
else:
    print('Nečekaný výsledek')
