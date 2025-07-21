import flask
import passgen

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return flask.render_template('index.html',password=None)


@app.route('/generate',methods=['POST'])
def generate():
    length = int(flask.request.form['length'])
    use_special_char = 'speccar' in flask.request.form
    passinit = passgen.random_pass_gen(length,use_special_char)
    passfinal = passgen.get_not_breached(passinit,length,use_special_char)
    return flask.render_template('index.html',password=passfinal)

if __name__ == "__main__":
    app.run(debug=True) 