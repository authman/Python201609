
from system.core.router import routes

routes['default_controller'] = 'Posts'
routes['/'] = 'Posts#index'
routes['POST']['/posts/create'] = 'Posts#create'
