
from system.core.model import Model

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

        pass
    def update_product(self,info):
        errors = []
        if not len(info['name']) > 0:
            errors.append('name must not be blank')
        if not len(info['price']) > 0:
            errors.append('price must not be blank')
            if info['price'] < 0:
                errors.append('price can not be negative')

        if errors:
            return {'status':False, 'errors':errors}

        ####come back heer #######################
        # need to add sql query to update product


        sql = "UPDATE restfull_routes.product SET name=:name, description=:description, price=:price updated_at= NOW() WHERE id=:id;"
        pass
    def delete_product(self,_id):
        pass
    """
    def add_message(self):
        sql = "INSERT into products (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True

    def grab_messages(self):
        query = "SELECT * from products where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """
