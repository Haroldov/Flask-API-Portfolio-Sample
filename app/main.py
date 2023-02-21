from flask import Flask

from routers.health_check_router import health_check

app = Flask(__name__)

app.add_url_rule("/health", view_func=health_check, methods=["GET"])
