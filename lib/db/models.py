from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Salon(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)
    product = Column(String)
    price = Column(String)
    quantity = Column(Integer)


    def __repr__(self):
        return f"\n<Salon "\
        + f"id={self.id}," \
        + f"product={self.product}," \
        + f"price={self.price}," \
        + f"quantity={self.quantity}," 
      