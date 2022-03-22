ru = 3987863
print('Application of Y Cafeteria')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)
i = 0
id = [100, 101, 102, 103, 104, 105, 200, 201] # Identificator of items
desc = ['Hot Dog', 'Double Hot dog', 'X-Egg', 'X-Salad', 'X-Bacon', 'X-Everything', 'Soda Tin', 'Cold Tea'] # Items
value = [9.00, 11.00, 12.00, 13.00, 14.00, 17.00, 5.00, 4.00] # Value of items
order_data = {'Order Code':[], 'Item':[], 'Value':[]}
cod = 0
count =0

def s_code(p1):
    cd = p1
    for i in range(0, len(id), 1):
        if int(cd) not in id:
            return 'Invalid Option'
        elif int(cd) == id[i]:
            return ['Code: ',id[i],'Description: ', desc[i],'Value: ', value[i]]
        else:
            continue

def take_info(p1):
    if type(p1) is list:
        inf = p1
        n_inf = inf[3]
        a_inf = inf[5]
        return [n_inf, a_inf]

def calc_amount():
    values = order_data['Value']
    sum_amount: float = 0
    amount = 0
    c = 0
    while c != len(values):
        amount = values[c]
        sum_amount += amount
        c += 1
    return sum_amount

def s_order():
    t0 = order_data['Order Code']
    t1 = order_data['Item']
    t2 = order_data['Value']
    e = 0
    while e <= len(t0):
        print(e)
        print('Code: {} | Item: {} | Value: {}'.format(t0[e], t1[e], t2[e]))
        e += 1
while True:
    print('Select a option with the code: ')
    for i in range(0, len(id), 1):
        print('Code: {} | Description: {} | Value: {}'.format(id[i], desc[i], value[i]))
    cod = int(input('Insert the code of your product: [0 to Exit] '))
    if cod != 0:
        count += 1
        print('- -' * 20)
        info = s_code(cod)
        print("You've selected: ")
        if type(info) is list:
            print('Code: {} | Description: {} | Value: {}'.format(info[1], info[3], info[5]))
        else:
            print(info)
        print('- -' * 20)
        order = take_info(info)
        order_data['Order Code'].append(count)
        order_data['Item'].append(order[0])
        order_data['Value'].append(order[1])
        prog= input('Do you want to continue: [Y][N]')
        if prog not in 'Yy':
            print('Finishing...')
            break
        continue
    elif cod == 0:
        print('Finishing...')
        break

tot_amount = calc_amount()
print('The total amount of you order is: {}'.format(tot_amount))
print("You ve ordered: ")
s_order()