""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class ProductModel(Model):
    def __init__(self):
        super(ProductModel, self).__init__()
    

    def get_all_products(self):
        return self.db.query_db("SELECT * FROM product;")


    def get_product_by_id(self, id):
        query = "SELECT * from product where id = :id"
        data = {'id': id}
        chosen_product = self.db.get_one(query, data)
        return chosen_product

    def add_product(self, data):
        sql = "INSERT into product (name, description, price) values (:name, :description, :price)"
        data = {'name':data['name'], 'description':data['description'], 'price':data['price']}
        return self.db.query_db(sql, data)
        #return True
    
    def edit_product(self, id, data):
        data2 = {
            'name':data['name'],
            'description':data['description'],
            'price':data['price'],
            'id': id
        }
        sql = "UPDATE product SET name=:name, description=:description, price=:price WHERE id=:id"
        return self.db.query_db(sql, data2)

    def delete_product(self, id):
      query = "DELETE FROM product WHERE id = :id"
      data = { 'id':id }
      return self.db.query_db(query, data)
        
        
    