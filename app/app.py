import os
from flask import Flask

from routers.health_check_router import health_check
from routers.text_parser_router import TextRouter
from services.text_service import TextService

text_service = TextService()
text_router = TextRouter(text_service)

app = Flask(__name__)

app.add_url_rule("/health", view_func=health_check, methods=["GET"])
app.add_url_rule("/word-count", view_func=text_router.words_count, methods=["POST"])
app.add_url_rule("/word-quantity", view_func=text_router.words_number, methods=["POST"])
app.add_url_rule("/full-text-length", view_func=text_router.full_text_length, methods=["POST"])
app.add_url_rule("/text-statistic", view_func=text_router.text_statistic, methods=["POST"])

if __name__ == "__main__":
    app.run(
        host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True
    )
