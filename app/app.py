import os
from flask import Flask

from routers.health_check_router import health_check

app = Flask(__name__)

app.add_url_rule("/health", view_func=health_check, methods=["GET"])

if __name__ == "__main__":
    app.run(
        host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True
    )
