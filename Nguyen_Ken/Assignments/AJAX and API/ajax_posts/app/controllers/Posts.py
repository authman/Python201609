
from system.core.controller import *

class Posts(Controller):
    def __init__(self, action):
        super(Posts, self).__init__(action)

        self.load_model('Post')




    def index(self):

        posts = self.models['Post'].get_all()

        return self.load_view('index.html', posts = posts)

    def create(self):
        data={
            'description' : request.form['description']
            }

        self.models['Post'].create_post(data)
        #now retrieve for ajax
        posts = self.models['Post'].get_all()
        return self.load_view('/partial/posts.html', posts = posts)
