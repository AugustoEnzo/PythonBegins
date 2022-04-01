from typing import Any

from selenium import webdriver
from selenium.webdriver.common.by import By
tot_converted = 0


def get_dollars():
    driver = webdriver.Chrome()
    id = "zci--currency-amount-right"

    driver.get("https://duckduckgo.com/?q=dollar+to+real&t=brave&ia=currency")
    driver.implicitly_wait(1)

    input_dollars = driver.find_element(by = By.ID, value=id).get_attribute("value")

    driver.quit()
    return input_dollars

def get_real():
    driver = webdriver.Chrome()
    id = "zci--currency-amount-right"

    driver.get("https://duckduckgo.com/?q=real+to+dollar&t=brave&ia=currency")
    driver.implicitly_wait(1)

    input_real = driver.find_element(by=By.ID, value=id).get_attribute("value")

    driver.quit()


ru = 3987863
print('XYZ Bikes - Stock Control Software')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

piece_data: dict[str, list[Any]] = {'Client ID':[], 'Piece ID':[], 'Piece Name':[], 'Manufacturer Name':[],'Piece value':[]}


def valid_pic_name(piece_nm):
    c_space = 0
    pic_nm = piece_nm
    if 0 > len(pic_nm) <= 50:
        for c in range(pic_nm):
            if pic_nm[c] == ' ':
                c_space += 1
        if c_space == len(pic_nm):
            return 'You have inserted only spaces in the piece name.'
        else:
            return 'Valid piece name!'
    else:
        if len(pic_nm) == 0:
            return 'You have a null piece name'
        elif len(pic_nm) > 50:
            return "Certainly you don't need a piece with more than fifty characters, please insert it again."


def valid_manuf_nm(manufacturer_nm):
    c_space = 0
    manuf_nm = manufacturer_nm
    if 0 > len(manuf_nm) <= 80:
        for c in range(manuf_nm):
            if manuf_nm[c] == ' ':
                c_space += 1
        if c_space == len(manuf_nm):
            return "You've inserted only spaces in the manufacturer name."
        else:
            return 'Valid manufacturer name!'
    else:
        if len(manuf_nm) == 0:
            return 'You have a null manufacturer name.'
        elif len(manuf_nm) > 80:
            return "Certainly you don't need a manufacturer name bigger than eighty characters, please insert it again."


def valid_p_value(piece_value, currency):
    global conv_value
    pc_value = piece_value
    cond = ''
    if 0 > pc_value <= 50000:
        cond = 'Valid piece value!'
    else:
        if pc_value < 0:
            cond = "You've inserted a negative value, please insert it again."
        elif pc_value > 50000:
            cond = "Certainly you don't need a piece value bigger than fifty thousands dollars, please insert it again."
    if len(currency) == 2:
        if currency == 'US':
            us_price = get_dollars()
            conv_value = piece_value * us_price
        elif currency == 'BR':
            br_price = get_real()
            conv_value = piece_value * br_price
    else:
        cond = "Your condition need to be exactly the same at one of the options US or BR."
    return cond, conv_value


def register_piece(cl_id, p_id):
    global piece_vle, currency, manufacturer_nm
    piece_id: int = p_id
    client_id = cl_id
    while True:
        val_p_name = ''
        piece_nm = ''
        while val_p_name != 'Valid piece name!':
            piece_nm = str(input('Insert your piece name: '))
            val_p_name = valid_pic_name(piece_nm)
            print(val_p_name)
        val_m_name = ''
        while val_m_name != 'Valid manufacturer name!':
            manufacturer_nm = str(input('Insert the manufacturer name: US$ '))
            val_m_name = valid_manuf_nm(manufacturer_nm)
            print(val_m_name)
        val_p_vle = ''
        while val_p_vle != 'Valid piece value!':
            piece_vle: float = float(input('Insert your piece value: '))
            currency: str = str(input('Input the currency that you want to convert: [US/BR]'))
            val_p_vle, tot_converted = valid_p_value(piece_vle, currency)
            print(val_p_vle)
        piece_id += 1
        piece_data['Client ID'].append(client_id)
        piece_data['Piece ID'].append(piece_id)
        piece_data['Piece Name'].append(piece_nm)
        piece_data['Manufacturer Name'].append(manufacturer_nm)
        piece_data['Piece value'].append(piece_vle)
        cont: str = str(input('Do you want to continue: [y/n] '))
        if cont.upper() != 'Y':
            print('Finishing this step...')
            break
    client_id += 1

