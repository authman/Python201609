
from system.core.router import routes


routes['default_controller'] = 'Surveys'
routes['POST']['/Surveys/process'] = 'Surveys#process'
routes['GET']['/Surveys/result'] = 'Surveys#result'
