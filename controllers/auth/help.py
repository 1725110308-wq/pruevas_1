import os
import web

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
render = web.template.render(os.path.join(root_path, 'proyecto', 'views'))
