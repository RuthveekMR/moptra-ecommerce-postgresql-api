from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

# ---------------------
# CUSTOMERS
# ---------------------
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def update_customer(db: Session, customer_id: str, updated_data: schemas.CustomerCreate):
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for field, value in updated_data.dict().items():
        setattr(db_customer, field, value)
    db.commit()
    return db_customer

def delete_customer(db: Session, customer_id: str):
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"message": "Customer deleted"}


# ---------------------
# GEOLOCATION
# ---------------------
def create_geolocation(db: Session, geo: schemas.GeolocationCreate):
    db_geo = models.Geolocation(**geo.dict())
    db.add(db_geo)
    db.commit()
    db.refresh(db_geo)
    return db_geo

def get_geolocations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Geolocation).offset(skip).limit(limit).all()

def update_geolocation(db: Session, zip_code: int, updated_data: schemas.GeolocationCreate):
    db_geo = db.query(models.Geolocation).filter(models.Geolocation.geolocation_zip_code_prefix == zip_code).first()
    if not db_geo:
        raise HTTPException(status_code=404, detail="Geolocation not found")
    for field, value in updated_data.dict().items():
        setattr(db_geo, field, value)
    db.commit()
    return db_geo

def delete_geolocation(db: Session, zip_code: int):
    db_geo = db.query(models.Geolocation).filter(models.Geolocation.geolocation_zip_code_prefix == zip_code).first()
    if not db_geo:
        raise HTTPException(status_code=404, detail="Geolocation not found")
    db.delete(db_geo)
    db.commit()
    return {"message": "Geolocation deleted"}


# ---------------------
# ORDERS
# ---------------------
def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).offset(skip).limit(limit).all()

def update_order(db: Session, order_id: str, updated_data: schemas.OrderCreate):
    db_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    for field, value in updated_data.dict().items():
        setattr(db_order, field, value)
    db.commit()
    return db_order

def delete_order(db: Session, order_id: str):
    db_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted"}


# ---------------------
# ORDER ITEMS
# ---------------------
def create_order_item(db: Session, item: schemas.OrderItemCreate):
    db_item = models.OrderItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_order_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderItem).offset(skip).limit(limit).all()

def update_order_item(db: Session, order_id: str, order_item_id: int, updated_data: schemas.OrderItemCreate):
    db_item = db.query(models.OrderItem).filter(
        models.OrderItem.order_id == order_id,
        models.OrderItem.order_item_id == order_item_id
    ).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Order Item not found")
    for field, value in updated_data.dict().items():
        setattr(db_item, field, value)
    db.commit()
    return db_item

def delete_order_item(db: Session, order_id: str, order_item_id: int):
    db_item = db.query(models.OrderItem).filter(
        models.OrderItem.order_id == order_id,
        models.OrderItem.order_item_id == order_item_id
    ).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Order Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Order Item deleted"}


# ---------------------
# PAYMENTS
# ---------------------
def create_order_payment(db: Session, payment: schemas.OrderPaymentCreate):
    db_payment = models.OrderPayment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_order_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderPayment).offset(skip).limit(limit).all()

def update_order_payment(db: Session, order_id: str, payment_seq: int, updated_data: schemas.OrderPaymentCreate):
    db_payment = db.query(models.OrderPayment).filter(
        models.OrderPayment.order_id == order_id,
        models.OrderPayment.payment_sequential == payment_seq
    ).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    for field, value in updated_data.dict().items():
        setattr(db_payment, field, value)
    db.commit()
    return db_payment

def delete_order_payment(db: Session, order_id: str, payment_seq: int):
    db_payment = db.query(models.OrderPayment).filter(
        models.OrderPayment.order_id == order_id,
        models.OrderPayment.payment_sequential == payment_seq
    ).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(db_payment)
    db.commit()
    return {"message": "Payment deleted"}


# ---------------------
# REVIEWS
# ---------------------
def create_order_review(db: Session, review: schemas.OrderReviewCreate):
    db_review = models.OrderReview(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_order_reviews(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderReview).offset(skip).limit(limit).all()

def update_order_review(db: Session, review_id: str, order_id: str, updated_data: schemas.OrderReviewCreate):
    db_review = db.query(models.OrderReview).filter(
        models.OrderReview.review_id == review_id,
        models.OrderReview.order_id == order_id
    ).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    for field, value in updated_data.dict().items():
        setattr(db_review, field, value)
    db.commit()
    return db_review

def delete_order_review(db: Session, review_id: str, order_id: str):
    db_review = db.query(models.OrderReview).filter(
        models.OrderReview.review_id == review_id,
        models.OrderReview.order_id == order_id
    ).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Review not found")
    db.delete(db_review)
    db.commit()
    return {"message": "Review deleted"}


# ---------------------
# PRODUCTS
# ---------------------
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def update_product(db: Session, product_id: str, updated_data: schemas.ProductCreate):
    db_product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in updated_data.dict().items():
        setattr(db_product, field, value)
    db.commit()
    return db_product

def delete_product(db: Session, product_id: str):
    db_product = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}


# ---------------------
# SELLERS
# ---------------------
def create_seller(db: Session, seller: schemas.SellerCreate):
    db_seller = models.Seller(**seller.dict())
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller

def get_sellers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Seller).offset(skip).limit(limit).all()

def update_seller(db: Session, seller_id: str, updated_data: schemas.SellerCreate):
    db_seller = db.query(models.Seller).filter(models.Seller.seller_id == seller_id).first()
    if not db_seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    for field, value in updated_data.dict().items():
        setattr(db_seller, field, value)
    db.commit()
    return db_seller

def delete_seller(db: Session, seller_id: str):
    db_seller = db.query(models.Seller).filter(models.Seller.seller_id == seller_id).first()
    if not db_seller:
        raise HTTPException(status_code=404, detail="Seller not found")
    db.delete(db_seller)
    db.commit()
    return {"message": "Seller deleted"}