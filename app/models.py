from . import db
from datetime import datetime
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    
    product = db.relationship('Product', backref='sales')

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(100), default='0', nullable=False)
    payment_method = db.Column(db.String(50), default='cash', nullable=False)
    status = db.Column(db.String(50), default='pending', nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)