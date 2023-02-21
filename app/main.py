from flask import Flask
import os

app = Flask(__name__)

# import endpoints
app.add_url_rule('/user/<username>', 'show_user', show_user)
