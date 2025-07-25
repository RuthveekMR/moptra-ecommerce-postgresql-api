from sqlalchemy import Column, String, Integer, Float, Numeric, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 1. GEOLOCATION
class Geolocation(Base):
    __tablename__ = "olist_geolocation"

    geolocation_zip_code_prefix = Column(Integer, primary_key=True, nullable=False)
    geolocation_lat = Column(Float, nullable=False)
    geolocation_lng = Column(Float, nullable=False)
    geolocation_city = Column(String(50), nullable=False)
    geolocation_state = Column(String(2), nullable=False)

# 2. CUSTOMERS
class Customer(Base):
    __tablename__ = "olist_customers"

    customer_id = Column(String(100), primary_key=True, nullable=False)
    customer_unique_id = Column(String(100), nullable=False)
    customer_zip_code_prefix = Column(Integer, ForeignKey("olist_geolocation.geolocation_zip_code_prefix"), nullable=False)
    customer_city = Column(String(50), nullable=False)
    customer_state = Column(String(2), nullable=False)

# 3. SELLERS
class Seller(Base):
    __tablename__ = "olist_sellers"

    seller_id = Column(String(100), primary_key=True, nullable=False)
    seller_zip_code_prefix = Column(Integer, ForeignKey("olist_geolocation.geolocation_zip_code_prefix"), nullable=False)
    seller_city = Column(String(50), nullable=False)
    seller_state = Column(String(2), nullable=False)

# 4. PRODUCTS
class Product(Base):
    __tablename__ = "olist_products"

    product_id = Column(String(100), primary_key=True, nullable=False)
    product_category_name = Column(String(100), nullable=False)
    product_name_length = Column(Integer, nullable=False)
    product_description_length = Column(Integer, nullable=False)
    product_photos_qty = Column(Integer, nullable=False)
    product_weight_g = Column(Integer, nullable=False)
    product_length_cm = Column(Integer, nullable=False)
    product_height_cm = Column(Integer, nullable=False)
    product_width_cm = Column(Integer, nullable=False)

# 5. ORDERS
class Order(Base):
    __tablename__ = "olist_orders"

    order_id = Column(String(100), primary_key=True, nullable=False)
    customer_id = Column(String(100), ForeignKey("olist_customers.customer_id"), nullable=False)
    order_status = Column(String(20), nullable=False)
    order_purchase_timestamp = Column(DateTime, nullable=False)
    order_approved_at = Column(DateTime)
    order_delivered_carrier_date = Column(DateTime)
    order_delivered_customer_date = Column(DateTime)
    order_estimated_delivery_date = Column(DateTime)

# 6. ORDER ITEMS
class OrderItem(Base):
    __tablename__ = "olist_order_items"

    order_id = Column(String(100), ForeignKey("olist_orders.order_id"), primary_key=True, nullable=False)
    order_item_id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(String(100), ForeignKey("olist_products.product_id"), nullable=False)
    seller_id = Column(String(100), ForeignKey("olist_sellers.seller_id"), nullable=False)
    shipping_limit_date = Column(DateTime, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    freight_value = Column(Numeric(6, 2), nullable=False)

# 7. ORDER PAYMENTS
class OrderPayment(Base):
    __tablename__ = "olist_order_payments"

    order_id = Column(String(100), ForeignKey("olist_orders.order_id"), primary_key=True, nullable=False)
    payment_sequential = Column(Integer, primary_key=True, nullable=False)
    payment_type = Column(String(25), nullable=False)
    payment_installments = Column(Integer, nullable=False)
    payment_value = Column(Float, nullable=False)

# 8. ORDER REVIEWS
class OrderReview(Base):
    __tablename__ = "olist_order_reviews"

    review_id = Column(String(200), primary_key=True, nullable=False)
    order_id = Column(String(100), ForeignKey("olist_orders.order_id"), primary_key=True, nullable=False)
    review_score = Column(Integer, nullable=False)
    review_comment_title = Column(String(100))
    review_comment_message = Column(String(1000))
    review_creation_date = Column(DateTime, nullable=False)
    review_answer_timestamp = Column(DateTime, nullable=False)

