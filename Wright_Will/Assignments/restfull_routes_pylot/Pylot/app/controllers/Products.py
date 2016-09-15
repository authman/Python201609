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
        return redirect("/")
    def edit(self):
            return redirect("/")
    def show(self):
            return redirect("/")
    def create(self):
            return redirect("/")
    def destroy(self):
            return redirect("/")
    def update(self):
            return redirect("/")
