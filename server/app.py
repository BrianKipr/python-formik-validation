from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Customer model with SerializerMixin for JSON serialization
class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'Customer: {self.name}, age: {self.age}, email: {self.email}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers')
def customer_list():
    customers = Customer.query.all()
    return render_template('customer_list.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
