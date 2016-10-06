from system.core.controller import *

class posts(Controller):
    def __init__(self, action):
        super(posts, self).__init__(action)
        self.load_model('post')
        self.db = self._app.db

    def index(self):
        posts = self.models['post'].all()
        return self.load_view('index.html',posts=posts)

    def posts_html(self):
        posts = self.models['post'].all()
        return self.load_view('partials/posts.html',posts=posts)

    def create(self):
        new_post = request.form['text']
        self.models['post'].add(new_post)
        return redirect('/posts/html')

    def destroy(self):
        _id = request.form['id']
        self.models['post'].delete(_id)
        return redirect('/posts/html')
