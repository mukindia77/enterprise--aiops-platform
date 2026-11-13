from fastapi import FastAPI, HTTPException
from datetime import datetime
import requests

app = FastAPI(title="Ecommerce Order Service")

orders = []

PRODUCT_SERVICE_URL = "http://product-service:8000"
PAYMENT_SERVICE_URL = "http://payment-service:8000"

@app.get("/")
def home():
    return {"message": "Order Service is running"}

@app.post("/orders")
def create_order(product_id: int, quantity: int):

    product_response = requests.get(
        f"{PRODUCT_SERVICE_URL}/products/{product_id}",
        timeout=5
    )

    if product_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Product not found")

    product = product_response.json()
    amount = product["price"] * quantity
    order_id = len(orders) + 1

    payment_response = requests.post(
        f"{PAYMENT_SERVICE_URL}/payments",
        params={"order_id": order_id, "amount": amount},
        timeout=10
    )

    if payment_response.status_code != 200:
        raise HTTPException(status_code=502, detail="Payment failed")

    payment = payment_response.json()

    order = {
        "order_id": order_id,
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "amount": amount,
        "payment_id": payment["payment_id"],
        "payment_status": payment["status"],
        "status": "Confirmed",
        "created_at": datetime.now().isoformat()
    }

    orders.append(order)
    return order

@app.get("/orders")
def get_orders():
    return orders
