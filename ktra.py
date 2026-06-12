import logging

logging.basicConfig(
    filename="product_manager.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


product_db = [
    {
        "product_id": "P01",
        "product_name": "Coca Cola",
        "price": 15000,
        "quantity": 15
    },
    {
        "product_id": "P02",
        "product_name": "Pepsi",
        "price":12000,
        "quantity": 20
    },
{
        "product_id": "P03",
        "product_name": "Sprite",
        "price": 20000,
        "quantity": 18
    }
]

def display_products(products):
    if len(products) == 0:
        print("Chưa có sản phẩm nào")
        return
    products = sorted(products, key=lambda x: x["price"], reverse=True)

    print("STT | ID | TÊN | GIÁ | SL")
    print("----------------------------")

    for i, p in enumerate(products, 1):
        print(i, p["product_id"], p["product_name"], p["price"], p["quantity"])
    logging.info("User viewed product list")


def add_product(products):
    product_id = input("Nhập mã: ").upper()
    for p in products:
        if p["product_id"] == product_id:
            print("Trùng id! Vui lòng nhập lại")
            logging.warning(f"Duplicate product ID {product_id}")
            return

    try:
        name = input("Nhập tên: ")
        price = int(input("Nhập giá: "))
        quantity = int(input("Nhập số lượng: "))
        if price <= 0 or quantity <= 0:
            raise ValueError

    except ValueError:
        print("WARNING: Invalid input")
        logging.warning("Invalid price or quantity input")
        return
    products.append({
        "product_id": product_id,
        "product_name": name,
        "price": price,
        "quantity": quantity
    })
    print("INFO: Added new product", product_id)
    logging.info(f"Added new product {product_id}")

def update_product(products):
    product_id = input("Nhập mã cần sửa: ").upper()

    for p in products:
        if p["product_id"] == product_id:
            try:
                p["product_name"] = input("Tên mới: ")
                p["price"] = int(input("Giá mới: "))
                p["quantity"] = int(input("SL mới: "))

                if p["price"] <= 0 or p["quantity"] <= 0:
                    raise ValueError

            except ValueError:
                print("Dữ liệu không hợp lệ")
                logging.warning("Invalid update input")
                return

            print("INFO: Updated product", product_id)
            logging.info(f"Updated product {product_id}")
            return

    print("WARNING: Product not found")
    logging.warning(f"Product {product_id} not found")

    



while True :
    print("""===== HỆ THỐNG QUẢN LÝ SẢN PHẨM =====

1. Hiển thị danh sách sản phẩm
2. Thêm sản phẩm
3. Cập nhật sản phẩm
4. Thoát
          ==============================

""")
    
    choise =int(input("Mời bạn nhập lựa chọn:"))
    match choise:
        case 1:
            display_products(product_db)
        case 2:
             add_product(product_db)
        case 3:
            update_product(product_db)
        case 4:
            print("Thoát chương trình!")
            break
        case _:
            print("Vui lòng nhập lại!")
