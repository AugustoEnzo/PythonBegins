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


def val_dim(height, length, width):
    try:
        if type(height) is float or type(length) is float or type(width) is float:
            if height > 0 and length > 0 and width > 0:
                if height < 1000 and length < 1000 and width < 1000:
                    return 'Valid parameters!'
                else:
                    return 'Too large dimensions, please revise them.'
            else:
                return 'Negative dimensions are not accepted, please revise them.'
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
        if len(route) <= 2:
            if route in dest_code:
                return 'Valid code!'
            else:
                return 'Invalid code entered, please insert again!'
        else:
            return "You've inserted a too long code, please revise them."
    else:
        print("You've entered a invalid value, please insert again.")
        return TypeError


def dimensions_object():
    volume: float = float(h * l * w)
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
        return volume, vol_cost, vol_tier


def weight_object():
    wei_mult: float = 0
    wei_tier = 0
    try:
        if 0 > weight < 0.1:
            wei_mult = 1
            wei_tier = 1
        elif 0.1 <= weight < 1:
            wei_mult = 1.5
            wei_tier = 2
        elif 1 <= weight < 10:
            wei_mult = 2
            wei_tier = 3
        elif 10 <= weight < 30:
            wei_mult = 3
            wei_tier = 4
        else:
            print('You have a too heavy baggage, please redirect himself to the gate to be evaluated.')
    finally:
        return wei_mult, wei_tier


def route_object():
    try:
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
    return total

def src_dest(route):
    code = route
    src: str = ''
    dest: str = ''
    if code[0] == 'R':
        src = 'Rio de Janeiro'
    elif code[0] == 'S':
        src = 'São Paulo'
    elif code[0] == 'B':
        src = 'Brasilia'
    if code[1] == 'S':
        dest = 'São Paulo'
    elif code[1] == 'B':
        dest = 'Brasilia'
    elif code[1] == 'R':
        dest = 'Rio de Janeiro'
    return src, dest

# Main program:
while True:
    val_d = ''
    while val_d != 'Valid parameters!':
        try:
            h: float = float(input('Insert the height of the object: [cm] '))
            l: float = float(input('Insert the length of the object: [cm] '))
            w: float = float(input('Insert the width of the object: [cm] '))
            val_d: str = val_dim(h, l, w)
            print(val_d)
        except:
            print("You've entered an invalid value, only are allowed numeric values!\n Please Try again...")
    val_w = ''
    while val_w != 'Valid weight.':
        try:
            weight: float = float(input('Insert the weight value: [kg] '))
            val_w: str = val_weight()
            print(val_w)
        except:
            print("You've entered an invalid value, only are allowed numeric values!\n Please Try again...")
    e = 0
    while e < len(dest_code):
        print('Code: {} - Route: {}'.format(dest_code[e], dest_descr[e]))
        e += 1
    val_r = ''
    while val_r != 'Valid code!':
        try:
            route: str = input('Insert the destiny wanted: [RS] ')
            val_r: str = val_route()
            print(val_r)
        except:
            print("You've entered an invalid value, only are allowed alphabetic characters!\n Please Try again...")
    vol, vol_c, vol_t = dimensions_object()
    wei_m, wei_t = weight_object()
    route_m, route_t = route_object()
    tot = main_calculation()
    source, destiny = src_dest(route)
    print("The travel with source: {} and destiny: {}.\nHave a total value of: R$ {:.2g}".format(source, destiny, tot))
    print("With the following characteristics: \n Volume: {:.1g} cm³ with the cost of: R$ {:.2g} and be in the: {:.0g}º volume tier\n"
          " the weight was: {:.2g} kg with the: {:.1g}º weight tier".format(vol, vol_c, vol_t, weight, wei_t))
    ctn:str = input('Do you want to continue: [Y]\[N] ')
    if ctn not in 'Yy':
        print('Finishing...')
        break