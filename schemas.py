from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ----------------------------
# 1. Customers
# ----------------------------
class CustomerBase(BaseModel):
    customer_id: str
    customer_unique_id: str
    customer_zip_code_prefix: int
    customer_city: str
    customer_state: str

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    class Config:
        from_attributes = True


# ----------------------------
# 2. Geolocation
# ----------------------------
class GeolocationBase(BaseModel):
    geolocation_zip_code_prefix: int
    geolocation_lat: float
    geolocation_lng: float
    geolocation_city: str
    geolocation_state: str

class GeolocationCreate(GeolocationBase):
    pass

class GeolocationResponse(GeolocationBase):
    class Config:
        from_attributes = True


# ----------------------------
# 3. Orders
# ----------------------------
class OrderBase(BaseModel):
    order_id: str
    customer_id: str
    order_status: str
    order_purchase_timestamp: datetime
    order_approved_at: Optional[datetime]
    order_delivered_carrier_date: Optional[datetime]
    order_delivered_customer_date: Optional[datetime]
    order_estimated_delivery_date: Optional[datetime]

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    class Config:
        from_attributes = True


# ----------------------------
# 4. Order Items
# ----------------------------
class OrderItemBase(BaseModel):
    order_id: str
    order_item_id: int
    product_id: str
    seller_id: str
    shipping_limit_date: datetime
    price: float
    freight_value: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    class Config:
        from_attributes = True


# ----------------------------
# 5. Order Payments
# ----------------------------
class OrderPaymentBase(BaseModel):
    order_id: str
    payment_sequential: int
    payment_type: str
    payment_installments: int
    payment_value: float

class OrderPaymentCreate(OrderPaymentBase):
    pass

class OrderPaymentResponse(OrderPaymentBase):
    class Config:
        from_attributes = True


# ----------------------------
# 6. Order Reviews
# ----------------------------
class OrderReviewBase(BaseModel):
    review_id: str
    order_id: str
    review_score: int
    review_comment_title: Optional[str]
    review_comment_message: Optional[str]
    review_creation_date: datetime
    review_answer_timestamp: datetime

class OrderReviewCreate(OrderReviewBase):
    pass

class OrderReviewResponse(OrderReviewBase):
    class Config:
        from_attributes = True


# ----------------------------
# 7. Products
# ----------------------------
class ProductBase(BaseModel):
    product_id: str
    product_category_name: str
    product_name_length: int
    product_description_length: int
    product_photos_qty: int
    product_weight_g: int
    product_length_cm: int
    product_height_cm: int
    product_width_cm: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    class Config:
        from_attributes = True


# ----------------------------
# 8. Sellers
# ----------------------------
class SellerBase(BaseModel):
    seller_id: str
    seller_zip_code_prefix: int
    seller_city: str
    seller_state: str

class SellerCreate(SellerBase):
    pass

class SellerResponse(SellerBase):
    class Config:
        from_attributes = True

