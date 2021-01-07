from flask import Flask, render_template, redirect, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rogive'

@app.route('/')
def home():
  return 'Hello World'

@app.route('/about')
def about():
  return 'The About Page'

@app.route('/blog')
def blog():
  return '''
  <html>
  <head> </head>
  <body>
    <h2> Este es un buen blog </h2>
    <p> Un blog de drones entretenido </p>
  </body>
  </html>
  '''

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
  return 'This is blog post number ' + blog_id

@app.route('/template-blog')
def templateblog():
  pilots = [{'title': 'Piloto #1', 'author': 'Messi'},
            {'title': 'Piloto #2', 'author': 'Cristiano'}]
  content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
  return render_template('blog.html', author = "Ivan Rodriguez", sunny = True, pilots = pilots, content = content)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUpForm()
  if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
  return render_template('signup.html', form=form)

if __name__ == '__main__':
  app.run()