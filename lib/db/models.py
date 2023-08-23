from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

Base = declarative_base()


class Salon(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    product = Column(String, unique=True)
    price = Column(String)
    quantity = Column(Integer)

    nail_types = relationship("Nail_Type", backref="salon")


    def __repr__(self):
        return f"\n<Salon "\
        + f"id={self.id}," \
        + f"product={self.product}," \
        + f"price={self.price}," \
        + f"quantity={self.quantity}," 


class Nail_Type(Base):
    __tablename__ = "nail_types"

    id = Column(Integer, primary_key=True)
    white_tip = Column(Boolean)
    shape = Column(String)
    size = Column(Integer)

    salon_id = Column(Integer, ForeignKey("inventory.id"))


    def __repr__(self):
        return f"\n<Nail_Type" \
        + f"id={self.id}," \
        + f"white_tip={self.white_tip}," \
        + f"shape={self.shape}," \
        + f"size={self.size}"
      





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
      