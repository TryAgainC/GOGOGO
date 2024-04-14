from flask import Flask,send_file

app = Flask(__name__)

@app.route('/get_node')
def hello_world():  # put application's code here
    file_path = 'file.txt'
    rp = send_file(file_path, as_attachment=False)
    return rp


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
