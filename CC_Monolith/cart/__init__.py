import json

import products
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])



def get_cart(username: str) -> list[Product]:
    # Fetch cart details from the DAO
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []  # Return an empty list if the cart is empty or doesn't exist

    # Collect all unique product IDs from the cart contents
    product_ids = set()
    for cart_detail in cart_details:
        contents = cart_detail['contents']
        # Use json.loads for safer parsing and add product IDs to the set
        product_ids.update(json.loads(contents))
    
    # Fetch all product details in a single batch request
    products_map = products.get_products(list(product_ids))  # Assume it returns {id: Product}

    # Map product IDs to their corresponding Product objects
    cart_items = [products_map[product_id] for product_id in product_ids if product_id in products_map]
    
    return cart_items



def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)

def delete_cart(username: str):
    dao.delete_cart(username)


