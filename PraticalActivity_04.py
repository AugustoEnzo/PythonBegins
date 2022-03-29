from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
id = "zci--currency-amount-right"

driver.get("https://duckduckgo.com/?q=dollar+to+real&t=brave&ia=currency")
driver.implicitly_wait(1)

input_dollars = driver.find_element(by = By.ID, value=id).get_attribute("value")

driver.quit()


ru = 3987863
print('XYZ Bikes - Stock Control Software')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

piece_data = {'Client Id':[], 'Piece Name':[], 'Manufacturer Name':[],'Piece value':[]}


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
    pc_value = piece_value
    if 0 > pc_value <= 50000:
        return pc_value * input_dollars
        


def register_piece(clt_id):
    client_id: int = clt_id
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
        val_p_vle = valid_p_value(piece_vle)
        print(val_p_vle)
    if val_p_name == 'Valid Name!':
        piece_data['Client Id'].append(client_id)
        piece_data['Piece Name'].append(piece_nm)
        piece_data['Manufacturer Name'].append(manufacturer_nm)
        piece_data['Piece value'].append(piece_vle)