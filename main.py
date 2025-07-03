from product_base import PRODUCT_BASE_1

credit = 0
inventory = []
inventory_base = []

KEYS = list(PRODUCT_BASE_1["products"]["no hanging"].keys())
VALUE = list(PRODUCT_BASE_1["products"]["no hanging"].values())

KEYS_H = list(PRODUCT_BASE_1["products"]["hanging"].keys())
VALUE_H = list(PRODUCT_BASE_1["products"]["hanging"].values())

def add_product():
    
    for i, product in enumerate(PRODUCT_BASE_1['products']):
        print(f"{i+1}. {product}")
    
    choice = input("\nYour choice: ")
     
    if choice == '1': # NO HANGING            
        no_hanging_add()        
    elif choice == '2':
        hanging_add()
    else:
        print("Exist only two choice")


def no_hanging_add():
    global credit
    global inventory
    global inventory_base
    
    while True:
        print("")
        for i, (product, value) in enumerate(PRODUCT_BASE_1['products']['no hanging'].items()): # ALL PRODUCTS IN NO HANGING
            print(f"{i+1}. {product} - {value}grn")
                    
        try:    
            choose_products = input("\nWhat will you take (press 'E' to exit): ")
                    
            if choose_products.upper() == 'E': # EXIT
                #print(inventory_base)
                break
                    
            choose_product = int(choose_products) # DETECTING EXCEPT
                    
            if choose_product <= 0 or choose_product > len(KEYS): # CHECKING OUT OF RANGE  (EXCEPT)
                print("Invalid choice, out of range")
                continue
                    
            user_choose = KEYS[choose_product - 1] # user choose
            user_credit = VALUE[choose_product - 1] # user credit
                    
            credit += user_credit # OVERALL SUM
            inventory.append(user_choose) # OVERALL PRODUCTS
            
            print(f"You taked {', '.join(inventory)}. Total cost {credit}grn!!!")
            
            inventory_base.append({"name": user_choose, "credit": user_credit})   
                           
        except ValueError: # CATCHING EXCEPT
            print("Error: value error") 
     
  
def hanging_add():
    global credit
    global inventory
    global inventory_base
    
    while True:
        print("")
        for i, (product, value) in enumerate(PRODUCT_BASE_1['products']['hanging'].items()): # ALL PRODUCTS IN NO HANGING
            print(f"{i+1}. {product} - {value}grn")

        try:
            choose_products = input("\nWhat will you take (press 'E' to exit): ")    
            if choose_products.upper() == 'E': # EXIT
                #print(inventory_base)
                break 
            
            gramm_product = int(input("How much (type in gramm): "))  
                                         
            choose_product = int(choose_products) # DETECTING EXCEPT  
               
            if choose_product <= 0 or choose_product > len(KEYS): # CHECKING OUT OF RANGE  (EXCEPT)
                print("Invalid choice, out of range")
                continue
            
            user_choose = KEYS_H[choose_product - 1]
            user_per_1kg = VALUE_H[choose_product - 1]
            new_value = int((user_per_1kg / 1000) * gramm_product)
            credit += new_value
            inventory.append(user_choose)
            
            print(f"You taked {', '.join(inventory)}. Total cost {credit}grn!!!")
            
            inventory_base.append({"name": user_choose, "credit": new_value})
               
        except ValueError:
            print("Error: value error")

            
def delete_product():
    global inventory_base
    global credit

    while True:
        if not inventory_base:
            print("Inventory is empty")
            break

        print("\n-- Current Inventory --")
        for i, item in enumerate(inventory_base):
            print(f"{i+1}. {item['name']} - {item['credit']}grn")

        user_input = input("Write number to delete (press 'E' to exit): ")

        if user_input.upper() == 'E':
            break

        try:
            user_del = int(user_input) - 1

            if user_del < 0 or user_del >= len(inventory_base):
                print("Invalid number, try again.")
                continue

            credit -= inventory_base[user_del]['credit']

            del inventory_base[user_del]

            print(f"\nUpdated total credit: {credit}grn")

        except ValueError:
            print("Enter a valid number.")

            
def main():
    
    while True:    
        print("\n-------- MARKET --------")
        print("1. Add products in inventory")
        print("2. Delete products from inventory")
        print("3. Exit")
        
        choice = input("\nChoose an options: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            print("See you again")
            break
        else:
            print("Your choice out of range")


main()