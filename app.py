import mimetypes
import os
import web


class Static:
    def GET(self, path):
        safe_path = path.replace("../", "").replace("..\\", "")
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "proyecto", "static"))
        file_path = os.path.abspath(os.path.join(base_dir, safe_path))

        if not os.path.commonpath([base_dir, file_path]) == base_dir or not os.path.isfile(file_path):
            raise web.notfound()

        content_type, _ = mimetypes.guess_type(file_path)
        if content_type:
            web.header("Content-Type", content_type)

        with open(file_path, "rb") as f:
            return f.read()


urls = (
    '/static/(.+)', 'Static',
    '/', 'controllers.index.Index',
)
app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()