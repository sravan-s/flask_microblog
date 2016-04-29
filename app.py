from flask import Flask, render_template, send_from_directory
import glob
import os
import markdown

app = Flask(__name__)
cwd = os.path.dirname(os.path.abspath(__file__))
blogsFolder = cwd + "/blogs/"

# Lists blogs in folder blogs/
# Blohs must have extenstion .md
def listBlogs():
    blogs = []
    for file in os.listdir( cwd + "/blogs"):
        if file.endswith(".md"):
            blogs.append(file)
    return blogs

#Converts .md to html
def toHTML(fileName):
    plainStr = open(blogsFolder + fileName)
    html = markdown.markdown(plainStr.read())
    return render_template('blog.html', content = html)

# Routing section
@app.route('/')
def hello_world():
    myBlogs = listBlogs()
    return render_template('home.html', blogs = myBlogs)

@app.route('/blog/<blogname>')
def make_blog(blogname):
    return toHTML(blogname)

@app.route('/resources/<path:path>')
def send_js(path):
    return send_from_directory('resources', path)

#Init the app
if __name__ == '__main__':
    app.run(debug=True)
