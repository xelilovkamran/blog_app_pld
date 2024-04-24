from flask import Flask, request, jsonify, render_template, redirect
from dotenv import load_dotenv
import os
from models.blog import Blog


path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=path)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def home():
    if request.method == 'POST':
        data = request.form
        Blog.addBlog(data)

    blogs = Blog.getBlogs()
    return render_template('home.html', blogs=blogs)


@app.route('/blog/<int:id>', methods=['GET'], strict_slashes=False)
def show_blog(id):
    blog = Blog.getBlog(id)
    if not blog:
        return jsonify({"message": "Blog not found"}), 404
    return render_template('blog.html', blog=blog)


@app.route('/edit/<int:id>', methods=['GET', 'POST'], strict_slashes=False)
def edit_blog(id):
    if request.method == 'POST':
        data = request.form
        print(data)
        Blog.updateBlog(id, data)
        return redirect('/')
    blog = Blog.getBlog(id)
    return render_template('edit.html', blog=blog)


@app.route('/delete/<int:id>', methods=["DELETE"], strict_slashes=False)
def delete_blog(id):
    Blog.deleteBlog(id)
    return jsonify({"message": "Blog deleted"})


if __name__ == "__main__":
    app.run(debug=True)
