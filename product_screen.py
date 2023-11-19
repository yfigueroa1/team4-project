class Product:
    productID = 0
    productList = []

    def addProduct(self, productName, productStock, productPrice):
        Product.productID += 1
        productData = {
            "ID": Product.productID,
            "Name": productName,
            "Stock": productStock,
            "Price": productPrice
        }
        Product.productList.append(productData)

    def productSearch(self, searchID):
        for product in Product.productList:
            if product["ID"] == searchID:
                return product
        return None

    def printProductList(self):
        return Product.productList

productInstance = Product()


while True:
    print("Product Screen: \n1) Add new product \n2) Search product ID \n3) View product list \n4) Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Product Name:\n")
        stock = input("Product Stock:\n")
        price = input("Product Price:\n")
        productInstance.addProduct(name, stock, price)
    elif choice == 2:
        ID = int(input("Product ID:\n"))
        result = productInstance.productSearch(ID)
        if result:
            print("Product Found:", result)
        else:
            print("Product not found.")
    elif choice == 3:
        print("Product List:", productInstance.printProductList())
    elif choice == 4:
        break
    else:
        print("Invalid input")