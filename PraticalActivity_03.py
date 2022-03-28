ru = 3987863
print('Application of Z Logistics')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

dest_code: tuple = ('RS', 'SR', 'BS', 'SB', 'BR', 'RB') # Assign the id of the routes to the var
dest_descr: list = ['From Rio de Janeiro to São Paulo', 'From São Paulo to Rio de Janeiro', # Assign the description of the route to the var
                    'From Brasilia to São Paulo', 'From São Paulo to Brasilia',
                    'From Brasilia to Rio de Janeiro ', 'From Rio de Janeiro to Brasilia']
dest_mult: tuple = ('1', '1', '1.2', '1.2', '1.5', '1.5') # Assign the multiplier based on the code of the route
dest_route = {'Code': [dest_code], 'Description': [dest_descr], 'Multiplier': [dest_mult]} # Assign all the data to a dict


def val_dim(height, length, width): # Function that validates the dimensions of the packet
    try: # Start the validation
        if type(height) is float or type(length) is float or type(width) is float: # Verify the type of the validation
            if height > 0 and length > 0 and width > 0: # Verify if the dimensions aren't negative
                if height < 1000 and length < 1000 and width < 1000: # Validates if the dimensions are too big
                    return 'Valid parameters!' # If both conditions are true returns continue code
                else:
                    return 'Too large dimensions, please revise them.' # If the number are too big don't allow continuing
            else:
                return 'Negative dimensions are not accepted, please revise them.' # The dimensions have negative values, break the code until a positive value have'been assigned
    except:
        print("You've inserted a invalid number, please try again") # One of the types was not a float, the parameters need to be reposed
        return TypeError


def val_weight(): # Function that validates the weight of the packet
    try: # Start the validation
        if type(weight) is float: # Verify the types of the parameters
            if weight <= 0 or weight > 30: # Verify if the weight is too tiny or too big
                return 'Invalid weight,please insert again.' # Prevent the code to proceed
            else:
                return 'Valid weight.' # Allows the code to proceed
    except:
        print("You've entered a invalid value, please insert again.") # Prevents the code to proceed, instructing the user
        return TypeError


def val_route(): # Function that validates the route
    if type(route) is str: # Verify the parameter type
        if len(route) <= 2: # Verify if size's adequate
            if route in dest_code: # Verify if route is an valid entrie
                return 'Valid code!' # Allows the code to proceed
            else:
                return 'Invalid code entered, please insert again!' # Prevents the code to proceed, instructing the user
        else:
            return "You've inserted a too long code, please revise them." # Prevents the code to proceed, instructing the user
    else:
        print("You've entered a invalid value, please insert again.") # Prevents the code to proceed, instructing the user
        return TypeError


def dimensions_object(): # Function that calculate the volume of the packet
    volume: float = float(h * l * w) # Calculus of the volume formula
    vol_cost: float = 0 # Create the first return var - Cost of volume
    vol_tier: int = 0 # Create teh second return var - Volume tier of packet
    try:
        if volume < 1000: # Verify if the volume is tier 1
            vol_tier = 1
            vol_cost = 10 # Assign the cost of a tier 1 packet
        elif 1000 <= volume < 10000: # Verify if the volume is tier 2
            vol_tier = 2
            vol_cost = 20 # Assign the cost of a tier 2 packet
        elif 10000 <= volume < 30000: # Verify if the volume is tier 3
            vol_tier = 3
            vol_cost = 30 # Assign the cost of a tier 3 packet
        elif 30000 <= volume < 100000: # Verify if the volume is tier 3
            vol_tier = 4
            vol_cost = 50 # Assign the cost of a tier 4 packet
        else:
            print("You've  a too much bulky baggage, please redirect himself to the gate to be evaluated.") # Identify that user has a too bulky package, prevent the code to proceed
    finally:
        return volume, vol_cost, vol_tier # Returns the values of the function


def weight_object(): # Function that calculate the multiplier and tier of the package
    wei_mult: float = 0  # Var that will receive the multiplier based on weight
    wei_tier = 0  # Var that will receive the tier based on weight
    try:
        if 0 > weight < 0.1:  # Verify if the weight is tier one
            wei_mult = 1  # Assigns the multiplier of the tier
            wei_tier = 1
        elif 0.1 <= weight < 1:  # Verify if the weight is tier two
            wei_mult = 1.5  # Assigns the multiplier of the tier
            wei_tier = 2
        elif 1 <= weight < 10:  # Verify if the weight is tier three
            wei_mult = 2  # Assigns the multiplier of the tier
            wei_tier = 3
        elif 10 <= weight < 30:  # Verify if the weight is tier four
            wei_mult = 3  # Assigns the multiplier of the tier
            wei_tier = 4
        else:
            print('You have a too heavy baggage, please redirect himself to the gate to be evaluated.')  # Prevents the code to continue, and instruct the user
    finally:
        return wei_mult, wei_tier  # Return the function result parameters


