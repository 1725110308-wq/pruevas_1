import os
import web

urls = (
    '/', 'controllers.index.Index',
    '/login', 'controllers.auth.login.Login',
    '/auth/login', 'controllers.auth.login.Login',
)
app = web.application(urls, globals())


if __name__ == '__main__':
    static_dir = os.path.join(os.path.dirname(__file__), 'proyecto')
    current_dir = os.getcwd()
    os.chdir(static_dir)
    try:
        app.run()
    finally:
        os.chdir(current_dir)