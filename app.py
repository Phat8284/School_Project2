from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")

def hello_world():

    return "<p>Hello, World!</p>"



@app.route("/hello4")
def hello():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('hello.html')



if __name__ == '__main__':

    # Chạy ứng dụng ở chế độ debug

    app.run(debug=True, port=9000)