from product_manager import create_product , read_all ,read_by_id
from product_manager import products , update , delete_by_id
from product import Product
def menu():
    message = '''
1 - Create product
2 - Read All Product
3 - Read by Id
4 - Update
5 - Delete
6 - Exit / Logout
'''
    choice = int(input(message))
    if choice == 1:
        name = input('Name : ')
        description = input('Description: ')
        category = input('Category : ')
        tags = input('Tags : ')
        stock = input('Stock : ')
        price = input('Price : ')
        id = -1

        product = Product(id,name , description, category,tags,stock,price)
        create_product(product)
        print("Product Created successfully.")

    elif choice == 2:
        products = read_all()
        print("Product: ")
        for product in products:
            print(product)
            
    elif choice == 3:
        id = int(input("Id : "))
        product = read_by_id(id)
        if product == None:
            print("Product not Found")
        else:
            print(product)
    elif choice == 4:
        id = int(input("ID : "))
        old_product = read_by_id(id)
        if old_product == None:
            print("Product not Found ")
        else :
            print(old_product)
            name = input('Name : ')
            description = input('Description: ')
            category = input('Category : ')
            tags = input('Tags : ')
            stock = input('Stock : ')
            price = input('Price : ')
            new_product = Product(id,name , description, category,tags,stock,price)
            update(new_product)
            print("Product Updated Successfully")
    elif choice == 5:
        id = int(input("ID : "))
        old_product = read_by_id(id)
        if old_product == None:
            print("Product not Found ")
        else :
            print('old_product')
            if input("Are you sure want to delete(y/n) ?") == 'y':
                delete_by_id(id)
                print("Product deleted Successfully")
    return choice

def menus():
    print("Salary management App")
    choice = menu()
    while choice != 6:
        choice = menu()
    print("Thank you for using app.")
menus()