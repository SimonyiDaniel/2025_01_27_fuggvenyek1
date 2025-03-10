'''Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!
'''

def osszegzo(list):
    osszesen = 0
    for szam in list:
        osszesen += szam
    return osszesen

szamok = [3, 5, 19, 11, 17, 1]
print(osszegzo(szamok))