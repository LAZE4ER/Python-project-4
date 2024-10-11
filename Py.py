

def read_products_list(file):
    products_list = {}
    with open(file, 'r') as f:
        for line in f:
            prod,quant = line.strip().split(',')
            products_list[prod] = int(quant)
    return products_list


def write_products_list(file, products_list):
    
    with open(file, 'w' ) as f:
        for prod, quant in products_list.items():
            f.write(f'{prod},{quant}\n')



def add_products(products_list):
    prod = input('Введіть назву продукту:')
    quant = int(input('Введіть кількість продукту:'))
    products_list[prod] = quant
    print('Продукт успішно додано до списку')
    
    
    file = 'Products.txt'
    write_products_list(file, products_list )

def view_products(products_list):
    if len(products_list) >= 1:
        print('Список покупок:')
        for prod,quant in products_list.items():
            print(f'{prod},{quant}')
    else:
        print('Список пустий')
        
def edit_products(products_list):
    prod = input('Який продукт ви хочете відредагувати?')
    if prod in products_list:
        new_quant = int(input('Введіть нову кількість:'))
        products_list[prod] = new_quant
        print('Успішно')
    else:
        print('Продукт не знайдено')
        
def delete_products(products_list):
    prod = input('Введіть назву продукту який хочете видалити:')
    if prod in products_list:
        del products_list[prod]
        print('Успішно')
    else:
        print('Продукт не знайдено')
        
    file = 'Products.txt'
    write_products_list(file, products_list )
    
    
    
def menu():
    file = 'Products.txt'
    products_list = read_products_list(file)
    
    while True:
        
        inp = int(input('Що ви хочете зробити (1 - додати продукти , 2 - подивитися наявний список продуктів, \n3 - редагувати продукти, 4 - видалити продукти, 0 - вийти  )'))
        if inp == 1:
            add_products(products_list)   
        elif inp == 2:
            view_products(products_list)
        elif inp == 3:
            edit_products(products_list)
        elif inp == 4:
            delete_products(products_list)
        elif inp == 0:
            break
        else:
            print('Невірно вказано число')
    
         
menu()
