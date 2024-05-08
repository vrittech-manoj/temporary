def search():
    search_keyword = input("what to search ? #>>>...")
    print(f"searchin {search_keyword} .... ")
    file_obj = open("products_datasets.txt","r")
    total_lines = file_obj.readlines()
    for line in total_lines:
        if search_keyword in line:
            print(" search found ! ")
            product = line.split(",") 
            product_name = product[0]
            product_brand = product[1]
            product_price = product[2]
            print(f"prouct name:{product_name}  product_brand:{product_brand}   product_price:{product_price}")

def display():
    print("""
    WELCOME TO KTM ELECTRONICS!!!
    ***************************************************
        Please select Menu 
    type 1 for store  products
    type 2 for display products
    type 3 for search products
    type 4 for delete products

        
    **************************************************"""
    )
while True:
    display()
    menu_type =  int(input("Please Enter#>>>..."))
    if menu_type == 1:
        # storeProduct() #please make  your own logic
        pass
    elif menu_type == 2:
        # displayProducts() #please make  your own logic
        pass
    elif menu_type  == 3:
        search()
    elif menu_type == 4:
        # deleteProduct() #please make  your own logic
        pass 
    
