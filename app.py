from flask import Flask, render_template
import glob
import os

app = Flask(__name__)

# Lists blogs in folder blogs/
# Blohs must have extenstion .md
def listBlogs():
    blogs = []
    cwd = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir( cwd + "/blogs"):
        if file.endswith(".md"):
            blogs.append(file)
    return blogs

# Routing section
@app.route('/')
def hello_world():
    myBlogs = listBlogs()
    return render_template('home.html', blogs = myBlogs)

@app.route('/blog/<blogname>')
def make_blog(blogname):d
    return blogname

#Init the app
if __name__ == '__main__':
    app.run(debug=True)
