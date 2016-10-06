
from system.core.model import Model
import re

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()


    def get_products(self):
        query = "SELECT * from product"
        return self.db.query_db(query)

    def get_product(self,_id):
        query = "SELECT * from product where id = :id"
        data = {'id': _id}
        return self.db.get_one(query, data)
    def add_product(self,info):
        errors =[]
        errors = self.validate_product_info(info,errors)
        if errors:
            return {'status':True,'errors':errors}
        sql = "INSERT into product (name, description, price) values(:name, :description, :price)"
        _id = self.db.query_db(sql, info)
        return {'status':False}
    # ask autman how to pull this validation code out into one method...
    def update_product(self,info):
        errors = []
        errors = self.validate_product_info(info,errors)
        if errors:
            return {'status':True, 'errors':errors}
        sql = "UPDATE restfull_routes.product SET name=:name, description=:description, price=:price, updated_at= NOW() WHERE id=:id;"
        _id = self.db.query_db(sql, info)
        return {'status': False, '_id':info['id']}

    def delete_product(self,_id):
        sql_data= {"id":_id}
        sql = "DELETE FROM product WHERE id=:id;"
        self.db.query_db(sql, sql_data)
        return

    def validate_product_info(self,info,errors):
        if len(info['name']) == 0:
            errors.append('name must not be blank')
        if len(info['price']) == 0:
            errors.append('price must be a valid number')
        if info['price'] < 0:
            errors.append('price can not be negative')
        return errors
