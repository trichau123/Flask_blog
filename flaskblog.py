from flask import Flask, render_template
app = Flask(__name__)

posts = [
{
	'author': 'Tri Chau',
	'title': 'Travel',
	'content': 'I love travel',
	'date_posted':'April 20, 2022'	
},
{
	'author': 'Tony Dien',
	'title': 'food',
	'content': 'I love food',
	'date_posted':'April 22, 2022'	
}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html',title='About')

if __name__ == '__main__':
	app.run(debug=True)