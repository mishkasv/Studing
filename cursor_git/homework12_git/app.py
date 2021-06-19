from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def welcome():
	return render_template("welcome.html")

@app.route('/calc/<int:x>/<int:y>/<string:func>')
def calc(x,y,func):
	if func=='div':
		return render_template('calc.html', x=x, y=y, res=x/y, func=func)
	if func=='sum':
		return render_template('calc.html', x=x, y=y, res=x+y, func=func)
	if func=='mult':
		return render_template('calc.html', x=x, y=y, res=x*y, func=func)
	if func=='dif':
		return render_template('calc.html', x=x, y=y, res=x-y, func=func)

if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0')