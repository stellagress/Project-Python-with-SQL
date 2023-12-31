# SQLAlchemy modules 
from models import Salon, Nail_Polish, Place_Order
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random



# Create a SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///data.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data from tables
session.query(Salon).delete()
session.query(Nail_Polish).delete()
session.query(Place_Order).delete()

# Define a list of items in inventory
inventory = [
    Salon(product="acetone", unit="galon", price="$10.99", quantity=12),
    Salon(product="base coat", unit="unit", price="$5", quantity=11),
    Salon(product="clippers nail kit", unit="unit", price="$8", quantity=20),
    Salon(product="cotton", unit="40 ft", price="$9.99", quantity=5),
    Salon(product="cuticle softener", unit="galon", price="$14.99", quantity=5),
    Salon(product="gloves", unit="500 pairs", price="$50", quantity=8),
    Salon(product="nail buffer", unit="50pcs", price="$12.5", quantity=11),
    Salon(product="nail extensions", unit="50pcs", price="$6", quantity=6),
    Salon(product="nail file", unit="50pcs", price="$20", quantity=9),
    Salon(product="nail glue", unit="unit 30oz", price="$1.5", quantity=35),
    Salon(product="nail polish", unit="unit", price="from $1 to $20", quantity=144),
    Salon(product="towel", unit="pack of 24", price="$49.99", quantity=5)
]

# Bulk insert the inventory items into the database
session.bulk_save_objects(inventory)

# Query for a specific salon inventory item
salon = session.query(Salon).filter_by(product="nail polish").first()

# Define a list of nail polish products
nail_polishes = [

    # Regular - Colorama
    Nail_Polish(polishType="Regular", brand="Colorama", color="Black", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Bronze Shimmer", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Burgundy", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Classic Beige", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Emerald Green", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="French Manicure", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Glitter", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Gray", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Lilac", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Mauve", price="$20", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Mint Green", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Nude", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Onyx Black", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Pastel Lavender", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Pink", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Rose Gold Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Sapphire Blue", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Silver Metallic", price="$20", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Taupe", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Teal", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="Vibrant Orange", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Colorama", color="White", price="$10", salon_id=salon.id),


    # Gel - Colorama
    Nail_Polish(polishType="Gel", brand="Colorama", color="Amethyst Purple", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Baby Blue", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Emerald Green", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="French Manicure", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Glitter", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Gray", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Lilac", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Mauve", price="$20", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Mint Green", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Nude", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Onyx Black", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Pastel Lavender", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Pink", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Rose Gold Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Sapphire Blue", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Silver Metallic", price="$20", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Taupe", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Teal", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="Vibrant Orange", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Colorama", color="White", price="$10", salon_id=salon.id),

    # Regular - Impala
    Nail_Polish(polishType="Regular", brand="Impala", color="Amethyst Purple", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Impala", color="Baby Blue", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Impala", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Impala", color="Lilac", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Impala", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Impala", color="White", price="$12", salon_id=salon.id),


    # Gel - Impala
    Nail_Polish(polishType="Gel", brand="Impala", color="Amethyst Purple", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Baby Blue", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Lilac", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="White", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Sapphire Blue", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Rose Gold Metallic", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Black", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Glitter", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Mint Green", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Pink", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Teal", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Cherry Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Nude", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Taupe", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Amethyst Purple", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Deep Plum", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Glitter", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Sapphire Blue", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Rose Gold Metallic", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Black", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Mauve", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Impala", color="White", price="$12", salon_id=salon.id),

    # Regular - Risque
    Nail_Polish(polishType="Regular", brand="Risque", color="Coral", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Silver Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Red", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Teal", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Cherry Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Nude", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Regular", brand="Risque", color="Taupe", price="$10", salon_id=salon.id),

    # Gel - Risque
    Nail_Polish(polishType="Gel", brand="Risque", color="Amethyst Purple", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Bronze Shimmer", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Coral", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Deep Plum", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Emerald Green", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Gold Metallic", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Lilac", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Mauve", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Red", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Rose Gold Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Silver Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Teal", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Vibrant Orange", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Lilac", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Gold Metallic", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Amethyst Purple", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Coral", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Silver Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Red", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Teal", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Cherry Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Nude", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Taupe", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Baby Blue", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Black", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="French Manicure", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Lilac", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Mint Green", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Pink", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="White", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Rose Gold Metallic", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Deep Plum", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Teal", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="White", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Amethyst Purple", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Black", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Coral", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Taupe", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Silver Metallic", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Red", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Teal", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Cherry Red", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Nude", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Taupe", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Baby Blue", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Black", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="French Manicure", price="$3", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Gray", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Lilac", price="$10", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Mint Green", price="$1", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Pink", price="$5", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="White", price="$15", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Amethyst Purple", price="$12", salon_id=salon.id),
    Nail_Polish(polishType="Gel", brand="Risque", color="Black", price="$10", salon_id=salon.id),

]

# Bulk insert the nail polish products into the database
session.bulk_save_objects(nail_polishes)

# Define a list of place orders
place_orders = [
    Place_Order(product_id=1, quantity=5, order_number='AHL98712', date_order_placed='placeholder'),
    Place_Order(product_id=2, quantity=3, order_number='EYU85263', date_order_placed='placeholder'),
]

# Bulk insert the place orders into the database
session.bulk_save_objects(place_orders)

# Commit the changes to the database
session.commit()


# debugging tool
# import ipdb; ipdb.set_trace()

