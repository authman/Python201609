"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

"""
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
"""

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('ProductsModel')

    def index(self):
        all_products = self.models['ProductsModel'].get_all_products() #get_all_products is the result of the query in the model
        return self.load_view('products.html', all_products=all_products) #will load landing page, and all_products takes the model variable and passes it so you can use it on the view.
    
    def show(self, id):
        chosen_product = self.models['ProductsModel'].get_product_by_id(id)
        return self.load_view('show.html', chosen_product=chosen_product)

    
    def edit(self, id):
        chosen_product = self.models['ProductsModel'].get_product_by_id(id)
        return self.load_view('edit.html', chosen_product=chosen_product)

    
    def new(self):

        return self.load_view('new.html')

    def create(self):
        chosen_product=self.models['ProductsModel'].add_product(request.form)
        return redirect('/products')

    def destroy(self, id):
        deleted_product=self.models['ProductsModel'].delete_product(id)
        return redirect('/products')

    def update(self, id):
        self.models['ProductsModel'].update_product(id, request.form) 
        return redirect('/products')













