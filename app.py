from flask import *
import pymysql, hashlib, time

app = Flask(__name__)

with open(r'C:\Users\12hydrogen\Documents\GitHub\singlePythonBlog\key', 'rb') as key:
	app.secret_key = key.readline()

@app.route('/')
def rootroute():
	return render_template('frontpage.html')

@app.route('/data', methods=['POST', 'GET'])
def dataroute():
	return ''

@app.route('/login', methods=['POST', 'GET'])
def logincheck():
	call = {'status': 'error', 'user': 'anonymous', 'timestamp': '', 'hash': ''}
	dbc = [database('username'), database('password')]
	if 'username' in request.form and 'password' in request.form and 'timestamp' in request.form:
		checkhash = hashlib.sha256()
		checkhash.update(bytes(request.form['username'] + request.form['password'] + str(request.form['timestamp']), 'utf-8'))
		checkhash = checkhash.hexdigest()
		if checkhash == request.form['hash']:
			hashname = hashlib.sha256()
			hashname.update(request.form['username'].encode('utf-8'))
			hashname = hashname.hexdigest()
			for names in dbc[0]:
				call['user'] = request.form['username']
				if names[0] == hashname:
					if dbc[1][dbc[0].index(names)][0] == request.form['password']:
						call['status'] = 'accept'
						session['username'] = request.form['username']
						session['password'] = request.form['password']
						session['timestamp'] = int(1000 * time.time())
						break
					else:
						call['status'] = 'refused'
						break
				else:
					call['status'] = 'refused'
	elif 'username' in session and 'password' in session and 'timestamp' in session:
		tm = int(1000 * time.time())
		ts = session['timestamp']
		if ts < tm - 1000 * 60 * 60 * 24 * 7 or ts > tm:
			call['user'] = session['username']
			call['status'] = ''
		else:
			uname = session['username']
			hashname = hashlib.sha256()
			hashname.update(uname.encode('utf-8'))
			uname = hashname.hexdigest()
			for names in dbc[0]:
				call['user'] = session['username']
				if names[0] == uname:
					if dbc[1][dbc[0].index(names)][0] == session['password']:
						call['status'] = 'accept'
						break
					else:
						call['status'] = 'refused'
						break
				else:
					call['status'] = 'refused'
	call['timestamp'] = int(1000 * time.time())
	checkhash = hashlib.sha256()
	checkhash.update(bytes(call['status'] + call['user'] + str(call['timestamp']), 'utf-8'))
	call['hash'] = checkhash.hexdigest()
	return call

def database(name='*'):
	db = pymysql.connect('localhost', 'testuser', 'qaz123-=', 'testdb')
	cursor = db.cursor()
	cursor.execute('select {} from users'.format(name))
	return cursor.fetchall()

if __name__ == "__main__":
	app.run()