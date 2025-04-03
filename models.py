from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, index=True)
    description = Column(String)
    pictures = Column(String)

    products = relationship("Product", back_populates="category")


class CustomerCustomerDemo(Base):
    __tablename__ = 'customer_customer_demo'

    customer_id = Column(String, ForeignKey('customers.customer_id'), primary_key=True)
    customer_type_id = Column(String, ForeignKey('customer_demographics.customer_type_id'), primary_key=True)

    customer = relationship("Customer", back_populates="customer_customer_demo")
    customer_demographics = relationship("CustomerDemographics", back_populates="customer_customer_demo")


class CustomerDemographics(Base):
    __tablename__ = 'customer_demographics'

    customer_type_id = Column(String, primary_key=True, index=True)
    customer_desc = Column(String)

    customer_customer_demo = relationship("CustomerCustomerDemo", back_populates="customer_demographics")


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(String, primary_key=True, index=True)
    company_name = Column(String, index=True)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)

    customer_customer_demo = relationship("CustomerCustomerDemo", back_populates="customer")
    orders = relationship("Order", back_populates="customer")


class EmployeeTerritories(Base):
    __tablename__ = 'employee_territories'

    employee_id = Column(Integer, ForeignKey('employees.employee_id'), primary_key=True)
    territory_id = Column(String, ForeignKey('territories.territory_id'), primary_key=True)

    employee = relationship("Employee", back_populates="employee_territories")
    territory = relationship("Territory", back_populates="employee_territories")


class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, index=True)
    first_name = Column(String, index=True)
    title = Column(String)
    title_of_courtesy = Column(String)
    birth_date = Column(String)
    hire_date = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    home_phone = Column(String)
    extension = Column(String)
    photo = Column(String)
    notes = Column(String)
    reports_to = Column(Integer, ForeignKey('employees.employee_id'))
    photo_path = Column(String)

    employee_territories = relationship("EmployeeTerritories", back_populates="employee")


class OrderDetails(Base):
    __tablename__ = 'order_details'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    unit_price = Column(Float)
    quantity = Column(Integer)
    discount = Column(Float)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String, ForeignKey('customers.customer_id'))
    employee_id = Column(Integer, ForeignKey('employees.employee_id'))
    order_date = Column(String)
    required_date = Column(String)
    shipped_date = Column(String)
    ship_via = Column(Integer)
    freight = Column(Float)
    ship_name = Column(String)
    ship_address = Column(String)
    ship_city = Column(String)
    ship_region = Column(String)
    ship_postal_code = Column(String)
    ship_country = Column(String)

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetails", back_populates="order")


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.supplier_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    quantity_per_unit = Column(String)
    unit_price = Column(Float)
    units_in_stock = Column(Integer)
    units_on_order = Column(Integer)
    reorder_level = Column(Integer)
    discontinued = Column(Integer)

    order_details = relationship("OrderDetails", back_populates="product")
    supplier = relationship("Supplier", back_populates="products")
    category = relationship("Category", back_populates="products")


class Region(Base):
    __tablename__ = 'regions'

    region_id = Column(String, primary_key=True, index=True)
    region_description = Column(String)

    territories = relationship("Territory", back_populates="region")


class Shipper(Base):
    __tablename__ = 'shippers'

    shipper_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    phone = Column(String)


class Supplier(Base):
    __tablename__ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    contact_name = Column(String)
    contact_title = Column(String)
    address = Column(String)
    city = Column(String)
    region = Column(String)
    postal_code = Column(String)
    country = Column(String)
    phone = Column(String)
    fax = Column(String)
    home_page = Column(String)

    products = relationship("Product", back_populates="supplier")
    territories = relationship("Territory", back_populates="suppliers")


class Territory(Base):
    __tablename__ = 'territories'

    territory_id = Column(String, primary_key=True, index=True)
    territory_description = Column(String)
    region_id = Column(String, ForeignKey('regions.region_id'))

    employee_territories = relationship("EmployeeTerritories", back_populates="territory")
    suppliers = relationship("Supplier", back_populates="territories")
    region = relationship("Region", back_populates="territories")


class UsState(Base):
    __tablename__ = 'us_states'

    state_id = Column(String, primary_key=True, index=True)
    state_name = Column(String, index=True)
    state_abbreviation = Column(String, index=True)
    country_id = Column(String, ForeignKey('countries.country_id'))

    territories = relationship("Territory", back_populates="us_states")
