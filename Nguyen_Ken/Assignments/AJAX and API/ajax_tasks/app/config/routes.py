
from system.core.router import routes

routes['default_controller'] = 'Tasks'
routes['/'] = 'Tasks#index'
routes['POST']['/tasks/add'] = 'Tasks#add'
routes['POST']['/tasks/edit'] = 'Tasks#edit'
