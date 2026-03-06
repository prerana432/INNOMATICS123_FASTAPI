from fastapi import FastAPI
from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Mouse", "price": 500, "category": "electronics", "in_stock": True},
    {"id": 2, "name": "Keyboard", "price": 1500, "category": "electronics", "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 8000, "category": "electronics", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 200, "category": "accessories", "in_stock": True},

    # New Products
    {"id": 5, "name": "Laptop Stand", "price": 1200, "category": "accessories", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 3500, "category": "electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 2500, "category": "electronics", "in_stock": True}
]

@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }

@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered_products = []

    for product in products:
        if product["category"].lower() == category_name.lower():
            filtered_products.append(product)

    if len(filtered_products) == 0:
        return {"error": "No products found in this category"}

    return {"products": filtered_products}

@app.get("/products/instock")
def get_instock_products():
    in_stock_products = [p for p in products if p["in_stock"] == True]

    return {
        "in_stock_products": in_stock_products,
        "count": len(in_stock_products)
    }

@app.get("/store/summary")
def store_summary():
    total_products = len(products)

    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    matched_products = [p for p in products if keyword.lower() in p["name"].lower()]

    if not matched_products:
        return {"message": "No products matched your search"}

    return {
        "matched_products": matched_products,
        "count": len(matched_products)
    }


