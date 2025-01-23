from products import dao
from functools import lru_cache

class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data):
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])




@lru_cache(maxsize=128)  # Adjust maxsize based on memory constraints
def list_products() -> list[Product]:
    # Fetch the data from DAO and process it
    return [Product(
        id=product['id'],
        name=product['name'],
        description=product['description'],
        cost=product['cost'],
        qty=product['qty']
    ) for product in dao.list_products()]




def get_product(product_id: int) -> Product:
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)


