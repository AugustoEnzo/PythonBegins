ru = 3987863
print('Application of Z Logistics')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

dest_code: tuple = ('RS', 'SR', 'BS', 'SB', 'BR', 'RB')
dest_descr: list = ['From Rio de Janeiro to São Paulo', 'From São Paulo to Rio de Janeiro',
                    'From Brasilia to São Paulo', 'From São Paulo to Brasilia',
                    'From Brasilia to Rio de Janeiro ', 'From Rio de Janeiro to Brasilia']
dest_mult: tuple = ('1', '1', '1.2', '1.2', '1.5', '1.5')
dest_route = {'Code': [dest_code], 'Description': [dest_descr], 'Multiplier': [dest_mult]}

count = 0


def val_dim():
    try:
        if type(height) is float or type(length) is float or type(width) is float:
            if height > 0 and length > 0 and width > 0:
                if height < 10000 and length < 10000 and width < 10000:
                    return 'Valid parameters!'
                else:
                    return 'Too large dimensions, please revise them.'
            else:
                return 'Too tiny dimensions, please revise them.'
    except:
        print("You've inserted a invalid number, please try again")
        return TypeError


def val_weight():
    if weight <= 0 or weight > 30:
        return 'Invalid weight,please insert again.'
    else:
        return 'Valid weight.'


def val_route():
    if len(route) <= 1:
        if route in dest_code:
            return 'Valid code!'
        else:
            return 'Invalid code entered, please insert again!'
    else:
        return "You've inserted a too long code, please revise them."


def input_data():
    while True:
        val_d = ''
        while val_d != 'Valid parameters!':
            height: float = float(input('Insert the height of the object: [cm]'))
            length: float = float(input('Insert the length of the object: [cm]'))
            width: float = float(input('Insert the height of the object: [cm]'))
            global height, length, width
            val_d: str = val_dim()
            print(val_d)
        val_w = ''
        while val_w != 'Valid weight.':
            weight: float = float(input('Insert the weight value: [kg]'))
            global weight
            val_w: str = val_weight()
            print(val_w)
        for e in range(dest_code):
            print('Code: {} - Route: {}'.format(dest_code[e], dest_route[e]))
        val_r = ''
        while val_r != 'Valid code!':
            global route
            route: str = str(input('Insert the destiny wanted: [RS]'))
            val_r: str = val_route()
            print(val_r)


def dimensions_object():
    volume: float = float(height * width * length)
    vol_cost: float = 0
    tier: int = 0
    try:
        if volume < 1000:
            tier = 1
            vol_cost = 10
        elif 1000 <= volume < 10000:
            tier = 2
            vol_cost = 20
        elif 10000 <= volume < 30000:
            tier = 3
            vol_cost = 30
        elif 30000 <= volume < 100000:
            tier = 4
            vol_cost = 50
    finally:
        return vol_cost, tier
