from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class Salon(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    product = Column(String, unique=True)
    price = Column(String)
    quantity = Column(Integer)

    nail_polishes = relationship("Nail_Polish", backref="salon")


    def __repr__(self):
        return f"\n<Salon "\
        + f"id={self.id}," \
        + f"product={self.product}," \
        + f"price={self.price}," \
        + f"quantity={self.quantity}"
        + ">" 


class Nail_Polish(Base):
    __tablename__ = "nail_polishes"

    id = Column(Integer, primary_key=True)
    polishType = Column(String)
    brand = Column(String)
    color = Column(String)
    price = Column(String)


    salon_id = Column(Integer, ForeignKey("inventory.id"))


    def __repr__(self):
        return f"\n<Nail_Polish" \
        + f"id={self.id}," \
        + f"polishType={self.polishType}," \
        + f"brand={self.brand}," \
        + f"color={self.color}," \
        + f"price={self.price}" \
        + ">"
      





#       from sqlalchemy.orm import declarative_base
# from sqlalchemy import Column, Integer, String

# Base = declarative_base()


# class Salon(Base):
#     __tablename__ = "inventory"

#     id = Column(Integer, primary_key=True)
#     product = Column(String, unique=True)
#     price = Column(String)
#     quantity = Column(Integer)


#     def __repr__(self):
#         return f"\n<Salon "\
#         + f"id={self.id}," \
#         + f"product={self.product}," \
#         + f"price={self.price}," \
#         + f"quantity={self.quantity}," 
      