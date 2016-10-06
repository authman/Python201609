
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('ProductModel')
   
    def index(self):
        all_products = self.models['ProductModel'].get_all_products()
        return self.load_view('index.html', all_products=all_products)
    
    def show(self, id):
        chosen_product = self.models['ProductModel'].get_product_by_id(id)
        return self.load_view('show.html', chosen_product=chosen_product)


    def new(self):
        return self.load_view('new.html')

    def edit(self, id):
        chosen_product = self.models['ProductModel'].get_product_by_id(id)
        return self.load_view('edit.html', chosen_product=chosen_product)

    def create(self):
        created_product = self.models['ProductModel'].add_product(request.form)
        return redirect('/products')

    def destroy(self, id):
        deleted_product = self.models['ProductModel'].delete_product(id)
        return redirect('/products')

    def update(self, id):
        chosen_product = self.models['ProductModel'].edit_product(id, request.form)
        return redirect('/products')

