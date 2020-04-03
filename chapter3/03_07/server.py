
import flask, jinja2, io, base64
import stereo

app = flask.Flask(__name__)

template = jinja2.Template("""
<html>
  <body>
    <img src="{{imgdata}}" />
  </body>
</html>
""")

def make_img_data(img):
    buffer = io.BytesIO()
    img.save(buffer, format = 'PNG')
    return base64.b64encode(buffer.getvalue()).decode('ascii')

@app.route('/<sol>')
def get_sol(sol):
    left, right = stereo.getday(sol).__next__()
    img = stereo.blend(stereo.getimage(left), stereo.getimage(right))
    
    html = template.render(imgdata = make_img_data(img))
    return flask.Response(html)

@app.route('/')
def hello_world():
    return flask.Response('<html><body><p>Hello, world!</p></body></html>')

app.run(host = '127.0.0.1')
