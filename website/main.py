import flask

app = flask.Flask(__name__)

@app.route('/')
def home(path):
  return flask.render_template("index.html")
app.run()
