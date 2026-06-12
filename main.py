from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

@app.route('/')
def index():
	ip_addr = request.remote_addr
	d = db.Database()
	data = d.get_zadachi_by_ip(ip_addr)
	d.close()
	return render_template('index.html', data=data)

@app.route('/add_zadacha', methods=['POST', 'GET'])
def add_zadacha():
	if request.method == 'POST':
		zadacha = request.form['zadacha']
		ip_addr = request.remote_addr
		d = db.Database()
		d.add_task(ip_addr, zadacha)
		d.close()
		return redirect('/')
	else:
		return redirect('/')

@app.route('/delete_zadacha/<int:zadacha_id>', methods=['POST', 'GET'])
def delete_zadacha(zadacha_id):
	if request.method == 'POST':
		d = db.Database()
		d.delete_zadacha_by_id(zadacha_id)
		d.close()
		return redirect('/')
	else:
		return redirect('/')

@app.route('/set_done/<int:zadacha_id>', methods=['POST', 'GET'])
def set_done(zadacha_id):
	if request.method == 'POST':
		d = db.Database()
		d.change_zadacha_done(zadacha_id)
		d.close()
		return redirect('/')
	else:
		return redirect('/')


app.run()