
from system.core.router import routes

routes['default_controller'] = 'Maps'
routes['/'] = 'Maps#index'
routes['POST']['/directions'] = 'Maps#get_directions'
