
from system.core.router import routes

routes['default_controller'] = 'Notes'
routes['/'] = 'Notes#index'

routes['POST']['/notes/addTitle'] ='Notes#addTitle'
routes['POST']['/notes/addDescription/'] = 'Notes#addDescription'
routes['POST']['/notes/delete/'] = 'Notes#delete'
