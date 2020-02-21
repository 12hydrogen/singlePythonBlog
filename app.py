from flask import *
import sqlite3, hashlib, time

app = Flask(__name__)

with open(r'C:\Users\12hydrogen\Documents\GitHub\singlePythonBlog\key', 'rb') as key:
	app.secret_key = key.readline()

@app.route('/')
def rootroute():
	return render_template('frontpage.html')

@app.route('/home')
def homeroute():
	return render_template('homepage.html')

@app.route('/about')
def aboutroute():
	return render_template('about.html')

@app.route('/pages')
def pageroute():
	return render_template('pages.html')

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
		if ts < tm - 1000 * 60 * 60 * 24 * 3 or ts > tm:
			call['user'] = session['username']
			call['status'] = 'refused'
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

@app.route('/register')
def regroute():
	call = {'status': 'error', 'user': 'anonymous', 'timestamp': '', 'hash': ''}
	if 'username' in request.form and 'password' in request.form and 'timestamp' in request.form:
		checkhash = hashlib.sha256()
		checkhash.update(bytes(request.form['username'] + request.form['password'] + str(request.form['timestamp']), 'utf-8'))
		checkhash = checkhash.hexdigest()
		if checkhash == request.form['hash']:
			hashname = hashlib.sha256()
			hashname.update(request.form['username'].encode('utf-8'))
			hashname = hashname.hexdigest()
			if 'email' in request.form:
				e = request.form['email']
			else:
				e = ''
			if 'gender' in request.form:
				g = request.form['gender']
			else:
				g = 'secret'
			if 'type' in request.form:
				t = request.form['type']
			else:
				t = 'guest'
			val = [hashname, request.form['password'], e, g, t]
			database(method='put', value=val)
	call['timestamp'] = int(1000 * time.time())
	checkhash = hashlib.sha256()
	checkhash.update(bytes(call['status'] + call['user'] + str(call['timestamp']), 'utf-8'))
	call['hash'] = checkhash.hexdigest()
	return call

def database(name='*', method='get', table='users', column=['username', 'password', 'email', 'gender', 'type'], value=['', '', '', '', '']):
	db = sqlite3.connect('test.db')
	cursor = db.cursor()
	if method == 'get':
		cursor.execute('select {} from {};'.format(name, table))
		b = cursor.fetchall()
		db.close()
		return b
	elif method == 'put' and len(column) == len(value):
		try:
			cursor.execute('''insert into {}({})
			value ({});'''.format(table, li(column), li(value)))
			db.commit()
			db.close()
			return 'ok'
		except:
			db.rollback()
			db.close()
			return 'error'

def li(ls):
	if ls is list:
		a = ''
		for i, element in enumerate(ls):
			if i == len(ls) - 1:
				a = a + '"' + str(element) + '"'
			else:
				a = a + '"' + str(element) + '"' + ', '
		return a
	else:
		return ''

if __name__ == "__main__":
	app.run()