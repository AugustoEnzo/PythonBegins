from typing import Any  # Importing Any type to be used inside a list set
from selenium import webdriver # Importing webdriver to query the actual currencies
from selenium.webdriver.common.by import By # Import By to find a element in a web page

tot_converted = 0


def get_real(): # Gets the Actual currency of Brazilian Real (BRL)
    driver = webdriver.Chrome() # Select a webdriver
    id = "zci--currency-amount-right" # Set an ID to find elements

    driver.get("https://duckduckgo.com/?q=dollar+to+real&t=brave&ia=currency") # Access this URL though webdriver
    driver.implicitly_wait(1) # Wait one second

    input_dollars: float = float(driver.find_element(by=By.ID, value=id).get_attribute("value")) # Keeps the currency in a var

    driver.quit() # Close the web driver
    return input_dollars # Returns the currency


def get_dollars(): # Gets the Actual currency of United States Dollar (USD)
    driver = webdriver.Chrome() # Select a webdriver
    id = "zci--currency-amount-right" # Set an ID to find elements

    driver.get("https://duckduckgo.com/?q=real+to+dollar&t=brave&ia=currency") # Access this URL though webdriver
    driver.implicitly_wait(1) # Wait one second

    input_real:float = float(driver.find_element(by=By.ID, value=id).get_attribute("value")) # Keeps the currency in a var

    driver.quit() # Close the web driver
    return input_real # Returns the currency


ru = 3987863
print('XYZ Bikes - Stock Control Software')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

piece_data: dict[str, list[Any]] = {'Client ID': [], 'Piece ID': [], 'Piece Name': [], 'Manufacturer Name': [],
                                    'Piece value': [], 'Currency':[], 'Converted Value':[]} # This dict keeps all the data from the program


def valid_pic_name(piece_nm):  # Function that validates piece name
    c_space = 0
    pic_nm = piece_nm
    if len(pic_nm) > 0 and len(pic_nm) <= 50: # Valid if the length of piece name is too short or too large
        for c in range(len(pic_nm)): # Verify for each character if the piece name is made only by spaces
            if pic_nm[c] == ' ':
                c_space += 1
        if c_space == len(pic_nm): # Validate if the piece name is made only by spaces
            return 'You have inserted only spaces in the piece name.'
        else:
            return 'Valid piece name!'
    else:
        if len(pic_nm) == 0: # Validate if the piece name is empty
            return 'You have a null piece name'
        elif len(pic_nm) > 50: # Validate if the piece name if larger than fifty characters
            return "Certainly you don't need a piece with more than fifty characters, please insert it again."


def valid_manuf_nm(manufacturer_nm): # Function that validate the manufacturer name
    c_space = 0
    manuf_nm = manufacturer_nm
    if len(manuf_nm) > 0 and len(manuf_nm) <= 80: # Validate if the length of the manufacturer name is bigger than 0 and shorter than 80 characters
        for c in range(len(manuf_nm)): # Verify for each character if the manufacturer name is made only by spaces
            if manuf_nm[c] == ' ':
                c_space += 1
        if c_space == len(manuf_nm): # Validate if the piece name is made only by spaces
            return "You've inserted only spaces in the manufacturer name."
        else:
            return 'Valid manufacturer name!'
    else:
        if len(manuf_nm) == 0: # Validate if the piece name is empty
            return 'You have a null manufacturer name.'
        elif len(manuf_nm) > 80: # Validate if the piece name if larger than eighty characters
            return "Certainly you don't need a manufacturer name bigger than eighty characters, please insert it again."


