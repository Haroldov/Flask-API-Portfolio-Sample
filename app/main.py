from flask import Flask
import os

app = Flask(__name__)

# import endpoints
app.add_url_rule('/user/<username>', 'show_user', show_user)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)
