import web
render=web.template.render('proyecto/views')
class Index:
    def GET(self):
        return render.index()