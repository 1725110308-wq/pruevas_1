from .help import render


class Login:
    def GET(self):
        return render.auth.login()