import os

def calculate_cart_total(cart_sum, tier, promos):
    price = cart_sum
    if cart_sum > 15000:
        price = cart_sum * 0.85
    return price
# эта строка специально сделана очень длинной чтобы вызвать ошибку flake8 по длине строки и посмотреть как работает quality gate
