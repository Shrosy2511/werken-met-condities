kaas = input('is de kaas geel? ')

if kaas == 'ja':
    vraag1 = input('zitten er gaten in? ')
    if vraag1 == 'ja':
        vraag2 = input('is de kaas belachelijk duur? ')
        if vraag2 == 'ja':
            print('het is de emmenthaler')
    else:
        vraag3 = input('is de kaas hard als steen? ')
        if vraag3 == 'ja':
            print('het is de pamigiano reggiano')
        else:
            print('het is de goudse kaas')
else:
    vraag4 = input('heeft de kaas blauwe schimmel? ')
    if vraag4 == 'ja':
        vraag5 = input('heeft de kaas een korst? ')
        if vraag5 == 'ja':
            print('het is de blue de rochbarron')
        else:
            print('het is de foume d ambert')
    else:
        vraag6 = input('heeft de kaas een korst? ')
        if vraag6 == 'ja':
            print('het is de camembert')
        else:
            print('het is de mozzarella')