'''
Az KERESÉS esetében azt vizsgáljuk, 
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában),
és ha igen, hányadik helyen.

A program azt vizsgálja, hogy szerepel-e a piros szín a listában, és ha igen, hányadik helyen.
'''
lista = ['kék', 'zöld', 'piros', 'fehér', 'piros']

talalat = False
index = 0
while index < len(lista) and not talalat:
        if lista[index] == 'piros':
            talalat = True
        index = index + 1

if 'piros' in lista:
    print('Van a listában piros szín, az indexe: ', )
else:
    print('Nincs a listában piros szín.')

print(lista.count('piros'), "piros van")


# for - lista elemek
piros = 0
for szin in lista:
    if szin == 'piros':
        piros += 1
print(piros)

# for ciklus index-szel
hanyszorpiros = 0
for index in range(len(lista)):
    if lista[index] == 'piros':
        hanyszorpiros += 1
print("Ennyiszer fordul elő: ", hanyszorpiros)

