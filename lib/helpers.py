import random


def generate_order_number():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    order_number = ''.join(random.choice(letters) for _ in range(3)) + ''.join(random.choice(digits) for _ in range(5))
    return order_number

