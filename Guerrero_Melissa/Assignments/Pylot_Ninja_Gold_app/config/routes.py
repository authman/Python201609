"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['GET']['/index'] = 'Welcome#index'
routes['POST']['/process_money'] = 'Welcome#process_money'
routes['POST']['/reset'] = 'Welcome#reset'


