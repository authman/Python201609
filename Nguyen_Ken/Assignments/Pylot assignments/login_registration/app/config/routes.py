
from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/users/registration'] = 'Users#registration'
routes['POST']['/users/login'] = 'Users#login'