def valid_p_value(piece_value, currency): # Function that validate the piece value
    global conv_value
    pc_value = piece_value
    cond = ''
    if 0 > pc_value <= 50000:  # Validate if the value of the piece is Smaller than 50000 and bigger than 0:
        cond = 'Valid piece value!'
    else: # If no valid
        if pc_value < 0: # Verify if the value of the piece is smaller than 0
            cond = "You've inserted a negative value, please insert it again."
        elif pc_value > 50000: # Verify if the value of the piece is bigger than 50000
            cond = "Certainly you don't need a piece value bigger than fifty thousands dollars, please insert it again."
    if len(currency) == 2: # Verify if the length of the currency is equal 2
        if currency == 'US': # Verify if the currency is USD
            us_price = get_dollars() # Gets the currency from the function get_dollars and assign to a var
            conv_value = piece_value * us_price # Calculates the value converted
            cond = "Valid piece value!"
        elif currency == 'BR': # Verify if the currency is BRL
            br_price = get_real() # Gets the currency from the function get_real and assign to a var
            conv_value = piece_value * br_price # Calculates the value converted
            cond = "Valid piece value!"
        else:
            cond = "Your condition need to be exactly the same at one of the options US or BR."
    else:
        cond = "Your condition need to be exactly the same at one of the options US or BR."
    return cond, conv_value


def register_piece(cl_id): # Function that register the values
    global piece_name, currency, tot_converted, piece_vle, manufacturer_nm
    piece_id: int = 1
    client_id = cl_id
    while True: # Starts an infinite loop
        val_p_name = ''
        piece_nm = ''
        print("Your Client ID is: {}\nYour Piece ID is: {}".format(client_id, piece_id)) # Makes a print of the client ID and Piece ID for this piece
        while val_p_name != 'Valid piece name!':  # starts and continue a loop where the condition returned by the validate function is not accomplished
            piece_nm = str(input('Insert your piece name: [Carter] ')) # Input the piece name
            val_p_name = valid_pic_name(piece_nm) # the validation function validates the name and return a condition for it
            print(val_p_name) # Shows the condition returned
        val_m_name = ''
        while val_m_name != 'Valid manufacturer name!': # starts and continue a loop where the condition returned by the validate function is not accomplished
            manufacturer_nm = str(input('Insert the manufacturer name: [Armor] ')) # Input the manufacturer name
            val_m_name = valid_manuf_nm(manufacturer_nm)  # the validation function validates the name and return a condition for it
            print(val_m_name) # Shows the condition returned
        val_p_vle = ''
        while val_p_vle != 'Valid piece value!': # starts and continue a loop where the condition returned by the validate function is not accomplished
            piece_vle = float(input('Insert your piece value: ')) # Input the piece value
            currency = str(input('Input the currency that you want to convert: [US/BR]')) # Select a currency to convert the value
            val_p_vle, tot_converted = valid_p_value(piece_vle, currency) # The validation function validates the value and returns condition and total converted
            print(val_p_vle) # Shows the condition
        piece_data['Client ID'].append(client_id) # Append the client id to the database
        piece_data['Piece ID'].append(piece_id) # Append the piece id to the database
        piece_data['Piece Name'].append(piece_nm) # Append the piece name to the database
        piece_data['Manufacturer Name'].append(manufacturer_nm) # Append the manufacturer name to the database
        piece_data['Piece value'].append(piece_vle) # Append the piece value to the database
        piece_data['Currency'].append(currency) # Append the currency to the database
        piece_data['Converted Value'].append(tot_converted) # Append the Total Converted value to the database
        piece_id += 1 # Add 1 to the next piece
        cont: str = str(input('Do you want to continue: [y/n] ')) # Asks if the user wants to continue
        if cont.upper() != 'Y':  # Verify if the user wants to continue
            print('Finishing this step...') # Shows the finishing dialog
            break
    client_id += 1 # Add one to the client id


