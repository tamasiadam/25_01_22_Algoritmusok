'''
Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).

A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
'''

lista = [2, 5, 4, 8, 9, 11, 10, 12, 15]
szamok = []

index = 0
while index < len(lista):
    if lista[index] % 3 == 0:
        szamok.append(lista[index])
    index = index + 1

if szamok == []:
    print('Nincs a listában hárommal osztható szám.')
else:
    print('Van a listában hárommal osztható szám. Ezek a ', szamok)