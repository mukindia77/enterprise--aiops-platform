from fastapi import FastAPI

app = FastAPI(title="Ecommerce Payment Service")

payments = []

@app.get("/")
def home():
    return {"message": "Payment Service is running"}

@app.post("/payments")
def make_payment(order_id: int, amount: float):
    payment = {
        "payment_id": len(payments) + 1,
        "order_id": order_id,
        "amount": amount,
        "status": "Successful"
    }
    payments.append(payment)
    return payment

@app.get("/payments")
def get_payments():
    return payments