def query_piece():
    while True:
        print('[1] - Query all pieces \n [2] - Query pieces by piece name \n [3] - Query pieces by code \n [4] - Query '
              'pieces per Manufacturer \n [5] - Return')
        menu_q: str = input('Select the option that you want to query the database: [1|2|3]')
        if menu_q == 1:
            for i in range(0, len(piece_data['Client Id']), 1):
                print('Client ID: {} | Piece Name: {} | Manufacturer Name: {}| Piece value: {}'.format(
                    piece_data['Client Id'[i]],
                    piece_data['Piece Name'][i],
                    piece_data['Manufacturer Name'][i],
                    piece_data['Piece value'][i]))
        elif menu_q == 2:
            p_nm: list = piece_data['Piece Name']
            while True:
                inp_p_nm: str = str(input('Insert the piece name that you want to search for: [Carter]'))
                if inp_p_nm in p_nm:
                    for i in range(0, len(p_nm), 1):
                        if currency == 'US':
                            print("Client ID: {} | Piece Name: {} | Manufacturer Name: {}| Piece value: US$ {:.2f}".format(
                                piece_data['Client Id'[i]],
                                piece_data['Piece Name'][i],
                                piece_data['Manufacturer Name'][i],
                                piece_data['Piece value'][i]))
                        elif currency == 'BR':
                            print("Client ID: {} | Piece Name: {} | Manufacturer Name: {}| Piece value: RS$ {:.2f}".format(
                                piece_data['Client Id'[i]],
                                piece_data['Piece Name'][i],
                                piece_data['Manufacturer Name'][i],
                                piece_data['Piece value'][i]))
                    cont: str = input("Do you want to continue searching [Y/N]")
                    if cont.upper != 'Y':
                        print('Finishing...')
                        break
                else:
                    print("The piece name that you've entered was not located in the database, please it again...")
        elif menu_q == 3:
            c_id: list = piece_data['Client Id']
            while True:
                inp_c_id: int = int(input('Insert the code that you want to search: [1]'))
                if inp_c_id in c_id:
                    for i in range(0, len(piece_data['Client Id']), 1):
                        if inp_c_id == c_id[i]:
                            if currency == 'US':
                                print("Client ID: {} | Piece Name: {} | Manufacturer Name: {}| Piece value: US$ {:.2f}".format(
                                    piece_data['Client Id'[i]],
                                    piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i],
                                    piece_data['Piece value'][i]))
                            elif currency == 'BR':
                                print("Client ID: {} | Piece Name: {} | Manufacturer Name: {}| Piece value: RS$ {:.2f}".format(
                                    piece_data['Client Id'[i]],
                                    piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i],
                                    piece_data['Piece value'][i]))
                    cont: str = input('Do you want to continue searching [Y/N]')
                    if cont not in 'Yy':
                        print('Finishing...')
                        break
                else:
                    print("The code you've inserted aren't in the database, please try again...")
        elif menu_q == 4:
            while True:
                inp_man_nm: str = str(input('Insert the manufacturer name: [ARMOR-IIMAK]'))
                m_nm: list = piece_data['Manufacturer Name']
                if inp_man_nm in m_nm:
                    for i in range(0, len(m_nm), 1):
                        if inp_man_nm == m_nm[i]:
                            if currency == 'US':
                                print('Client ID: {} | Piece ID: {} | Piece Name: {} | Manufacturer Name: {} | Piece value: US$ {:.2f}'.format(
                                    piece_data['Client ID'][i], piece_data['Piece ID'][i], piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i], piece_data['Piece value'][i]))
                            elif currency == 'BR':
                                print('Client ID: {} | Piece ID: {} | Piece Name: {} | Manufacturer Name: {}| Piece value: RS$ {:.2f}'.format(
                                    piece_data['Client ID'][i], piece_data['Piece ID'][i], piece_data['Piece Name'][i],
                                    piece_data['Manufacturer Name'][i], piece_data['Piece value'][i]))
                            cont: str = str(input("Do you want to continue: [Y/N]"))
                            if cont.upper != 'Y':
                                print("Finishing this step...")
                                break
                else:
                     print("You've inserted a manufacturer name that doesn't are in the database, please insert it again.")
        elif menu_q == 5:
            print('Returning to main menu...')
            break


def remove_piece():
    piece_code = piece_data['Piece ID']
    while True:
        rem_piec_cd: str = str(input('Insert the code of the piece that you want to remove: '))
        if piece_code in piece_code:
            for code in piece_code:
                if rem_piec_cd == piece_code:
                    if currency == 'US':
                        print("Client ID: {} | Piece ID: {} | Piece Name: {} | Manufacturer Name: {} | Piece value: US$ {}".format(
                            piece_data['Client ID'][code], piece_data['Piece ID'][code], piece_data['Piece Name'][code],
                            piece_data['Manufacturer Name'][code], piece_data['Piece value'][code]))
                    elif currency == 'BR':
                        print("Client ID: {} | Piece ID: {} | Piece Name: {} | Manufacturer Name: {} | Piece value: RS$ {}".format(
                            piece_data['Client ID'][code], piece_data['Piece ID'][code], piece_data['Piece Name'][code],
                            piece_data['Manufacturer Name'][code], piece_data['Piece value'][code]))
                    cond: str = str(input('Do you really want to delete this piece: [y][n]'))
                    if cond.upper() == 'Y':
                        piece_data['Client ID'].remove(code)
                        piece_data['Piece ID'].remove(code)
                        piece_data['Piece Name'].remove(code)
                        piece_data['Manufacturer Name'].remove(code)
                        piece_data['Piece value'].remove(code)
        else:
             print("Your code hasn't in the database, please verify it and try again...")
             continue
        cont: str = str(input("Do you want to remove another piece: [y|n]"))
        if cont.upper() != 'N':
            print('Finishing the delete module...')
            break


# Main program:
client_id = 1
piece_id = 0
while True:
    print("{} | MENU | {}".format('-'*20, '-'*20))
    print(" [1] - Register Piece \n [2] - Query Piece \n [3] - Remove Piece \n [4] - Exit")
    m_menu:str = str(input("Insert the job that you want to do: "))
    if m_menu == 1:
        register_piece(client_id, piece_id)
        client_id = piece_data['Client ID'][-1]
        piece_id = piece_data['Piece ID'][-1]
        continue
    if m_menu == 2:
        query_piece()