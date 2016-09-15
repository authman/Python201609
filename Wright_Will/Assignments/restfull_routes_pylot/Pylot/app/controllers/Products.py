from system.core.controller import *
from random import randint
from time import strftime

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        self.load_model('Product')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def new(self):
        return self.load_view('new.html')
    def edit(self):
            return self.load_view('edit.html')
    def show(self):
            return self.load_view('show.html')
    def create(self):
            return redirect("/products")
    def destroy(self):
            return redirect("/products")
    def update(self):
            return redirect("/products")
