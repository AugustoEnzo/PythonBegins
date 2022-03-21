ru = 3987863
print('Sales application of X Company .Inc')
print('Made by Enzo Augusto Lima Brasil ', 'RU:', ru)

sales_amount_disc = 0.0 # Total amount of sales with discount
sales_amount = 0.0 # Absolute total amount of sales
sales_qtt = 0 # Total quantity of sales
prod_name = '' # Name of product
prod_amt = 0.0 # Amount of product
prod_qtt = 0 # Quantity of a product
prod_disc = 0.0 # Total amount of a product with discount
total_prod = 0 # Absolute amount of product
total_disc = 0 # amount with discount of product based on the quantity

while True:
    prod_name = input('Insert the name of the product: ')
    prod_amt = float(input('Insert the unitary amount of the product: [R$ 1.99] '))
    prod_qtt = int(input('Insert the quantity that you want of the product: '))
    if prod_qtt <= 9:
        total_prod = prod_amt * prod_qtt  # Amount total of a product without discount
        sales_qtt += prod_qtt # Keeping the sales quantity register of all the history of the program
        sales_amount += prod_amt # Keeping the absolute sales amount register of all the history of the program
        print('The product: {}\n'
              'With value: R$ {}\n'
              'And the amount of: {}\n'
              'Have the absolute total of: R$ {}'.format(prod_name, prod_amt, prod_qtt, total_prod))
    elif prod_qtt > 9:
        if prod_qtt > 9 and prod_qtt < 100:
            prod_disc = prod_amt - (prod_amt * 0.05) # Calculate the unitary product discount
            total_disc = prod_disc * prod_qtt # Total amount of product with amount discount multiplied by quantity
            total_prod = prod_amt * prod_qtt # Total absolute amount of product with amount multiplied by quantity
            sales_qtt += prod_qtt # Keeping the sales quantity register of all the history of the program
            sales_amount += (prod_amt * prod_qtt) # Keeping the absolute sales amount register of all the history of the program
            sales_amount_disc += (prod_disc * prod_qtt) # Keeping the discounted sales amount register of all the history of the program
            print('The product: {}\n'
                  'With value: R$ {}\n'
                  'Have the unitaty value with discount: {}\n'
                  'And the amount of: {}\n'
                  'Have the absolute total of: R$ {}\n'
                  'And the total amount with discount of: R$ {}'
                  .format(prod_name, prod_amt, prod_disc, prod_qtt,total_prod, total_disc))
        elif prod_qtt > 100 and prod_qtt < 1000:
            prod_disc = prod_amt - (prod_amt * 0.1) # Calculate the unitary product discount
            total_disc = prod_disc * prod_qtt # Total amount of product with amount discount multiplied by quantity
            total_prod = prod_amt * prod_qtt # Total absolute amount of product with amount multiplied by quantity
            sales_qtt += prod_qtt # Keeping the sales quantity register of all the history of the program
            sales_amount += (prod_amt * prod_qtt) # Keeping the absolute sales amount register of all the history of the program
            sales_amount_disc += (prod_disc * prod_qtt) # Keeping the discounted sales amount register of all the history of the program
            print('The product: {}\n'
                  'With value: R$ {}\n'
                  'Have the unitaty value with discount: {}\n'
                  'And the amount of: {}\n'
                  'Have the absolute total of: R$ {}\n'
                  'And the total amount with discount of: R$ {}'
                  .format(prod_name, prod_amt, prod_disc, prod_qtt, total_prod, total_disc))
        elif prod_qtt >= 1000:
            prod_disc = prod_amt - (prod_amt * 0.15) # Calculate the unitary product discount
            total_disc = prod_disc * prod_qtt # Total amount of product with amount discount multiplied by quantity
            total_prod = prod_amt * prod_qtt # Total absolute amount of product with amount multiplied by quantity
            sales_qtt += prod_qtt # Keeping the sales quantity register of all the history of the program
            sales_amount += (prod_amt * prod_qtt) # Keeping the absolute sales amount register of all the history of the program
            sales_amount_disc += (prod_disc * prod_qtt) # Keeping the discounted sales amount register of all the history of the program
            print('The product: {}\n'
                  'With value: R$ {}\n'
                  'Have the unitaty value with discount: {}\n'
                  'And the amount of: {}\n'
                  'Have the absolute total of: R$ {}\n'
                  'And the total amount with discount of: R$ {}'
                  .format(prod_name, prod_amt, prod_disc, prod_qtt, total_prod, total_disc))
    else:
        print('You ve entered a invalid number, please try again...')
    prog = input('Do you want to continue ? [Y][N]')
    if prog not in 'Yy':
        print('Finishing...')
        break

print('The total history amount of sales: R$ {}'.format(sales_amount))
print('The total history amount of sales with discount: R$ {}'.format(sales_amount_disc))
print('The total history quantity of sales: {}'.format(sales_qtt))