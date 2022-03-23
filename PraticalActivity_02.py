ru = 3987863
print('Application of Y Cafeteria')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)
i = 0
id = [100, 101, 102, 103, 104, 105, 200, 201] # Identificator of items
desc = ['Hot Dog', 'Double Hot dog', 'X-Egg', 'X-Salad', 'X-Bacon', 'X-Everything', 'Soda Tin', 'Cold Tea'] # Items
value = [9.00, 11.00, 12.00, 13.00, 14.00, 17.00, 5.00, 4.00] # Value of items
order_data = {'Order Code':[], 'Item':[], 'Value':[]} # Keeping data of items ordered
cod = 0 # Variable that keeps the cod of item ordered
count =0 # Count of Orders

def s_code(p1): # Function that lookup for the code of the item ordered in the list
    cd = p1 # cd receives the parameter
    for i in range(0, len(id), 1): # a repeat structure is executed for each value of i in the lenght of id, with the step of one
        if int(cd) not in id: # Valid if the code inputed is in the id list, if not in returns 'Invalid Option'
            return 'Invalid Option'
        elif int(cd) == id[i]: # If the code is in the id list, returns the values with the code, description as the item, and the value by the item
            return ['Code: ',id[i],'Description: ', desc[i],'Value: ', value[i]]
        else:
            continue

def take_info(p1): # Function that takes the information from the temporary list that keeps the information by the order
    if type(p1) is list: # Valid if the parameter type is list
        inf = p1 # Assign the parameter to the variable info
        n_inf = inf[3] # Takes the item name from the temporary data
        a_inf = inf[5] # Takes the amount value from the temporary data
        return [n_inf, a_inf]

def calc_amount(): # Create the function that calculate the result sum of all orders values
    values = order_data['Value'] # Assign the absolute values data into a variable values
    sum_amount: float = 0 # Create the variable that will receive the sum of amount
    amount = 0 #  Create the variable that will receive the temporary values to be keeped in the sum_amount variable
    c = 0 # Create a count variable
    while c != len(values): # Create the repeate structure that continues when c is different from the length of variable values
        amount = values[c] # Assign the specific values of each order to the variable amount
        sum_amount += amount # Keeps the sum of amounts
        c += 1 # Plus 1 to the count var
    return sum_amount # To finish the function returns the value of sum_amount var

def s_order(): # Create the function that searc for a order
    t0 = order_data['Order Code'] # Assign all order codes to a temporary var called t0
    t1 = order_data['Item'] # Assign all order item names to a temporary var called t1
    t2 = order_data['Value'] # Assign the order values to a temporary var called t2
    e = 0 # Create a count var
    while e < len(t0): # Create a rope with execute a instruction to each value while the count var is less than the lenght of t0
        print('Code: {} | Item: {} | Value: {}'.format(t0[e], t1[e], t2[e])) # for each value in the length of t0 the function will print: The code of product ordered, the item name and the value
        e += 1 # The count var plus 1 to each t0 value printed

while True: # Start the main code with a infinity loop
    print('Select a option with the code: ') # print the introduction to the first command
    for i in range(0, len(id), 1): # Starts the rope that print the selection menu to the user
        print('Code: {} | Description: {} | Value: {}'.format(id[i], desc[i], value[i])) # print the menu of items to the user with: code, description and value
    cod = int(input('Insert the code of your product: [0 to Exit] ')) # Call the user to action inserting the code of the desired item, especifing that 0 is the option to exit
    if cod != 0: # Valid if the user wants to continue, if he've inserted 0 or no
        count += 1 # Plus one to the var that count the amount of items ordered
        print('- -' * 20) # Effects of separation
        info = s_code(cod) # Assign to the info var the returns of s_code function
        print("You've selected: ") # Introduct the user to the next step
        if type(info) is list: # Valid if the info is a list or a string
            print('Code: {} | Description: {} | Value: {}'.format(info[1], info[3], info[5])) # Print the item selected now, containing code, description and value
            print('- -' * 20)  # Effect of separation
            order = take_info(info) # Call the function that takes the info from the orders and assing the return to a transaction var, that hold the data that will be transfered to the order_data dictionary, with the absolute data
            order_data['Order Code'].append(count)  # Append the count of orders to order_data
            order_data['Item'].append(order[0])  # Append the item name to order_data
            order_data['Value'].append(order[1])  # Append the item value to order_data
            prog = input('Do you want to continue: [Y][N]')  # Ask if the user wants to make a new order
            if prog not in 'Yy':  # Valid if the user wants to continue ordering and continue the program loop, if not break the infinity loop and finish the program
                print('Finishing...')
                break
            continue
        else:
            print('- -' * 20)  # Effect of separation
            print(info) # print the error return of the function and returns to begin of the program
            print('Try Again...') # Encourage the user to try again
            print('- -' * 20)  # Effect of separation
            continue
    elif cod == 0: # Valid if the user wants to finish the program before selecting a item, if yes (insert 0) break the infinite loop and finishe the program, else continue ordering
        print('Finishing...')
        break

tot_amount = calc_amount() # Call the function that calculate the sum of all amounts
print('The total amount of you order is: {}'.format(tot_amount)) # Shows the ordering final sum
print("You ve ordered: ") # Introduces the user to the next step, that will show all orders
s_order() # Call the function that shows all orders