'''Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!'''
szavak = input("Adj meg 3 szot: ").split()
def legrövidebb(szavak):
    rövid = szavak[0]
    for szo in szavak:
        if len(szo) < len(rövid):
            rövid = szo
    print("A legrövidebb szó:", rövid)
legrövidebb(szavak)