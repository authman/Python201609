
from system.core.model import Model
import re

PRICE_REGEX = re.compile(r'^[0-9]*\.{0,1}[0-9]{0,2}$')


class Product(Model):
    def __init__(self):
        super(Product, self).__init__()

    def get_all_products(self):
        get_products_query = 'SELECT * FROM product ORDER BY id DESC'
        all_products = self.db.query_db(get_products_query)
        return all_products

    def show_one_product(self, id):
        data = {
            'id' : id
        }
        query = 'SELECT * FROM product WHERE id = :id LIMIT 1'
        product = self.db.query_db(query, data)
        return product

    def create_product(self, info):
        errors = []
        if not info['name']:
            errors.append('Course title cannot be blank')
        if not info['description']:
            errors.append('Course description cannot be blank')
        if not info['price']:
            errors.append('Price cannot be blank')
        elif not PRICE_REGEX.match(info['price']):
            errors.append('Price must only contain numbers')

        if errors:
            return {'status' : False, 'errors' : errors}

        create_data = {
            'name' : info['name'],
            'description' : info['description'],
            'price' : info['price']
        }
        create_query = 'INSERT INTO product (name, description, price, created_at, updated_at) VALUES (:name, :description, :price, NOW(), NOW())'
        new_product_id = self.db.query_db(create_query, create_data)

        return {'status' : True, 'new_id' : new_product_id }

    def update_product(self, info):
        errors = []
        if not info['name']:
            errors.append('Course title cannot be blank')
        if not info['description']:
            errors.append('Course description cannot be blank')
        if not info['price']:
            errors.append('Price cannot be blank')
        elif not PRICE_REGEX.match(info['price']):
            errors.append('Price must only contain numbers')

        if errors:
            return {'status' : False, 'errors' : errors}

        data = {
            'id' : info['id'],
            'name' : info['name'],
            'description' : info['description'],
            'price' : info['price']
        }
        update_query = 'UPDATE product SET name=:name, description=:description, price=:price WHERE id=:id'
        self.db.query_db(update_query, info)
        return {'status' : True}

    def delete_product(self, info):
        data = {
            'id' : info['id']
        }
        delete_query = 'DELETE FROM product WHERE id=:id'
        self.db.query_db(delete_query, data)