def query_piece(): # Function that query the database
    while True: # Starts an infinite loop
        print("{} Query Database Menu: {}".format('-' * 20, '-' * 20))
        print('[1] - Query all pieces \n[2] - Query pieces by piece name \n[3] - Query pieces by code \n[4] - Query '
              'pieces per Manufacturer \n[5] - Return') # Shows the menu options
        menu_q: int = int(input('Select the option that you want to query the database: [1|2|3|4|5] ')) # Ask what's the option of the user
        print("{} Query Database Selected: {}".format('-' * 30, '-' * 30))
        if menu_q == 1: # Verify if he wants to see al pieces
            p_id_list: list = piece_data['Piece ID'] # Assign the Piece ID list to a var
            for i in range(0, len(p_id_list), 1): # print each item in the database
                print('Client ID: {} | Piece ID: {} |Piece Name: {} | Manufacturer Name: {} | Piece value: {:.2f} | Currency: {} | Converted Value: {}'.format(
                    piece_data['Client ID'][i],
                    piece_data['Piece ID'][i],
                    piece_data['Piece Name'][i],
                    piece_data['Manufacturer Name'][i],
                    piece_data['Piece value'][i],
                    piece_data['Currency'][i],
                    piece_data['Converted Value'][i]))
            continue
        elif menu_q == 2: # Verify if he wants to query by piece name
            p_nm: list = piece_data['Piece Name'] # Assigns the Piece Name list to a var
            while True: # Starts a infinite loop
                inp_p_nm: str = str(input('Insert the piece name that you want to search for: [Carter] ')) # Input the piece name to search
                print("{} Query Database Result: {}".format('-' * 30, '-' * 30))
                if inp_p_nm in p_nm: # Verify if the piece name searched is on the database
                    for i in range(0, len(p_nm), 1):  # Verify each item in the database
                        if inp_p_nm == p_nm[i]: # if input equals to one item, print item
                            print(
                                'Client ID: {} | Piece ID: {} |Piece Name: {} | Manufacturer Name: {} | Piece value: {:.2f} | Currency: {} | Converted Value: {}'.format(
                                    piece_data['Client ID'][i],
                                    piece_data['Piece ID'][i],
                                    piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i],
                                    piece_data['Piece value'][i],
                                    piece_data['Currency'][i],
                                    piece_data['Converted Value'][i]))
                    cont: str = input("Do you want to continue searching [Y/N]") # Ask if the user wants to search for other piece name
                    if cont.upper != 'Y': # Validates the user choice
                        print('Finishing...')
                        break
                else: # if the item was not in the database
                    print("The piece name that you've entered was not located in the database, please insert again...") # Cond if not in the database
        elif menu_q == 3: # Verify if the user wants to query by piece code
            p_id_list: list = piece_data['Piece ID'] # Assign Piece ID list to a var
            while True: # Starts a infinite loop
                inp_p_id: int = int(input('Insert the product code that you want to search: [1] ')) # User's input the product code
                print("{} Query Database Result: {}".format('-' * 30, '-' * 30))
                if inp_p_id in p_id_list: # Verify if the product code searched is in the database
                    for i in range(0, len(p_id_list), 1): # Verify each item in the database
                        if inp_p_id == p_id_list[i]: # If the value searched is equal to value being readm print the item
                            print(
                                'Client ID: {} | Piece ID: {} |Piece Name: {} | Manufacturer Name: {} | Piece value: {:.2f} | Currency: {} | Converted Value: {}'.format(
                                    piece_data['Client ID'][i],
                                    piece_data['Piece ID'][i],
                                    piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i],
                                    piece_data['Piece value'][i],
                                    piece_data['Currency'][i],
                                    piece_data['Converted Value'][i]))
                    cont: str = input('Do you want to continue searching [Y/N]') # Ask if the user wants to continue
                    if cont.upper() != 'Y': # Validates the user choice
                        print('Finishing this step.')
                        break
                else: # If not in the database
                    print("The code you've inserted aren't in the database, please try again...") # Shows the else condition
        elif menu_q == 4: # If the user want to search by manufacturer name
            while True: # Starts an infinite loop
                inp_man_nm: str = str(input('Insert the manufacturer name: [ARMOR-IIMAK]')) # User inputs the manufacturer name
                print("{} Query Database Result: {}".format('-' * 30, '-' * 30))
                m_nm: list = piece_data['Manufacturer Name'] # Assign the manufacturer name list to a var
                if inp_man_nm in m_nm: # Verify if the manufacturer name is in the database
                    for i in range(0, len(m_nm), 1): # Read each item in the database
                        if inp_man_nm == m_nm[i]: # If user's manufacturer name is read, print the items with this manufacturer name
                            print(
                                'Client ID: {} | Piece ID: {} |Piece Name: {} | Manufacturer Name: {} | Piece value: {:.2f} | Currency: {} | Converted Value: {}'.format(
                                    piece_data['Client ID'][i],
                                    piece_data['Piece ID'][i],
                                    piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i],
                                    piece_data['Piece value'][i],
                                    piece_data['Currency'][i],
                                    piece_data['Converted Value'][i]))
                    cont: str = str(input("Do you want to continue: [Y/N]")) # Users choice to continue or not
                    if cont.upper() != 'Y': # Validate user's choice
                        print("Finishing this step.")
                        break
                else: # Else for item not in database
                    print(
                        "You've inserted a manufacturer name that doesn't are in the database, please insert it again.") # Cond if else is true
        elif menu_q == 5: # Selected if user wants to leave the query menu.
            print('Returning to main menu...')
            break


