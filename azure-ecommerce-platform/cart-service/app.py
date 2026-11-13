from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Ecommerce Cart Service")

cart = []

PRODUCT_SERVICE_URL = "http://product-service:8000"

@app.get("/")
def home():
    return {"message": "Cart Service is running"}

@app.post("/cart/{product_id}")
def add_to_cart(product_id: int, quantity: int = 1):
    response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products/{product_id}",
        timeout=5
    )

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Product not found")

    product = response.json()

    item = {
        "product_id": product_id,
        "product_name": product["name"],
        "price": product["price"],
        "quantity": quantity
    }

    cart.append(item)
    return {"message": "Product added to cart", "item": item}

@app.get("/cart")
def get_cart():
    return cart
