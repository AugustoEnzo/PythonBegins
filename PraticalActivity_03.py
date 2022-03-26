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
                if height < 1000 and length < 1000 and width < 1000:
                    return 'Valid parameters!'
                else:
                    return 'Too large dimensions, please revise them.'
            else:
                return 'Too tiny dimensions, please revise them.'
    except:
        print("You've inserted a invalid number, please try again")
        return TypeError


def val_weight():
    try:
        if type(weight) is float:
            if weight <= 0 or weight > 30:
                return 'Invalid weight,please insert again.'
            else:
                return 'Valid weight.'
    except:
        print("You've entered a invalid value, please insert again.")
        return TypeError


def val_route():
    if type(route) is str:
        if len(route) <= 1:
            if route in dest_code:
                return 'Valid code!'
            else:
                return 'Invalid code entered, please insert again!'
        else:
            return "You've inserted a too long code, please revise them."
    else:
        print("You've entered a invalid value, please insert again.")
        return TypeError


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
    global volume, vol_cost, vol_tier
    volume: float = float(height * width * length)
    vol_cost: float = 0
    vol_tier: int = 0
    try:
        if volume < 1000:
            vol_tier = 1
            vol_cost = 10
        elif 1000 <= volume < 10000:
            vol_tier = 2
            vol_cost = 20
        elif 10000 <= volume < 30000:
            vol_tier = 3
            vol_cost = 30
        elif 30000 <= volume < 100000:
            vol_tier = 4
            vol_cost = 50
        else:
            print("You've  a too much bulky baggage, please redirect himself to the gate to be evaluated.")
    finally:
        return vol_cost, vol_tier


def weight_object():
    global wei_mult, wei_tier
    wei_mult: float = 0
    wei_tier = 1
    try:
        if 0 > weight < 0.1:
            wei_mult = 1
            wei_tier = 1
        elif 0.1 >= weight < 1:
            wei_mult = 1.5
            wei_tier = 2
        elif 1 >= weight < 10:
            wei_mult = 2
            wei_tier = 3
        elif 10 >= weight < 30:
            wei_mult = 3
            wei_tier = 4
        else:
            print('You have a too heavy baggage, please redirect himself to the gate to be evaluated.')
    finally:
        return wei_mult, wei_tier


def route_object():
    try:
        global mult_route, tier_route
        mult_route: float = float(0)
        tier_route: int = 0
        if route == 'RS':
            mult_route = 1
            tier_route = 1
        elif route == 'SR':
            mult_route = 1
            tier_route = 1
        elif route == 'BS':
            mult_route = 1.2
            tier_route = 2
        elif route == 'SB':
            mult_route = 1.2
            tier_route = 2
        elif route == 'BR':
            mult_route = 1.5
            tier_route = 3
        elif route == 'RB':
            mult_route = 1.5
            tier_route = 3
    finally:
        return mult_route, tier_route

def main_calculation():
    global total
    total = ((vol_c* wei_m) * route_m)


# Main program:
while True:
    input_data()
    vol_c = dimensions_object()[0]
    vol_t = dimensions_object()[1]
    wei_m = weight_object()[0]
    wei_t = weight_object()[1]
    route_m = route_object()[0]
    route_t = route_object()[1]