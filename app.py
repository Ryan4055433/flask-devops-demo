from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello this is my Flask App in Docker with GitHub Actions and Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)