def get_discounted_price(item_name, item_price, promo_code):
    if promo_code.upper() == "SAVE10":
        discount = item_price * 0.1
        return item_price - discount

    if promo_code.upper() == "HALFOFF":
        discount = item_price * 0.5
        return item_price - discount

    return item_price