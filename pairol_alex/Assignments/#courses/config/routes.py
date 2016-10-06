from system.core.router import routes


routes['default_controller'] = 'Courses'
routes['GET']['/destroy/<id>'] = 'Courses#destroy_confirm'
routes['GET']['/yes_delete/<id>']= 'Courses#delete'
routes['GET']['/return'] = 'Courses#index'
routes['POST']['/create_course'] = 'Courses#create'
