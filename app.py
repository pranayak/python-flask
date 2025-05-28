from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form.get('username')
    return render_template('greet.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
