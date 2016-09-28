
from system.core.router import routes

routes['default_controller'] = 'Courses'
routes['POST']['/courses/add'] = 'Courses#add'
routes['GET']['/courses/destroy/<course_id>'] = 'Courses#destroy'
routes['GET']['/courses/delete/<course_id>'] = 'Courses#delete'
