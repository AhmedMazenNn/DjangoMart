import requests

application_name = input("Enter you django app name where you created your models: (products) ").lower() or "products"
product_model_name = input("Enter the Class name for products: (Product) ").lower() or "product"
category_model_name = input("Enter the Class name for categories: (Category) ").lower() or "category"

response = requests.get("https://dummyjson.com/products?limit=100")
products = response.json()["products"]

categories = set([product["category"] for product in products])
category_ids = {cat_name: cat_id for cat_id, cat_name in enumerate(categories)}
print(category_ids)

with open("tables.sql", "w") as file:
    file.write(f"""\
        INSERT INTO {application_name}_{category_model_name} \
        (id, name) VALUES {
        " ".join([ f"({cat_id}, '{cat_name}')" for cat_name, cat_id in category_ids.items()])
        }\n
    """)
    file.write(f"""\
        INSERT INTO {application_name}_{product_model_name} \
        (title, description, price, rating, category_id, thumbnail,created_at, updated_at) VALUES {
        " ".join([ 
            f"(\'{product["title"].replace("\'","")}\', \'{product["description"].replace("\'","")}\', {product["price"]}, {product["rating"]}, "\
            f"{category_ids[product["category"]]}, \'{product["thumbnail"].replace("\'","")}\' ,CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),\n" 
            for product in products])
        }\n
    """)
    # Write product insert statement
    # product_values = ",\n".join([
    #     f"('{product['title'].replace(\"'\", \"''\")}', "
    #     f"'{product['description'].replace(\"'\", \"''\")}', "
    #     f"{product['price']}, {product['rating']}, "
    #     f"{category_ids[product['category']]}, "
    #     f"'{product['thumbnail'].replace(\"'\", \"''\")}', "
    #     f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
    #     for product in products
    # ])
    # file.write(
    #     f"INSERT INTO {application_name}_{product_model_name} "
    #     f"(title, description, price, rating, category_id, thumbnail, created_at, updated_at) VALUES\n{product_values};\n"
    # )

