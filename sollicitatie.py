#Circusdirecteur voor Circus HotelDeBotel

print('sollicitatie lijst voor circusdirecteur')

score = 0
dierenDressuur = int(input('hoeveel jaar ervaring heeft u in dieren dressuur: '))
if dierenDressuur > int(3):
    score += 1

jongleren = int(input('hoeveel jaar ervaring heeft u in jongleren: '))
if jongleren > int(4):
    score += 1

acrobatiek = int(input('hoeveel jaar ervaring heeft u in acrobatiek: '))
if acrobatiek > int(2):
    score += 1

diploma = (input('heeft u een mbo4 diploma in ondernemen j/n: '))
if diploma == 'j':
    score += 1

rijbewijs = (input('heeft u een geldig vrachtwagen rijbewijs j/n: '))
if rijbewijs == 'j':
    score += 1

hoed = (input('heeft u een hoge hoed j/n: '))
if hoed == 'j':
    score += 1

geslacht = (input('bent u een man of vrouw: '))
if geslacht == 'man':
    snor = (input('heeft u een snor j/n: '))
    if snor == 'j':
        snorLength = int(input('hoelang is uw snor antwoord in cm: '))
        if snor == 'j' and snorLength > int(9):
            score += 1
else:
    haar = (input('heb je rood krulhaar j/n'))
    if haar == 'j':
        haarLength = (input('hoelang is uw haar antwoord in cm: '))
        if haar == 'j' and haarLength > int(19):
            score += 1

lengte = int(input('hoelang bent u in cm: '))
if lengte > int(150):
    score += 1

gewicht = int(input('wat is uw gewicht in kg: '))
if gewicht > int(149):
    score += 1

certificaat = (input('heeft u het certificaat overleven met gevaarlijke personen j/n: '))
if certificaat == 'j':
    score += 1

print(score)

if score > 8:
    print('u bent door de kwalificatie heen u bent geschikt voor de baan')
else:
    print('u ben niet gekwalificeerd voor de baan')