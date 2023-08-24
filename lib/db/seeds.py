from models import Salon, Nail_Polish
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

fake = Faker()
engine = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Salon).delete()
session.query(Nail_Polish).delete()

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
    Salon(product="nail polish", price="from $1 to $20", quantity=144),
    Salon(product="towel (pack of 24)", price="$49.99", quantity=5)
]

session.bulk_save_objects(inventory)

# salon = session.query(Salon).all()
salon = session.query(Salon).filter_by(product="nail polish").first()


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

session.bulk_save_objects(nail_polishes)

session.commit()



import ipdb; ipdb.set_trace()





# nail_polishes = [
#     Nail_Polish(
#         polishType=random.choice(polish_types),
#         brand=random.choice(brands),
#         color=random.choice(colors),
#         price=random.choice(price_ranges),
#         salon_id=salon.id
#     )
#     for salon in inventory
# ]

# session.bulk_save_objects(nail_polishes)
# session.commit()






# polish_types = ["Regular", "Gel"]
# brands = ["Risque", "Colorama", "Impala"]
# colors = [ 
#     "Nude",
#     "Red",
#     "Pink",
#     "French Manicure",
#     "Burgundy",
#     "Coral",
#     "Taupe",
#     "Deep Plum",
#     "Pastel Lavender",
#     "Mint Green",
#     "Baby Blue",
#     "Silver Metallic",
#     "Gold Metallic",
#     "Rose Gold Metallic",
#     "Black",
#     "White",
#     "Gray",
#     "Teal",
#     "Glitter",
#     "Classic Beige",
#     "Sapphire Blue",
#     "Emerald Green",
#     "Amethyst Purple",
#     "Onyx Black",
#     "Lilac",
#     "Cherry Red",
#     "Mauve",
#     "Vibrant Orange",
#     "Bronze Shimmer"]
# price_ranges = ["$1", "$3", "$5", "$10", "$12", "$15", "$20"]


# nail_polish_product = session.query(Salon).filter_by(product="nail polish").first()
# nail_polishes = [
#     Nail_Polish(
#         polishType=random.choice(polish_types),
#         brand=random.choice(brands),
#         color=random.choice(colors),
#         price=random.choice(price_ranges),
#         salon=nail_polish_product
#     )
#     for _ in range(83)
# ]

# session.bulk_save_objects(nail_polishes)
# session.commit()















