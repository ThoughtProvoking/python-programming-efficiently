
import flask, jinja2, base64
import marsmap

app = flask.Flask(__name__)

template = jinja2.Template("""
<html>
  <body>
    <img src="data:image/png;base64,{{img_data}}"
  </body>
</html>
""")

@app.route('/<sol>')
def get_sol(sol):
    coords = marsmap.get_location(float(sol))
    buffer = marsmap.plot_location(coords)
    img = base64.b64encode(buffer.getvalue()).decode('ascii')
    
    html = template.render(img_data = img)
    return flask.Response(html)

@app.route('/')
def home_page():
    return flask.Response('Welcome')

app.run(host = '127.0.01')