def route_object():  # Function that set the multiplier based on the route selected
    try:
        mult_route: float = float(0)  # Var that will receive the multiplier of the route
        tier_route: int = 0  # Var that'll receive route tier
        if route == 'RS':  # Verify if route is Rio - SP
            mult_route = 1  # Assign the multiplier of tier one routes
            tier_route = 1
        elif route == 'SR':  # Verify if route is SP - Rio
            mult_route = 1  # Assign the multiplier of tier one routes
            tier_route = 1
        elif route == 'BS':  # Verify if route is BRA - SP
            mult_route = 1.2  # Assign the multiplier of tier two routes
            tier_route = 2
        elif route == 'SB':  # Verify if route is SP - BRA
            mult_route = 1.2  # Assign the multiplier of tier two routes
            tier_route = 2
        elif route == 'BR':  # Verify if route is BRA - RIO
            mult_route = 1.5  # Assign the multiplier of tier three routes
            tier_route = 3
        elif route == 'RB':  # Verify if route is Rio - BRA
            mult_route = 1.5  # Assign the multiplier of tier three routes
            tier_route = 3
    finally:
        return mult_route, tier_route  # Returns the two function result parameters

def main_calculation():  # Function that calculates the travel result
    global total
    total = ((vol_c * wei_m) * route_m) # Formula of the total result ((vol_cost * wei_mult) * route_mult)
    return total  # Returns the total


def src_dest(route):  # Function that identify the travel's source and destiny
    code = route  # Assign the route choose by the user in a local var
    src: str = ''  # Create the source var
    dest: str = ''  # Create the destiny var
    if code[0] == 'R':  # Verify if the package comes from Rio
        src = 'Rio de Janeiro' # Assign Rio to source if true
    elif code[0] == 'S':  # Verify if the package comes from SP
        src = 'São Paulo'  # Assign SP to source if true
    elif code[0] == 'B':  # Verify if the package comes from BRA
        src = 'Brasilia'  # Assign BRA to source if true
    if code[1] == 'S':  # Verify if the package will gone to SP
        dest = 'São Paulo'  # Assign SP to destiny if true
    elif code[1] == 'B':  # Verify if the package will gone to BRA
        dest = 'Brasilia'  # Assign BRA to destiny if true
    elif code[1] == 'R':  # Verify if the package will gone to Rio
        dest = 'Rio de Janeiro'  # Assign RIO to destiny if true
    return src, dest  # Returns function result vars

# Main program:
while True: # Open a infinite loop
    val_d = '' # Create a reference to break the input of dimensions
    while val_d != 'Valid parameters!': # Condition to input can be stopped
        try:
            h: float = float(input('Insert the height of the object: [cm] '))  # User will insert the package height
            l: float = float(input('Insert the length of the object: [cm] '))  # User will insert the package length
            w: float = float(input('Insert the width of the object: [cm] '))  # User will insert the package width
            val_d: str = val_dim(h, l, w)  # The control var receives the returns codes, if met the condition, continues the code
            print(val_d)
        except:
            print("You've entered an invalid value, only are allowed numeric values!\n Please Try again...")  # The user has inserted a non-numeric value
    val_w = ''  # Create a reference to break the input of weight
    while val_w != 'Valid weight.':  # Condition to input can be stopped
        try:
            weight: float = float(input('Insert the weight value: [kg] '))  # User will insert the package weight
            val_w: str = val_weight()  # The control var receives the returns codes, if met the condition, continues the code
            print(val_w)
        except:
            print("You've entered an invalid value, only are allowed numeric values!\n Please Try again...")  # User has inserted a non-numeric value
    e = 0  # Control var to print all routes
    while e < len(dest_code):  #  Rope the print all routes, while the control var is less than the total codes
        print('Code: {} - Route: {}'.format(dest_code[e], dest_descr[e]))  # Print the code and the route, on next the user choose a option
        e += 1  # Count plus one to control var
    val_r = ''  # Create a control var to the rope of route
    while val_r != 'Valid code!':  # Continues to request while there be inserted invalid values
        try:
            route: str = input('Insert the destiny wanted: [RS] ')  # Receives the route desired
            val_r: str = val_route()  # Control var receives the returns codes from validation route function
            print(val_r)  # Shows the result of the control var
        except:
            print("You've entered an invalid value, only are allowed alphabetic characters!\n Please Try again...")  # User has inserted a non-numeric value
    vol, vol_c, vol_t = dimensions_object()  # Receives from the function that calculates the main volume proprietes the volume, volume_cost and volume_tier var
    wei_m, wei_t = weight_object()  # Receives from the function that calculates the main weight proprietes the weight_multiplier and weight_tier var
    route_m, route_t = route_object()  # Receives from the function that calculates the main route proprietes the route_multiplier and route_tier var
    tot = main_calculation()  # Receives the total of the travel
    source, destiny = src_dest(route)  # Receives the source and destiny of the travel
    print("The travel with source: {} and destiny: {}.\nHave a total value of: R$ {:.2g}".format(source, destiny, tot))  # Show the informations of the travel as: source, destiny and totol
    print("With the following characteristics: \n Volume: {:.1g} cm³ with the cost of: R$ {:.2g} and be in the: {:.0g}º volume tier\n" # Show some characteristics of the travel as volume, volume cost and volume tier 
          " the weight was: {:.2g} kg with the: {:.1g}º weight tier".format(vol, vol_c, vol_t, weight, wei_t))  # Shows some characteristics of the travel as: weight and weight tier
    ctn:str = input('Do you want to continue: [Y]\[N] ')  # Control if the user wants to simulate other travel
    if ctn not in 'Yy':  # Verify if users wants to simulate other travel
        print('Finishing...')  # Show the finish advice
        break  # Ends the code