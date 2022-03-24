ru = 3987863
print('Application of Z Logistics')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

dest_code: tuple = ('RS', 'SR', 'BS', 'SB', 'BR', 'RB')
dest_descr:list = ['From Rio de Janeiro to São Paulo', 'From São Paulo to Rio de Janeiro', 'From Brasilia to São Paulo',
                   'From São Paulo to Brasilia', 'From Brasilia to Rio de Janeiro ', 'From Rio de Janeiro to Brasilia']
dest_mult: tuple = ('1', '1', '1.2', '1.2', '1.5', '1.5')
dest_route = {'Code':[dest_code], 'Description':[dest_descr], 'Multiplier':[dest_mult]}

count = 0
def val_dim(h1, l1, w1):
    height = h1
    length = l1
    width = w1
    val = False
    if type(height) is not float or type(length) is not float or type(width) is not float:
        if type(height) is not float and type(length)  is float and type(width) is float:
            return 'The height value is invalid, please input again...'
        elif type(height) is float and type(length) is not float and type(width) is float:
            return 'The length value is invalid, please input again...'
        elif type(height) is float and type(length) is float and type(width) is not float:
            return 'The width values is invalid, please input again...'
        else:
            return 'Please, insert all dimensions again.'
    if height > 0 and length > 0 and width > 0:
        if height < 10000 and length < 10000 and width < 10000:
            return 'Valid parameters!'
        else:
            return 'Too large dimensions, please revise them.'
    else:
        return 'Too tiny dimensions, please revise them.'

def val_weight(p1):
    weight: float = p1
    if p1 <= 0 or p1 > 30:
        return 'Invalid weight,please insert again.'
    else:
        return 'Valid weight.'

def val_route(p1):
    route: str = p1
    if len(route) <= 1:
        if route in dest_code:
            return 'Valid code!'
        else:
            return 'Invalid code entered, please insert again!'
    else:
        return "You've inserted a too long code, please revise them."

def input_data():
    while True:
        height: float = float(input('Insert the height of the object: [cm]'))
        length:float = float(input('Insert the length of the object: [cm]'))
        width:float = float(input('Insert the height of the object: [cm]'))
        val_d: str = val_dim(height, length, width)
        print(val_d)
        weight: float = float(input('Insert the weight value: [kg]'))
        val_w:str = val_weight(weight)
        print(val_w)
        for e in range(dest_code):
            print('Code: {} - Route: {}'.format(dest_code[e], dest_route[e]))
        val_r = ''
        while val_r != 'Valid code!':
            route: str = str(input('Insert the destiny wanted: [RS]'))
            val_r: str = val_route(route)
            print(val_r)