def remove_piece(): # Function that removes an item from database
    piece_code = piece_data['Piece ID'] # Assign piece code list to a var
    while True: # Starts an infinite loop
        rem_piec_cd: int = int(input('Insert the code of the piece that you want to remove: ')) # User's input the piece code to remove
        if rem_piec_cd in piece_code: # Verify is the item is in the database
            for code in piece_code: # Reads each item in the database
                if rem_piec_cd == piece_code[code]: # Verify if the read item have the code inserted by user, then print the item to confirm
                    print(
                        'Client ID: {} | Piece ID: {}|Piece Name: {} | Manufacturer Name: {} | Piece value: {:.2f} | Currency: {} | Converted Value: {}'.format(
                            piece_data['Client ID'][code],
                            piece_data['Piece ID'][code],
                            piece_data['Piece Name'][code],
                            piece_data['Manufacturer Name'][code],
                            piece_data['Piece value'][code],
                            piece_data['Currency'][code],
                            piece_data['Converted Value'][code]))
                    cond: str = str(input('Do you really want to delete this piece: [y][n]')) # Ask if the user really wants to delete this item
                    if cond.upper() == 'Y': # Delete item if condition is True
                        piece_data['Client ID'].remove(piece_data['Client ID'][code])
                        piece_data['Piece ID'].remove(piece_data['Piece ID'][code])
                        piece_data['Piece Name'].remove(piece_data['Piece Name'][code])
                        piece_data['Manufacturer Name'].remove(piece_data['Manufacturer Name'][code])
                        piece_data['Piece value'].remove(piece_data['Piece value'][code])
                        piece_data['Currency'].remove(piece_data['Currency'][code])
                        piece_data['Converted Value'].remove(piece_data['Converted Value'][code])
        else: # Else condition for item's not in the database
            print("Your code hasn't in the database, please verify it and try again...") # Shows else condition return
            continue
        cont: str = str(input("Do you want to remove another piece: [y|n]")) # Ask if users wants to remove other item
        if cont.upper() != 'Y': # Verify the user's choice for delete other item
            print('Finishing the delete module...')
            break


# Main program:
client_id = 1 # Assign value to id var
piece_id = 0 # Assign value to id var
while True: # Starts an infinite loop
    print("{} | MENU | {}".format('-' * 20, '-' * 20))
    print(" [1] - Register Piece \n [2] - Query Piece \n [3] - Remove Piece \n [4] - Exit") # Shows Main Menu
    m_menu: int = int(input("Insert the job that you want to do: ")) # Ask user's to input what he wants to do
    if m_menu == 1: # Validate if user's choice is to Register a piece
        register_piece(client_id) # Calls function that register items
        client_id = piece_data['Client ID'][-1] # Assign the new code to id var
        piece_id = piece_data['Piece ID'][-1] # Assign the new code to id var
        continue
    elif m_menu == 2:  # Validate if user's choice is to Query an item
        query_piece() # Call the function that search for items
        continue
    elif m_menu == 3:  # Validate if user's choice's to remove an item
        remove_piece() # Call the function that remove items
        continue
    elif m_menu == 4: # Validate if user's choice's to Exit the program
        print("Exiting the program...") # Show finishing messages
        print("Thanks for the use.")
        break # Ends the program
