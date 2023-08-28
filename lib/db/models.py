from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


# base class for declarative models 
Base = declarative_base()


# Main table - contains salon's inventory core info 
class Salon(Base):

    # naming first table
    __tablename__ = "inventory"

    # naming columns 
    id = Column(Integer, primary_key=True)
    product = Column(String, unique=True)
    price = Column(String)
    quantity = Column(Integer)
    unit = Column(String)

# States a relationship with the Nail_Polish class
    nail_polishes = relationship("Nail_Polish", backref="salon")

# String format of Salon object
    def __repr__(self):
        return f"\n<Salon "\
        + f"id={self.id}," \
        + f"product={self.product}," \
        + f"price={self.price}," \
        + f"quantity={self.quantity}," \
        + f"unit={self.unit}" \
        + ">" 

# Second table - contains information about nail polishes and its specifications available in inventory  
class Nail_Polish(Base):

    # naming second table
    __tablename__ = "nail_polishes"

    # adding columns (specifications) to the table
    id = Column(Integer, primary_key=True)
    polishType = Column(String)
    brand = Column(String)
    color = Column(String)
    price = Column(String)

    # Define a foreign key relationship with the Salon class 
    salon_id = Column(Integer, ForeignKey("inventory.id"))

    # String representation of the Nail_Polish object
    def __repr__(self):
        return f"\n<Nail_Polish" \
        + f"id={self.id}," \
        + f"polishType={self.polishType}," \
        + f"brand={self.brand}," \
        + f"color={self.color}," \
        + f"price={self.price}" \
        + ">"


# Define the Place_Order class, which represents order information
class Place_Order(Base):

    #naming third table
    __tablename__ = "place_order"

    # adding columns (specifications) to the table
    id = Column(Integer, primary_key = True)
    product_id = Column(Integer, ForeignKey("inventory.id"))
    quantity = Column(Integer)
    order_number = Column(String, unique=True)
    date_order_placed = Column(String)

    # Define a relationship with the Salon class
    product = relationship("Salon", backref="orders")

    # String representation of the Place_Order object
    def __repr__(self):
        return f"\n<Place_Order " \
            + f"id={self.id}," \
            + f"product_id={self.product_id}," \
            + f"quantity={self.quantity}," \
            + f"order_number={self.order_number}," \
            + f"date_order_placed={self.date_order_placed}" \
            + ">"
      




      