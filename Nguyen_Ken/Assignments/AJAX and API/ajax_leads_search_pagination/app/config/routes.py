
from system.core.router import routes

routes['default_controller'] = 'Leads'
routes['/'] = 'Leads#index'
routes['/loadLeads'] = 'Leads#loadLeads'
routes['POST']['/search'] = 'Leads#search'
