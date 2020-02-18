from flask import *

app = Flask(__name__)

@app.route('/')
def rootroute():
	return render_template('frontpage.html')

@app.route('/<string:name>')
def nameroute(name):
	return 'Hello,{}'.format(name)

if __name__ == "__main__":
	app.run()