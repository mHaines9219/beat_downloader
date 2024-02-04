from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/download')
def hello_world():
    return jsonify([1,2,3,4,5,6,7,8,9,10])




if __name__ == '__main__':
    app.run(debug=True)