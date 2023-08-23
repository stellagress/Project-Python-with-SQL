from models import Salon
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)

session = Session()

session.query(Salon).delete()

inventory = [
    Salon(product="acetone(galon)", price="$10.99", quantity=12),
    Salon(product="base coat", price="$5", quantity=11),
    Salon(product="clippers nail kit", price="$8", quantity=20),
    Salon(product="cotton (40 ft)", price="$9.99", quantity=5),
    Salon(product="cuticle softener(galon)", price="$14.99", quantity=5),
    Salon(product="gloves (500 pairs)", price="$50", quantity=8),
    Salon(product="nail buffer (50 pcs)", price="$12.5", quantity=11),
    Salon(product="nail extensions (500 pcs)", price="$6", quantity=6),
    Salon(product="nail file (50 pcs)", price="$20", quantity=9),
    Salon(product="nail glue", price="$1.5", quantity=35),
    Salon(product="nail polish", price="from $1 to $20", quantity=193),
    Salon(product="towel (pack of 24)", price="$49.99", quantity=5)
]

session.bulk_save_objects(inventory)
session.commit()

print(inventory)

print("Testing code")
