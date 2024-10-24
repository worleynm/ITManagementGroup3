from flask import Flask, render_template

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# About page route
@app.route('/charter')
def about():
    return render_template('Project_charter.html')

# Services page route
@app.route('/services')
def services():
    return render_template('services.html')

# Contact page route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Charter page route
# @app.route('/charter')
# def contact():
    # return render_template('charter.html')

# Projects page route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Blog page route
@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)
# NEED TO CHANGE FILE NAMES STILL
