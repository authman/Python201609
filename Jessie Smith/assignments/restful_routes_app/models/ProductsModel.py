
from system.core.model import Model

class ProductsModel(Model):
    def __init__(self):
        super(ProductsModel, self).__init__()

    def get_all_products(self): 
        query = "SELECT * from product"   
        return self.db.query_db(query)
        # this query will return all info from product table

    def get_product_by_id(self, id):
        query = "SELECT * from product where id = :id"
        data = {'id': id}
        chosen_product = self.db.get_one(query, data)
        return chosen_product
        # this query will return a specific id's info

    def update_product(self, id, data):
        data2 = {
            'name' :data['name'],
            'description':data['description'],
            'price':data['price'],
            'id' : id
        }
        sql = "UPDATE product SET name=:name, description=:description, price=:price WHERE id=:id"
        return self.db.query_db(sql, data2)

    def add_product(self, data):
        sql = "INSERT into product (name, description, price) values(:name, :description, :price)"
        data = {'name': data['name'], 'description': data['description'], 'price': data['price']}
        return self.db.query_db(sql, data)
        # this query will submit all info into product table

    def delete_product(self, id):
        query = "DELETE FROM product WHERE id=:id"
        data = {"id":id}
        return self.db.query_db(query, data)
    

       
        
    

 