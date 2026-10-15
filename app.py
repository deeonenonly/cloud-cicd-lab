from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version 2: Automatic deployment using GitHub Webhook, Jenkins, Docker, and AWS EC2!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
