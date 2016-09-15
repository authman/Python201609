from system.core.controller import *
from random import randint
from time import strftime

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        product_data = self.models['Product'].get_products()
        return self.load_view('index.html',product_data=product_data)

    def new(self):
        return self.load_view('new.html')
    def edit(self,_id):
        product = self.models['Product'].get_product(_id)
        return self.load_view('edit.html',product=product)
    def show(self,_id):
        product = self.models['Product'].get_product(_id)
        return self.load_view('show.html',product=product)
    def create(self):
        return redirect("/products")
    def destroy(self,_id):
        return redirect("/products")
    def update(self):
        
        return redirect("/products")
