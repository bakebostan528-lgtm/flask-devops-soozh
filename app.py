from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello DevOps Flask App'

@app.route('/health')
def health():
    return {'status': 'OK'}, 200

if __name__ == '__main__':
    app.run(debug=True)
