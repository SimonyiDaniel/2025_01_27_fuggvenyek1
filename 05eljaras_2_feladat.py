'''Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!'''
def eljaras(szam):
    if szam > 0:
        print('Pozitív')
    elif szam < 0:
        print('Negatív')
    else:
        print('Nulla')


while True:
    szam = (input('Adj meg egy számot: '))
    if szam == "":
        break
    eljaras(int(szam))