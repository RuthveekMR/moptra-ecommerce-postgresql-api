from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

# Create all tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Moptra E-Commerce API", version="1.0")

# -------------------- CUSTOMERS --------------------

@app.post("/customers/", response_model=schemas.CustomerResponse)
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

@app.get("/customers/", response_model=list[schemas.CustomerResponse])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_customers(db, skip=skip, limit=limit)

@app.put("/customers/{customer_id}", response_model=schemas.CustomerResponse)
def update_customer(customer_id: str, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.update_customer(db, customer_id, customer)

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    return crud.delete_customer(db, customer_id)

# -------------------- GEOLOCATION --------------------

@app.post("/geolocation/", response_model=schemas.GeolocationResponse)
def create_geo(geo: schemas.GeolocationCreate, db: Session = Depends(get_db)):
    return crud.create_geolocation(db, geo)

@app.get("/geolocation/", response_model=list[schemas.GeolocationResponse])
def read_geos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_geolocations(db, skip=skip, limit=limit)

@app.put("/geolocation/{zipcode}", response_model=schemas.GeolocationResponse)
def update_geo(zipcode: int, geo: schemas.GeolocationCreate, db: Session = Depends(get_db)):
    return crud.update_geolocation(db, zipcode, geo)

@app.delete("/geolocation/{zipcode}")
def delete_geo(zipcode: int, db: Session = Depends(get_db)):
    return crud.delete_geolocation(db, zipcode)

# -------------------- ORDERS --------------------

@app.post("/orders/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders/", response_model=list[schemas.OrderResponse])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_orders(db, skip=skip, limit=limit)

@app.put("/orders/{order_id}", response_model=schemas.OrderResponse)
def update_order(order_id: str, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.update_order(db, order_id, order)

@app.delete("/orders/{order_id}")
def delete_order(order_id: str, db: Session = Depends(get_db)):
    return crud.delete_order(db, order_id)

# -------------------- ORDER ITEMS --------------------

@app.post("/order_items/", response_model=schemas.OrderItemResponse)
def create_order_item(item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.create_order_item(db, item)

@app.get("/order_items/", response_model=list[schemas.OrderItemResponse])
def read_order_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_order_items(db, skip, limit)

@app.put("/order_items/{order_id}/{item_id}", response_model=schemas.OrderItemResponse)
def update_order_item(order_id: str, item_id: int, item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    return crud.update_order_item(db, order_id, item_id, item)

@app.delete("/order_items/{order_id}/{item_id}")
def delete_order_item(order_id: str, item_id: int, db: Session = Depends(get_db)):
    return crud.delete_order_item(db, order_id, item_id)

# -------------------- ORDER PAYMENTS --------------------

@app.post("/order_payments/", response_model=schemas.OrderPaymentResponse)
def create_payment(payment: schemas.OrderPaymentCreate, db: Session = Depends(get_db)):
    return crud.create_order_payment(db, payment)

@app.get("/order_payments/", response_model=list[schemas.OrderPaymentResponse])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_order_payments(db, skip, limit)

@app.put("/order_payments/{order_id}/{seq}", response_model=schemas.OrderPaymentResponse)
def update_payment(order_id: str, seq: int, payment: schemas.OrderPaymentCreate, db: Session = Depends(get_db)):
    return crud.update_order_payment(db, order_id, seq, payment)

@app.delete("/order_payments/{order_id}/{seq}")
def delete_payment(order_id: str, seq: int, db: Session = Depends(get_db)):
    return crud.delete_order_payment(db, order_id, seq)

# -------------------- ORDER REVIEWS --------------------

@app.post("/order_reviews/", response_model=schemas.OrderReviewResponse)
def create_review(review: schemas.OrderReviewCreate, db: Session = Depends(get_db)):
    return crud.create_order_review(db, review)

@app.get("/order_reviews/", response_model=list[schemas.OrderReviewResponse])
def read_reviews(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_order_reviews(db, skip, limit)

@app.put("/order_reviews/{review_id}/{order_id}", response_model=schemas.OrderReviewResponse)
def update_review(review_id: str, order_id: str, review: schemas.OrderReviewCreate, db: Session = Depends(get_db)):
    return crud.update_order_review(db, review_id, order_id, review)

@app.delete("/order_reviews/{review_id}/{order_id}")
def delete_review(review_id: str, order_id: str, db: Session = Depends(get_db)):
    return crud.delete_order_review(db, review_id, order_id)

# -------------------- PRODUCTS --------------------

@app.post("/products/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/", response_model=list[schemas.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_products(db, skip, limit)

@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(product_id: str, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@app.delete("/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)

# -------------------- SELLERS --------------------

@app.post("/sellers/", response_model=schemas.SellerResponse)
def create_seller(seller: schemas.SellerCreate, db: Session = Depends(get_db)):
    return crud.create_seller(db, seller)

@app.get("/sellers/", response_model=list[schemas.SellerResponse])
def read_sellers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_sellers(db, skip, limit)

@app.put("/sellers/{seller_id}", response_model=schemas.SellerResponse)
def update_seller(seller_id: str, seller: schemas.SellerCreate, db: Session = Depends(get_db)):
    return crud.update_seller(db, seller_id, seller)

@app.delete("/sellers/{seller_id}")
def delete_seller(seller_id: str, db: Session = Depends(get_db)):
    return crud.delete_seller(db, seller_id)