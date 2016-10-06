
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        all_products = self.models['Product'].get_all_products()
        return self.load_view('index.html', products = all_products)

    def new(self):
        return self.load_view('new.html')

    def create(self):
        info = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'price' : request.form['price']
        }
        create_product = self.models['Product'].create_product(info)

        if create_product['status'] == False:
            errors = create_product['errors']
            for error in errors:
                flash(error, 'error')
            return self.load_view('new.html')
        return redirect('/')

    def show(self, id):
        product = self.models['Product'].show_one_product(id)
        return self.load_view('show.html', product = product[0])

    def edit(self, id):
        product = self.models['Product'].show_one_product(id)
        return self.load_view('edit.html', product = product[0])

    def update(self, id):
        info = {
            'id' : id,
            'name' : request.form['name'],
            'description' : request.form['description'],
            'price' : request.form['price']
        }
        update_product = self.models['Product'].update_product(info)

        if update_product['status'] == False:
            errors = update_product['errors']
            for error in errors:
                flash(error, 'error')
            return self.load_view('edit.html', product = info)
        return redirect('/')

    def destroy(self, id):
        data = {
            'id' : id
        }
        self.models['Product'].delete_product(data)
        return redirect('/')
